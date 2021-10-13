**How to use GBK_to_FASTA.py**
```bash
python nucleotides_to_amino_acids.py path_to_sequence_file

# Optional second argument to name the output .fas file
python nucleotides_to_amino_acids.py files/sod1_mrna.gb output_file.fas
```

**How to import amino acids from .fas**
```python
reading_frames = []
for amino_acid in SeqIO.parse("works.fas", "fasta"):
    reading_frames.append(amino_acid)
```

---

# Links
* biopython reference ([biopython.org](http://biopython.org/DIST/docs/tutorial/Tutorial.html)).
* Download from genbank ([reddit.com](https://www.reddit.com/r/bioinformatics/comments/5h4qnc/what_is_the_best_way_to_download_genbank_data/)).





