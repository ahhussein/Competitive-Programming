import queue

class Node:
    def __init__(self, node_idx: int, parent: int, locking_user: Optional[int] = None):
        self.node_idx = node_idx
        self.locking_user = locking_user
        self.children: Set[Node] = set()
        self.parent = parent
            
    def add_child(self, node):
        self.children.add(node)
        
    def __eq__(self, other):
        if isinstance(other, Item):
            return (self.node_idx == other.node_idx) 
        else:
            return False
        
    def __hash__(self):
        return hash(self.node_idx)
    
    
class LockingTree:

    def __init__(self, parent: List[int]):
        self.nodes = []
        for idx, parent_idx in enumerate(parent):
            self.nodes.append(Node(idx, parent_idx))
        
        for idx, parent_idx in enumerate(parent):
            node = self.nodes[idx]
            if parent_idx != -1:
                self.nodes[parent_idx].add_child(node)

    def lock(self, num: int, user: int) -> bool:
        if not self.nodes[num].locking_user:
            self.nodes[num].locking_user = user
            return True
        return False
        

    def unlock(self, num: int, user: int) -> bool:
        if self.nodes[num].locking_user == user:
            self.nodes[num].locking_user = None
            return True
        return False
        

    def upgrade(self, num: int, user: int) -> bool:
        # If locked, reject op
        if self.nodes[num].locking_user:
            return False
        
        # If at least one locked ancestor, reject op
        parent = self.nodes[num].parent
        while parent != -1:
            parent_node = self.nodes[parent]
            if parent_node.locking_user:
                return False
            parent = parent_node.parent
        
        # If at least one locked descedant, execute op
        upgrade = False
        descenandats_queue = queue.Queue()
        for child in self.nodes[num].children:
            descenandats_queue.put(child)
            
        while not descenandats_queue.empty():
            descenandat = descenandats_queue.get()
            # condition satisifed
            if descenandat.locking_user:
                descenandat.locking_user = None
                upgrade = True
                
            for child in descenandat.children:
                descenandats_queue.put(child)
        
        if upgrade:
            self.nodes[num].locking_user = user
        return upgrade
                            

        
        


# Your LockingTree object will be instantiated and called as such:
# obj = LockingTree(parent)
# param_1 = obj.lock(num,user)
# param_2 = obj.unlock(num,user)
# param_3 = obj.upgrade(num,user)


# ٍsave user name to lock
# Save lock state
# hash value for descenants
