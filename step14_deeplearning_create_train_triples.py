import time
import logging
import os
import pdb
import sys
from datetime import datetime
import numpy as np
from collections import defaultdict
import pickle
import argparse, os, shutil, hashlib
from datetime import datetime
import random
from tqdm import tqdm
from allennlp.common import Tqdm
Tqdm.default_mininterval = 1

from dataprocessing.readcollection import ReadDocument, ReadTopic

parser = argparse.ArgumentParser()
parser.add_argument('--colldir', type=str, default='[PATH]/collection',
                    help='location of the collection')
parser.add_argument('--ctmodel', type=str, default='raw',
                    help='raw, dctr')
parser.add_argument('--maxnegs', type=int, default=20,
                    help='maximum number of negative samples')



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
run_cnt_threshold = 1000
#outputpath = os.path.join(args.colldir, 'DLfiles/triples.train.%s#th%d#neg%d.tsv' % (args.ctmodel, run_cnt_threshold,
#                                                                                     args.negsamplescnt))
outputpath = os.path.join(args.colldir, 'DLfiles/triples.train.%s#neg%d.tsv' % (args.ctmodel, args.maxnegs))

readdocument = ReadDocument(logger)
readtopic = ReadTopic(logger)

docs_dirpath = os.path.join(args.colldir, 'Docs')
queriesdir = os.path.join(args.colldir, 'Topics')

## Reading Documents
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

logger.info("Creating triple IDs")
dataids = []
for part in ['head', 'torso', 'tail']:

    logger.info("*** Part %s ****" % part)
    
    
    ## Reading qrels
    qrelpath = os.path.join(args.colldir, 'QRels/qrels.%s.%s.train.txt' % (args.ctmodel, part))
    logger.info('Loading train pair data from QRel %s' % qrelpath)
    qrels={}
    with open(qrelpath) as fr:
        for line in fr.readlines():
            _vals = line.strip().split(' ')
            _qid = int(_vals[0])
            if _qid not in qrels:
                qrels[_qid] = []
            qrels[_qid].append((int(_vals[2]), int(_vals[3]))) # [qid] := [(docid, relevance_score)...]


    
    ## Reading Train run
    runpath = os.path.join(args.colldir, 'DLfiles/run.trip.BM25.%s.train.txt' % part)
    run_query_docids = defaultdict(list)
    logger.info('Reading run file %s' % runpath)
    with open(runpath, "r", encoding="utf8") as run_file:
        for line in tqdm(run_file):
            ls = line.strip().split(" ") # 4 Q0 5635494 1 14.044700 Anserini
            qid = int(ls[0])
            doc_id = int(ls[2])
            if int(ls[3]) > run_cnt_threshold:
                continue
            run_query_docids[qid].append(doc_id)
    for qid in run_query_docids[qid]:
        np.random.shuffle(run_query_docids[qid])

    ## Creating triple ids
    for qid in tqdm(qrels):
        
        _q_dataids = []
        qrels[qid].sort(key=lambda x: x[1], reverse=True)
        for docid_i in range(len(qrels[qid])):
            if qrels[qid][docid_i][1] <= 0:
                continue
            for docid_j in range(docid_i+1, len(qrels[qid])):
                if qrels[qid][docid_i][1] > qrels[qid][docid_j][1]:
                    _q_dataids.append((qid, qrels[qid][docid_i][0], qrels[qid][docid_j][0]))
        dataids.extend(_q_dataids)
        
        if len(_q_dataids) < args.maxnegs:
            _tobeadded_cnt = args.maxnegs - len(_q_dataids)
            if qid not in run_query_docids:
                continue

            for _tuple_i, _tuple in enumerate(qrels[qid]):#[:-1]
                _docid_judged, _rel_score = _tuple
                assert _docid_judged in docs
                
                if _rel_score > 0:
                    _added_cnt = 0
                    for _docid_unjudged in run_query_docids[qid]:
                        if (_docid_unjudged not in qrels[_qid]):                
                            dataids.append((qid, _docid_judged, _docid_unjudged))
                            _added_cnt += 1
                        if _added_cnt >= _tobeadded_cnt:
                            break

    logger.info('# of triples %d' % len(dataids))


dataids = np.array(dataids)
logger.info('# of triples %d' % len(dataids))

logger.info("Shuffeling triple IDs")
np.random.shuffle(dataids)

## Reading queries
_path = os.path.join(queriesdir, 'topics.all.txt')
logger.info("Reading %s" % _path)
queries = {}
for qry in readtopic.read_trectopicfile(_path):
    queries[int(qry['topicid'])] = qry['title']
logger.info('# of queries %d' % len(queries.keys()))


## Saving triple texts
_path = os.path.join(outputpath)
logger.info('Saving train triples data to %s' % _path)
fw = open(_path, 'w')
for item_i, item in enumerate(dataids):
    if item[0] not in queries:
        logger.info("query %d is not found. Ignored!" % item[0])
        continue
    fw.write("%s\t%s\t%s\n" % (queries[item[0]].replace('\t', ' '), 
                               docs[item[1]].replace('\t', ' '),
                               docs[item[2]].replace('\t', ' ')))
    if item_i % 1000000 == 0:
        logger.info('Fetching triple text %d/%d' % (item_i, len(dataids)))
        fw.close()
        fw = open(_path, 'a')
fw.close()

logger.info('Ferting!')



