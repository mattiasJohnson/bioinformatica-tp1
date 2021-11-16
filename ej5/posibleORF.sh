#!/bin/bash

# default values
declare minsize sequence outseq
minsize="200"
sequence="sod1_mrna.gb"
outseq="sod1_mrna.orf"

while getopts m:s:o: flag
do
    case "${flag}" in
        m) minsize=${OPTARG};;
        s) sequence=${OPTARG};;
        o) outseq=${OPTARG};;
    esac
done
echo "Running getorf with: "
echo "minsize: $minsize";
echo "sequence: $sequence";
echo "outseq: $outseq";

getorf -minsize $minsize -sequence $sequence -outseq $outseq
