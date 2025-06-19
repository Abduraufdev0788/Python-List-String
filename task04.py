def email_Domen(mail:str):
    domen = []
    a = mail.split(",")
    for i in a:
        if "@" in i :
            num = i.index("@")
            right_hand = i[num :]
            domen.append(right_hand)
            
        else:
            print(f"Xatolik: '{i.strip()}' noto‘g‘ri email!")
    return domen    
    


mail = input("Emaillarni kiriting:  ")
print(email_Domen(mail))
