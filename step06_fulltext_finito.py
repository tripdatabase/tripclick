import os
import csv
import numpy as np 
import re
import pickle
import pdb
from urllib.parse import urlparse
import argparse

## Parameters
parser = argparse.ArgumentParser(description='')
parser.add_argument('--origindatadir', type=str, default='[PATH]/rawdata_etl',
                    help='dir location of the origin TRIP data files')
args = parser.parse_args()


collection = 'pubmed' 
origindatadir = args.origindatadir


## Loading docs_info
_path = os.path.join(origindatadir, 'docs_info.txt')
print ("Loading %s" % _path)
docs_info = {}
with open(_path, 'r') as fr:
    for line in fr:
        values = line.strip().split('\t')
        if len(values) != 3:
            pdb.set_trace()
        _url = values[2]
        site = urlparse(_url).netloc
        _isadd = False
        if collection == 'pubmed' and site == 'www.ncbi.nlm.nih.gov':
            _isadd = True
        if _isadd:
            docs_info[int(values[0])] = _url

print ("%d documents for %s" % (len(docs_info), collection))

## loadiong index file
pkls_dir = os.path.join(origindatadir, "doc_text/%s_pkls" % collection)
index_path = pkls_dir + "/index.pkl"
print ("Loading index from at %s" % index_path)
with open(index_path, 'rb') as fr:
    index = pickle.load(fr)

## finding text
print ("Tracing over documents...")
loaded_pkls = {}
data = {}
_missing_cnt = 0
_missing_ids = []
for _docid_i, _docid in enumerate(docs_info.keys()):
    _url = docs_info[_docid]
    
    _matches = re.search('(?<=list_uids=)([^&]*)(?=&)?', _url)
    if _matches is None:
        _matches = re.search("(?<=pubmed/)([^?]*)(?=\?)?", _url)
    if _matches is None and 'PMC' not in _url and 'PMH' not in _url:
        if len(_matches) > 0:
            pdb.set_trace()

    if _matches is not None:
        _sitedocid = _matches[0]

    if _sitedocid not in index:
        _missing_cnt += 1
        _missing_ids.append(_sitedocid)
        
        print ("DocID %d with sitedocid %s missing! (%d, %d)" % (_docid, _sitedocid, _missing_cnt, _docid_i))
        data[_docid] = ""
        continue
        
    _file = index[_sitedocid]
    
    if _file not in loaded_pkls:
        if len(loaded_pkls.keys()) > 100:
            _a_key = list(loaded_pkls.keys())[0]
            #print ("Removing file %s" % _a_key)
            del loaded_pkls[_a_key] # remove one key to free memory
        pkl_path = pkls_dir + "/%s" % (_file)
        #print ("Loading file %s" % pkl_path)
        with open(pkl_path, 'rb') as fr:
            loaded_pkls[_file] = pickle.load(fr)

    data[_docid] = loaded_pkls[_file][_sitedocid]

    if _docid_i % 10000 == 0:
        print ("%d/%d" % (_docid_i, len(docs_info)))
    
print ("Missing %d/%d docids" % (_missing_cnt, _docid_i))
print (_missing_ids)

save_path = os.path.join(origindatadir, "doc_text/%s_fulltext_final.pkl" % collection)
print ("Saving at %s" % save_path)
with open(save_path, 'wb') as fw:
    pickle.dump(data, fw)

print ("Fertig!")
        
        
