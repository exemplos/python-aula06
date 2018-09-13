

f = open("nomes.txt", "r", encoding="utf-8")
lines = f.read().splitlines()
f.close()

print("Nomes já incluidos")
print(lines)

nome = ""
while nome != "N":
    nome = input("Digite um nome:")
    nome = nome.upper()
    if(nome != "N"):
        if nome not in lines:
            lines.append(nome)
        else:    
            print("Nome ja inserido")

f = open("nomes.txt", "w", encoding="utf-8")

print("Após novas inserções")
for line in lines:
    f.write(line + "\n")

print(lines)