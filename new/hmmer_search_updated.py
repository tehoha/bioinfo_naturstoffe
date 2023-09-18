import os
import pyhmmer
from Bio import SeqIO

# Path to the database
pfam_hmm_database = "/Users/theohaas/Desktop/MBW_Master/2._Semester/Synthese_Naturstoffe/output_hmm/"

# Input path folder containing .fasta files
input_path = "/Users/theohaas/Desktop/MBW_Master/2._Semester/Synthese_Naturstoffe/testrun_folder/RiPP_antismash_shortset"
output_path = "/Users/theohaas/Desktop/MBW_Master/2._Semester/Synthese_Naturstoffe/testrun_folder/RiPP_antismash_shortset/output"


enzymes = ["ycao", "P450", "radical SAM", "methyltransferase"]
#enzymes = [["ycao", "ycaO", "YCAO"], ["P450", "p450"], ["radical SAM"], ["methyltransferase"]]

# List all files in the input path folder with .fasta extension
fasta_files = [f for f in os.listdir(input_path) if f.endswith(".fasta")]

# Load sequences into a dictionary
sequences_dict = {}
dict_filnames = {}

for filename in os.listdir(pfam_hmm_database):
    for enzyme in enzymes:
        if enzyme in filename:
            # Perform actions with the matched file
            file_path = os.path.join(pfam_hmm_database, filename)

            #enzyme_output_path = os.path.join(output_path, f"{enzyme}_hmmer.fasta")

            for fasta_file in fasta_files:
                # Construct the input and output file paths
                input_sequence_file = os.path.join(input_path, fasta_file)
                output_file = os.path.join(output_path, f"{os.path.splitext(fasta_file)[0]}_{enzyme}_hmmer.fasta")
                print(input_sequence_file)
                for record in SeqIO.parse(input_sequence_file, "fasta"):
                    header = record.description
                    #sequence = str(record.seq)
                    sequences_dict[header] = record

                records_in_fasta = []
                # Perform HMMER using the pyhmmer module
                with pyhmmer.easel.SequenceFile(input_sequence_file, digital=True) as seq_file:
                    sequences = list(seq_file)

                with open(output_file, "w") as output_file:
                    
                    with pyhmmer.plan7.HMMFile(file_path) as hmm_file:
                        for hits in pyhmmer.hmmsearch(hmm_file, sequences, cpus=4):
                            for hit in hits:
                                evalue = hit.evalue
                                hit_name = hit.name
                                hit_description = hit.description
                                #print(dir(hit))

                                #start_index = hit_description.find(b"(") + 1
                                #end_index = hit_description.find(b")")
                                extracted_part = hit_name.decode() + " " +  hit_description.decode()

                                #[start_index:end_index].decode()
                                if extracted_part in records_in_fasta:
                                    continue
                                # Check evalue
                                if evalue < 10e-2:
                                    record = sequences_dict[extracted_part]
                                    #print(record.id)

                                    SeqIO.write(record, output_file, "fasta")
                                    records_in_fasta.append(extracted_part)
                                    break

            print(f"Hits saved to {output_file}")

