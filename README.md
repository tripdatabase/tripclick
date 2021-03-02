## Usage
1) In configs/jku-msmarco-passge-PGN.yaml in lines 6-12 uncomment/comment needed work folders;
2) 7.06.20 14:00 the config is set to start validation after just 50 training batches to catch the feeding bug (issue #4) which comes up after 56k batches of validation;
3) python3 train.py --run-name experiment1 --config-file configs/jku-msmarco-passage-PGN.yaml --cuda --gpu-id 0

### Usage - test
```sh
$ python3 train.py --cuda --gpu-id 0 --run-folder /share/home/oleg/experiments/NEUROIR_WORKS/msmarco-passage/generative/2020-08-17_112302.61_KNRM_performance --test
```
* key ```--custom-test-depth <int>``` to fix reranking depth during test;
* key ```--test-files-prefix <str>``` to add meaningful pre to saved test files. Files do not get overwrited. Meaningless prefixes are added in case of conflicts.

Set those three below for new custom test set:
* key ```--custom-test-tsv <str>```
* key ```--custom-test-qrels <str>```
* key ```--custom-test-candidates <str>```

### Usage - test commands:
Test-set 1: **SPARCE**
```sh
$ python3 train.py --cuda --test --custom-test-depth 200 --custom-test-tsv "/share/cp/datasets/ir/msmarco/passage/processed/validation.not-subset.top200.cleaned.split-4/*" --custom-test-qrels "/share/cp/datasets/ir/msmarco/passage/qrels.dev.tsv" --custom-test-candidates "/share/cp/datasets/ir/msmarco/passage/run.msmarco-passage.BM25_k1_0.9_b_0.4.dev.txt" --test-files-pretfix "SPARSE-" --run-folder <run_folder> --gpu-id 0
```

Test-set 2: **TREC - 2019**
```sh
$ python3 train.py --cuda --test --custom-test-depth 200 --custom-test-tsv "/share/cp/datasets/ir/msmarco/passage/processed/test2019.top1000.cleaned.split-4/*" --custom-test-qrels "/share/cp/datasets/ir/msmarco/passage/test2019-qrels.txt" --custom-test-candidates "/share/cp/datasets/ir/msmarco/passage/run.msmarco-passage.BM25-k1_0.82_b_0.72.test2019.txt" --test-files-pretfix "TREC-19-" --run-folder <run_folder> --gpu-id 0
```


## Other
* key ```--debug``` can be used to check if the whole pipeline is in one piece: it shortens training, validation and test;
* make sure to adjust "expirement_base_path" and "debug_base_path" in ```configs/*.yaml```

## "Best" settings for running different models
* KNRM
```sh
$ python train.py --config-file [PATH_TO_CONFIG_FILE] --cuda --gpu-id 0 --config-overwrites "model: knrm, loss: maxmargin, param_group0_learning_rate: 0.001"
```
