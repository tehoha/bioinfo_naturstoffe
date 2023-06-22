import pyhmmer


# Path to the database 
pfam_hmm_database = "/Users/theohaas/Desktop/MBW_Master/2._Semester/Synthese_Naturstoffe/output.hmm"

# Path to the input sequence file in FASTA format
input_sequence_file = "/Users/theohaas/Desktop/MBW_Master/2._Semester/Synthese_Naturstoffe/datasets/RiPP_antismash_out_genbank_files_out_full_analysis/NRPS_antismash_DB_methyltransferase.fasta"

# 
with pyhmmer.easel.SequenceFile(input_sequence_file, digital=True) as seq_file:
    sequences = list(seq_file)
# Path where to safe the outputfile 
output_file = "/Users/theohaas/Desktop/MBW_Master/2._Semester/Synthese_Naturstoffe/outputtrynew.txt"

# performing HMMER using the pyhmmer module
with open(output_file, "w") as file:
    with pyhmmer.plan7.HMMFile(pfam_hmm_database) as hmm_file:
        for hits in pyhmmer.hmmsearch(hmm_file, sequences, cpus=4):
            for hit in hits:
                evalue = hit.evalue

                # def of evalue 
                if evalue >10e-5:
                    # adding defined infos as query, accession, brief description and exact evalue 
                    file.write(f"Query: {hits.query_name.decode()}\n")
                    file.write(f"Accession: {hits.query_accession.decode()}\n")
                    file.write(f"Description: {hit.description}\n")
                    file.write(f"Score: {hit.score}\n")
                    file.write(f"E-value: {hit.evalue}\n")
                    file.write("----")
print(f"Hits saved to {output_file}")
