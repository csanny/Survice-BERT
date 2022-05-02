# Survice-BERT

- `Survice-BERT` is a model for BioNER(Biomedical Named Entity Recognition) in disease surveillance reports. 
- The model is developed by fine-tuning the BERT model using NERDA.
- The purpose of the model is to collect key information of infectious diseases from disease surveillance reports and utilize as training data for prediction model of infectious disease.


## NER tags

- Date(Year, Month, Week, Day)
- Location
- Disease name
- The number of Case and Death


## Datasets




## Requirements

- import torch/1.9.0+cu102 
- import NERDA/0.9.5


## Reference

[1] [BERT](https://github.com/google-research/bert) \n
[2] [BioBERT](https://github.com/dmis-lab/biobert) \n
[3] [SciBERT](https://github.com/allenai/scibert) \n
[4] [NERDA](https://github.com/ebanalyse/NERDA)
