Performing 16S sequencing analysis using QIIME2 on the dataset from the paper: 'Virulence genes are a signature of the microbiome in the colorectal tumor microenvironment'.

* Country: USA
* ENA Accession Code: PRJNA284355
* No. of samples = 88
* Reference link for QIIME2 pipeline: https://docs.qiime2.org/2024.10/tutorials/moving-pictures/

## SAMPLE METADATA

Get the patient metadata file from the paper and download it. Since the SRR accession codes corresponding to each sample ID are not present, run a Python code to import the IDs into the metadata file from the ENA browser and save it as a TSV file (.tsv). The code is in the file **manifest.py**. Label your metadata file as **manifest.tsv**. The TSV file should contain the columns sample_id, forward_absolute_filepath (filepath to forward read), reverse_absolute_filepath (filepath to reverse read), and sample_type (tumor or normal condition).

## IMPORTING METADATA FILE AND OBTAINING DATA

Create a QIIME2 environment using conda and import the metadata file onto QIIME2 using the code from the file **import.sh**. Once the QZA file (paired-end-demux.qza) is generated, create a QZV file (paired-end-demux.qzv) to visualize the sample reads quality on the QIIME2 viewer. The visualization code is given in **visualization.sh**. 

## DADA2

Demultiplexing is not required if the reads are already demultiplexed, i.e. if the samples and their respective barcode files are already associated in the metadata file or the manifest file. 

Perform DADA2 with the code from **dada2.sh**. The trim-lengths are the number of base pairs to be cut from the start and truncate-lengths are the number of base pairs to be cut from the end. Using the paired-end-demux.qzv file to visualize the sample data, decide the trim-length and truncate-length and change it in the code. 

##FEATURETABLE AND FEATUREDATA SUMMARIES

To analyse the resulting data, make FeatureTable and FeatureData summaries using the code given in **table.sh**. To visualize the QZA files, use the same code in **visualization.sh** to convert them to QZV files. These QZV files can be viewed on QIIME2 viewer. 

##PHYLOGENETIC TREE

To produce a phylogenetic tree from the data, use the code given in **phylogeny.sh**. 

##ALPHA AND BETA DIVERSITY ANALYSIS

