import data_viz as dv
import gzip
import sys
import matplotlib as ml
import time
import matplotlib.pylab as plt
from hash-tables-ellenwaddle import hash_functions as hf
from hash-tables-ellenwaddle import hash_tables as ht
ml.use('Agg')

###use this script to plot gene expression distribution in tissue groups (SMST)
#t0_linear = time.time()


data_file_name =
'GTEx_Analysis_2017-06-05_v8_RNASeQCv1.1.9_gene_reads.acmg_59.gct'
sample_info_file_name =
'GTEx_Analysis_v8_Annotations_SampleAttributesDS.txt'
tissue_group_name = 'SMTS'  # could also change this to 'SMTSD' for tissue type
sample_id_col_name = 'SAMPID'
gene_name = 'BRCA2'


def linear_search(key, L):

    hit = -1
    for i in range(len(L)):
        curr = L[i]
        if key == curr:
            return i
    return -1


samples = []
sample_info_header = None


def hashfct(group, file):
    header = None
    target = []
    hash = ht.ChainedHash(90000, hf.h_rolling)

    for l in open(file):
        sample_data = l.rstrip().split('\t')
        if header is None:
            header = sample_data
            continue

        sample_id = linear_search('SAMPID', header)
        target_id = linear_search(group, header)

        if target_id == -1:
            return None, target

        key = sample_data[target_id]
        val = sample_data[sample_id]
        query = hash.search(key)

        if search is None:
            hash.add(key, [val])
            target.append(key)
        else:
            search.append(value)

        return hash, target




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

for l in open(data_file_name, 'rt'): #no longer a gzip so I removed gzip.open
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

#t1_binary = time.time()
#total_binary_time = t1_binary-t0_binary
#prop_increase = (total_linear_time - total_binary_time) / total_linear_time
#print(total_linear_time, total_binary_time, prop_increase)



def main():
    parser = argparse.ArgumentParser(
                description='find tissue counts for specific gene',
                prog='bay')
    parser.add_argument('--gene_reads',
                type=str,
                help='GTEX gene counts',
                required=True)
    parser.add_argument('--sample',
                type=str,
                help='GTEX samples file',
                required=True)
    parser.add_argument('--gene',
                type=str,
                help='gene name',
                required=True)
    parser.add_argument('--output_file',
                type=str,
                help='desired output file name',
                required=True)

    args=parser.parse_args()

    version = None
    dim = None
    count_headers = None
    for l in gzip.open(args.gene_reads, 'rt'):
        if version is None:
            v = l
            continue
        if dim is None:
            dim = l
            continue
        if count_headers is None:
            count_headers = l.rstrip.split('\t')
            count_h = []
            for i in range(len(count_headers)):
                count_h.append([count_header[i], i])

        counts = l.rstrip().split('\t')
        d_id = linear_search('Description', count_headers)

    if counts[d_id] == args.gene: #might need to change this
        to_return = []
        chainedhash = ht.ChainedHash(1000000, hf.h_rolling)
        for i in range (d_id +1, len(count_headers)):
            chainedhash.add(count_headers[i], int(counts[i]))
        for t in group:
            list_counts = []
            location = table.search(t)
            if location is None:
                continue
            for s in location:
                count = chainedhash.search(s)
                if count is None:
                    continue
                list_counts.append(count)
            to_return.append(list_counts)

        dv.boxplot(to_return, args.output_file, 'x', 'y', 'title', groups = group)

if __name__ == '__main__':
    main()
