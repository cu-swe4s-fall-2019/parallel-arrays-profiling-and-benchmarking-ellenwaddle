import data_viz as dv
import gzip
import sys
import matplotlib as ml
ml.use('Agg')
import matplotlib.pylab as plt

def linear_search(key, L):
    hit = -1
    for i in range(len(L)):
        curr = L[i]
        if key == curr:
            return i
    return -1

data_file_name = 'GTEx_Analysis_2017-06-05_v8_RNASeQCv1.1.9_gene_reads.acmg_59.gct.gz'
sample_info_file_name = 'GTEx_Analysis_v8_Annotations_SampleAttributesDS.txt'

tissue_group_name = 'SMTS'
tissue_type_name = 'SMTSD'
sample_id_col_name = 'SAMPID'

samples = []
sample_info_header = None

def binary_search(key, L):
    lo = -1
    hi = len(D)
    while (hi - lo >1):
        mid = (hi + lo) // 2

        if key == D[mid][0]:
            return D[mid][1]

        if (key < D[mid][0]):
            hi = mid
        else:
            lo = mid
    return -1


for l in open(sample_info_file_name):
    if sample_info_header == None:
        sample_info_header=l.rstrip().split('\t')
    else:
        samples.append(l.rstrip().split('\t'))

tissue_group_idx = linear_search(tissue_group_name, sample_info_header)
tissue_type_idx = linear_search(tissue_type_name, sample_info_header)
sample_id_col_idx = linear_search(sample_id_col_name, sample_info_header)

groups = []
types = []
members = []

for row_idx in range(len(samples)):
    sample = samples[row_idx]
    sample_name = sample[sample_id_col_idx]
    curr_group = sample[tissue_group_idx]
    curr_type = sample[tissue_type_idx]

    curr_group_idx = linear_search(curr_group, groups)
    curr_type_idx = linear_search(curr_type, types)

    if curr_group_idx == -1:
        curr_group_idx = len(groups)
        groups.append(curr_group)
        members.append([])

    if curr_type_idx == -1:
        curr_type_idx = len(types)
        types.append(curr_type)
        members.append([])

    members[curr_group_idx].append(sample_name)

version = None
dim = None
data_header = None

gene_name_col = 1
gene_name = 'BRCA2'

group_counts = [ [] for i in range(len(groups))]
type_counts = [ [] for i  in range(len(types))]

for l in gzip.open(data_file_name, 'rt'):
    if version == None:
        version = l
        continue

    if dim == None:
        dim = [int(x) for x in l.rstrip().split()]
        continue

    if data_header == None:
        data_header = l.rstrip().split('\t')
        continue

    A = l.rstrip().split('\t')

    if A[gene_name_col] == gene_name:
        for group_idx in range(len(groups)):
            for member in members[group_idx]:
                member_idx = linear_search(member, data_header)
                if member_idx != -1:
                    group_counts[group_idx].append(int(A[member_idx]))
        break

        for type_idx in range(len(types)):
            for member in members[type_idx]:
                if type_idx != -1:
                    type_counts[type_idx].append(int(A[type_idx]))

        break

dv.boxplot(group_counts,'grp1', tissue_group_name)
dv.boxplot(type_counts,'grp2', tissue_type_name)



def main():
    pass

if __name__ == '__main__':
    main()
