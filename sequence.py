import sys

def from3to1(aa):
    if aa == "ALA":
        return "A"
    elif aa == "ARG" :
        return "R"
    elif aa == "HIS" :
        return "H"
    elif aa == "LYS" :
        return "K"
    elif aa == "ASP" :
        return "D"
    elif aa == "GLU" :
        return "E"
    elif aa == "SER" :
        return "S"
    elif aa == "THR" :
        return "T"
    elif aa == "ASN" :
        return "N"
    elif aa == "GLN" :
        return "Q"
    elif aa == "CYS" :
        return "C"
    elif aa == "GLY" :
        return "G"
    elif aa == "PRO" :
        return "P"
    elif aa == "VAL" :
        return "V"
    elif aa == "ILE" :
        return "I"
    elif aa == "LEU" :
        return "L"
    elif aa == "MET" :
        return "M"
    elif aa == "PHE" :
        return "F"
    elif aa == "TYR" :
        return "Y"
    elif aa == "TRP" :
        return "W"


chaine = sys.argv[1]

"""protein = open("protein.pdb",'r')
text =((protein.read()).split('\n'))
protein.closed
print(text)"""


"""fichier = open("4DOJ.pdb", "r")
text= fichier.read().split('\n')
fichier.close()"""


sequence = ""
with open("4DOJ.pdb", "r") as fichier:
    for line in fichier:
        colonnes = line.split()
        #print(line)
        #print(colonnes)
        if colonnes[0] == "ATOM" and colonnes[2] == "CA" and line[21] == chaine:
            sequence += from3to1(colonnes[3])
            #print(sequence)

print(sequence)
