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


# Sobre el trabajo

**esto dijo cuando explico el tp:**
* buscar genes que expliquen la enfermedad
* como llamar a blast desde python?
* a partir de la secuencia de ese gen, responder las preguntas teóricas y prácticas.
* si es hereditaria: la mutación en el gen es lo que da el origen a la enfermedad
* si no es hereditaria, no hay un solo gen que la explica, sino que ciertas mutaciones en ciertos genes permiten predecir cómo se va a expresar esa enfermedad. 
* LA CUESTIÓN ES ENCONTRAR UN GEN (porque la secuencia es lo que necesitamos) QUE EXPRESE/EXPLIQUE la enfermedad





