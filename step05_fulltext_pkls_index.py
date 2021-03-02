import os
import csv
import pdb
import pickle
import argparse



parser = argparse.ArgumentParser(description='')
parser.add_argument('--origindatadir', type=str, default='[PATH]/rawdata_etl/doc_text',
                    help='dir location of the origin TRIP data files')

args = parser.parse_args()

collection = "pubmed"
_dir = os.path.join(args.origindatadir, "%s_pkls" % collection)
index = {}
for i, _file in enumerate(os.listdir(_dir)):
    if _file == 'index.pkl' or (not _file.endswith('pkl')):
        continue
    _filepath = os.path.join(_dir, _file)
    print (_filepath)
    with open(_filepath, 'rb') as fr:
        data = pickle.load(fr)
    for key in data:
        index[key] = _file
    
save_path = os.path.join(_dir, "index.pkl")
print ("Saving at %s" % save_path)
with open(save_path, 'wb') as fw:
    pickle.dump(index, fw)

print ("Fertig!")
