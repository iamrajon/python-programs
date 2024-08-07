
class Demo(object):
    def __init__(self, data):
        self.data = data

    def __add__(self, other):
        f = str(self.data)
        s = str(other.data)

        result = f + s
        return Demo(result)
    
    def __repr__(self) -> str:
        return f"Demo({self.data})"




if __name__ == "__main__":
    d1 = Demo(10)
    d2 = Demo(20)

    d3 = d1 + d2
    print(d3)
    print(type(d3))
    print(repr(d3))
    
    