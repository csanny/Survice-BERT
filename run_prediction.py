#!/usr/bin/env python
# coding: utf-8

# import module
import torch
from NERDA.models import NERDA

# import model
model = torch.load('SurviceBERT_V2_32-16.pt')

# predict NER ex1
model.predict_text('During the period 12 January to 15 March 2022, a total of 53 suspected yellow fever cases, including six deaths, have been reported from Isiolo county, central Kenya.')

# predict NER ex2
model.predict_text('On 5 April 2022, WHO was notified of 10 cases of severe acute hepatitis of unknown aetiology in children under the age of 10 years, across central Scotland.')
