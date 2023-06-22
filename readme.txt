processing_CDS_in_range.py searches for CDS in defined range to biosynthetic CDS with specified enzymes.
The range (numbers of CDS to search before and after) for the search has to be entered after calling the script
by entering for example: processing_CDS_in_range.py 2 2 
This would search for two CDS to the left and two to the right.
The found sequences will be print in .fasta files including the name of the enzyme.

The script hmmer_search.py performs a search based on a hidden markov model. 

To filter the Pfam-A.hmm dataset by defined pfam domains the script filtering_PfamA_DB.py can be used.


