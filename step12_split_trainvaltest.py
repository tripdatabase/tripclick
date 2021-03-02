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
parser.add_argument('--ctmodels', nargs='*', default=('raw', 'dctr'),
                    help='Click through models to split their QRels: [dctr,raw]')
args = parser.parse_args()

VAL_SIZE = 1175
TEST_SIZE = 1175

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

def loading_queries(_path):
    ## Loading topics
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
    return queries

#_path = os.path.join(args.colldir, 'Topics/topics.all.txt')
#queries_all = loading_queries(_path)
#qryids_all = set(list(queries_all.keys()))
#print ('Number of all queries %d' % len(queries_all.keys()))

_path = os.path.join(args.colldir, 'Topics/topics.head.all.txt')
queries_head = loading_queries(_path)
qryids_head = list(queries_head.keys())
print ('Number of head queries %d' % len(queries_head.keys()))

_path = os.path.join(args.colldir, 'Topics/topics.torso.all.txt')
queries_torso = loading_queries(_path)
qryids_torso = list(queries_torso.keys())
print ('Number of torso queries %d' % len(queries_torso.keys()))


_path = os.path.join(args.colldir, 'Topics/topics.tail.all.txt')
queries_tail = loading_queries(_path)
qryids_tail = list(queries_tail.keys())
print ('Number of tail queries %d' % len(queries_tail.keys()))

_path = os.path.join(args.origindatadir, 'querystats.pkl')
print ("loading querystats at %s" % _path)
with open(_path, 'rb') as fr:
    querystats = pickle.load(fr)

qryoccurs_tail = np.array([querystats[x][0] for x in qryids_tail])
qryoccurs_torso = np.array([querystats[x][0] for x in qryids_torso])
qryoccurs_head = np.array([querystats[x][0] for x in qryids_head])

# Splitting to train validation test
print ("splitting ...")

np.random.seed(21)
qryids_tail_valtest = np.random.choice(qryids_tail, size=TEST_SIZE+VAL_SIZE, replace=False,
                                       p=qryoccurs_tail/float(np.sum(qryoccurs_tail)))
qryids_torso_valtest = np.random.choice(qryids_torso, size=TEST_SIZE+VAL_SIZE, replace=False,
                                       p=qryoccurs_torso/float(np.sum(qryoccurs_torso)))
qryids_head_valtest = np.random.choice(qryids_head, size=TEST_SIZE+VAL_SIZE, replace=False,
                                       p=qryoccurs_head/float(np.sum(qryoccurs_head)))

_validxs=list(range(int((VAL_SIZE+TEST_SIZE)/VAL_SIZE)-1, len(qryids_tail_valtest), int((VAL_SIZE+TEST_SIZE)/VAL_SIZE)))
qryids_tail_val = qryids_tail_valtest[_validxs]
qryids_tail_test = [x for x in qryids_tail_valtest if x not in qryids_tail_val]
qryids_head_train = set(copy.copy(qryids_head))
qryids_tail_train = set(copy.copy(qryids_tail))
for x in qryids_tail_val: qryids_tail_train.remove(x)
for x in qryids_tail_test: qryids_tail_train.remove(x)
qryids_tail_train = list(qryids_tail_train)
print ("Tail train/val/test: %d/%d/%d" % (len(qryids_tail_train), len(qryids_tail_val), len(qryids_tail_test)))

_validxs=list(range(int((VAL_SIZE+TEST_SIZE)/VAL_SIZE)-1, len(qryids_torso_valtest), int((VAL_SIZE+TEST_SIZE)/VAL_SIZE)))
qryids_torso_val = qryids_torso_valtest[_validxs]
qryids_torso_test = [x for x in qryids_torso_valtest if x not in qryids_torso_val]
qryids_torso_train = set(copy.copy(qryids_torso))
for x in qryids_torso_val: qryids_torso_train.remove(x)
for x in qryids_torso_test: qryids_torso_train.remove(x)
qryids_torso_train = list(qryids_torso_train)
print ("Torso train/val/test: %d/%d/%d" % (len(qryids_torso_train), len(qryids_torso_val), len(qryids_torso_test)))

