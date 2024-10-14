slova = []
slovo = ""
stroka = input("Введите строку: ")
bukva = input("Введите букву: ")
stroka = stroka.lower()
bukva = bukva.lower()
for s in stroka:
    if s != " " and s != "\t":
        slovo += s
    else:
        if slovo.endswith(bukva):
            slova.append(slovo)
        slovo = ""
if slovo.endswith(bukva):
    slova.append(slovo)
bukva = bukva.upper()
if not slova:
    print(f"Слов, оканчивающихся на букву <{bukva}> нет")
else:
    print(f"Слова, оканчивающиеся на букву <{bukva}>:", ", ".join(slova))