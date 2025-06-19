def echo(text:str):
    a = text.split("|")
    while True:
        for i in a:  
            print(i)

text = input("matn kiriting (|) : ")
print(echo(text))