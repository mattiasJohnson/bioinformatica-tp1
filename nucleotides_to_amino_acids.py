from Bio import SeqIO
import sys

# ===================FUNCTONS=================================

# Returns the 6 reading frames in a dictionary
def createReadingFrames(sequence_full):
    # Create reading frames
    reading_frames = {}

    # Create forward reading frames
    for i in range(3):
        reading_frames[i+1] = sequence_full[i:]

    # Create reverse reading frames
    sequence_full_reverse = sequence_full[::-1]
    for i in range(3):
        reading_frames[-(i+1)] = sequence_full_reverse[i:]

    # Ensure divisible by 3 by truncation
    for key, sequence in reading_frames.items():
            n_extra_nucleotides = len(sequence) % 3
            if n_extra_nucleotides != 0:
                reading_frames[key] = sequence[:-n_extra_nucleotides]

    return reading_frames


# Returns indices of ORFs
# WARNING: Needs sequence.seq object
def findORF(sequence, n_codons_min):
# Add complements?
    codons_start_RNA = ["AUG"]
    codons_start_DNA = ["ATG"]
    codons_start = codons_start_RNA + codons_start_DNA

    codons_stop_RNA = ["UAG", "UAA", "UGA"]
    codons_stop_DNA = ["TAG", "TAA", "TGA", "GAC"]
    codons_stop = codons_stop_RNA + codons_stop_DNA


# Split by stop codons
    ORF_indices_list = []
    idx_split_start = 0
    for i in range(0, len(sequence), 3):
        codon = str(sequence[i:i+3])
        
        # Check if stop codon
        if codon in codons_stop or i == len(sequence)-3:
            idx_split_end = i
            
            # Skip if split is below minumum length
            split_length = (idx_split_end -idx_split_start)/3
            if split_length < n_codons_min:
                idx_split_start = idx_split_end + 3
                continue

            # Check for orfs by finding start codons
            for j in range(idx_split_start, idx_split_end, 3):
                codon_orf = str(sequence[j:j+3])

                if codon_orf in codons_start:
                    idx_start = j
                    idx_end = idx_split_end -3 # -3 since should not include end codon
                    indices = (idx_start, idx_end)
                    codon_length = (idx_end - idx_start)/3
                    
                    if codon_length >= n_codons_min:
                        # print(f"start: {j}, end codon (not included): {idx_split_end} with length {codon_length}")
                        # print()
                        ORF_indices_list.append(indices)
                    
            # New start index
            idx_split_start = idx_split_end
            
    return ORF_indices_list


# Translates ORFs
def translateORFs(sequence_nucleotides_full, ORF_indices_list):

    # Extract ORFs from nucleotide sequence
    ORF_aminoacids_list = []
    for ORF_indices in ORF_indices_list:

        idx_start = ORF_indices[0]
        idx_end = ORF_indices[1]

        # Ensure multiple of 3
        if (idx_end - idx_start)%3 == 0:
            ORF_nucleotides = sequence_nucleotides_full[idx_start:idx_end]
        else:
            print(f"Error: number of nucleotides between start {idx_start} and end {idx_end} is not divisble by 3.")
            continue
        
        # Translate and append ORF
        ORF_aminoacids = ORF_nucleotides.translate()
        ORF_aminoacids_list.append(ORF_aminoacids)
        
    return ORF_aminoacids_list
        

# Writes aminoacids to drive
def saveORFsToFasta(ORF_aminoacids_list, sequence_id, frame="no_frame"):
    for i, ORF_aminoacids in enumerate(ORF_aminoacids_list):
        file_name = f"ORF_{sequence_id}_frame{str(frame)}_{i:02}.fas"
        file_path = "translated_ORFs/" + file_name
        SeqIO.write(ORF_aminoacids, file_path, "fasta")
        print(f"Written fasta to {file_name}")



# ===================MAIN=PROGRAM=============================

def main():
    
    # PARSE COMMAND LINE ARGUMENT
    # Quit if no path to .gb file is provided
    if (len(sys.argv) < 2):
        print("Error: provide path to")
        exit()
        
    file_path = sys.argv[1]
    
    # Optional - set minimum number of codons
    n_codons_min = 20
    if (len(sys.argv) == 3):
        n_codons_min = int(sys.argv[2])

    
    # Check if supported file extension
    file_extension = file_path.split(".")[-1]
    file_formats = {
        "gbk": "genbank",
        "gb": "genbank",
        "fas": "fasta",
        "fasta": "fasta"
    }
    if file_extension not in file_formats:
        print(f"Error: file extension .{file_extension} not supported.")
        quit()

    file_format = file_formats[file_extension]


    # PARSE GENBANK FILE
    try:
        sequence_nucleotides_full = list(SeqIO.parse(file_path, "genbank"))[0]
    except:
        print("Error: could not parse {file_path}")
        quit()
        
        
    # CREATE READING FRAMES
    reading_frames = createReadingFrames(sequence_nucleotides_full)
    
    for key, sequence in reading_frames.items():
        
        # GET ORF INDICES
        ORF_indices_list = findORF(sequence.seq, n_codons_min)
    

        # TRANSLATE ORFs
        ORF_aminoacids_list = translateORFs(sequence, ORF_indices_list)


        # SAVE TRANSLATED ORFS TO DISK
        saveORFsToFasta(ORF_aminoacids_list, sequence.id, key)
            


if __name__ == "__main__":
    main()