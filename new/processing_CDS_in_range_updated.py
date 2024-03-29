from Bio import SeqIO
import os
import argparse

# Set path to the dataset directory and define BGC types and gene kind to search for
path = '/Users/theohaas/Desktop/MBW_Master/2._Semester/Synthese_Naturstoffe/testrun_folder/RiPP_antismash_shortset/'
BGC_types = ["NRPS", "PKS"]
gene_kind = "biosynthetic"

# Create the parser for input of search range 
parser = argparse.ArgumentParser()
parser.add_argument('search_range_before', help='Number of CDS to check before the biosynthetic gene')
parser.add_argument('search_range_after', help='Number of CDS to check after the biosynthetic gene')
# Parse the arguments
args = parser.parse_args()

# Convert the search range arguments to integers
num_cds_before = int(args.search_range_before)  # Number of CDS to check before the biosynthetic gene
num_cds_after = int(args.search_range_after)  # Number of CDS to check after the biosynthetic gene


# Iterate over BGC types
for BGC_type in BGC_types:
    # Create the output file for the current BGC type
    output_path = open(path + BGC_type + "_antismash_DB" + ".fasta", "w")

    # Iterate over files in the dataset directory
    for progenome_file in os.listdir(path):
        if progenome_file.endswith(".gbk"):
            try:
                # Parse the GenBank file
                for seq_record in SeqIO.parse(path + progenome_file, "gb"):

                    # Get all CDS features in the sequence record
                    cds_features = [feature for feature in seq_record.features if feature.type == "CDS"]
                    enzyme_sequences = []

                    # Iterate over the CDS features
                    for i, seq_feature in enumerate(cds_features):
                        # Check if the gene_kind is "biosynthetic"
                        if seq_feature.qualifiers.get("gene_kind", [""])[0] == gene_kind:
                            # Check surrounding CDS within the specified range
                            start_index = max(i - num_cds_before, 0)
                            end_index = min(i + num_cds_after + 1, len(cds_features))

                            # Iterate over nearby CDS features
                            for nearby_feature in cds_features[start_index:end_index]:
                                if nearby_feature.qualifiers.get("gene_kind", [""])[0] != gene_kind:
                                    assert len(nearby_feature.qualifiers['translation']) == 1
                                    # Generate the enzyme sequence entry
                                    enzyme_sequence = (
                                        ">%s from %s (%s)\n%s\n" % (
                                            nearby_feature.qualifiers['locus_tag'][0],
                                            seq_record.name,
                                            nearby_feature.qualifiers["product"],
                                            nearby_feature.qualifiers['translation'][0]))
                                    enzyme_sequences.append(enzyme_sequence)

                    # Write the enzyme sequences to the output file if any were found
                    if enzyme_sequences:
                        output_path.write('\n'.join(enzyme_sequences))

            except Exception as e:
                print("Error:", e)

    # Close the output file
    output_path.close()
