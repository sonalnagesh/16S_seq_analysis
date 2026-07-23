import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ==========================================
# Read Shannon diversity values
# ==========================================

shannon = pd.read_csv(
    "shannon_entropy.tsv",
    sep="\t"
)

# Rename columns
shannon = shannon.rename(columns={
    "Sample ID": "SampleID",
    "shannon_entropy": "Shannon"
})

# Remove QIIME metadata row if present
shannon = shannon[shannon["SampleID"] != "#q2:types"]

# Convert Shannon values to numeric
shannon["Shannon"] = pd.to_numeric(shannon["Shannon"], errors="coerce")

# Remove any rows with missing Shannon values
shannon = shannon.dropna(subset=["Shannon"])

print("Shannon table:")
print(shannon.head())

# ==========================================
# Read metadata (manifest)
# ==========================================

metadata = pd.read_csv(
    "manifest2.tsv",
    sep="\t"
)

# Rename Sample ID column
metadata = metadata.rename(columns={
    "sample-id": "SampleID"
})

print("\nMetadata:")
print(metadata.head())

# ==========================================
# Merge Shannon values with metadata
# ==========================================

data = pd.merge(shannon, metadata, on="SampleID")

print("\nMerged dataframe:")
print(data.head())

print("\nColumn types:")
print(data.dtypes)

# Ensure sample-type is lowercase
data["sample-type"] = data["sample-type"].str.lower()

# ==========================================
# Plot
# ==========================================

plt.figure(figsize=(6,6))

sns.boxplot(
    data=data,
    x="sample-type",
    y="Shannon",
    order=["normal", "tumor"],
    showfliers=False
)

sns.stripplot(
    data=data,
    x="sample-type",
    y="Shannon",
    order=["normal", "tumor"],
    color="black",
    jitter=0.2,
    size=5
)

plt.title("Shannon Diversity")
plt.xlabel("")
plt.ylabel("Shannon Index")

plt.tight_layout()

plt.savefig("Shannon_Boxplot.png", dpi=300)

plt.show()
