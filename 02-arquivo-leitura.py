

with open("arquivo2.txt") as f:
    lines = f.read().splitlines()
    for line in lines:
        print(line)
