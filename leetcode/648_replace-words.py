class TrieNode:
    def __init__(self, c, end_of_word = False):
        self.letter = c
        self.children = {}
        self.end_of_word = end_of_word
    
    def addChild(self, c, end_of_word = False):
        if not c in self.children:
            node = TrieNode(c, end_of_word)
            self.children[c] = node
            return node
        else:
            node = self.children[c]
            if end_of_word:
                node.end_of_word = True
            return node
            
        
class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie_root = TrieNode('')
        for word in dictionary:
            node = trie_root
            for i, w in enumerate(word):
                node = node.addChild(w, i == len(word) - 1)
        
        result = []
        for word in sentence.split(' '):
            result.append(self.replaceWord(word, trie_root))
        
        return ' '.join(result)
    
    def replaceWord(self, word, trie_root):
        node = trie_root
        
        match_so_far = ''
        for c in word:
            if not c in node.children:
                return word
            match_so_far += c
            node = node.children[c]
            if node.end_of_word:
                return match_so_far
        
        return word
                
                
                
        

        
