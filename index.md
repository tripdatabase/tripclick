### Welcome
We present a large-scale domain-specific dataset of click logs, obtained from user interactions of the [Trip Database](https://www.tripdatabase.com) health web search engine. Our clicklog dataset comprises approximately 5.2 million user interactionscollected between 2013 and 2020. We use this dataset to create a standard IR evaluation benchmark **TripClick** with around 700,000 unique free-text queries and 1.3 million pairs of query-document relevance signals, whose relevance is estimated by two click-through models. As such, the collection is one of the few datasets offering the necessary data richness and scale to train neural IR models with large amount of parameters, and notably the first in the health domain.

[paper]: https://arxiv.org/abs/2103.07901
[citation]: https://github.com/tripdatabase/tripclick/blob/gh-pages/cite.bib

Available resources:
* TripClick Logs Dataset
* TripClick IR Benchmark
* TripClick Training Package for Deep Learning Models

Please consult the **Getting the Data** section if you wish to obtain one or more of the listed above.

* [Code used for creating the benchmark](https://github.com/tripdatabase/tripclick/tree/main)
* Related [publication][paper] ([Bibtex Citation][citation])

### TripClick Logs Dataset

TheTripClicklogs dataset consists of the user interactions of the Trip search engine collected between January 2013 and October 2020. Each entry consists of date and time of search (in Unix time, in milliseconds),search session identifier, submitted query (Keywordsfield), document identifiers of the top 20 retrieved documents, and the metadata of the clicked document. For the clicked document, the provided data contains its unique identifier and URL. If the clicked document is a scientific publication, its title, DOI, and clinical areas are also stored. We should emphasize that the privacy of individual users is preserved in the clicked search logs by cautiously removing any personally identifiable information. The TripClicklogs dataset consists of approximately 5.2 million click log entries, appeared in around 1.6 million search sessions (∼3.3 interactions per session). The click logs contain around 1.6 million unique queries. These unique queries appear in the logs at varying frequencies. Examples of a frequent and a rare query are “asthma pregnancy”, and “antimicrobial activity of medicinal plants”, respectively. The log files contain approximately 2.3 million documents. Together with the dataset of click logs, we provide the corresponding titles and URLs of all documents. Examining the origin of clicked documents, we observe that approximately 80% of the documents point to articles in the MEDLINE catalog, around 11% to entries in https://clinicaltrials.gov, and the rest to various publicly available resources on the web.

<img src="qry_hist_corona.gif" alt="COVID-19 related queries histogram" width="400"/>

Finally, looking at the query contents, figure above reports the number of times a query related to the COVID-19 virus is submitted to the search engine in the period of 2018-2020. The data for 2018 and 2019 are presented as annual sums, while for the year 2020,numbers are reported per month. While there are only few COVID-19-related queries before the February of 2020, the information needrapidly gains popularity with a peak in April. The provided data is potentially a useful resource for studying the COVID-19 pandemic,as well as the reaction and evolution of search engines regarding thesudden emergence of previously unknown/uncommon disease.

See [the paper][paper] for more detail.

### TripClick IR Benchmark
**Documents** To create the TripClick benchmark, we use a subset of click log entries that refer to those documents that are indexed in the MEDLINE catalog. This subset encom-passes around 4 million log entries. The collection of documents that appear in the subset of click logs, results in approximately 1.5 million unique documents. For each document, we fetch the corresponding article from the MEDLINE catalog. Similar to the TREC Precision Medicine track we use the title and abstract of the articles as documents of the TripClick benchmark.

**Queries** The queries from the subset of click logs, comprise around 692,000 unique entities. We split thequeries into three groups, namely HEAD,TORSO, and TAIL, such that the queries in this sets cover 20%, 30%, and 50% of the search enginetraffic (according to the subset of click logs). This, in fact, results in assigning the queries with frequencies lower than 6 to TAIL, the ones between 6 and 44 to TORSO, and all the rest with frequencies higher higher than 44 to HEAD. While the numbers of unique queries in HEAD and TORSO are much smaller than those in TAIL, the former together still cover half of the search engine’straffic since their queries repeat much more often than the ones of TAIL.

**Relevance**  We provide two sets of query-to-document relevance signals, each created using a click-through model. The first relevance set, referred to as RAW, follows a simple approach by considering every clicked document as relevant to its corresponding query. The second set uses the Document Click-Through Rate (DCTR). Creating two sets using different click-through models provides insight about the effect of each click-through model on the final evaluation results, achieved using the corresponding relevance signals.

See [the paper][paper] for more detail.

### TripClick DL Training Package
Our Training Package provides sufficiemt volume of data to facilitate training of deep neural IR models. It has structure similar to [MS MARCO](https://microsoft.github.io/msmarco/TREC-Deep-Learning-2019). Note that TripClick data is specific to health domain and user behaviour patterns present in it may differ significantly from ones observed in more general purpouse datasets.

See [the paper][paper] for more detail and experiment reports.

### Getting the Data
We offer the three following resource packages:
1. TripClick Logs Dataset
2. TripClick IR Benchmark
3. TripClick Training Package for Deep Learning Models

One or more of the listed above can be acquired for free through filling and sending [this form](https://docs.google.com/document/d/1RHVxVnZsPBDDZMDcSvbB8VyNZDl2cn6KpeeSvIu6g_c/edit?usp=sharing) to [jon.brassey@tripdatabase.com](mailto:jon.brassey@tripdatabase.com?subject=[TripClick]%20Data%20Request).
<br>Please, **specify needed data packages and intended use of the data**.

Below we describe contents of each package in detail.
#### TripClick Logs Dataset

| File Name | Format | Description |
|---|---|---|
| allarticles.txt | tsv: id	title	url | article collection |
| \<YYYY>-\<MM>-\<DD>.json | JSON | log records |

Total archive size: **871M**

The **\<YYYY>-\<MM>-\<DD>.json** files contain by day-split logs, e.g. **2017-03-24.json**, ... with one json-formatted log record per line.
The exact record format is described in [the paper][paper].

#### TripClick IR Benchmark

| File Name | Format | Description |
|---|---|---|
| documents/docs_grp_\<*\[00-15]*>.txt | TREC format | document collection split between 16 files|
| qrels/qrels.dctr.head.\<*\[train, val]*>.txt | qid, “0”, docid, rating | DCTR-based qrels in two files:<br />(train, val) |
| qrels/qrels.raw.\<*\[head, torso, tail]*>.\<*\[train, val]*>.txt | qid, “0”, docid, rating | RAW-based qrels in six files:<br />(train, val)\*(head, torso, tail) |
| topics/topics.\<*\[head, torso, tail]*>.\<*\[test, train, val]*>.txt | TREC format | Topics in nine files:<br />(test, train, val)\*(all, head, torso, tail) |

Total archive size: **930M**

#### TripClick Training Package for Deep Learning Models

| File Name | Format | Description |
|---|---|---|
| run.trip.BM25.\<*\[head, torso, tail]*>.val.txt | TREC-like:<br />qid, “Q0”, docid, rank, score, runstring | Pre-ranking results, three files:<br />(**val**)\*(head, torso, tail) |
| runs_test/run.trip.BM25.\<*\[head, torso, tail]*>.test.txt | TREC-like:<br />qid, “Q0”, docid, rank, score, runstring | Pre-ranking results, three files:<br />(**test**)*(head, torso, tail) |
| triples.train.tsv | tsv:<br />query, pos. passage, neg. passage | Plain-text training data<br />**(size: 86G)**|
| tuples.\<*\[head, torso, tail]*>.\<*\[test, val]*>.top200.tsv | tsv:<br />qid, pid, query, passage | test and validation sets, six files:<br />(test, val)\*(head, torso, tail)|

Total archive size: **29G**

#### Checksums

| Data Package | File Name | md5 |
|---|---|---|
| TripClick Logs Dataset | logs.tar.gz | 1d3a548685c2fbef9b2076b0b04ba44f |
| TripClick IR Benchmark | benchmark.tar.gz | 6062c9748f5d62cd57228d36f8954da4 |
| TripClick Training Package for Deep Learning Models | dlfiles.tar.gz | 1f256c19466b414e365324d8ef21f09c |
|  |dlfiles_runs_test.tar.gz | 2b5e98c683a91e19630636b6f83e3b15 |

### Terms and Conditions
The provided datasets are intended for non-commercial research purposes to promote advancement in the field of natural language processing, information retrieval and related areas, and are made available free of charge without extending any license or other intellectual property rights. In particular:
* Any parts of the datasets cannot be publicly shared or hosted (with exception for aggregated findings and visualizations);
* The datasets can only be used for non-commercial research purposes;
Upon violation of any of these terms, your rights to use the dataset will end automatically.
The datasets are provided “as is” without warranty. The side granting access to the datasets is not liable for any damages related to use of the dataset.


### Citation
```
@inproceedings{rekabsaz2021fairnessir,
    title={TripClick: The Log Files of a Large Health Web Search Engine},
    author={Rekabsaz, Navid and Lesota, Oleg and Schedl, Markus and Brassey, Jon and Eickhoff, Carsten},
    booktitle={In Proceedings of the 44th International ACM SIGIR Conference on Research and Development in Information Retrieval (SIGIR'21), July 11–15, 2021, Virtual Event, Canada},
    doi={10.1145/3404835.3463242}
    year={2021},
    publisher = {{ACM}}
}
```

### Contact Us
If you have any questions regarding technical aspects of the dataset, please, contact us:
* [Oleg Lesota](https://www.jku.at/en/institute-of-computational-perception/about-us/people/oleg-lesota/) (Johannes Kepler University, Linz, Austria)
* [Navid Rekab-Saz](https://www.jku.at/en/institute-of-computational-perception/about-us/people/navid-rekab-saz/) (Johannes Kepler University, Linz, Austria)

Please, address questions related to obtaining the data as well as to the terms of use to:
* [Jon Brassey](mailto:jon.brassey@tripdatabase.com?subject=[TripClick]) (Trip Database)


<img src="https://www.tripdatabase.com/static/img/trip-logo.png" alt="TripClick logo" width="90"/>
