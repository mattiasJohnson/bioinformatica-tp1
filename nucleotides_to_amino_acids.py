from Bio import SeqIO
import sys

def main():

    # Quit if no path to .gbk file is provided
    if (len(sys.argv) < 2):
        print("Error: path to sequence file needed as command line argument.")
        exit()
        
    file_path = sys.argv[1]
    
    # Check if supported file extension
    file_extension = file_path.split(".")[-1]
    file_formats = {
        "gbk": "genbank",
        "fas": "fasta",
        "fasta": "fasta"
    }
    if file_extension not in file_formats:
        print(f"Error: file extension .{file_extension} not supported.")
        quit()

    file_format = file_formats[file_extension]

    # Translate and write to file
    try:
        for seq_record in SeqIO.parse(file_path, file_format):

            n_nucleotides = len(seq_record)
            reading_frames = []

            # Translate in forward direction
            for start_idx in range(3):

                # Ensure sequence multiple of 3
                cutoff = (n_nucleotides - start_idx) % 3
                end_idx = (n_nucleotides- start_idx) - cutoff + start_idx
                
                # Translate
                amino_acid_sequence = seq_record[start_idx:end_idx].translate()
                reading_frames.append(amino_acid_sequence)
            
            # Translate in reverse direction
            seq_reverse = seq_record[::-1]
            for start_idx in range(3):

                # Ensure sequence multiple of 3
                cutoff = (n_nucleotides - start_idx) % 3
                end_idx = (n_nucleotides - start_idx) - cutoff + start_idx

                # Translate
                amino_acid_sequence = seq_reverse[start_idx:end_idx].translate()
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
