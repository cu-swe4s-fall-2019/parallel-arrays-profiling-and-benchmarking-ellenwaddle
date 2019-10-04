import data_viz as dv
import gzip
import sys
import matplotlib as ml
import time
import matplotlib.pylab as plt
ml.use('Agg')


t0_linear = time.time()


def linear_search(key, L):

    hit = -1
    for i in range(len(L)):
        curr = L[i]
        if key == curr:
            return i
    return -1


data_file_name =
'GTEx_Analysis_2017-06-05_v8_RNASeQCv1.1.9_gene_reads.acmg_59.gct.gz'

sample_info_file_name =
'GTEx_Analysis_v8_Annotations_SampleAttributesDS.txt'

tissue_group_name = 'SMTS'  # could also change this to 'SMTSD' for tissue type
sample_id_col_name = 'SAMPID'

samples = []
sample_info_header = None


for l in open(sample_info_file_name):
    if sample_info_header is None:
        sample_info_header = l.rstrip().split('\t')
    else:
        samples.append(l.rstrip().split('\t'))

tissue_group_idx = linear_search(tissue_group_name, sample_info_header)
sample_id_col_idx = linear_search(sample_id_col_name, sample_info_header)

groups = []
members = []

for row_idx in range(len(samples)):
    sample = samples[row_idx]
    sample_name = sample[sample_id_col_idx]
    curr_group = sample[tissue_group_idx]

    curr_group_idx = linear_search(curr_group, groups)

    if curr_group_idx == -1:
        curr_group_idx = len(groups)
        groups.append(curr_group)
        members.append([])

    members[curr_group_idx].append(sample_name)

version = None
dim = None
data_header = None

gene_name_col = 1
gene_name = 'BRCA2'

group_counts = [[] for i in range(len(groups))]

for l in gzip.open(data_file_name, 'rt'):
    if version is None:
        version = l
        continue

    if dim is None:
        dim = [int(x) for x in l.rstrip().split()]
        continue

    if data_header is None:
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

t1_linear = time.time()
total_linear_time = t1_linear-t0_linear

t0_binary = time.time()  # repeat to show time diff w binary search.


def binary_search(key, D):
    lo = -1
    hi = len(D)
    while (hi - lo > 1):
        mid = (hi + lo) // 2

        if key == D[mid][0]:
            return D[mid][1]

        if (key < D[mid][0]):
            hi = mid
        else:
            lo = mid
    return -1


tissue_group_idx = binary_search(tissue_group_name, sample_info_header)
sample_id_col_idx = binary_search(sample_id_col_name, sample_info_header)

groups = []
members = []

for row_idx in range(len(samples)):
    sample = samples[row_idx]
    sample_name = sample[sample_id_col_idx]
    curr_group = sample[tissue_group_idx]

    curr_group_idx = binary_search(curr_group, groups)

    if curr_group_idx == -1:
        curr_group_idx = len(groups)
        groups.append(curr_group)
        members.append([])

    members[curr_group_idx].append(sample_name)

version = None
dim = None
data_header = None

gene_name_col = 1
gene_name = 'BRCA2'

group_counts = [[] for i in range(len(groups))]

for l in gzip.open(data_file_name, 'rt'):
    if version is None:
        version = l
        continue

    if dim is None:
        dim = [int(x) for x in l.rstrip().split()]
        continue

    if data_header is None:
        data_header = l.rstrip().split('\t')
        continue

    A = l.rstrip().split('\t')

    if A[gene_name_col] == gene_name:
        for group_idx in range(len(groups)):
            for member in members[group_idx]:
                member_idx = binary_search(member, data_header)
                if member_idx != -1:
                    group_counts[group_idx].append(int(A[member_idx]))
        break

t1_binary = time.time()
total_binary_time = t1_binary-t0_binary
prop_increase = (total_linear_time - total_binary_time) / total_linear_time
print(total_linear_time, total_binary_time, prop_increase)

dv.boxplot(group_counts, 'BRCA2.png', tissue_group_name)


def main():
    pass


if __name__ == '__main__':
    main()
