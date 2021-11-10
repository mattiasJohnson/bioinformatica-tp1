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
 
    soup = BeautifulSoup(contents, 'html.parser')

    # Finding a pattern(certain text)
    pattern = lambda t: (pattern_input) in t
 
    # Anchor tag
    # soup.find('hit_def', text = pattern).parent
    all = soup.findAll('hit_def', text = pattern)
    # parent=all.find_parent('hit')
    for val in all:
        parent=val.parent
        # html=parent.prettify("utf-8")
        print(parent)
        output.write(str(parent))

    # html = soup.prettify("utf-8")
    # print(html)
    # output.write(html)

    # input.close()
    # output.close()

except Exception as e:
    output.close()
    input.close()
    print("Error")
    print(e)
 

 

