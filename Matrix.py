
class MatrixError(BaseException):
    def __init__(self, m1, m2):
        self.matrix1 = m1
        self.matrix2 = m2


class Matrix:

    def __init__(self, lists):
        self.matr = [lis.copy() for lis in lists]

    def __str__(self):
        self.text = ''
        for lis in self.matr:
            self.text += str(lis)[1:-1] + '\n'
        self.text = self.text.replace(', ', '\t')
        self.text = self.text[:-1]
        return self.text

    def size(self):
        return len(self.matr), len(self.matr[0])

    def __add__(self, second):
        s = self.size()
        if s == second.size():
            ans = [[(self.matr[i][j]) + (second.matr[i][j]) for j in
                   range(s[1])] for i in range(s[0])]
        else:
            raise MatrixError(self, second)
        return Matrix(ans)

    def __mul__(self, alpha):
        if isinstance(alpha, int) or isinstance(alpha, float):
            ans = [[j * alpha for j in i] for i in self.matr]
            return Matrix(ans)
        elif isinstance(alpha, Matrix): #alpha extended to could be a matrix
            s1 = self.size()
            s2 = alpha.size()
            if s1[1] == s2[0]:
                a = []
                for j in range(s1[0]):
                    answer = []
                    for k in range(s2[1]):
                        ans = 0
                        for i in range(s1[1]):
                            ans += self.matr[j][i] * alpha.matr[i][k]
                        answer.append(ans)
                    a.append(answer)
                return(Matrix(a))
            else:
                raise MatrixError(self, alpha)

    __rmul__ = __mul__

    def transpose(self):
        mirror = self.matr.copy()
        s = self.size()
        self.matr = [[mirror[j][i] for j in range(s[0])] for i in range(s[1])]
        return Matrix(self.matr)

    @staticmethod
    def transposed(matrix):
        s = matrix.size()
        ans = [[matrix.matr[j][i] for j in range(s[0])] for i in range(s[1])]
        return Matrix(ans)

    def definitor(self, size):
        ex_m = self.matr.copy()
        ex_m.extend(self.matr[0:size - 1])
        ans = 0
        for i in range(size):
            d1 = 1
            d2 = 1
            for j in range(size):
                d1 *= ex_m[i + j][j]
                d2 *= ex_m[i + j][size - 1 - j]
            ans += d1 - d2
        return ans

    def solve(self, frees):
        definitors = []
        s = self.size()[0]
        D = self.definitor(s)
        if D == 0:
            raise Exception(self, frees)
        else:
            for i in range(s):
                cop = Matrix.transposed(self)
                cop.matr[i] = frees
                cop = cop.transpose()
                definitors.append(cop.definitor(s) / D)
            return definitors


class SquareMatrix(Matrix):

    def __pow__(self, power):
        if power < 2:
            ans = self
        elif power == 2:
            ans = self * self
        else:
            ans = self * self ** (power - 1)
        return ans
