import logging, os, pdb, sys, pickle
from datetime import datetime
import numpy as np
import json
import re
import copy
import argparse
from sklearn.model_selection import train_test_split

## Parameters
parser = argparse.ArgumentParser(description='')
parser.add_argument('--origindatadir', type=str, default='[PATH]/rawdata_etl/',
                    help='dir location of the origin TRIP data files')
parser.add_argument('--colldir', type=str, default='[PATH]/collection/',
                    help='dir location to store files of collection')
args = parser.parse_args()

TAIL_MAX = 5
TORSO_MAX = 44

def load_qrels(_path):
    print ("Loading %s" % _path)
    qrels = {}
    with open(_path, 'r') as fr:
        for line in fr:
            line = line.strip()
            values = line.split(' ')
            _qid = int(values[0])
            _docid = int(values[2])
            _relscr = int(values[3])

            if _qid not in qrels:
                qrels[_qid] = []
            qrels[_qid].append((_docid, _relscr))
    return qrels


def write_queries(queries, qryids, path):
    with open(_path, 'w') as fw:
        for _qryid in qryids:
            fw.write('<top>\n\n')
            fw.write('<num> Number: %d\n' % _qryid)
            fw.write('<title> %s\n\n' % queries[_qryid][0])
            fw.write('<desc> Descrption:\n\n')
            fw.write('<narr> Narrative:\n\n')
            fw.write('</top>\n\n')

## Loading topics
_path = os.path.join(args.colldir, 'Topics/topics.all.txt')
print ("Loading %s" % _path)
queries = {}
with open(_path, 'r') as fr:
    for line in fr:
        if line.startswith('<num>'):
            _qid = int(line.strip().replace('<num> Number:', ''))
            line = next(fr)
            _title = line.strip().replace('<title>', '').strip()
            line = next(fr)
            line = next(fr)
            _desc = line.strip().replace('<desc> Descrption:', '').strip()
            line = next(fr)
            line = next(fr)
            narr = line.strip().replace('<narr> Narrative:', '').strip()
            
            queries[_qid] = (_title,)
qryids_all = set(list(queries.keys()))
print ('Number of queries %d' % len(queries.keys()))

_path = os.path.join(args.origindatadir, 'querystats.pkl')
print ("loading querystats at %s" % _path)
with open(_path, 'rb') as fr:
    querystats = pickle.load(fr)

# head torso tail
print ("dividing into HEAD TORSO TAIL  ...")

query_occurs_tuple = [(x, querystats[x][0]) for x in qryids_all]
query_occurs_tuple.sort(key=lambda x: x[1], reverse=True)
qryids_tail = np.array([x[0] for x in query_occurs_tuple if x[1]<=TAIL_MAX])
qryoccurs_tail = np.array([x[1] for x in query_occurs_tuple if x[1]<=TAIL_MAX])
qryids_torso = np.array([x[0] for x in query_occurs_tuple if (x[1]<=TORSO_MAX) and (x[1]>TAIL_MAX)])
qryoccurs_torso = np.array([x[1] for x in query_occurs_tuple if (x[1]<=TORSO_MAX) and (x[1]>TAIL_MAX)])
qryids_head = np.array([x[0] for x in query_occurs_tuple if x[1]>TORSO_MAX])
qryoccurs_head = np.array([x[1] for x in query_occurs_tuple if x[1]>TORSO_MAX])

# Splitting to train validation test

qryids_tail.sort()
qryids_torso.sort()
qryids_head.sort()

## Save files
### Queries
_path = os.path.join(args.colldir, 'Topics/topics.tail.all.txt')
print ("Saving %d  tail queries at %s" % (len(qryids_tail), _path))
write_queries(queries, qryids_tail, _path)

_path = os.path.join(args.colldir, 'Topics/topics.torso.all.txt')
print ("Saving %d torso queries at %s" % (len(qryids_torso), _path))
write_queries(queries, qryids_torso, _path)

_path = os.path.join(args.colldir, 'Topics/topics.head.all.txt')
print ("Saving %d head queries at %s" % (len(qryids_head), _path))
write_queries(queries, qryids_head, _path)

    
print ('Fertig!')