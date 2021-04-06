import copy
class Solution:

    def exist(self, board, word):

        x = len(board[0])
        y = len(board)
        set1 =set()
        def help(i,j,word):
            if len(word)==0:
                return True

            if 0<=i<=y-1 and 0<=j<=x-1:

                if board[i][j]!=word[0] or (i,j) in set1:
                    return False

                if board[i][j]==word[0]:
                    word = word[1:]
                    set1.add((i,j))

                    if help(i-1,j,word) or help(i+1,j,word) or help(i,j-1,word) or help(i,j+1,word):
                        return True
                    else:
                        set1.remove((i,j))
            else:
                return False

        for m in range(y):
            for n in range(x):
                if help(m,n,word):
                    return True
        return False
board =[
    ["A","B","C","E"],
    ["S","F","E","S"],
    ["A","D","E","E"]]
word = "ABCESE"
s = Solution()
q = s.exist(board,word)
print(q)










