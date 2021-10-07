from Bio import SeqIO
import sys

def main():

    # Quit if no path to .gbk file is provided
    if (len(sys.argv) < 2):
        print("Error: path to .gbk file needed as command line argument.")
        exit()
        
    file_path = sys.argv[1]

    try:
        for seq_record in SeqIO.parse(file_path, "genbank"):

            reading_frames = []

            # Translate in forward direction
            for start_idx in range(3):
                cutoff_end = (3 - start_idx) % 3
                amino_acid_sequence = seq_record[start_idx:-cutoff_end].translate()
                reading_frames.append(amino_acid_sequence)
            
            # Translate in reverse direction
            seq_reverse = seq_record[::-1]
            for start_idx in range(3):
                cutoff_end = (3 - start_idx) % 3
                amino_acid_sequence = seq_reverse[start_idx:-cutoff_end].translate()
                reading_frames.append(amino_acid_sequence)
            
            # Write to .fas file
            if (len(sys.argv) == 3):
                file_name = sys.argv[2]
            else:
                file_name = seq_record.id + ".fas"

            SeqIO.write(reading_frames, file_name, "fasta")
            print(f"Fasta file saved as '{file_name}'")
    except:
        print(f"Error: could not process file '{file_path}'.")
        exit()
        


if __name__ == "__main__":
    main()
