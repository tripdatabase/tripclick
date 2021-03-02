import logging, os, pdb, sys, pickle
from datetime import datetime
import numpy as np
import json
import re
import argparse
from urllib.parse import urlparse


## Parameters
parser = argparse.ArgumentParser(description='')
parser.add_argument('--origindatadir', type=str, default='[PATH]/rawdata_etl',
                    help='dir location of the origin TRIP data files')
parser.add_argument('--colldir', type=str, default='[PATH]/collection',
                    help='dir location to store files of collection')
args = parser.parse_args()


origindatadir = args.origindatadir
colldir = args.colldir
fulltextdir = os.path.join(origindatadir, 'doc_text')

collections = ['pubmed']

## Loading docs_info
_path = os.path.join(origindatadir, 'docs_info.txt')
print ("Loading %s" % _path)
docs_info = {}
with open(_path, 'r') as fr:
    for line in fr:
        values = line.strip().split('\t')
        docs_info[int(values[0])] = (values[1], values[2])

docids = list(docs_info.keys())
docids.sort()

## loading full text files
fulltexts = {}
for _coll in collections:
    _fulltext_path = os.path.join(fulltextdir, "%s_fulltext_final.pkl" % _coll)
    print ("Loading fulltext %s" % _fulltext_path)
    with open(_fulltext_path, 'rb') as fr:
        fulltexts[_coll] = pickle.load(fr)


# Writing docs in trecified version
#cnt_docperfile = 10000
#for _sublist_i, _docids_sublist in enumerate([docids[x:x+cnt_docperfile] for x in range(0, len(docids), cnt_docperfile)]):
doc_cnt = 0
file_cnt = 0
_path = os.path.join(colldir, 'Docs/docs_grp_%02d.txt' % file_cnt)
print ("Creating file %s" % _path)
fw = open(_path, 'w')

for i, _docid in enumerate(docids):
    site = urlparse(docs_info[_docid][1]).netloc
    if site == 'www.ncbi.nlm.nih.gov':
        _coll = 'pubmed'
    #elif site == 'clinicaltrials.gov':
    #    _coll = 'clinicaltrials'
    else:
        continue

    fulltext = fulltexts[_coll][_docid]
    if fulltext == None:
        continue
    if len(fulltext) < 500:
        continue
        
    fw.write('<DOC>\n')
    fw.write('<DOCNO> %d </DOCNO>\n' % _docid)
    fw.write('\n')
    #fw.write('<HEADER>\n')
    fw.write('<TITLE> %s </TITLE>\n' % docs_info[_docid][0])
    fw.write('<URL> %s </URL>\n' % docs_info[_docid][1])
    #fw.write('\n')
    #fw.write('</HEADER>\n')
    fw.write('\n')
    fw.write('<TEXT>\n')
    fw.write('%s\n' % fulltext)
    fw.write('</TEXT>\n')
    fw.write('\n')
    fw.write('</DOC>\n')
    fw.write('\n')
    
    doc_cnt += 1
    
    if doc_cnt % 100000 == 0:
        if fw is not None:
            fw.close()
        file_cnt += 1
        _path = os.path.join(colldir, 'Docs/docs_grp_%02d.txt' % file_cnt)
        print ("Creating file %s" % _path)
        fw = open(_path, 'w')
        
    if doc_cnt % 5000 == 0:
        print ("%s %d" % (_path, doc_cnt))
        
fw.close()

print ("%d saved documents" % doc_cnt)
print ('Fertig!')