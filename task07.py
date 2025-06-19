def beatiful_name(text:str):
    a = text.split(", ")
    for i in a:
        print(i)
    
    
    
text = input("Formatni kiriting : ")
print(beatiful_name(text))