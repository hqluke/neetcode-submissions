class TrieNode():
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class PrefixTree:

    def __init__(self):
        # always start with a TrieNode, contains a hashmap in children, chars as keys, 
        # and TrieNodes as values (so we can access children and check endOfWord bool)
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            # add character if not already added
            if c not in curr.children:
                curr.children[c] = TrieNode()
            # increment to newly added char
            curr = curr.children[c]
        # mark end of word
        curr.endOfWord = True


    def search(self, word: str) -> bool:
        curr = self.root
        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        # whole word has to match and last char has to be marked as endOfWord
        return curr.endOfWord

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for c in prefix:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        # only care that we didn't return false IE some word starts with it
        return True
        
        