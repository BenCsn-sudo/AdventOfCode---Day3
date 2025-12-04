with open('input.txt', 'r', encoding='utf-8') as fichier:
    instructions = fichier.read().split()

res = 0

for batteries in instructions:
    maxi1 = -1
    indice = -1
    
    # On trouve le max pour les dizaines
    # On s'arrête avant le dernier chiffre pour laisser de la place au 2ème
    for i in range(len(batteries) - 1):
        val = int(batteries[i])
        if val > maxi1:
            maxi1 = val
            indice = i
            
    # 2. Trouver le max pour les unités
    maxi2 = 0
    # Si on a trouvé un premier chiffre valide
    if indice != -1:
        for i in range(indice + 1, len(batteries)):
            val = int(batteries[i])
            if val > maxi2:
                maxi2 = val
        
        # Calcul mathématique simple
        res += (maxi1 * 10) + maxi2

print(res)