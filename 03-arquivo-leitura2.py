
f = open("arquivo2.txt", "r", encoding="utf-8")
lines = f.read().splitlines()
for line in lines:
    print(line)

f.close()