import pdb
import argparse
import os
import sys
import logging
sys.path.append(os.getcwd())

from dataprocessing.readcollection import ReadDocument, ReadTopic


#
# config
#
parser = argparse.ArgumentParser()

parser.add_argument('--colldir', type=str, default='[PATH]/collection',
                    help='location of the collection')
parser.add_argument('--set', type=str,
                    help='[test,val]')
parser.add_argument('--group', type=str,
                    help='[tail,torso,head]')
parser.add_argument('--topN', type=int, default=200,
                    help='how many docs per query to take')
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
readtopic = ReadTopic(logger)

docs_dirpath = os.path.join(args.colldir, 'Docs')
queriesdir = os.path.join(args.colldir, 'Topics')

_runpath = os.path.join(args.colldir, 'DLfiles/run.trip.BM25.%s.%s.txt' % (args.group, args.set))
_outputpath = os.path.join(args.colldir, 'DLfiles/%s.%s.top%d.tsv' % (args.group, args.set, args.topN))



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

## Reading queries
queries = {}
for topicpath in ['topics.all.txt']:
    _path = os.path.join(queriesdir, topicpath)
    logger.info("Reading %s" % _path)
    for qry in readtopic.read_trectopicfile(_path):
        queries[int(qry['topicid'])] = qry['title']
logger.info('# of queries %d' % len(queries.keys()))

## produce output

logger.info('Reading from %s' % _runpath)
logger.info('Saving tuples to %s' % _outputpath)
fw = open(_outputpath, "w", encoding="utf8")
with open(_runpath, "r", encoding="utf8") as run_file:
    for line_i, line in enumerate(run_file):
        if line_i % 1000000 == 0 and line_i != 0:
            logger.info('lines %d' % line_i)
            fw.close()
            fw = open(_outputpath, 'a', encoding="utf8")

        ls = line.strip().split(" ") # 4 Q0 5635494 1 14.044700 Anserini
        query_id = int(ls[0])
        doc_id = int(ls[2])
        if int(ls[3]) > args.topN:
            continue
        fw.write("%d\t%d\t%s\t%s\n" % (query_id, doc_id, 
                                       queries[query_id].replace('\t', ' '),
                                       docs[doc_id].replace('\t', ' ')))

fw.close()

logger.info('Ferting!')

            