__author__ = 'navid'

#import sys
import codecs
import pdb
import re
import os, sys
import pickle

class ReadDocument():

    def __init__(self, logger):
        self.logger = logger

    def read_trecdocfile(self, path) :

        f=open(path, 'r', encoding='utf-8')
        docs=[]
        lines=iter(f.read().splitlines())
        for line in lines:
            line = line.strip()

            if len(line) == 0:
                continue

            if (line == '<DOC>'):
                doc = {}
                isinheader = False
                isintext = False
            else:
                try:
                    if '<DOCNO>' in line:
                        m = re.match("<(.*)>(.*)</\\1>", line)
                        if m:
                            if m.group(1)=='DOCNO':
                                doc['docno']=m.group(2).strip()
                        else:
                            line = next(lines)
                            doc['docno'] = line.replace('</DOCNO>', '').strip()
                    #self.logger.info("Reading %s starting with %s"%(path, str(doc['docno'])))
                    elif '<TITLE>' in line:
                        m = re.match("<(.*)>(.*)</\\1>", line)
                        if m:
                            if m.group(1)=='TITLE':
                                doc['title']=m.group(2).strip()
                        else:
                            line = next(lines)
                            doc['title'] = line.replace('</TITLE>', '').strip()
                    elif '<TEXT>' in line:
                        text = line.replace('<TEXT>', '')
                        if '</TEXT>' in line:
                            text=line.replace('</TEXT>', '')
                        else:
                            while (1):
                                line=next(lines)
                                if '</TEXT>' in line:
                                    text += " " + line.replace('</TEXT>', '')
                                    break
                                elif '</DOC>' in line:
                                    isintext=False
                                    break
                                else:
                                    text += " " + line

                        doc['text'] = text.strip()

                        if not isintext:
                            docs.append(doc)
                            continue

                        while (1):
                            line=next(lines)
                            if '</DOC>' in line:
                                docs.append(doc)
                                break
                except(StopIteration):
                    #break and return whatever docs you gathered so far
                    sys.stdout.write("trouble in reading file: %s" % path)
                    sys.stdout.flush()
                    break

        f.close()

        return docs

class ReadTopic():
    def __init__(self, logger):
        self.logger=logger

    def read_trectopicfile(self, path) :
        topics=[]

        f=open(path, 'r', encoding='utf-8')
        lines=f.read().splitlines()
        topic={}
        pos=''
        for line in lines:
            if line.startswith("<"):
                pos=''
                m = re.match("<(.*?)>(.*)</.*>", line)
                if not m:
                    m = re.match("<(.*?)>(.*)", line)
                if m:
                    if m.group(1)=='top':
                        topic={}
                        pos='top'
                    elif m.group(1)=='/top':
                        if 'title' not in topic:
                            pdb.set_trace()
                        topics.append(topic)
                        pos='/top'
                    elif m.group(1)=='num':
                        topic['topicid'] = m.group(2).replace('Number: ','').strip()
                        pos='num'
                    elif m.group(1)=='title':
                        topic['title'] = m.group(2).replace('Topic: ','').strip()
                        pos = 'title'
            else:
                if (pos=='title'):
                    topic['title']+=' '+line
                    topic['title'] = topic['title'].strip()
        f.close()

        return topics
