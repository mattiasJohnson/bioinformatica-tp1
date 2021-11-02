from Bio import SeqIO
from Bio.Align.Applications import ClustalwCommandline
import argparse
import os

def main():
    arg_parser = argparse.ArgumentParser(description='Script to run multiple sequence alignment on FASTA sequences.')
    arg_parser.add_argument('-i', dest='input', help='Path to input FASTA file with multiple sequences.', type=str)
    arg_parser.add_argument('-clustalw', dest='clustalw', help='Path to CLUSTALW executable (if not already in PATH).', 
        required=False, type=str)
    arg_parser.add_argument('-o', dest='output', help='Path to output file.', required=False,
        default='./msa.out', type=str)

    args = vars(arg_parser.parse_args())

    input_path = args['input'];
    output_path = args['output'];
    clustalw_exe = args['clustalw'] if args['clustalw'] is not None else 'clustalw2'

    # Check if supported file extension
    file_extension = input_path.split(".")[-1]
    file_formats = {
        "fas": "fasta",
        "fasta": "fasta"
    }
    if file_extension not in file_formats:
        print(f"Error: file extension .{file_extension} not supported. File must be in FASTA format.")
        quit()
    
    file_format = file_formats[file_extension]
    record = SeqIO.parse(input_path, file_format)
    cline = ClustalwCommandline(clustalw_exe, infile=input_path)
    stdout, stderr = cline()

if __name__ == "__main__":
    main()