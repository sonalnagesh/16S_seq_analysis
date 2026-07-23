qiime diversity alpha-rarefaction \
  --i-table table.qza \
  --i-phylogeny rooted-tree.qza \
  --p-max-depth 250000 \
  --m-metadata-file manifest2.tsv \
  --o-visualization alpha-rarefaction.qzv
