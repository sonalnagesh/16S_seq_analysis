#SILVA_classifier#
qiime feature-classifier classify-sklearn \
  --i-classifier SILVA138.2_SSURef_NR99_weighted_classifier_full-length_human-stool.qza \
  --i-reads rep-seqs.qza \
  --o-classification taxonomy_SILVA.qza

#GreenGenes_classifier#
qiime feature-classifier classify-sklearn \
  --i-classifier 2024.09.backbone.full-length.nb.sklearn-1.4.2.qza \
  --i-reads rep-seqs.qza \
  --o-classification taxonomy_GG.qza
