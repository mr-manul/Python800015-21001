dico = {}
for i in range(5):
    name = input("name: ")
    number = input("number: ")
    dico[name] = number
search = input("\nsearch: ")
if search in dico:
    print(dico[search])
else:
    print("Not found \n")