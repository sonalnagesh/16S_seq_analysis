import pandas as pd
import requests
import os

# Metadata Excel file
metadata_file = r"\\wsl.localhost\Ubuntu\home\sonal\16s\13073_2015_177_MOESM1_ESM.xlsx"

# Folder containing the FASTQ files
fastq_folder = r"\\wsl.localhost\Ubuntu\home\sonal\16s"

# Output file
output_file = "manifest2.tsv"

print("Reading metadata...")

metadata = pd.read_excel(metadata_file)

# Keep only required columns
metadata = metadata[['SampleID', 'Description']]

# Rename columns
metadata.columns = ['SampleID', 'SampleType']

print(f"Metadata contains {len(metadata)} samples.")

print("Downloading ENA run information...")

url = (
    "https://www.ebi.ac.uk/ena/portal/api/filereport?"
    "accession=PRJNA284355"
    "&result=read_run"
    "&fields=run_accession,sample_alias"
    "&format=tsv"
)

response = requests.get(url)

if response.status_code != 200:
    raise Exception("Unable to download ENA run table.")

ena = pd.read_csv(
    pd.io.common.StringIO(response.text),
    sep="\t"
)

# Keep only SRR2059295–SRR2059382
valid_runs = {f"SRR{i}" for i in range(2059295, 2059383)}

ena = ena[ena["run_accession"].isin(valid_runs)]

print(f"Using {len(ena)} SRR2059 entries.")

ena_lookup = dict(zip(ena["sample_alias"], ena["run_accession"]))

manifest = []

missing = []

for _, row in metadata.iterrows():

    sample = str(row["SampleID"]).strip()
    sample_type = str(row["SampleType"]).strip()

    if sample in ena_lookup:

        run = ena_lookup[sample]

        forward = os.path.join(
            fastq_folder,
            f"{run}_1.fastq.gz"
        )

        reverse = os.path.join(
            fastq_folder,
            f"{run}_2.fastq.gz"
        )

        manifest.append({
            "sample-id": sample,
            "forward-absolute-filepath": forward,
            "reverse-absolute-filepath": reverse,
            "sample-type": sample_type
        })

    else:

        missing.append(sample)

manifest = pd.DataFrame(manifest)

manifest.to_csv(
    output_file,
    sep="\t",
    index=False
)

print("\n=====================================")
print("Manifest successfully created!")
print("=====================================")

print(f"Matched samples : {len(manifest)}")
print(f"Missing samples : {len(missing)}")

if len(missing) > 0:

    print("\nSamples not found in ENA:")

    for s in missing:
        print(s)

print(f"\nOutput written to: {output_file}")
