1. filtering PfamA Database:


The script should search for the PFAM domains given in the Liste "groups" for the different Enzymes.
For YCAO, P450 and radicalSAM the domains are hardcoded, the domains of the methyltransferases are extracted out of a .tsv file. 

Input Files:

Pfam-A.hmm: The PFAM HMM database file.
entries.tsv: TSV file containing PFAM domains of methyltranseferases.
Output Directory: Place where the Output hmm files being saved  

Running the script:

Run the script to process the input file for methyltransferases and generate HMM files.

Output HMM Files:

Separate HMM files for each defined protein group.


2. processing CDS in range:

This Python script is designed to extract biosynthetic gene sequences from GenBank files related to RiPP BGCs. The script needs you to specify the search range before and after the biosynthetic gene.

Input Directory: Path variable to the directory containing GenBank files of interest. The script will search for biosynthetic genes within these file.
BGC Types: Define the BGC (Biosynthetic Gene Cluster) types you want to search for. For example, BGC_types = ["NRPS", "PKS"] will search for NRPS and PKS.
Gene Kind: Specify the gene_kind variable to define the type to search for. (-->biosynthetic)
Search Range: Use command-line arguments to set the search range before and after the biosynthetic gene. Example:

python script.py 2 2

This will search in a range of two entries before and After the biosynthetic gene.

Output Files: The script will generate one output FASTA file per BGC type (e.g., "NRPS_antismash_DB.fasta", "PKS_antismash_DB.fasta") containing the extracted biosynthetic gene sequences.

Workflow:
The script iterates over the BGC types.
For each BGC Type, it opens an output FASTA file to store the extracted sequences.
It iterates over GenBank files in the specified directory.
For each GenBank file, the script parses the file and extracts biosynthetic gene sequences based on the criteria.
The extracted gene sequences are written to its output FASTA file.
Errors occuring during processing are displayed with an "Error" message.


3. Hmm search

The script searches sequences using HMMER (tool, using Hidden Markov Model). The script searches protein sequences in FASTA format against a database of HMM profiles and extracts matching sequences based on the given criteria.

Input FASTA Files: The script automatically identifies and processes all .fasta files in the input path folder.

Output Files: The code generates one output FASTA file per input FASTA file for each specified enzyme. The output files containing sequences that match the HMM profile for the specific enzyme.

Workflow
The script loads HMM profiles from the database path and identifies profiles associated with the enzymes of interest.
Then iterates over the input FASTA files and reads their sequences.
For each input FASTA and enzyme, the script performs HMMER sequence searches using pyhmmer.
If a Match is found: E-values below 10e-2 are extracted and saved to its corresponding output FASTA file.
The script prevents duplicate sequences from being saved to the output file.
It repeats the process for each input FASTA file and enzyme combination.

