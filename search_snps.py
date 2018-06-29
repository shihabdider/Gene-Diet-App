import csv

class Gene:
    def __init__(self):
        self.gene_name = ''
        self.snps = []
        self.phenotype = []

gene_list = []
with open('Gene_Selection.csv', 'r') as gene_map:
    for line in gene_map:
        clean_line = []
        if '"' not in line:
            clean_line.extend(line.strip().split(','))
        else:
            for elem in line.strip().split('"'):
                if elem not in [',', '']:
                    if elem.endswith(','):
                        clean_line.append(elem[:-1])
                    else:
                        clean_line.append(elem)
        
        gene_list.append(clean_line)

gene_objs = []

for entry in gene_list:
    gene_obj = Gene()
    gene_objs.append(gene_obj)
    if len(entry[0].split(',')) == 2:
        gene_obj.gene_name = entry[0].split(',')[0]
        gene_obj.snps.append(entry[0].split(',')[1]) 
        gene_obj.snps += entry[1].split(',')
    else:
        gene_obj.gene_name = entry[0]
        gene_obj.snps = entry[1].split(',')
    if len(entry) > 2:
        gene_obj.phenotype = entry[2].split(',')

with open('huA9AFFD_23andme.txt', 'r') as client_1:
    for line in client_1:
        if not line.startswith('#'):
            client_snp = line.split()[0]
            for gene_obj in gene_objs:
                if client_snp in gene_obj.snps:
                    print gene_obj.gene_name, client_snp, gene_obj.phenotype

print len(gene_objs)
