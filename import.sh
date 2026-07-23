qiime tools import \
  --type 'SampleData[PairedEndSequencesWithQuality]'\
  --input-path manifest.tsv \
  --output-path paired-end-demux.qza 
  --input-format PairedEndFastqManifestPhred33V2
