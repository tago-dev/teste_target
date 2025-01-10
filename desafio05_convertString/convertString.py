textoUser = input("Digite uma palavra: ")
string_invertida = ""

for i in range(len(textoUser) - 1, -1, -1):
    string_invertida += textoUser[i]

print(string_invertida)
