# Introducción a la Bioinformática - Trabajo Práctico

## Prerequisitos

Para correr los scripts es necesario de Python y las librerías bioinformáticas de BioPython. En Linux, estos se pueden instalar de la siguiente manera

```
sudo apt-get install software-properties-common
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt-get update
sudo apt-get install python3.8
pip install biopython
```

Una vez corridos estos comandos, ya tendrá instalado Python 3 y las librerías de BioPython.

## Ejercicio 1

El script para este ejercicio toma un archivo GenBank como entrada e imprime un archivo FASTA de salida con todos los ORF encontrados. Los archivos necesarios para el ejercicio 1 se pueden encontrar dentro del directorio ej1/. Una vez dentro de este directorio, se puede correr el programa utilizando el siguiente comando:

```
usage: orf_finder.py [-h] [-i INPUT] [-o OUTPUT] [-l LENGTH]

optional arguments:
  -h, --help  show this help message and exit
  -i INPUT    Path to GenBank file with sequence.
  -o OUTPUT   Path to output FASTA file
  -l LENGTH   Minimum ORF length
```

Por ejemplo:

```
python .\orf_finder.py -i .\files\SOD1_mrna.gb -o ORFs.fasta -l 50
```

## Ejercicio 2

El script para este ejercicio toma secuencias de aminoácidos de un archivo FASTA, realiza una consulta BLAST y guarda los resultados en un reporte de salida. Todos los archivos necesarios se encuentran dentro del directorio ej2/. Una vez dentro de este directorio, se puede correr el comando de la siguiente manera:

```
usage: aminoacids_blast.py [-h] [-i INPUT] [-o OUTPUT] [-n SIZE] [-db DATABASE] [-blastp BLASTP] [-e EVALUE]

Script to run Blast query on FASTA protein sequence.

optional arguments:
  -h, --help      show this help message and exit
  -i INPUT        Path to FASTA file
  -o OUTPUT       Path to output Blast file
  -n SIZE         BLAST hit list size
  -db DATABASE    Local database name (if running locally)
  -blastp BLASTP  Path to blastp binary (if not already in PATH)
  -e EVALUE       Expect value for saving hits
```

La consulta BLAST se puede realizar tanto de manera remota como local.
Por ejemplo, para correr el script utilizando la base de datos de NCBI remota:

```
python .\aminoacids_blast.py -i .\files\ORFs.fasta -o output.blast
```

Si se quiere correr el script de manera local, es necesario tener instalada una base de datos para realizar la consulta. Además, se necesita tener instalada la herramienta BLAST+ para ejecutar la consulta local. Esta herramienta se puede encontrar en ftp.ncbi.nlm.nih.gov/blast/executables/blast+/LATEST/ . En Linux, se puede utilizar el comando:

```
sudo apt-get install ncbi-blast+
```

Una vez instalada la herramienta, se puede agregar el directorio del ejecutable a la variable de entorno PATH o bien ingresar la ruta del ejecutable como parámetro del comando de la siguiente manera:

```
python .\aminoacids_blast.py -i .\files\ORFs.fasta -o output.blast -db 'C:\NCBI\databases\swissprot' -blastp 'C:\NCBI\blast-2.12.0+\bin\blastp.exe'
```

## Ejercicio 3

El script para este ejercicio toma varias secuencias de un archivo FASTA y realiza un alineamiento múltiple de estas. Luego se imprime el resultado de este alineamiento a un archivo .aln. Todos los archivos necesarios se encuentran dentro del directorio ej3/. Una vez dentro de este directorio, se puede correr el siguiente comando:

```
usage: multiple_alignment.py [-h] [-i INPUT] [-clustalw CLUSTALW] [-o OUTPUT]

Script to run multiple sequence alignment on FASTA sequences.

optional arguments:
  -h, --help          show this help message and exit
  -i INPUT            Path to input FASTA file with multiple sequences.
  -clustalw CLUSTALW  Path to CLUSTALW executable (if not already in PATH).
  -o OUTPUT           Path to output file.
```

Para realizar el alineamiento multiple se utiliza la herramienta ClustalW. Esta se puede descargar desde http://www.clustal.org/clustal2/#Download . En Linux, se puede descargar e instalar con el siguiente comando:

```
sudo apt install clustalw
```

Una vez instalada la herramienta, se puede agregar el directorio del ejecutable a la variable de entorno PATH o bien ingresar la ruta del ejecutable como parámetro del comando de la siguiente manera:

```
python .\multiple_alignment.py -i .\files\SOD1_sequences.fasta -clustalw 'C:\ClustalW2\clustalw2.exe' -o "output.aln"
```

## Ejercicio 4

El script de este ejercicio toma como entrada el BLAST output del ejercicio 2 y un pattern y busca ese pattern dentro de la descripcion de ese BLAST. utiliza la libreria beautifulsoup4, la cual requiere instalacion

```
pip install bs4 o pip install beautifulsoup4
```

Una vez instalada la libreria:

```
usage: ej4.py [-h] -p PATTERN [-i INPUT] [-o OUTPUT_FOLDER]

Blast Parser

optional arguments:
  -h, --help            show this help message and exit
  -p PATTERN, --pattern PATTERN
                        Pattern determinado a buscar
  -i INPUT, --input INPUT
                        path al archivo a parsear
  -o OUTPUT_FOLDER, --output_folder OUTPUT_FOLDER
                        carpeta donde guardar el archivo de salida
```

## Ejercicio 5

Este ejercicio contiene dos archivos, uno que busca los ORF posibles, y otro los motivos, ambos scripts de bash.
Se requeire la instalacion de EMBOSS

```
sudo apt-get install -y emboss
```

```
bash ./posibleORF.sh -m minSize -s pathInputSequence -o pathOutputSequence
```

```
bash ./prositeAnalysis.sh -s pathInputSequence -o pathOutputSequence
```
