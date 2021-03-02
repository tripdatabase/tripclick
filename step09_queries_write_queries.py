import logging, os, pdb, sys, pickle
from datetime import datetime
import numpy as np
import json
import re
import argparse


## Parameters
parser = argparse.ArgumentParser(description='')
parser.add_argument('--origindatadir', type=str, default='[PATH]/rawdata_etl/',
                    help='dir location of the origin TRIP data files')
parser.add_argument('--colldir', type=str, default='[PATH]/collection/',
                    help='dir location to store files of collection')
args = parser.parse_args()

## loading queries
_path = os.path.join(args.origindatadir, 'queries.pkl')
print ("loading queries at %s" % _path)
with open(_path, 'rb') as fr:
    queries = pickle.load(fr)

print ("Number of Queries: %d" % len(queries.keys()))

## loading qrels
_path = os.path.join(args.colldir, 'QRels/qrels.raw.all.txt')
print ("Loading %s" % _path)
qrel_qids = []
with open(_path, 'r') as fr:
    for line in fr:
        line = line.strip()
        values = line.split(' ')
        _qid = int(values[0])
        qrel_qids.append(_qid)
qrel_qids = set(qrel_qids)

## Save files
_path = os.path.join(args.colldir, 'Topics/topics.all.txt')
print ("Saving queries at %s" % _path)
_qtuples = list(queries.items())
_qtuples.sort(key=lambda x: x[1])
cnt = 0
with open(_path, 'w') as fw:
    for _qtuple in _qtuples:
        if _qtuple[1] in qrel_qids:
            fw.write('<top>\n\n')
            fw.write('<num> Number: %d\n' % _qtuple[1])
            fw.write('<title> %s\n\n' % _qtuple[0])
            fw.write('<desc> Descrption:\n\n')
            fw.write('<narr> Narrative:\n\n')
            fw.write('</top>\n\n')
            cnt += 1
print ("%d queries saved" % cnt)

print ("Fertig!")    
    
    
        