with open('input.txt', 'r', encoding='utf-8') as fichier:
    instructions = fichier.read().split()

res = 0
res_temp = ""

def maximum(chaine):
    """
    Fonction qui détermine le maximum d'une chaine de nombre 
    ainsi que son indice dans la chaine
    
    :param chaine: la chaine de nombre
    """
    maxi = -1
    #print(chaine)
    for i in range(len(chaine)):
        if int(chaine[i]) > maxi:
            maxi = int(chaine[i])
            indice = i
    return maxi, indice


for batteries in instructions:
    maxi = -1
    digits = 11
    indice = 0
    for i in range(digits, -1, -1):
        if i == 0:
            maxi, temp = maximum(batteries[indice:])
            res_temp += str(maxi)
            break
        maxi, temp = maximum(batteries[indice:-i])
        indice += temp+1
        res_temp += str(maxi)
    res += int(res_temp)
    res_temp = ""

print(res)