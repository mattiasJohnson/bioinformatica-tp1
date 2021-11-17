#!/bin/bash

# default values
declare sequence outseq
sequence="files/sod1_mrna.orf"
outseq="files/sod1_mrna.patmatmotifs"

while getopts s:o: flag
do
    case "${flag}" in
        s) sequence=${OPTARG};;
        o) outseq=${OPTARG};;
    esac
done
echo "Running patmatmotifs with: "
echo "sequence: $sequence";
echo "outseq: $outseq";

patmatmotifs -full -sequence $sequence -outfile $outseq