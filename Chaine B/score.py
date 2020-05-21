import sys
score = ""
dico={}
with open("score_B.txt", "r") as fichier:
    for line in fichier:
        colonnes = line.split()
        #print(line)
        #print(colonnes)
        dico[colonnes[0]]=colonnes[1]


with open("BetT.B.pdb",'r') as fichier:
	for line in fichier:
		if line.startswith('ATOM'):
			colonnes=line.split()
			s=colonnes[4]
			print(line[:56]+'{0:4}'.format(dico[s]))
		else:
			print(line)

