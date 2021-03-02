import logging, os, pdb, sys, pickle
from datetime import datetime
import numpy as np
import json
import re
import argparse


## Parameters
parser = argparse.ArgumentParser(description='Processing queries from log files')
parser.add_argument('--logsdir', type=str, default='[PATH]/dataset/logs',
                    help='dir location of log files')
parser.add_argument('--origindatadir', type=str, default='[PATH]/rawdata_etl',
                    help='dir location of the origin TRIP data files')
args = parser.parse_args()


# returns 
## BOOL: is_ignore the query
## STR : processed query text
def process_tripqueries(qtext):
    if "tag:" in qtext:
        return True, qtext
    if "title:" in qtext:
        qtext = qtext.replace("title:", "")
    if "from:" in qtext:
        qtext = re.sub('from:\d+', '', qtext)
    if "to:" in qtext:
        qtext = re.sub('to:\d+', '', qtext)
    if "~" in qtext:
        qtext = re.sub('~\d+', '', qtext)
    if "NOT" in qtext:
        qtext = re.sub('\(NOT[^)]*\)', '', qtext)
        qtext = re.sub('NOT.*', '', qtext)
    if ("AND" in qtext) or ("OR" in qtext):
        qtext = re.sub('OR|AND', '', qtext)
    if ("(" in qtext) or (")" in qtext):
        qtext = re.sub('\(|\)', ' ', qtext)
    qtext = re.sub('[*]', '', qtext)
    qtext = re.sub('[“”",]', ' ', qtext)
    while '  ' in qtext:
        qtext = qtext.replace('  ', ' ')
    qtext = qtext.strip()
    
    if qtext == "":
        return True, qtext
    return False, qtext 


## Initialization
queries={}
queryid=0
queryclickdata={}
querystats={}


## Read Log Files
for filename in sorted(os.listdir(args.logsdir)):
    filepath = os.path.join(args.logsdir, filename)
    if not os.path.isfile(filepath):
        continue
    
    print ("Starting %s" % (filepath)) 
    with open(filepath) as fr:
        _lines = fr.readlines()
        
    for _line in _lines:
        _line_text = _line.strip().strip(',').lstrip('[').rstrip(']')
        if _line_text == "":
            continue
        logitem = json.loads(_line_text)
        _isignore, _qtext = process_tripqueries(logitem['Keywords'])
        if _isignore:
            continue
        
        docid_clicked = int(logitem['DocumentId'])
        
        docs_retrieved = None
        if logitem['Documents'] is not None:
            docs_retrieved = []
            for _doc in re.sub('["\[\]]', '', logitem['Documents']).split(','):
                _docid, _relscr = _doc.split(':')
                try:
                    _docid = int(_docid)
                    _relscr = float(_relscr)
                except:
                    print ("Problem in digit conversion of %s" % _doc)
                    continue
                docs_retrieved.append((_docid, _relscr))
                
            if len(docs_retrieved) == 0:
                print ("Weirdly list of retrieved docs is empty at log item %s" % logitem)
                pdb.set_trace()
                continue

        if _qtext in queries.keys():
            _qid = queries[_qtext]
            querystats[_qid][0] += 1
        else:
            queryid += 1
            _qid = queryid
            queries[_qtext] = _qid
            querystats[_qid] = [1, len(_qtext.split(' '))] # (# of occurrences, query length)
            
        if _qid not in queryclickdata:
            queryclickdata[_qid] = []
        queryclickdata[_qid].append((docid_clicked, docs_retrieved))
        
        
    #print ("Finished %s with queryid %d" % (filepath, queryid)) 
    
print ("Number of Queries: %d" % len(queries.keys()))

_path = os.path.join(args.origindatadir, 'queries.pkl')
print ("Saving queries at %s" % _path)
with open(_path, 'wb') as fw:
    pickle.dump(queries, fw)

_path = os.path.join(args.origindatadir, 'queryclickdata.pkl')
print ("Saving queryclickdata at %s" % _path)
with open(_path, 'wb') as fw:
    pickle.dump(queryclickdata, fw)

_path = os.path.join(args.origindatadir, 'querystats.pkl')
print ("Saving querystats at %s" % _path)
with open(_path, 'wb') as fw:
    pickle.dump(querystats, fw)


print ("Fertig!")    
    
    
        