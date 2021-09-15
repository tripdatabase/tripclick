/*
FORMAT:
<date><descr><team> <ndcg@10_VAL><rec@10_VAL> <ndcg@10_TEST><rec@10_TEST> <paper><code>
["date","descr","team","-","-",  "-","-",  "",""]
*/
var data_head_dctr = [
 ["2021/06/03","TK (baseline)","-",0.221,0.194,0.208,0.189,"",""],
 ["2021/06/03","KNRM (baseline)","-",0.196,0.174,0.191,0.173,"",""],
 ["2021/06/03","BM25 (baseline)","-",0.149,0.145,0.140,0.138,"",""],

 ["2021/06/07","BERT_Cat Re-Ranking (Top-200 BM25) Ensemble (2x PubMedBERT, 1x SciBERT)","TU Wien (Sebastian Hofstätter, Sophia Althammer, Allan Hanbury)",
  "-","-",  0.3036,0.2915,  "",""],
 ["2021/09/13","CEDR_BM25_top1000 (capreolus)","mpi-d5","0.2216","0.2154",  "0.2105","0.2119",  "","https://github.com/capreolus-ir/capreolus"]
];

var data_head_raw = [
 ["2021/06/03","TK (baseline)","-",0.302,0.174,0.284,0.167,"",""],
 ["2021/06/03","KNRM (baseline)","-",0.268,0.156,0.254,0.151,"",""],
 ["2021/06/03","BM25 (baseline)","-",0.209,0.129,0.199,0.128,"",""],

 ["2021/06/07","BERT_Cat Re-Ranking (Top-200 BM25) Ensemble (2x PubMedBERT, 1x SciBERT)","TU Wien (Sebastian Hofstätter, Sophia Althammer, Allan Hanbury)",
  "-","-",  0.4091,0.2381,  "",""],
 ["2021/09/13","CEDR_BM25_top1000 (capreolus)","mpi-d5","0.2989","0.1802",  "0.2851","0.1754",  "","https://github.com/capreolus-ir/capreolus"]
];

var data_torso_raw = [
 ["2021/06/03","TK (baseline)","-",0.281,0.326,0.272,0.321,"",""],
 ["2021/06/03","KNRM (baseline)","-",0.242,0.286,0.235,0.283,"",""],
 ["2021/06/03","BM25 (baseline)","-",0.224,0.271,0.206,0.262,"",""],

 ["2021/06/07","BERT_Cat Re-Ranking (Top-200 BM25) Ensemble (2x PubMedBERT, 1x SciBERT)","TU Wien (Sebastian Hofstätter, Sophia Althammer, Allan Hanbury)",
  "-","-",  0.3695,0.4412,  "",""]
];

var data_tail_raw = [
 ["2021/06/03","TK (baseline)","-",0.310,0.471,0.295,0.459,"",""],
 ["2021/06/03","KNRM (baseline)","-",0.289,0.429,0.272,0.409,"",""],
 ["2021/06/03","BM25 (baseline)","-",0.285,0.429,0.267,0.409,"",""],
 
 ["2021/06/07","BERT_Cat Re-Ranking (Top-200 BM25) Ensemble (2x PubMedBERT, 1x SciBERT)","TU Wien (Sebastian Hofstätter, Sophia Althammer, Allan Hanbury)",
  "-","-",  0.4197,0.5957,  "",""]
];
