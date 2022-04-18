---
mailinglist: tripclick@jku.at
---

<head>
  <link rel="stylesheet" type="text/css" href="https://cdn.datatables.net/1.10.21/css/jquery.dataTables.min.css" />
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
  <script src="https://code.jquery.com/jquery-3.5.1.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>
  <script type="text/javascript" charset="utf8" src="https://cdn.datatables.net/1.10.13/js/jquery.dataTables.min.js"></script>
  <script type="text/javascript" charset="utf8" src="leaderboard.js"></script>

</head>
<style>
  .table.dataTable  {
    font-family: Verdana, Geneva, Tahoma, sans-serif;
    font-size: 12px;
}
</style>


[paper]: https://arxiv.org/abs/2103.07901

TripClick is a large-scale dataset of click logs in the health domain, obtained from user interactions of the [Trip Database](https://www.tripdatabase.com) health web search engine. The clicklog dataset comprises approximately **5.2 million user interactions**, collected between 2013 and 2020. This dataset is accompanied with an IR evaluation benchmark and the required files to train deep learning IR models.

**Paper:** [TripClick: The Log Files of a Large Health Web Search Engine][paper]
```
@inproceedings{rekabsaz2021fairnessir,
    title={TripClick: The Log Files of a Large Health Web Search Engine},
    author={Rekabsaz, Navid and Lesota, Oleg and Schedl, Markus and Brassey, Jon and Eickhoff, Carsten},
    booktitle={Proceedings of the 44th International ACM SIGIR Conference on Research and Development in Information Retrieval},
    doi={10.1145/3404835.3463242},
    pages={2507--2513},
    year={2021},
    publisher = {{ACM}}
}
```

* [Leaderboards](#leaderboards)
* [TripClick dataset](#tripclick-dataset)
* [Additional resources by collaborators](#additional-resources-by-collaborators)
* [Team and contact](#team-and-contact)

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



### Instruction for submitting to leaderboards
We look forward to your submissions with the aim of fostering collaboration in the commuinty and tracking the progress on the benchmarks. To ensure the integrity of the official test results, the relevance information of the test set is not publically available. You can submit your TREC-formatted run files on the validation and test queries of all/either of the benchmarks. Please follow the instructions below for the run files submission.

- Prepare run files for the test and validation queries of all/either of the HEAD, TORSO, and TAIL group in the TREC format. If you want to know about TREC format, [Joao Palotti](https://github.com/joaopalotti/trectools) provides a nice explanation and a set of useful tools.
- The name of each run file should follow the format `[team-name]_[head/torso/tail]_[validation/test]_[datetime].run`. 
  - `team-name` is the name of your team.
  - `head/torso/tail` is the query set, namely `head`, `torso`, or `tail`.
  - `datetime` The date and time of submission in `YYYYMMDD` format.
  - `validation/test` Whether the run file is on validation (`validation`) or test (`test`) queries.
  - An example: `myteam_head_test_20210512.run`
- Attach the run file(s) to the email, containing the following points:
  - To: [{{ page.mailinglist }}](mailto:{{ page.mailinglist }})
  - Subject: submission of *team-name*
  - Content
    - Team: *team-name*
    - Description: any description about the submission
    - Paper: URL to the related paper (optional)
    - Code: URL to the related code (optional)

## TripClick dataset

### How to access the dataset
To gain access to one or more of the collection's data packages, please fill [this form](https://docs.google.com/document/d/1RHVxVnZsPBDDZMDcSvbB8VyNZDl2cn6KpeeSvIu6g_c/edit?usp=sharing) and send it to [jon.brassey@tripdatabase.com](mailto:jon.brassey@tripdatabase.com?subject=[TripClick]%20Data%20Request). In the form, please **specify needed data packages and intended use of the data**.

### Logs Dataset
The logs consist of the user interactions of the Trip search engine collected between January 2013 and October 2020. Approximately **5.2 million click log entries** from around **1.6 million search sessions** are available. The provided `logs.tar.gz` contains `allarticles.txt` which provides the titles and URLs of all documents, and the `\<YYYY>-\<MM>-\<DD>.json` files contain the log entries split by date, e.g.: `2017-03-24.json`. In the log files, each line represents a single json-formatted log record.

* `logs.tar.gz`: size **871M**, MD5 checksum `1d3a548685c2fbef9b2076b0b04ba44f`

| File Name | Format | Description |
|---|---|---|
| allarticles.txt | tsv: id	title	url | article collection |
| \<YYYY>-\<MM>-\<DD>.json | JSON | log records |


### Information Retrieval Collection
The IR evaluation benchmark/collection is created from around **4 million** click log entries which refer to those documents that are indexed in the MEDLINE catalog. The collection has approximately **1.5 million documents**, and around **692,000 queries** split into three groups: HEAD, TORSO, and TAIL. The query-to-document relevance signals are derived using RAW and Document Click-Through Rate (DCTR) click-through models. See the [paper][paper] for more details. The code used to create the benchmark from log files is available [here](https://github.com/tripdatabase/tripclick/tree/main).


To make the use of the collection easier, we provide the benchmark in two formats: TREC-style and TSV format. The contents of both formats are exactly the same. 

#### TREC format

* `benchmark.tar.gz`: size **930M**, MD5 checksum `6e5d3deeba138750e9a148b538f30a8f`

| File Name | Format | Description |
|---|---|---|
| documents/docs_grp_\<*\[00-15]*>.txt | TREC format | document collection split between 16 files|
| qrels/qrels.dctr.head.\<*\[train, val]*>.txt | qid, 0, docid, relevance | DCTR-based qrels in two files:<br />(train, val) |
| qrels/qrels.raw.\<*\[head, torso, tail]*>.\<*\[train, val]*>.txt | qid, 0, docid, relevance | RAW-based qrels in six files:<br />(train, val)\*(head, torso, tail) |
| topics/topics.\<*\[head, torso, tail]*>.\<*\[test, train, val]*>.txt | TREC format | Topics in nine files:<br />(test, train, val)\*(all, head, torso, tail) |

#### TSV format

* `benchmark_tsv.tar.gz`: size **930M**, MD5 checksum `dff5f68eed8f9574eac432ea580275f7`

| File Name | Format | Description |
|---|---|---|
| documents/docs.tsv | docid \t doctext | documents |
| qrels/qrels.dctr.head.\<*\[train, val]*>.tsv | qid \t 0 \t docid \t relevance | DCTR-based qrels in two files:<br />(train, val) |
| qrels/qrels.raw.\<*\[head, torso, tail]*>.\<*\[train, val]*>.tsv | qid \t 0 \t docid \t relevance | RAW-based qrels in six files:<br />(train, val)\*(head, torso, tail) |
| topics/topics.\<*\[head, torso, tail]*>.\<*\[test, train, val]*>.tsv | qid \t qtext | Topics in nine files:<br />(test, train, val)\*(all, head, torso, tail) |

### Training package for deep learning models
To facilitate the training of deep IR models, we also create and provide the required training files alongside the benchmark. The provided files follow a similar format to the one of the [MS MARCO](https://microsoft.github.io/msmarco/TREC-Deep-Learning-2019) collection.

* `dlfiles.tar.gz`: size: **29G** MD5 checksum `1f256c19466b414e365324d8ef21f09c`
* `dlfiles_runs_test.tar.gz`: size **35M** MD5 checksum `2b5e98c683a91e19630636b6f83e3b15`

| File Name | Format | Description |
|---|---|---|
| run.trip.BM25.\<*\[head, torso, tail]*>.val.txt | TREC-like:<br />qid, “Q0”, docid, rank, score, runstring | Pre-ranking results, three files:<br />(**val**)\*(head, torso, tail) |
| runs_test/run.trip.BM25.\<*\[head, torso, tail]*>.test.txt | TREC-like:<br />qid, “Q0”, docid, rank, score, runstring | Pre-ranking results, three files:<br />(**test**)*(head, torso, tail) |
| triples.train.tsv | tsv:<br />query, pos. passage, neg. passage | Plain-text training data<br />**(size: 86G)**|
| tuples.\<*\[head, torso, tail]*>.\<*\[test, val]*>.top200.tsv | tsv:<br />qid, pid, query, passage | test and validation sets, six files:<br />(test, val)\*(head, torso, tail)|


## Additional resources by collaborators

* Pyserini guideline for creating BM25 baselines: [link](https://github.com/castorini/pyserini/blob/master/docs/experiments-tripclick-doc.md)
* A new set of training triples (`triples.train.tsv`) provided by Hofst{\"a}tter et al.: [github](https://github.com/sebastian-hofstaetter/tripclick), [Training triples](https://huggingface.co/datasets/sebastian-hofstaetter/tripclick-training)

## Team and Contact
For any question regarding obtaining the data and terms of use please contact [Jon Brassey](mailto:jon.brassey@tripdatabase.com?subject=[TripClick]). If you have any question regarding the technical aspects drop an email to [{{ page.mailinglist }}](mailto:{{ page.mailinglist }}).

<br>
<div class="row">
    <div class="col-md-4 text-center">
        <a href="https://www.jku.at/en/institute-of-computational-perception/about-us/people/navid-rekab-saz/"><img src="images/navid.png" width="150" height="150"><br><strong>Navid Rekab-saz</strong><br>Johannes Kepler University Linz</a>
    </div>
    <div class="col-md-4 text-center">
        <a href="https://www.jku.at/en/institute-of-computational-perception/about-us/people/oleg-lesota/"><img src="images/oleg.webp" width="150" height="150"><br><strong>Oleg Lesota</strong><br>Johannes Kepler University Linz</a>
    </div>
    <div class="col-md-4 text-center">
        <a href="https://www.jku.at/en/institute-of-computational-perception/about-us/people/markus-schedl"><img src="images/markus.jpg" width="87" height="150"><br><strong>Markus Schedl</strong><br>Johannes Kepler University Linz</a>
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

### Terms and conditions
The provided datasets are intended for non-commercial research purposes to promote advancement in the field of natural language processing, information retrieval and related areas, and are made available free of charge without extending any license or other intellectual property rights. In particular:
* Any parts of the datasets cannot be publicly shared or hosted (with exception for aggregated findings and visualizations);
* The datasets can only be used for non-commercial research purposes;
* The statistical models or any further resources created based on the datasets cannot be shared publicly without the permission of the data owners. These include for instance the weights of deep learning models trained on the provided data.

Upon violation of any of these terms, my rights to use the dataset will end automatically. 
The datasets are provided “as is” without warranty. The side granting access to the datasets is not liable for any damages related to use of the dataset.


<img src="images/trip-logo.png" alt="TripClick logo" width="90"/>

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
