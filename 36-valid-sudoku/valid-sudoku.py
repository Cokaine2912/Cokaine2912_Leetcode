class Solution:
    def isValidSudoku(self, board) -> bool:
        
        # print("Rows")
        for i in range(9) :
            row = {}
            for j in range(9) :
                if board[i][j] != "." and board[i][j] in row :
                    # print("Flaw !!!")
                    return False
                else :
                    row[board[i][j]] = 1
            # print(row)

        # print("Coloumns")
        for i in range(9) :
            coloum = {}
            for j in range(9) :
                if board[j][i] != "." and board[j][i] in coloum :
                    # print("Flaw !!!")
                    return False
                else :
                    coloum[board[j][i]] = 1
            # print(coloum)


        # print('Boxes')

        for k in range(3) :

            box = {}
            for i in range(3) :
                for j in range(3) :
                    if board[i][j + 3*k] != "." and board[i][j+ 3*k]  in box :
                        # print("Flaw !!")
                        return False
                    else :
                        box[board[i][j+ 3*k]] = 1
            # print(box)


            box = {}
            for i in range(3,6) :
                for j in range(3) :
                    if board[i][j + 3*k] != "." and board[i][j+ 3*k]  in box :
                        # print("Flaw !!")
                        return False
                    else :
                        box[board[i][j+ 3*k]] = 1
            # print(box)


            box = {}
            for i in range(6,9) :
                for j in range(3) :
                    if board[i][j + 3*k] != "." and board[i][j+ 3*k]  in box :
                        # print("Flaw !!")
                        return False
                    else :
                        box[board[i][j+ 3*k]] = 1
            # print(box)


        return True