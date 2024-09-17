# pip install biopython
from Bio.Blast import NCBIXML
from Bio.Blast.Applications import NcbiblastnCommandline

# Define the database and query files
database = "example_db"
query_file = "MEG3_DLK1_genes.fasta"
output_file = "results.xml"

# Run BLASTn
blastn_cline = NcbiblastnCommandline(query=query_file, db=database, evalue=0.001, outfmt=5, out=output_file)
stdout, stderr = blastn_cline()

# Parse the results
with open(output_file) as result_handle:
    blast_records = NCBIXML.parse(result_handle)
    for blast_record in blast_records:
        for alignment in blast_record.alignments:
            for hsp in alignment.hsps:
                print(f"Query: {blast_record.query}")
                print(f"Subject: {alignment.title}")
                print(f"Identity: {hsp.identities} / {hsp.align_length}")
                print(f"Score: {hsp.score}")
                print(f"E-value: {hsp.expect}")
                print("-" * 80)
