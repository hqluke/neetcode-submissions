class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
    
    def addWord(self, word):
        curr = self
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.isWord = True
        
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        # create trie from all words
        for w in words:
            root.addWord(w)

        # initialize vars
        ROWS, COLS = len(board), len(board[0])
        res, visit = set(), set()
        def dfs(r, c, node, word):
            # base return
            if (r < 0 or c < 0 or 
                r == ROWS or c == COLS or
                board[r][c] not in node.children or (r,c) in visit):
                return
            #mark as visited and get TrieNode at board pos(IE the current char)
            visit.add((r,c))
            node = node.children[board[r][c]]
            # update current word (with current char)
            word += board[r][c]
            # check if its end of word(we already confirmed that the word exists in our trie
            # from our base return case)
            if node.isWord:
                res.add(word)

            #check every square around current char (Up, down, left, right)
            dfs(r + 1, c, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)
            #remove current char as visited so it doesn't interfere with next iterations.
            visit.remove((r,c))

        #call dfs, having each char on the board start as a staring pos
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, "")
        return list(res)