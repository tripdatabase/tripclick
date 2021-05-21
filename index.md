TripClick is a large-scale dataset of click logs in the health domain, obtained from user interactions of the [Trip Database](https://www.tripdatabase.com) health web search engine. The clicklog dataset comprises approximately **5.2 million user interactions**, collected between 2013 and 2020. This dataset is accompanied with an IR evaluation benchmark and the required files to train deep learning IR models. The following data packages are provided:
* [TripClick Logs Dataset](#tripclick-logs-dataset)
* [TripClick IR Benchmark](#tripclick-ir-benchmark)
* [TripClick Training Package for Deep Learning Models](#tripclick-training-package-for-deep-learning-models)


[paper]: https://arxiv.org/abs/2103.07901
[citation]: #citation

In order to gain access to one or more of these data packages, please fill [this form](https://docs.google.com/document/d/1RHVxVnZsPBDDZMDcSvbB8VyNZDl2cn6KpeeSvIu6g_c/edit?usp=sharing) and send it to [jon.brassey@tripdatabase.com](mailto:jon.brassey@tripdatabase.com?subject=[TripClick]%20Data%20Request). In the form, please **specify needed data packages and intended use of the data**.

[Paper][paper] ([Bibtex Citation][citation])

### TripClick Logs Dataset
The logs consist of the user interactions of the Trip search engine collected between January 2013 and October 2020. Approximately **5.2 million click log entries** from around **1.6 million search sessions** are available. The provided `logs.tar.gz` contains `allarticles.txt` which provides the titles and URLs of all documents, and the `\<YYYY>-\<MM>-\<DD>.json` files contain the log entries split by date, e.g.: `2017-03-24.json`. In the log files, each line represents a single json-formatted log record.

| File Name | Format | Description |
|---|---|---|
| allarticles.txt | tsv: id	title	url | article collection |
| \<YYYY>-\<MM>-\<DD>.json | JSON | log records |

* `logs.tar.gz`: size **871M**, MD5 checksum `1d3a548685c2fbef9b2076b0b04ba44f`


### TripClick IR Benchmark
The IR evaluation benchmark/collection is created from around **4 million** click log entries which refer to those documents that are indexed in the MEDLINE catalog. The collection has approximately **1.5 million documents**, and around **692,000 queries** split into three groups: HEAD, TORSO, and TAIL. The query-to-document relevance signals are derived using RAW and Document Click-Through Rate (DCTR) click-through models. See the [paper][paper] for more details.

| File Name | Format | Description |
|---|---|---|
| documents/docs_grp_\<*\[00-15]*>.txt | TREC format | document collection split between 16 files|
| qrels/qrels.dctr.head.\<*\[train, val]*>.txt | qid, “0”, docid, rating | DCTR-based qrels in two files:<br />(train, val) |
| qrels/qrels.raw.\<*\[head, torso, tail]*>.\<*\[train, val]*>.txt | qid, “0”, docid, rating | RAW-based qrels in six files:<br />(train, val)\*(head, torso, tail) |
| topics/topics.\<*\[head, torso, tail]*>.\<*\[test, train, val]*>.txt | TREC format | Topics in nine files:<br />(test, train, val)\*(all, head, torso, tail) |

* `benchmark.tar.gz`: size **930M**, MD5 checksum `6e5d3deeba138750e9a148b538f30a8f`
* [Code used for creating the benchmark from log files](https://github.com/tripdatabase/tripclick/tree/main)

### TripClick Training Package for Deep Learning Models
To facilitate the training of deep IR models, we also provide the required training files created from the benchmark. The provided files follow the structure similar to the one of the [MS MARCO](https://microsoft.github.io/msmarco/TREC-Deep-Learning-2019) collection.


| File Name | Format | Description |
|---|---|---|
| run.trip.BM25.\<*\[head, torso, tail]*>.val.txt | TREC-like:<br />qid, “Q0”, docid, rank, score, runstring | Pre-ranking results, three files:<br />(**val**)\*(head, torso, tail) |
| runs_test/run.trip.BM25.\<*\[head, torso, tail]*>.test.txt | TREC-like:<br />qid, “Q0”, docid, rank, score, runstring | Pre-ranking results, three files:<br />(**test**)*(head, torso, tail) |
| triples.train.tsv | tsv:<br />query, pos. passage, neg. passage | Plain-text training data<br />**(size: 86G)**|
| tuples.\<*\[head, torso, tail]*>.\<*\[test, val]*>.top200.tsv | tsv:<br />qid, pid, query, passage | test and validation sets, six files:<br />(test, val)\*(head, torso, tail)|

* `dlfiles.tar.gz`: size: **29G** MD5 checksum `1f256c19466b414e365324d8ef21f09c`
* `dlfiles_runs_test.tar.gz`: size **35M** MD5 checksum `2b5e98c683a91e19630636b6f83e3b15`

## Terms and Conditions
The provided datasets are intended for non-commercial research purposes to promote advancement in the field of natural language processing, information retrieval and related areas, and are made available free of charge without extending any license or other intellectual property rights. In particular:
* Any parts of the datasets cannot be publicly shared or hosted (with exception for aggregated findings and visualizations);
* The datasets can only be used for non-commercial research purposes;
* The statistical models or any further resources created based on the datasets cannot be shared publicly without the permission of the data owners. These include for instance the weights of deep learning models trained on the provided data.

Upon violation of any of these terms, my rights to use the dataset will end automatically. 
The datasets are provided “as is” without warranty. The side granting access to the datasets is not liable for any damages related to use of the dataset.


## Citation
```
@inproceedings{rekabsaz2021fairnessir,
    title={TripClick: The Log Files of a Large Health Web Search Engine},
    author={Rekabsaz, Navid and Lesota, Oleg and Schedl, Markus and Brassey, Jon and Eickhoff, Carsten},
    booktitle={In Proceedings of the 44th International ACM SIGIR Conference on Research and Development in Information Retrieval (SIGIR'21), July 11–15, 2021, Virtual Event, Canada},
    doi={10.1145/3404835.3463242}
    year={2021},
    publisher = {ACM}
}
```

## Contact Us
If you have any questions regarding technical aspects of the dataset, please, contact us:
* [Oleg Lesota](https://www.jku.at/en/institute-of-computational-perception/about-us/people/oleg-lesota/) (Johannes Kepler University, Linz, Austria)
* [Navid Rekab-saz](https://www.jku.at/en/institute-of-computational-perception/about-us/people/navid-rekab-saz/) (Johannes Kepler University, Linz, Austria)

Please, address questions related to obtaining the data as well as to the terms of use to:
* [Jon Brassey](mailto:jon.brassey@tripdatabase.com?subject=[TripClick]) (Trip Database)


<img src="https://www.tripdatabase.com/static/img/trip-logo.png" alt="TripClick logo" width="90"/>
