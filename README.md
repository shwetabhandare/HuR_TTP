# HuR_TTP 

This repository consists of PAR-CLIP data sets used to test HuR, and TTP on computational methods. 

#Prerequisites:

1. Download PyML and install it. Here is the link:
https://sourceforge.net/projects/pyml/
2. Make sure PyML is present in the PYTHON_PATH directory.
3. Verify that PyML is installed correctly by running python

```>>> from PyML import *```

#Data sets
The data directory contains data sets that were obtained from the authors of the following two papers:

1. HuR: http://www.sciencedirect.com/science/article/pii/S1097276511004229
2. TTP: http://www.genomebiology.com/2014/15/1/R12
3. The bedFiles directory under data/ contains bed files that were obtained from the above two links
4. HuR: to_ucsc.fp_0.05.filtered.hg19.elavl1_conservative.bed
5. TTP: GSM1286117_ZFP36_clusters.bed
6. The other bed files in the directory contain HuR specific clusters, TTP specific clusters, and clusters that are common to both HuR and TTP. These were obtained using bedtools intersect option. 


