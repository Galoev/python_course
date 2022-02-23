import numpy as np


class Matrix:
    def __init__(self, data):
        self.data = data
        self.rows = len(data)
        self.cols = len(data[0])
    
    def _check_shapes(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise Exception("Incorrect matrix dimension")

    def __add__(self, other):
        self._check_shapes(other)
        res_mat = Matrix([[0 for i in range(self.cols)] for i in range(self.rows)])
        
        for i in range(self.rows):
            for j in range(self.cols):
                res_mat.data[i][j] = self.data[i][j] + other.data[i][j]
        
        return res_mat
    
    def __mul__(self, other):
        self._check_shapes(other)
        res_mat = Matrix([[0 for i in range(self.cols)] for i in range(self.rows)])

        for i in range(self.rows):
            for j in range(self.cols):
                res_mat.data[i][j] = self.data[i][j] * other.data[i][j]
        
        return res_mat

    def __matmul__(self, other):
        if self.cols != len(other.data):
            raise Exception("Incorrect matrix dimension")
        
        res_mat = Matrix([[0 for i in range(self.cols)] for i in range(self.rows)])
        
        for i in range(self.rows):
            for j in range(other.cols):
                for k in range(other.rows):
                    res_mat.data[i][j] += self.data [i][k] * other.data[k][j]
        
        return res_mat
    
    def __str__(self) -> str:
        res = ""
        for i in range(self.rows):
            for j in range(self.cols):
                res = f"{res}{self.data[i][j]} "
            res = f"{res}\n"
        return res


if __name__ == "__main__":
    np.random.seed(0)
    mat1 = np.random.randint(0, 10, (10, 10))
    mat2 = np.random.randint(0, 10, (10, 10))
    # print(mat1 + mat2)
    # print(mat1 * mat2)
    # print(mat1 @ mat2)
    A = Matrix(mat1.tolist())
    B = Matrix(mat2.tolist())
    with open("artifacts/easy/A.txt", "w") as f:
        f.write(str(A))
    with open("artifacts/easy/B.txt", "w") as f:
        f.write(str(B))
    with open("artifacts/easy/matrix+.txt", "w") as f:
        f.write(str(A + B))
    with open("artifacts/easy/matrix*.txt", "w") as f:
        f.write(str(A * B))
    with open("artifacts/easy/matrix@.txt", "w") as f:
        f.write(str(A @ B))

