# parallel-arrays-profiling-and-benchmarking
Parallel Arrays, Profiling, and Benchmarking

Files:
- https://github.com/swe4s/lectures/blob/master/data_integration/gtex/GTEx_Analysis_2017-06-05_v8_RNASeQCv1.1.9_gene_reads.acmg_59.gct.gz?raw=true
- https://storage.googleapis.com/gtex_analysis_v8/annotations/GTEx_Analysis_v8_Annotations_SampleAttributesDS.txt

Profiling and Benchmarking:
- you'll find two different search functions: linear and binary. Linear searching is as expected: the algorithm searches an array in order. A binary search searches like a 'dictionary'; it uses the fact that a list can be ordered, and is able to more effectively by starting in the middle of an array, moving left or right, and searching the new shortened array, and continuing.

- using the dataset provided, I tested the speed of both searches. The linear search took nearly 15 seconds to complete, while the binary was about a second. It was a 98% improvement.

- I also profiled the speed of the version with only the linear search. the results of this Cprofile (terminal command is python -m Cprofile -s tottime plot_gtex.py), and the results of this file are in plot_gtex_linear_search.txt. 

Startup:

```
import unittest
import sys
import os
import data_viz as dv
import time



```
