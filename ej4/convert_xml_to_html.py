from xml.dom.minidom import parse, parseString

def convert(input_filename, output_filename):
    # Read XML file
    document = parse(input_filename)
    
    with open(output_filename, 'w') as myFile:
        # Write start HTML
        myFile.write(html_start)

        # Create HTML for hit
        for hit in document.getElementsByTagName("hit"):

            # Get hit values
            hit_num = hit.getElementsByTagName("hit_num")[0].firstChild.nodeValue
            hit_id = hit.getElementsByTagName("hit_id")[0].firstChild.nodeValue
            hit_def = hit.getElementsByTagName("hit_def")[0].firstChild.nodeValue
            hit_accession = hit.getElementsByTagName("hit_accession")[0].firstChild.nodeValue
            hit_len = hit.getElementsByTagName("hit_len")[0].firstChild.nodeValue
            
            # Create HTML for hit header
            html_header_hit = createHTMLHeaderHit(hit_num, hit_id, hit_def, hit_accession, hit_len)
            myFile.write(html_header_hit)

            # Create HTML for every hsp child
            for hsp in hit.getElementsByTagName("hsp"):
                html_hsp = createHTMLHsp(hsp)
                myFile.write(html_hsp)

        # Write end HTML 
        myFile.write(html_end)


def createHTMLHitDef(hit_def):
    hit_def_list = hit_def.split(">")
    
    html_start = "<ul style=\"hit-def-list\">"
    
    html_li_list = []
    for hit_def_single in hit_def_list:
        html_li = f"<li>{hit_def_single}</li>"
        html_li_list.append(html_li)
        
    html_mid = " ".join(html_li_list)
    html_end = "</ul>"
    
    html_string = html_start + html_mid + html_end
    
    return html_string



def createHTMLHeaderHit(hit_num, hit_id, hit_def, hit_accession, hit_len):
    html_hit_def_ul = createHTMLHitDef(hit_def)
    html_string = f'''<div class="header-hit">
    <ul class="header-hit-info">
    <li>Hit num: {hit_num}</li>
    <li>Hit ID: {hit_id}</li>
    <li>Accession: {hit_accession}</li>
    <li>Length of hit: {hit_len}</li>
    </ul>
    <p><strong>Hit defs:</strong></p>
    {html_hit_def_ul}
    </div>
    '''
    return html_string
    
def createHTMLHsp(hsp):
    # Get values
    hsp_num = hsp.getElementsByTagName("hsp_num")[0].firstChild.nodeValue
    hsp_bit_score = hsp.getElementsByTagName("hsp_bit-score")[0].firstChild.nodeValue
    hsp_score = hsp.getElementsByTagName("hsp_score")[0].firstChild.nodeValue
    hsp_evalue = hsp.getElementsByTagName("hsp_evalue")[0].firstChild.nodeValue
    hsp_query_from = hsp.getElementsByTagName("hsp_query-from")[0].firstChild.nodeValue
    hsp_query_to = hsp.getElementsByTagName("hsp_query-to")[0].firstChild.nodeValue
    hsp_hit_from = hsp.getElementsByTagName("hsp_hit-from")[0].firstChild.nodeValue
    hsp_hit_to = hsp.getElementsByTagName("hsp_hit-to")[0].firstChild.nodeValue
    hsp_query_frame = hsp.getElementsByTagName("hsp_query-frame")[0].firstChild.nodeValue
    hsp_hit_frame = hsp.getElementsByTagName("hsp_hit-frame")[0].firstChild.nodeValue
    hsp_identity = hsp.getElementsByTagName("hsp_identity")[0].firstChild.nodeValue
    hsp_positive = hsp.getElementsByTagName("hsp_positive")[0].firstChild.nodeValue
    hsp_gaps = hsp.getElementsByTagName("hsp_gaps")[0].firstChild.nodeValue
    hsp_align_len = hsp.getElementsByTagName("hsp_align-len")[0].firstChild.nodeValue

    hsp_qseq = hsp.getElementsByTagName("hsp_qseq")[0].firstChild.nodeValue
    hsp_hseq = hsp.getElementsByTagName("hsp_hseq")[0].firstChild.nodeValue
    hsp_midline = hsp.getElementsByTagName("hsp_midline")[0].firstChild.nodeValue
    
    # Fill template
    html_string = f'''
    <div class="hsp-body">
    <p>High-scoring Segment Pair number {hsp_num}</p>
    <p><strong>Scores</strong><br>Bit score: {hsp_bit_score}<br>Score: {hsp_score}<br>E-value:{hsp_evalue}</p>
    <p>hsp query from {hsp_query_from} to {hsp_query_to}</p>
    <p>hsp hit from {hsp_hit_from} to {hsp_hit_to}</p>
    <p>hsp query frame: {hsp_query_frame}</p>
    <p>hsp hit frame: {hsp_hit_frame}</p>
    <p>hsp identity: {hsp_identity}</p>
    <p>hsp positive: {hsp_positive}</p>
    <p>hsp gaps: {hsp_gaps}</p>
    <p>hsp align length: {hsp_align_len}</p>
    <p>sequence: {hsp_qseq}</p>
    </div>
    '''
    
    return html_string


html_start = '''<!DOCTYPE html>
<html>
<head>
<title>Blast Result</title>
<style>
.header-hit {
   border-style: solid; 
   border-color: #0d490582;
   border-radius: 8px 8px 0px 0px;
   background-color: #0d49051b;
   margin-top: 2em;
   max-width: 1080px;
   margin-bottom: 0px;
}

.header-hit > p {
    margin: 0.5em;
}

ul.header-hit-info > li {
    display: inline;
    margin-left: 1em;
    margin-right: 1em;
}

.hsp-body {
    border-style: solid;
   border-color: #0d49055f;
   border-radius: 0px 0px 8px 8px;
   background-color: #0d49051b;
   max-width: 1080px;
   background-clip: padding-box;
   overflow-wrap: break-word;
}

.hsp-body > p {
    margin: 0.5em;
}
</style>
</head>
<body>'''

html_end = '''</body>
</html>'''