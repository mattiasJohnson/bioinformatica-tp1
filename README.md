**How to use nucleotides_to_amino_acids.py**
```bash
python nucleotides_to_amino_acids.py path_to_sequence_file

# Optional second argument to give minimum number of codons (default = 20)
python nucleotides_to_amino_acids.py files/sod1_mrna.gb 15
```
* Fasta files will be saved in `translated_ORFs/`


# Guía rápida de Git
`git pull` - "pull down", cada vez antes que empiezas a trabajar cargas de github asi que estás con el codigo más reciente.

`git add archivo1` - añadir archivos en que has cambiado

`git commit -m "una corta explicación de lo que hiciste"` - hacer una commit (es como una saving point) con todos los archivos que has anadido.

`git push origin master` - hacer una push asi que el codigo se pone en Github.


**Se puede añadir muchos archivos a la vez**<br>
`git add archivo1 archivo2 archivo3 ...`


**Ver cuales archivos has anadido y que tal**<br>
`git status`

**Descargar el proyecto la primera vez**<br>
`git clone https://github.com/mattiasJohnson/bioinformatica-tp1.git`

---

# Links
* biopython reference ([biopython.org](http://biopython.org/DIST/docs/tutorial/Tutorial.html)).
* Download from genbank ([reddit.com](https://www.reddit.com/r/bioinformatics/comments/5h4qnc/what_is_the_best_way_to_download_genbank_data/)).
