import csv



pfam_hmm_database = "/Users/theohaas/Desktop/MBW_Master/2._Semester/Synthese_Naturstoffe/datasets/Pfam-A.hmm"
output_file = "/Users/theohaas/Desktop/MBW_Master/2._Semester/Synthese_Naturstoffe/output.hmm"


# Path to the TSV file with methyltranserases domains
tsv_file = "/Users/theohaas/Desktop/MBW_Master/2._Semester/Synthese_Naturstoffe/entries.tsv"

# List to store the PFAM domains. In list: ycao ("PF02624", "PF18381"), P450 ("PF00067"), radical SAM (""PF04055")
pfam_domains = ["PF00067", "PF04055", "PF02624", "PF18381"]

# Open the TSV file and read its contents
with open(tsv_file, "r") as file:
    tsv_reader = csv.reader(file, delimiter="\t")

    # Iterate over each row in the TSV file
    for row in tsv_reader:
        # Extract the PFAM domain from the first column
        pfam_domain = row[0]
        if pfam_domain.startswith("PF"):
            # Add the PFAM domain to the list
            pfam_domains.append(pfam_domain)


with open(output_file, "w") as output:
    with open(pfam_hmm_database, "r") as input_file:
        lines = input_file.read().split("//")
        for line in lines:
            if any(domain in line for domain in pfam_domains):
                output.write(line + "//")

print("Extraction complete.")

