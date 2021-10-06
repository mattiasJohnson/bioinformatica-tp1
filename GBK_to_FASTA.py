from Bio import SeqIO
import sys

def main():

    # Quit if no path to .gbk file is provided
    if (len(sys.argv) < 2):
        print("Error: path to .gbk file needed as command line argument.")
        exit()
        
    file_path = sys.argv[1]

    # Try parsing and saving .gbk file as a .fas
    try:
        for seq_record in SeqIO.parse(file_path, "genbank"):
            
            # Translation
            aminoacid_sequence = seq_record.translate()
            
            # Set .fas file name
            if (len(sys.argv) == 3):
                output_file_path = sys.argv[2]
            else:
                output_file_path = seq_record.id + ".fas"

            # Save as .fasta
            SeqIO.write(aminoacid_sequence, output_file_path, "fasta")
            print(f"Fasta file saved as {output_file_path}")

    except:
        print(f"Error: could not process file '{file_path}'.")
        exit()
        


if __name__ == "__main__":
    main()
