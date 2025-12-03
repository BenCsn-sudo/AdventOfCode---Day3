with open('input.txt', 'r', encoding='utf-8') as fichier:
    instructions = fichier.read().split()

res = 0
passe = True


for batteries in instructions:
    maxi1 = 0
    maxi2 = 0
    indice = 0
    for i in range(len(batteries)):
        if i == len(batteries)-1:
                if maxi1 == 0:
                    passe = False
                    res += maxi1
                break
        if int(batteries[i]) > maxi1:
            maxi1 = int(batteries[i])
            indices = i
    if passe:
        for e in range(indices+1, len(batteries)):
            if int(batteries[e]) > maxi2:
                maxi2 = int(batteries[e])
        res += int(str(maxi1)+str(maxi2))
    passe = True

print(res)