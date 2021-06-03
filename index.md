<head>
  <link rel="stylesheet" type="text/css" href="https://cdn.datatables.net/1.10.21/css/jquery.dataTables.min.css" />
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>
  <script src="leaderboard.js"></script>
</head>
<style>
  .table.dataTable  {
    font-family: Verdana, Geneva, Tahoma, sans-serif;
    font-size: 12px;
}
</style>

[paper]: https://arxiv.org/abs/2103.07901
[citation]: #citation

TripClick is a large-scale dataset of click logs in the health domain, obtained from user interactions of the [Trip Database](https://www.tripdatabase.com) health web search engine. The clicklog dataset comprises approximately **5.2 million user interactions**, collected between 2013 and 2020. This dataset is accompanied with an IR evaluation benchmark and the required files to train deep learning IR models.
* [Access Data](#sccess-data)
* [Leaderboards](#leaderboards)
* [TripClick Data Description](#tripclick-data-collection)
* [Terms and Conditions](#terms-and-conditions)
* [Team and Contacts](#team-and-contacts)

**Paper:** [TripClick: The Log Files of a Large Health Web Search Engine][paper]
```
@inproceedings{rekabsaz2021tripclick,
    title={TripClick: The Log Files of a Large Health Web Search Engine},
    author={Rekabsaz, Navid and Lesota, Oleg and Schedl, Markus and Brassey, Jon and Eickhoff, Carsten},
    booktitle={In Proceedings of the 44th International ACM SIGIR Conference on Research and Development in Information Retrieval (SIGIR'21), July 11–15, 2021, Virtual Event, Canada},
    doi={10.1145/3404835.3463242}
    year={2021},
    publisher = {ACM}
}
```

## Access Data
To gain access to one or more of the collection's data packages, please fill [this form](https://docs.google.com/document/d/1RHVxVnZsPBDDZMDcSvbB8VyNZDl2cn6KpeeSvIu6g_c/edit?usp=sharing) and send it to [jon.brassey@tripdatabase.com](mailto:jon.brassey@tripdatabase.com?subject=[TripClick]%20Data%20Request). In the form, please **specify needed data packages and intended use of the data**.

## Leaderboards

### HEAD Queries - DCTR

<div class="alert bg-success text-dark" cellspacing="0">
  <table id="leaderboard_head_dctr" class="table table-bordered" cellspacing="0">
    <thead>
      <tr><th>Date</th><th>Description</th><th>Team</th><th>NDCG@10 (val)</th><th>RECALL@10 (val)</th><th>NDCG@10 (test)</th><th>RECALL@10 (test)</th><th>Paper</th><th>Code</th></tr>
    </thead>
  </table>
</div>

### HEAD Queries - RAW

<div class="alert bg-info text-dark" cellspacing="0">
  <table id="leaderboard_head_raw" class="table table-bordered" cellspacing="0">
    <thead>
      <tr><th>Date</th><th>Description</th><th>Team</th><th>NDCG@10 (val)</th><th>RECALL@10 (val)</th><th>NDCG@10 (test)</th><th>RECALL@10 (test)</th><th>Paper</th><th>Code</th></tr>
    </thead>
  </table>
</div>

### TORSO Queries - RAW

<div class="alert bg-warning text-dark" cellspacing="0">
  <table id="leaderboard_torso_raw" class="table table-bordered" cellspacing="0">
    <thead>
      <tr><th>Date</th><th>Description</th><th>Team</th><th>NDCG@10 (val)</th><th>RECALL@10 (val)</th><th>NDCG@10 (test)</th><th>RECALL@10 (test)</th><th>Paper</th><th>Code</th></tr>
    </thead>
</table>
</div>

### TAIL Queries - RAW

<div class="alert bg-danger text-dark" cellspacing="0">
  <table id="leaderboard_tail_raw" class="table table-bordered" cellspacing="0">
    <thead>
      <tr><th>Date</th><th>Description</th><th>Team</th><th>NDCG@10 (val)</th><th>RECALL@10 (val)</th><th>NDCG@10 (test)</th><th>RECALL@10 (test)</th><th>Paper</th><th>Code</th></tr>
    </thead>
</table>
</div>



### Submission Instruction
TBD

## TripClick Data Description
### Logs Dataset
The logs consist of the user interactions of the Trip search engine collected between January 2013 and October 2020. Approximately **5.2 million click log entries** from around **1.6 million search sessions** are available. The provided `logs.tar.gz` contains `allarticles.txt` which provides the titles and URLs of all documents, and the `\<YYYY>-\<MM>-\<DD>.json` files contain the log entries split by date, e.g.: `2017-03-24.json`. In the log files, each line represents a single json-formatted log record.

| File Name | Format | Description |
|---|---|---|
| allarticles.txt | tsv: id	title	url | article collection |
| \<YYYY>-\<MM>-\<DD>.json | JSON | log records |

* `logs.tar.gz`: size **871M**, MD5 checksum `1d3a548685c2fbef9b2076b0b04ba44f`


### IR Benchmark
The IR evaluation benchmark/collection is created from around **4 million** click log entries which refer to those documents that are indexed in the MEDLINE catalog. The collection has approximately **1.5 million documents**, and around **692,000 queries** split into three groups: HEAD, TORSO, and TAIL. The query-to-document relevance signals are derived using RAW and Document Click-Through Rate (DCTR) click-through models. See the [paper][paper] for more details.

| File Name | Format | Description |
|---|---|---|
| documents/docs_grp_\<*\[00-15]*>.txt | TREC format | document collection split between 16 files|
| qrels/qrels.dctr.head.\<*\[train, val]*>.txt | qid, “0”, docid, rating | DCTR-based qrels in two files:<br />(train, val) |
| qrels/qrels.raw.\<*\[head, torso, tail]*>.\<*\[train, val]*>.txt | qid, “0”, docid, rating | RAW-based qrels in six files:<br />(train, val)\*(head, torso, tail) |
| topics/topics.\<*\[head, torso, tail]*>.\<*\[test, train, val]*>.txt | TREC format | Topics in nine files:<br />(test, train, val)\*(all, head, torso, tail) |

* `benchmark.tar.gz`: size **930M**, MD5 checksum `6e5d3deeba138750e9a148b538f30a8f`
* [Code used for creating the benchmark from log files](https://github.com/tripdatabase/tripclick/tree/main)

### Training Package for Deep Learning Models
To facilitate the training of deep IR models, we also create and provide the required training files alongside the benchmark. The provided files follow a similar format to the one of the [MS MARCO](https://microsoft.github.io/msmarco/TREC-Deep-Learning-2019) collection.


| File Name | Format | Description |
|---|---|---|
| run.trip.BM25.\<*\[head, torso, tail]*>.val.txt | TREC-like:<br />qid, “Q0”, docid, rank, score, runstring | Pre-ranking results, three files:<br />(**val**)\*(head, torso, tail) |
| runs_test/run.trip.BM25.\<*\[head, torso, tail]*>.test.txt | TREC-like:<br />qid, “Q0”, docid, rank, score, runstring | Pre-ranking results, three files:<br />(**test**)*(head, torso, tail) |
| triples.train.tsv | tsv:<br />query, pos. passage, neg. passage | Plain-text training data<br />**(size: 86G)**|
| tuples.\<*\[head, torso, tail]*>.\<*\[test, val]*>.top200.tsv | tsv:<br />qid, pid, query, passage | test and validation sets, six files:<br />(test, val)\*(head, torso, tail)|

* `dlfiles.tar.gz`: size: **29G** MD5 checksum `1f256c19466b414e365324d8ef21f09c`
* `dlfiles_runs_test.tar.gz`: size **35M** MD5 checksum `2b5e98c683a91e19630636b6f83e3b15`


### Additional Resources

* Pyserini guideline for creating BM25 baselines: [link](https://github.com/castorini/pyserini/blob/master/docs/experiments-tripclick-doc.md)



## Terms and Conditions
The provided datasets are intended for non-commercial research purposes to promote advancement in the field of natural language processing, information retrieval and related areas, and are made available free of charge without extending any license or other intellectual property rights. In particular:
* Any parts of the datasets cannot be publicly shared or hosted (with exception for aggregated findings and visualizations);
* The datasets can only be used for non-commercial research purposes;
* The statistical models or any further resources created based on the datasets cannot be shared publicly without the permission of the data owners. These include for instance the weights of deep learning models trained on the provided data.

Upon violation of any of these terms, my rights to use the dataset will end automatically. 
The datasets are provided “as is” without warranty. The side granting access to the datasets is not liable for any damages related to use of the dataset.


## Team and Contacts
For any question regarding obtaining the data and terms of use please contact [Jon Brassey](mailto:jon.brassey@tripdatabase.com?subject=[TripClick]). If you have any question regarding the technical aspects contact [Oleg Lesota](https://www.jku.at/en/institute-of-computational-perception/about-us/people/oleg-lesota/) or [Navid Rekab-saz](https://www.jku.at/en/institute-of-computational-perception/about-us/people/navid-rekab-saz/).

<br>
<div class="row">
    <div class="col-md-4 text-center">
        <a href="https://www.jku.at/en/institute-of-computational-perception/about-us/people/navid-rekab-saz/"><img src="images/navid.png" width="150" height="150"><br><strong>Navid Rekab-saz</strong><br>Johannes Kepler University Linz</a>
    </div>
    <div class="col-md-4 text-center">
        <a href="https://www.jku.at/en/institute-of-computational-perception/about-us/people/oleg-lesota/"><img src="images/oleg.webp" width="150" height="150"><br><strong>Oleg Lesota</strong><br>Johannes Kepler University Linz</a>
    </div>
    <div class="col-md-4 text-center">
        <a href="https://www.jku.at/en/institute-of-computational-perception/about-us/people/markus-schedl"><img src="images/markus.webp" width="101" height="150"><br><strong>Markus Schedl</strong><br>Johannes Kepler University Linz</a>
    </div>
</div>
<br>
<div class="row">
    <div class="col-md-6 text-center">
        <a href="mailto:jon.brassey@tripdatabase.com?subject=[TripClick]"><img src="images/jon.webp" width="150" height="150"><br><strong>Jon Brassey</strong><br>Trip Database</a>
    </div>
    <div class="col-md-6 text-center">
        <a href="https://brown.edu/Research/AI/people/carsten.html"><img src="images/carsten.png" width="150" height="150"><br><strong>Carsten Eickhoff</strong><br>Brown University</a>
    </div>
</div>

<img src="https://www.tripdatabase.com/static/img/trip-logo.png" alt="TripClick logo" width="90"/>

<script type="text/javascript" charset="utf8" src="http://ajax.aspnetcdn.com/ajax/jQuery/jquery-1.8.2.min.js"></script>
<script type="text/javascript" charset="utf8" src="http://ajax.aspnetcdn.com/ajax/jquery.dataTables/1.9.4/jquery.dataTables.min.js"></script>
<script type="text/javascript" charset="utf8" src="leaderboard.js"></script>
<script>
  $(function(){
    var otable_leaderboard_head_dctr = $("#leaderboard_head_dctr").dataTable({
        bAutoWidth: false, 
        bPaginate: false,
        sScrollX: "100%",
        bInfo : false,
        sDom: 'l<"toolbar">frtip',
        aoColumns: [
          { sWidth: '5%' },
          { sWidth: '35%' },
          { sWidth: '35%' },
          { sWidth: '5%' },
          { sWidth: '5%' },
          { sWidth: '5%' },
          { sWidth: '5%' },
          { sWidth: '5%' },
          { sWidth: '5%' }
        ],      
        aaData:data_head_dctr
    });
    otable_leaderboard_head_dctr.fnSort( [ [5,'desc'] ] );
    var otable_leaderboard_head_raw = $("#leaderboard_head_raw").dataTable({
        bAutoWidth: false, 
        bPaginate: false,
        sScrollX: "100%",
        bInfo : false,
        sDom: 'l<"toolbar">frtip',
        aoColumns: [
          { sWidth: '5%' },
          { sWidth: '35%' },
          { sWidth: '35%' },
          { sWidth: '5%' },
          { sWidth: '5%' },
          { sWidth: '5%' },
          { sWidth: '5%' },
          { sWidth: '5%' },
          { sWidth: '5%' }
        ],      
        aaData:data_head_raw
    });
    otable_leaderboard_head_raw.fnSort( [ [5,'desc'] ] );
    var otable_leaderboard_torso_raw = $("#leaderboard_torso_raw").dataTable({
        bAutoWidth: false, 
        bPaginate: false,
        sScrollX: "100%",
        bInfo : false,
        sDom: 'l<"toolbar">frtip',
        aoColumns: [
          { sWidth: '5%' },
          { sWidth: '35%' },
          { sWidth: '35%' },
          { sWidth: '5%' },
          { sWidth: '5%' },
          { sWidth: '5%' },
          { sWidth: '5%' },
          { sWidth: '5%' },
          { sWidth: '5%' }
        ],      
        aaData:data_torso_raw
    });
    otable_leaderboard_torso_raw.fnSort( [ [5,'desc'] ] );
    var otable_leaderboard_tail_raw = $("#leaderboard_tail_raw").dataTable({
        bAutoWidth: false, 
        bPaginate: false,
        sScrollX: "100%",
        bInfo : false,
        sDom: 'l<"toolbar">frtip',
        aoColumns: [
          { sWidth: '5%' },
          { sWidth: '35%' },
          { sWidth: '35%' },
          { sWidth: '5%' },
          { sWidth: '5%' },
          { sWidth: '5%' },
          { sWidth: '5%' },
          { sWidth: '5%' },
          { sWidth: '5%' }
        ],      
        aaData:data_tail_raw
    });
    otable_leaderboard_tail_raw.fnSort( [ [5,'desc'] ] );
  })  
  
</script>