from Bio.Seq import Seq
from Bio import SeqIO
import argparse

from Bio.SeqRecord import SeqRecord

def markStops(seq):
    result = ""
    i = 0
    for i in range(0, len(seq), 3):
        codon = str(seq[i:i+3])
        if codon in ["TAG", "TGA", "TAA"]:
            result += "."
        else:
            result += codon
        
    return result

def fromStart(orf):
    result = ""
    is_start = False
    for i in range(0, len(orf), 3):
        codon = str(orf[i:i+3])
        if codon == "ATG":
            is_start = True
        if is_start:
            result += codon

    return result

def findOrfs(seq, min_length):
    orfs = []
    for strand, nseq in [("+", seq), ("-", seq.reverse_complement())]:
        for frame in range(3):
            # Frame length to search codons in
            length = 3 * ((len(nseq)-frame) // 3)
            orfs.extend(
                [[fromStart(orf), strand] for orf in markStops(nseq[frame:frame+length]).split(".")]
            )
    
    return filter(lambda orf: len(orf[0]) >= min_length, orfs)

def main():

    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('-i', dest='input', help='Path to GenBank file with sequence.', type=str)
    arg_parser.add_argument('-o', dest='output', help='Path to output FASTA file', required=False,
        default='./output.fasta', type=str)
    arg_parser.add_argument('-l', dest='length', help='Minimum ORF length', required=False,
        default=30, type=int)
    args = vars(arg_parser.parse_args())

    input_path = args['input']
    output_path = args['output']
    min_length = args['length'];
    
    input_record = SeqIO.parse(input_path,"genbank")
    orfs = findOrfs(next(input_record).seq, min_length)
    records = [SeqRecord(
        Seq(orf[0]).translate(),
        id=f'ORF{index}',
        description=f'ORF{index} found with min. length {min_length}') for index, orf in enumerate(orfs)]
    SeqIO.write(records, output_path, "fasta")
    print(f"Fasta file saved as '{output_path}'")
        


if __name__ == "__main__":
    main()
