### Welcome!
We present a large-scale domain-specific dataset of click logs, obtained from user interactions of the [Trip Database](https://www.tripdatabase.com) health web search engine. Our clicklog dataset comprises approximately 5.2 million user interactionscollected between 2013 and 2020. We use this dataset to create a standard IR evaluation benchmark **TripClick** with around 700,000 unique free-text queries and 1.3 million pairs of query-document relevance signals, whose relevance is estimated by two click-through models. As such, the collection is one of the few datasets offering the necessary data richness and scale to train neural IR models with large amount of parameters, and notably the first in the health domain.

Available resources:
* TripClick Logs Dataset
* TripClick IR Benchmark
* TripClick Training Package for Deep Learning Models

Please consult the **Getting the Data** section if you wish to obtain one or more of the listed above.

### Introduction
### TripClick Logs Dataset

| Statistic of TripClick logs dataset | Value |
|---|---:|
| Number of click log entries | 5,272,064 |
| Number of sessions | 1,602,648 |
| Average number of query-document interactions per session | 3.3 |
| Number of unique queries | 1,647,749 |
| Number of documents (clicked or retrieved) | 2,347,977 |


### TripClick IR Benchmark

| Statistic of TripClick IR benchmark | Value |
|---|-----:|
| Number of query-document interactions | 4,054,593 |
| Number of documents | 1,523,878 |
| Number of queries <br> (HEAD / TORSO / TAIL) <br> (TOTAL) | 5,879 / 108,314 / 578,506 <br> 692,699 |
| Average query length | 4.4±2.4 |
| Average document length | 259.0±81.7 |
| Number of RAW relevance data points <br> (HEAD / TORSO / TAIL) <br> (TOTAL) | 246,754 / 994,529 / 1,629,543 <br> 2,870,826 |
| Average RAW relevance data points per query <br> (HEAD / TORSO / TAIL) | 41.9 / 9.1 / 2.8 |
| Number of DCTR relevance data points (HEAD) | 263,175 |
| Average DCTR relevance data points per query (HEAD) | 46.2 |
| Number of queries used in the training set: | 685,649 |
| Number of non-zero RAW relevance data points <br> used to create training set | 1,105,811 |
| Number of items in the training set | 23,222,038 |
| Number of queries in the validation sets <br> (HEAD / TORSO / TAIL) | 1,175 / 1,175 / 1,175 |
| Number of queries in the test sets <br> (HEAD / TORSO / TAIL) | 1,175 / 1,175 / 1,175 |

### Getting the Data
We offer the three following resource packages:
1. TripClick Logs Dataset
2. TripClick IR Benchmark
3. TripClick Training Package for Deep Learning Models

One or more of the listed above can be requested for free via an email: [contact person](mailto:contact@person.com?subject=[TripClick]%20Data%20Request).
<br>Please, **specify needed data packages and intended use of the data**.

Below we describe contents of each package in detail.
#### TripClick Logs Dataset

| File Name | File Size | Format | Description |
|---|---:|---|---|
| allarticles.tar.gz | 235M |
| 2013.tar.gz | 56M | . | . |
| 2014.tar.gz | 62M | . | . |
| 2015.tar.gz | 61M | . | . |
| 2016.tar.gz | 91M | . | . |
| 2017.tar.gz | 103M | . | . |
| 2018.tar.gz | 115M | . | . |
| 2019.tar.gz | 103M | . | . |
| 2020.tar.gz | 77M | . | . |

Total: **900M**
#### TripClick IR Benchmark

| File Name | File Size | Format | Description |
|---|---:|---|---|
| collection.tar.gz | 875M | . | . |
| qrels.dctr.head.tar.gz | 2M | . | . |
| qrels.raw.head.tar.gz | 2M | . | . |
| qrels.raw.tail.tar.gz | 10M | . | . |
| qrels.raw.torso.tar.gz | 6M | . | . |
| topics.all.tar.gz | 13M | . | . |
| topics.head.tar.gz | 1M | . | . |
| topics.tail.tar.gz | 22M | . | . |
| topics.torso.tar.gz | 4M | . | . |

Total: **930M**

#### TripClick Training Package for Deep Learning Models

| File Name | File Size | Format | Description |
|---|---:|---|---|
| run.trip.BM25.head.test.tar.gz | 12M | . | . |
| run.trip.BM25.tail.test.tar.gz | 12M | . | . |
| run.trip.BM25.torso.test.tar.gz | 12M | . | . |
| triples.train.tsv.tar.gz | 28G | . | . |
| tuples.head.test.top200.tar.gz | 130M | . | . |
| tuples.head.val.top200.tar.gz | 131M | . | . |
| tuples.tail.test.top200.tar.gz | 134M | . | . |
| tuples.tail.val.top200.tar.gz | 134M | . | . |
| tuples.torso.test.top200.tar.gz | 132M | . | . |
| tuples.torso.val.top200.tar.gz | 132M | . | . |

Total: **29G**

### Experiments
### Terms and Conditions
### Legal Notices
### Contact Us
