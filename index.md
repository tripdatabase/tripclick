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
|---|---:|
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
We offer the following three resource packages listed below:
* TripClick Logs Dataset
* TripClick IR Benchmark
* TripClick Training Package for Deep Learning Models

One or more of the listed above can be requested for free via an email.
Please, specify ...
### Experiments
### Terms and Conditions
### Legal Notices
### Contact Us







You can use the [editor on GitHub](https://github.com/tripdatabase/TripClick/edit/gh-pages/index.md) to maintain and preview the content for your website in Markdown files.

Whenever you commit to this repository, GitHub Pages will run [Jekyll](https://jekyllrb.com/) to rebuild the pages in your site, from the content in your Markdown files.

### Markdown

Markdown is a lightweight and easy-to-use syntax for styling your writing. It includes conventions for

```markdown
Syntax highlighted code block

# Header 1
## Header 2
### Header 3

- Bulleted
- List

1. Numbered
2. List

**Bold** and _Italic_ and `Code` text

[Link](url) and ![Image](src)
```

For more details see [GitHub Flavored Markdown](https://guides.github.com/features/mastering-markdown/).

### Jekyll Themes

Your Pages site will use the layout and styles from the Jekyll theme you have selected in your [repository settings](https://github.com/tripdatabase/TripClick/settings). The name of this theme is saved in the Jekyll `_config.yml` configuration file.

### Support or Contact

Having trouble with Pages? Check out our [documentation](https://docs.github.com/categories/github-pages-basics/) or [contact support](https://support.github.com/contact) and we’ll help you sort it out.
