def UnderLine(text):
    a = text.split(", ")
    a = tuple(a)
    snake_case ="_".join(a)
    print(a)
    return snake_case
    
    
    
    
    
text = input("matnni kiriting: ")
print(UnderLine(text))