"""
Operator overloading in pyton
"""

class Polygon:
    def __init__(self, shape, size):
        self.shape = shape
        self.size = size

    def calc(self):
        res = self.shape + self.size
        print("Result is: ", res)

    def __add__(self, other):
        sh = int(self.shape) + int(other.shape)
        si = int(self.size) + int(other.size)

        return Polygon(sh, si)

    def __repr__(self) -> str:
        return f"'Instance' - Polygon({self.shape}, {self.size})"

if __name__ == "__main__":
    p1 = Polygon(10, 20)
    p2 = Polygon(12, 22)
    # print(p1)
    # print(p2)

    p3 = p1 + p2
    # print(p3)

    print(p1.calc())
    print(p2.calc())
    print(p3.calc())

    