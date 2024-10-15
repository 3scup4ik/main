def ascii(x):
    result = ''
    for a in x:
        ascii_code = ord(a)
        if 'A' <= a <= 'Z':
            result += chr(ascii_code + 32)
        else:
            result += a
    return result
def Join(slova):
    string = ''
    for ss in slova:
        string += str(ss)
        string += ', '
    string = string[:-2]
    return string
slova = []
slovo = ""
stroka = input("Введите строку: ")
bukva = input("Введите букву: ")
stroka = ascii(stroka)
bukva = ascii(bukva)
print(bukva)
for s in stroka:
    if s != " " and s != "\t":
        slovo += s
    else:
        if slovo == "":
            continue
        else:
            if slovo[-1] == bukva:
                slova.append(slovo)
            slovo = ""
if slovo[-1] == bukva:
    slova.append(slovo)
if not slova:
    print(f"Слов, оканчивающихся на букву <{bukva}> нет")
else:
    print(f"Слова оканчивающиеся на букву {bukva}:", Join(slova))
