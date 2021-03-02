import xml.etree.ElementTree as ET
import numpy as np
import os
import pickle
import pdb
import argparse



parser = argparse.ArgumentParser(description='')
parser.add_argument('--rawdatadir', type=str, default='[PATH]/dataset',
                    help='dir location of the origin TRIP data files')
parser.add_argument('--origindatadir', type=str, default='[PATH]/rawdata_etl/doc_text',
                    help='dir location of the origin TRIP data files')

args = parser.parse_args()

_dir = "%s/pubmed/baseline" % args.rawdatadir
files = os.listdir(_dir)
for _file in files:
    if not _file.endswith("xml"):
        continue
    
    _filepath = "%s/%s" % (_dir, _file)
    print ("Reading %s" % _filepath)
    data={}
    tree = ET.parse(_filepath)
    root = tree.getroot()
    
    for i in range(len(root)):
        doc = root[i][0][3]
        sitedocid = root[i][0][0].text
        abstract=""
        for j in range(len(doc)):
            if doc[j].tag.lower()=="abstract":
                for elem in doc[j]:
                    if (elem.attrib != None) and ('Label' in elem.attrib):
                        abstract += elem.attrib['Label'] + ' : ' 
                    if elem.text != None:
                        abstract += elem.text + "\n"
                abstract = abstract.rstrip()
        data[sitedocid] = abstract
    
    _savepath = "%s/pubmed_pkls/%s.pkl" % (args.origindatadir, _file.replace(".xml", ""))
    print ("Saving %s" % _savepath)
    with open(_savepath, 'wb') as fw:
        pickle.dump(data, fw)


