qiime dada2 denoise-paired \
  --i-demultiplexed-seqs paired-end-demux.qza \
  --p-trim-left-f 30 \
  --p-trim-left-r 30 \
  --p-trunc-len-f 190 \
  --p-trunc-len-r 140 \
  --o-table table.qza \
  --o-representative-sequences rep-seqs.qza \
  --o-denoising-stats denoising-stats.qza
