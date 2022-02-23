import numpy as np

class SaveToFile:
    def save(self, file):
        with open(file, "w") as f:
            f.write(str(self))

class PrettyStr:
    def __str__(self) -> str:
        res = ""
        for i in range(self.rows):
            for j in range(self.cols):
                res = f"{res}{self.value[i][j]} "
            res = f"{res}\n"
        return res

class Getters:
    def get_val(self):
        return self.value

class Setters:
    def set_val(self, value):
        self.value = value

class Matrix(np.lib.mixins.NDArrayOperatorsMixin, SaveToFile, PrettyStr, Getters, Setters):
    def __init__(self, value):
        self.value = np.asarray(value)
        self.rows = len(value)
        self.cols = len(value[0])
    
    _HANDLED_TYPES = (np.ndarray,)

    def __array_ufunc__(self, ufunc, method, *inputs, **kwargs):
        out = kwargs.get('out', ())
        for x in inputs + out:
            if not isinstance(x, self._HANDLED_TYPES + (Matrix,)):
                return NotImplemented

        inputs = tuple(x.value if isinstance(x, Matrix) else x for x in inputs)
        
        if out:
            kwargs['out'] = tuple(
                x.value if isinstance(x, Matrix) else x
                for x in out)
        result = getattr(ufunc, method)(*inputs, **kwargs)

        if type(result) is tuple:
            return tuple(type(self)(x) for x in result)
        elif method == 'at':
            return None
        else:
            return type(self)(result)

if __name__ == "__main__":
    np.random.seed(0)
    mat1 = np.random.randint(0, 10, (10, 10))
    mat2 = np.random.randint(0, 10, (10, 10))

    A = Matrix(mat1.tolist())
    B = Matrix(mat2.tolist())
    A.save("artifacts/medium/A.txt")
    B.save("artifacts/medium/B.txt")
    (A + B).save("artifacts/medium/matrix+.txt")
    (A * B).save("artifacts/medium/matrix*.txt")
    (A @ B).save("artifacts/medium/matrix@.txt")