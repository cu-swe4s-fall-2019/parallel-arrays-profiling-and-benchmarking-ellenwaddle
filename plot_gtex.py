import data_viz as dv
import gzip
import sys
import argparse
import matplotlib as ml
import time
import matplotlib.pylab as plt
sys.path.insert(1, "./hash-tables-ellenwaddle")
import hash_functions as hf
import hash_tables as ht
ml.use('Agg')

###use this script to plot gene expression distribution in tissue groups (SMST)

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


#tissue_group_idx = linear_search(tissue_group_name, sample_info_header)
#sample_id_col_idx = linear_search(sample_id_col_name, sample_info_header)

#groups = []
#members = []

#for row_idx in range(len(samples)):
#    sample = samples[row_idx]
#    sample_name = sample[sample_id_col_idx]
#    curr_group = sample[tissue_group_idx]

#    curr_group_idx = linear_search(curr_group, groups)

#    if curr_group_idx == -1:
#        curr_group_idx = len(groups)
#        groups.append(curr_group)
#        members.append([])

#    members[curr_group_idx].append(sample_name)

version = None
dim = None
data_header = None

gene_name_col = 1
gene_name = 'BRCA2'


version = None
dim = None
data_header = None

gene_name_col = 1

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
    parser.add_argument('--group_type',
                type=str,
                help='group: either SMTS or SMTSD',
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
    for l in open(args.gene_reads, 'rt'):
        if version is None:
            v = l
            continue
        if dim is None:
            dim = l
            continue
        if count_headers is None:
            count_headers = l.rstrip.split('\t')
            for i in range(len(count_headers)):
                cch.append([count_headers[i], i])
            continue

    counts = l.rstrip().split('\t')
    desc = linear_search('Description', count_headers)

    if counts[desc] == args.gene:
        to_return = []
        chainedhash = ht.ChainedHash(1000000, hf.h_rolling)
        for i in range (desc +1, len(count_headers)):
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
