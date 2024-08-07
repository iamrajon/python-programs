class Student(object):
    def __init__(self):
        self.name = "Rajon"
        self.roll = 12
        print(self)

    def disp(self):
        print(f"Name of student is: {self.name}")
        print(f"Roll of Student is: {self.roll}")


if __name__ == "__main__":
    st = Student()
    st.disp()
    print(st)

    # dt = Student()
    # print(dt)


