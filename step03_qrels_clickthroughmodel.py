import logging, os, pdb, sys, pickle
from datetime import datetime
import numpy as np
import json
import re
import argparse
from collections import Counter
from urllib.parse import urlparse


## Parameters
parser = argparse.ArgumentParser(description='')
parser.add_argument('--origindatadir', type=str, default='[PATH]/rawdata_etl',
                    help='dir location of the origin TRIP data files')
parser.add_argument('--ctmodel', type=str, default='dctr',
                    help='Click through model: [dctr,raw]')
args = parser.parse_args()

## Loading queryclickdata
_path = os.path.join(args.origindatadir, 'queryclickdata.pkl')
print ("Loading %s" % _path)
with open(_path, 'rb') as fr:
    queryclickdata = pickle.load(fr)

## Loading missing_docids
missing_docids=[]
with open(os.path.join(args.origindatadir, 'missing_docids.txt')) as fr:
    missing_docids = set([int(l.strip()) for l in fr])

if args.ctmodel == 'dctr':
    
    ## Calculating DCTR with only the non-clicked documents which appear before the clicked one are set as non-relevant (0)
    print ("Calculating DCTR STEP 1") 
    qry_docretrieved_cnt = {}
    qry_docclicked_cnt={}
    cnt_none = 0
    cnt_all = 0
    for _qid in queryclickdata:
        _docids_retrieved = []
        _docids_clicked = []
        for _tuple in queryclickdata[_qid]:
            _docid_clicked = _tuple[0]
            _tuples_retrieved = _tuple[1]
            cnt_all += 1
            if _tuples_retrieved is None:
                _tuples_retrieved = [(_docid_clicked, 1.0)]
                #cnt_none += 1
                #continue
            _tuples_retrieved.sort(key=lambda x: x[1], reverse=True)
            _qry_docids_retrieved = [x[0] for x in _tuples_retrieved]
            try:
                _doc_clicked_index = _qry_docids_retrieved.index(_docid_clicked)
            except:
                _doc_clicked_index = -1
            if _doc_clicked_index != -1:
                _docids_retrieved.extend(_qry_docids_retrieved)#[:_doc_clicked_index+1]
                _docids_clicked.append(_docid_clicked)
        if len(_docids_retrieved) == 0 or len(_docids_clicked) == 0:
            continue
        
        _counter_docids_retrieved = Counter(_docids_retrieved)
        for _miss_docid in set([x for x in _counter_docids_retrieved.keys()]).intersection(missing_docids):
            _counter_docids_retrieved.pop(_miss_docid, None)
        _counter_docids_clicked = Counter(_docids_clicked)
        for _miss_docid in set([x for x in _counter_docids_clicked.keys()]).intersection(missing_docids):
            _counter_docids_clicked.pop(_miss_docid, None)
            
        if len(_counter_docids_clicked.keys()) == 0 or len(_counter_docids_retrieved.keys()) == 0:
            continue
        qry_docretrieved_cnt[_qid] = _counter_docids_retrieved
        qry_docclicked_cnt[_qid] = _counter_docids_clicked

    print (cnt_none, cnt_all)
    
    print ("Calculating DCTR STEP 2") 
    ctmodel = {} 
    MIN_RETRIEVED_CNT = 1
    for _qid in qry_docclicked_cnt.keys():
        ctmodel[_qid] = {}
        for _docid in qry_docretrieved_cnt[_qid].keys():
            _num_retrieved = float(qry_docretrieved_cnt[_qid][_docid])
            if _num_retrieved <= MIN_RETRIEVED_CNT: #filter cases that document is retrieved very rarely
                continue
            ctmodel[_qid][_docid] = 0
        for _docid in qry_docclicked_cnt[_qid].keys():
            if _docid not in qry_docretrieved_cnt[_qid].keys():
                continue
            _num_retrieved = float(qry_docretrieved_cnt[_qid][_docid])
            if _num_retrieved <= MIN_RETRIEVED_CNT: #filter cases that document is retrieved very rarely
                continue
            ctmodel[_qid][_docid] = qry_docclicked_cnt[_qid][_docid]/_num_retrieved
             
elif args.ctmodel == 'raw':
    ## Calculating DCTR with all non-clicked documents as non-relevant (0)
    print ("Calculating RAW STEP 1") 
    qry_docretrieved_cnt = {}
    qry_docclicked_cnt={}
    for _qid in queryclickdata:
        _docids_clicked = []
        _docids_retrieved = []
        for _tuple in queryclickdata[_qid]:
            _docid_clicked = _tuple[0]
            _tuples_retrieved = _tuple[1]
            if _tuples_retrieved is None:
                _tuples_retrieved = [(_docid_clicked, 1.0)]
            _qry_docids_retrieved = [x[0] for x in _tuples_retrieved]
            try:
                _doc_clicked_index = _qry_docids_retrieved.index(_docid_clicked)
            except:
                _doc_clicked_index = -1
            if _doc_clicked_index != -1:
                _docids_retrieved.extend(_qry_docids_retrieved[:_doc_clicked_index+1])
                _docids_clicked.append(_docid_clicked)
        if len(_docids_retrieved) == 0 or len(_docids_clicked) == 0:
            continue
        
        _counter_docids_retrieved = Counter(_docids_retrieved)
        for _miss_docid in set([x for x in _counter_docids_retrieved.keys()]).intersection(missing_docids):
            _counter_docids_retrieved.pop(_miss_docid, None)
        _counter_docids_clicked = Counter(_docids_clicked)
        for _miss_docid in set([x for x in _counter_docids_clicked.keys()]).intersection(missing_docids):
            _counter_docids_clicked.pop(_miss_docid, None)
            
        if len(_counter_docids_clicked.keys()) == 0 or len(_counter_docids_retrieved.keys()) == 0:
            continue
        qry_docretrieved_cnt[_qid] = _counter_docids_retrieved
        qry_docclicked_cnt[_qid] = _counter_docids_clicked
        
    print ("Calculating RAW STEP 2") 
    ctmodel = {} 
    for _qid in qry_docclicked_cnt.keys():
        ctmodel[_qid] = {}
        for _docid in qry_docretrieved_cnt[_qid].keys():
            ctmodel[_qid][_docid] = 0
        for _docid in qry_docclicked_cnt[_qid].keys():
            ctmodel[_qid][_docid] = np.sign(qry_docclicked_cnt[_qid][_docid])
    
            

save_path = os.path.join(args.origindatadir, "qry_doc_%s.pkl" % args.ctmodel)
print ("Saving at %s" % save_path)
with open(save_path, 'wb') as fw:
    pickle.dump(ctmodel, fw)

print ("Fertig!")
     