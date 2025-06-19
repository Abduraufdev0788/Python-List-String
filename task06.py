def teskari_soz(matn:str):
    a = matn.split(" ")
    lists = []
    for i in a:
        if i == i[::-1]:
            lists.append(i)
    return lists    
            
matn = input("matnni kiriting: ")
print(teskari_soz(matn))