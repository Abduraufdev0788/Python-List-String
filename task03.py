def numLine(line):
    a = []
    for i in line:
        a += i
    Rustam = "-".join(a)
    return Rustam
    
    
line = (input("raqamlarni kiriting: "))
print(numLine(line))