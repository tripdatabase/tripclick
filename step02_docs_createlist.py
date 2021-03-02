import logging, os, pdb, sys, pickle
from datetime import datetime
import numpy as np
import json
import re
import argparse

## Parameters
parser = argparse.ArgumentParser(description='')
parser.add_argument('--docsinfopath', type=str, default='[PATH]/dataset/allarticles.txt',
                    help='dir location of log files')
parser.add_argument('--origindatadir', type=str, default='[PATH]/rawdata_etl',
                    help='dir location of the origin TRIP data files')
args = parser.parse_args()


# Loading TRIP alldocs_info
print ("Loading %s" % args.docsinfopath)
docs_info = {}
with open(args.docsinfopath) as fr:
    next(fr) # file title
    for line_i, line in enumerate(fr):
        line = line.strip()
        vals = line.split('\t')
        if len(vals) < 3:
            print ("Skipping %s" % str(vals))
            continue
        
        _id = int(vals[0])
        _title = vals[1].strip()
        _url = vals[2]
        
        if len(_url) == 0:
            print ("Skipping %s" % str(vals))
            continue
        
        docs_info[_id] = (_title, _url)
        if line_i % 100000 == 0:
            print ("Line %d" % line_i)
        
## Loading data
_path = os.path.join(args.origindatadir, 'queryclickdata.pkl')
print ("Loading %s" % _path)
with open(_path, 'rb') as fr:
    queryclickdata = pickle.load(fr)

docids = []
for _qid in queryclickdata:
    docids.extend([y[0] for x in queryclickdata[_qid] if x[1] is not None for y in x[1]])
    docids.extend([x[0] for x in queryclickdata[_qid]])
docids = list(set(docids))

## Save file
_path = os.path.join(args.origindatadir, 'docs_info.txt')
print ("Saving doc info at %s" % _path)
missing_docids = []
with open(_path, 'w') as fw:
    for i, _docid in enumerate(docids):
        if _docid not in docs_info:
            missing_docids.append(_docid)
            continue
        fw.write('%d\t%s\t%s\n' % (_docid, docs_info[_docid][0], docs_info[_docid][1]))
        if i % 100000 == 0:
            print ("%d/%d documents" % (i, len(docids)))

_path = os.path.join(args.origindatadir, 'missing_docids.txt')
print ("Saving missing docids at %s" % _path)
with open(_path, 'w') as fw:
    for i, _docid in enumerate(missing_docids):
        fw.write('%d\n' % _docid)
print ("%d missing docids saved" % len(missing_docids))

print ('Fertig!')