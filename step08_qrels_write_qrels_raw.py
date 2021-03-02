import logging, os, pdb, sys, pickle
from datetime import datetime
import numpy as np
import json
import re
import argparse
from collections import Counter
from urllib.parse import urlparse
from tqdm import tqdm
from allennlp.common import Tqdm
Tqdm.default_mininterval = 1

from dataprocessing.readcollection import ReadDocument, ReadTopic

## Parameters
parser = argparse.ArgumentParser(description='')
parser.add_argument('--origindatadir', type=str, default='[PATH]/rawdata_etl/',
                    help='dir location of the origin TRIP data files')
parser.add_argument('--colldir', type=str, default='[PATH]/collection/',
                    help='dir location to store files of collection')
args = parser.parse_args()

## LOGGER
logger = logging.getLogger()
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
logger.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

## Initialization
readdocument = ReadDocument(logger)
docs_dirpath = os.path.join(args.colldir, 'Docs')

## Loading ctmodel
_path = os.path.join(args.origindatadir, 'qry_doc_raw.pkl')
print ("Loading %s" % _path)
with open(_path, 'rb') as fr:
    ctmodel = pickle.load(fr)

## reading documents
docs = {}        
for filename in os.listdir(docs_dirpath):
    if not filename.startswith('docs_grp'):
        continue
    _path = os.path.join(docs_dirpath, filename)
    logger.info("Reading %s" % _path)
    for _doc in readdocument.read_trecdocfile(_path):
        #docs[int(_doc['docno'])] = '<ttl> %s </ttl>' % _doc['title']
        docs[int(_doc['docno'])] = '%s <eot> %s ' % (_doc['title'], _doc['text'].replace('\n', ' '))
        
logger.info('# of documents %d' % len(docs.keys()))

## loading queries
_path = os.path.join(args.origindatadir, 'queries.pkl')
print ("loading queries at %s" % _path)
with open(_path, 'rb') as fr:
    queries = pickle.load(fr)
qids = set([x[1] for x in queries.items()])
logger.info('# of queries %d' % len(qids))

_path = os.path.join(args.origindatadir, 'querystats.pkl')
print ("loading querystats at %s" % _path)
with open(_path, 'rb') as fr:
    querystats = pickle.load(fr)


## filtering ctmodel
print ("Filtering ctmodel not in documents")
ctmodel_tuples = list(ctmodel.items())
ctmodel_tuples.sort(key=lambda x: x[0])
ctmodel_tuples_filtered = []
for _tuple in ctmodel_tuples:
    _qid = _tuple[0]
    _values = {}
    if _qid not in qids:
        continue
    if querystats[_qid][1] < 2: # length of query
        continue
    for _docid in _tuple[1].keys():
        if _docid not in docs:
            continue
        _values[_docid] = int(_tuple[1][_docid]) # raw scoring
        
    if len(_values.keys()) > 0:
        if sum(_values.values()) > 0:
            ctmodel_tuples_filtered.append((_qid, _values))

## Saving Files
_path = os.path.join(args.colldir, 'QRels/qrels.raw.all.txt')
print ("Saving qrels at %s" % _path)
with open(_path, 'w') as fw:
    for _tuple in ctmodel_tuples_filtered:
        _qid = _tuple[0]
        for _docid in _tuple[1].keys():
            _rel_score = _tuple[1][_docid]
            fw.write('%d 0 %d %d\n' % (_qid, _docid, _rel_score))

print ("Fertig!")
     