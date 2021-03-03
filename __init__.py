class calc:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def diff(self):
        return self.a - self.b

    def mul(self):
        return self.a * self.b

    def div(self):
        return self.a / self.b


x = int(input("a="))
y = int(input("b="))
obj = calc(x, y)
choice = 1
while choice!=0:
    print("0 to exit")
    print("1 to addition")
    print("2 to subtraction")
    print("3 to multiplication")
    print("4 for division")
    choice = int(input("enter choice"))
    if choice == 1:
        print("sum=", obj.add())
    elif choice == 2:
        print("diff=", obj.diff())
    elif choice == 3:
        print("prod=", obj.mul())
    elif choice == 4:
        print("quot=", obj.div())
    else:
        print("invalid option")



