# Survice-BERT

- `Survice-BERT` is a model for BioNER(Biomedical Named Entity Recognition) in disease surveillance reports. 
- The model is developed by fine-tuning the BERT model using NERDA.
- The purpose of the model is to collect key information of infectious diseases from disease surveillance reports and utilize as training data for prediction model of infectious disease.


## Datasets

- We build our datasets because of no open datasets containing the tags we want to extract.
- We created a dataset identical to the CoNLL-2003 dataset format.
- Example of datset

```bash
  'sentence': 'Update on the measles outbreak on ', 
              ' reported last week : As of 20 February 2012 ( week 8 ) , there are 1326 confirmed cases with 1113 deaths',  
  'tag': ['O','O','O','B-DISEASE','O','O'], 
         ['O','B-DATE_WEEK','O','O','O','O','B-DATE_DAY','B-DATE_MONTH','B-DATE_YEAR','O','O','B-DATE_WEEK','O','O','O','O','B-TOTAL_CASE','O','O','O','B-TOTAL_DEATH','O','O']
```

- NER tags

  - Date(Year, Month, Week, Day)
  - Location
  - Disease name
  - The number of Case and Death


## Requirements

```bash
import numpy/1.22.2
import pandas/1.4.4
import torch/1.13.0a0+936e930
import NERDA/0.9.6
```

## Reference

[1] [BERT](https://github.com/google-research/bert) 

[2] [BioBERT](https://github.com/dmis-lab/biobert) 

[3] [SciBERT](https://github.com/allenai/scibert) 

[4] [NERDA](https://github.com/ebanalyse/NERDA)

[5] [CoNLL-2003](https://www.clips.uantwerpen.be/conll2003/ner/)
