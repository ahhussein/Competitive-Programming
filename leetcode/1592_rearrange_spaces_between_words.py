# 1592. Rearrange Spaces Between Words: https://leetcode.com/problems/rearrange-spaces-between-words/
class Solution:
    def reorderSpaces(self, text: str) -> str:
        # Iterate once to count spaces and words
        # Divide spaces by words
        # space_between_words = spaces // (words - 1)
        # space_at_the_end = spaces % (words - 1)

        spacesCount = 0
        wordsCount = 0
        lastChar = None
        words = []
        word = []

        for ch in text:
            if ch != " ":
                word.append(ch)


            elif ch == " " and lastChar and lastChar != " ":
                # End of word
                words.append(''.join(word))
                word = []
                spacesCount += 1
                wordsCount += 1

            elif ch == " ":
                spacesCount += 1

            lastChar = ch

        # If a word ends a sentence with no additional spaces
        if word:
            words.append(''.join(word))
            wordsCount += 1

        res = []
        if wordsCount == 1:
            spaceBetweenWords = 0
            spaceAtEnd = spacesCount
        else:
            spaceBetweenWords = spacesCount // (wordsCount - 1)
            spaceAtEnd = spacesCount % (wordsCount - 1)

        for i, word in enumerate(words):
            res.append(word)

            if i == len(words) - 1:
                continue

            for i in range(spaceBetweenWords):
                res.append(" ")

        for i in range(spaceAtEnd):
            res.append(" ")

        return "".join(res)