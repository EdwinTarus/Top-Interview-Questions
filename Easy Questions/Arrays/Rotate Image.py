class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        #transpose the matrix
        for row in range(len(matrix)):
            for col in range (row, len(matrix)):
                matrix[row][col],matrix[col][row] = matrix[col][row], matrix[row][col]

        #reverse each row/list in the matrix
        for row in matrix:
            print(len(row))
            l,r = 0, len(row)-1
            print(f"l : {l}, r: {r}")
            while l<r:
                row[l], row[r] = row[r],row[l]
                l+=1
                r-=1
           
            row.reverse()
