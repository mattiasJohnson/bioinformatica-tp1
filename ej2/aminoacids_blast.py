from Bio import SeqIO
from Bio.Blast import NCBIWWW
from Bio.Blast.Applications import NcbiblastpCommandline
import argparse

def main():

    arg_parser = argparse.ArgumentParser(description='Script to run Blast query on FASTA protein sequence.')
    arg_parser.add_argument('-i', dest='input', help='Path to FASTA file', type=str)
    arg_parser.add_argument('-o', dest='output', help='Path to output Blast file', required=False,
        default='./output.blast', type=str)
    arg_parser.add_argument('-n', dest='size', help='BLAST hit list size', required=False,
        default=50, type=int)
    arg_parser.add_argument('-db', dest='database', help='Local database name (if running locally)', required=False,
        default=None, type=str)
    arg_parser.add_argument('-blastp', dest='blastp', help='Path to blastp binary (if not already in PATH)', required=False,
        default=None, type=str)
    arg_parser.add_argument('-e', dest='evalue', help='Expect value for saving hits', required=False,
        default=10, type=str)
    
    args = vars(arg_parser.parse_args())

    input_path = args['input']
    output_path = args['output']
    hitlist_size = args['size']
    database = args['database'];
    blastp = args['blastp'] if args['blastp'] is not None else 'blastp'
    evalue = args['evalue']
    
    # Check if supported file extension
    file_extension = input_path.split(".")[-1]
    file_formats = {
        "fas": "fasta",
        "fasta": "fasta"
    }
    if file_extension not in file_formats:
        print(f"Error: file extension .{file_extension} not supported. File must be in FASTA format.")
        quit()

    if database is None:
        try:
            save_file = open(output_path, "w")
            input_file = open(input_path)
            print("Querying NCBI database...")
            result = NCBIWWW.qblast("blastp", "nr", input_file.read(), hitlist_size=hitlist_size, expect=evalue)
            print("Saving BLAST report...")
            save_file.write(result.read())
            result.close()
            save_file.close()
            print(f"BLAST report saved in {output_path}")    
        except Exception as e:
            save_file.close()
            result.close()
            print(e)
    else:
        print(f"Querying local {database} database...")
        blastx_cline = NcbiblastpCommandline(cmd=blastp, query=input_path, db=database, evalue=evalue,
                                            outfmt=5, out=f'{output_path}.blast', num_alignments=hitlist_size)
        stdout, stderr = blastx_cline()

if __name__ == "__main__":
    main()