_validxs=list(range(int((VAL_SIZE+TEST_SIZE)/VAL_SIZE)-1, len(qryids_head_valtest), int((VAL_SIZE+TEST_SIZE)/VAL_SIZE)))
qryids_head_val = qryids_head_valtest[_validxs]
qryids_head_test = [x for x in qryids_head_valtest if x not in qryids_head_val]
for x in qryids_head_val: qryids_head_train.remove(x)
for x in qryids_head_test: qryids_head_train.remove(x)
qryids_head_train = list(qryids_head_train)
print ("Head train/val/test: %d/%d/%d" % (len(qryids_head_train), len(qryids_head_val), len(qryids_head_test)))



qryids_tail_val.sort()
qryids_tail_test.sort()
qryids_tail_train.sort()
qryids_torso_val.sort()
qryids_torso_test.sort()
qryids_torso_train.sort()
qryids_head_val.sort()
qryids_head_test.sort()
qryids_head_train.sort()

## Save files
### Queries

_path = os.path.join(args.colldir, 'Topics/topics.tail.val.txt')
print ("Saving %d validation tail queries at %s" % (len(qryids_tail_val), _path))
write_queries(queries_tail, qryids_tail_val, _path)

_path = os.path.join(args.colldir, 'Topics/topics.torso.val.txt')
print ("Saving %d validation torso queries at %s" % (len(qryids_torso_val), _path))
write_queries(queries_torso, qryids_torso_val, _path)

_path = os.path.join(args.colldir, 'Topics/topics.head.val.txt')
print ("Saving %d validation head queries at %s" % (len(qryids_head_val), _path))
write_queries(queries_head, qryids_head_val, _path)

_path = os.path.join(args.colldir, 'Topics/topics.tail.test.txt')
print ("Saving %d test tail queries at %s" % (len(qryids_tail_test), _path))
write_queries(queries_tail, qryids_tail_test, _path)

_path = os.path.join(args.colldir, 'Topics/topics.torso.test.txt')
print ("Saving %d test torso queries at %s" % (len(qryids_torso_test), _path))
write_queries(queries_torso, qryids_torso_test, _path)

_path = os.path.join(args.colldir, 'Topics/topics.head.test.txt')
print ("Saving %d test head queries at %s" % (len(qryids_head_test), _path))
write_queries(queries_head, qryids_head_test, _path)

_path = os.path.join(args.colldir, 'Topics/topics.tail.train.txt')
print ("Saving %d train tail queries at %s" % (len(qryids_tail_train), _path))
write_queries(queries_tail, qryids_tail_train, _path)

_path = os.path.join(args.colldir, 'Topics/topics.torso.train.txt')
print ("Saving %d train torso queries at %s" % (len(qryids_torso_train), _path))
write_queries(queries_torso, qryids_torso_train, _path)

_path = os.path.join(args.colldir, 'Topics/topics.head.train.txt')
print ("Saving %d train head queries at %s" % (len(qryids_head_train), _path))
write_queries(queries_head, qryids_head_train, _path)


