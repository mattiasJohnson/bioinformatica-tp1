import argparse
import pickle
import re
from urllib.request import install_opener

from bs4 import BeautifulSoup
from bs4.builder import HTMLTreeBuilder

argparser = argparse.ArgumentParser(description='Blast Parser',
                                    formatter_class=argparse.RawTextHelpFormatter)

argparser.add_argument('-p', '--pattern', type=str, required=True,help='Pattern determinado a buscar')
argparser.add_argument('-i', '--input', help='path al archivo a parsear',
                       type=str, default='edit.blast', required=False)
argparser.add_argument('-o', '--output_folder', help='carpeta donde guardar el archivo de salida',
                       type=str, default='./', required=False)
args = vars(argparser.parse_args())

try:
    input=open(args['input'])
    output=open(args['output_folder'] + 'ej4.blast','w')
    pattern_input=args['pattern']
    contents = input.read()
 
    start='''<?xml version="1.0"?>
            <!DOCTYPE BlastOutput PUBLIC "-//NCBI//NCBI BlastOutput/EN" "http://www.ncbi.nlm.nih.gov/dtd/NCBI_BlastOutput.dtd">
            <BlastOutput>
                <BlastOutput_iterations>
                    <Iteration>
                        <Iteration_hits>'''

    output.write(start)
    soup = BeautifulSoup(contents, 'html.parser')

    # Finding a pattern(certain text)
    pattern = lambda t: (pattern_input) in t
 
    all = soup.findAll('hit_def', text = pattern)
    # parent=all.find_parent('hit')
    for val in all:
        parent=val.parent
        # html=parent.prettify("utf-8")
        print(parent)
        output.write(str(parent))

    end ='''<Iteration_hits>
            <Iteration>
            <BlastOutput_iterations>
            <BlastOutput>'''
    output.write(end)
    # html = soup.prettify("utf-8")
    # print(html)
    # output.write(html)

    input.close()
    output.close()

except Exception as e:
    output.close()
    input.close()
    print("Error")
    print(e)
 

 

