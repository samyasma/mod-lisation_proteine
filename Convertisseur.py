

# Logiciel pour rendre en fasta

alignment_filename = "4DOJ_C_BetT.fasta"
alignment_file = open(alignment_filename, 'r')
text = (alignment_file.read()).split('\n')
alignment_file.close()

sequences = {}
for line in text:
        if (not line.strip()) or line.startswith("Sequence") or line.startswith("Matched") or line.startswith("CLUSTAL") or "*" in line:
                continue
        fields = line.split()
        if fields[0] not in sequences:
                sequences[fields[0]] = fields[1]
        else:
                sequences[fields[0]] += fields[1]


result_filename = "sequence4DOJ_C_BetT.fasta"
result_file = open(result_filename, 'w')
for i in sequences:
        result_file.write(">{0}\n".format(i))
        result_file.write("{0}\n".format(sequences[i]))

result_file.close()