### QRels
for _ctmodel in args.ctmodels:
    _path = os.path.join(args.colldir, 'QRels/qrels.%s.all.txt' % _ctmodel)
    _qrels = load_qrels(_path)

    _path = os.path.join(args.colldir, 'QRels/qrels.%s.tail.train.txt' % _ctmodel)
    print ("Saving %s train tail qrels at %s" % (_ctmodel, _path))
    with open(_path, 'w') as fw:
        for _qryid in qryids_tail_train:
            if _qryid not in _qrels:
                continue
            for _tuple in _qrels[_qryid]:
                fw.write('%d 0 %d %d\n' % (_qryid, _tuple[0], _tuple[1]))

    _path = os.path.join(args.colldir, 'QRels/qrels.%s.torso.train.txt' % _ctmodel)
    print ("Saving %s train torso qrels at %s" % (_ctmodel, _path))
    with open(_path, 'w') as fw:
        for _qryid in qryids_torso_train:
            if _qryid not in _qrels:
                continue
            for _tuple in _qrels[_qryid]:
                fw.write('%d 0 %d %d\n' % (_qryid, _tuple[0], _tuple[1]))

    _path = os.path.join(args.colldir, 'QRels/qrels.%s.head.train.txt' % _ctmodel)
    print ("Saving %s train head qrels at %s" % (_ctmodel, _path))
    with open(_path, 'w') as fw:
        for _qryid in qryids_head_train:
            if _qryid not in _qrels:
                continue
            for _tuple in _qrels[_qryid]:
                fw.write('%d 0 %d %d\n' % (_qryid, _tuple[0], _tuple[1]))

    _path = os.path.join(args.colldir, 'QRels/qrels.%s.tail.val.txt' % _ctmodel)
    print ("Saving %s validation tail qrels at %s" % (_ctmodel, _path))
    with open(_path, 'w') as fw:
        for _qryid in qryids_tail_val:
            if _qryid not in _qrels:
                continue
            for _tuple in _qrels[_qryid]:
                fw.write('%d 0 %d %d\n' % (_qryid, _tuple[0], _tuple[1]))
                
    _path = os.path.join(args.colldir, 'QRels/qrels.%s.torso.val.txt' % _ctmodel)
    print ("Saving %s validation torso qrels at %s" % (_ctmodel, _path))
    with open(_path, 'w') as fw:
        for _qryid in qryids_torso_val:
            if _qryid not in _qrels:
                continue
            for _tuple in _qrels[_qryid]:
                fw.write('%d 0 %d %d\n' % (_qryid, _tuple[0], _tuple[1]))
                
    _path = os.path.join(args.colldir, 'QRels/qrels.%s.head.val.txt' % _ctmodel)
    print ("Saving %s validation head qrels at %s" % (_ctmodel, _path))
    with open(_path, 'w') as fw:
        for _qryid in qryids_head_val:
            if _qryid not in _qrels:
                continue
            for _tuple in _qrels[_qryid]:
                fw.write('%d 0 %d %d\n' % (_qryid, _tuple[0], _tuple[1]))
                
    _path = os.path.join(args.colldir, 'QRels/qrels.%s.tail.test.txt' % _ctmodel)
    print ("Saving %s test tail qrels at %s" % (_ctmodel, _path))
    with open(_path, 'w') as fw:
        for _qryid in qryids_tail_test:
            if _qryid not in _qrels:
                continue
            for _tuple in _qrels[_qryid]:
                fw.write('%d 0 %d %d\n' % (_qryid, _tuple[0], _tuple[1]))
                
    _path = os.path.join(args.colldir, 'QRels/qrels.%s.torso.test.txt' % _ctmodel)
    print ("Saving %s test torso qrels at %s" % (_ctmodel, _path))
    with open(_path, 'w') as fw:
        for _qryid in qryids_torso_test:
            if _qryid not in _qrels:
                continue
            for _tuple in _qrels[_qryid]:
                fw.write('%d 0 %d %d\n' % (_qryid, _tuple[0], _tuple[1]))
                
    _path = os.path.join(args.colldir, 'QRels/qrels.%s.head.test.txt' % _ctmodel)
    print ("Saving %s test head qrels at %s" % (_ctmodel, _path))
    with open(_path, 'w') as fw:
        for _qryid in qryids_head_test:
            if _qryid not in _qrels:
                continue
            for _tuple in _qrels[_qryid]:
                fw.write('%d 0 %d %d\n' % (_qryid, _tuple[0], _tuple[1]))
 
print ('Fertig!')