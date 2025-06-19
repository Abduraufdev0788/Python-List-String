def ismni_ozg(fish:str):
    name = fish.split()
    SurName = name[0]
    ism_va_sharif = ' '.join(name[1:])
    natija = f" {ism_va_sharif}, {SurName}"
    return natija

fish = input("familya ism sharifingizni kirrriting: ")
print(ismni_ozg(fish))
    