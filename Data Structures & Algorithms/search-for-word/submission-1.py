class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        path = set()
        def dfs(r, c, i):
            # because of the early return statements below,
            # we only advance if we've matched all the chars in the word
            # so we can just return true if the length is the same
            if i == len(word):
                return True
            
            # return if we're out of bounds, or the char we're checking isn't the next char in the word
            # or if we've already checked the char in the current iteration
            if (r < 0 or c < 0 or
                r >= ROWS or c >= COLS or
                word[i] != board[r][c] or
                (r,c) in path):
                return False

            # add to path so we don't use same board pos multiple times
            # check in all directions
            path.add((r,c))
            res = (dfs(r + 1, c, i + 1) or 
                   dfs(r - 1, c, i + 1) or 
                   dfs(r, c + 1, i + 1) or
                   dfs(r, c- 1, i + 1))
            # remove board pos so it doesn't mess up next iteration
            path.remove((r,c))
            return res

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r,c,0):
                    return True
        return False