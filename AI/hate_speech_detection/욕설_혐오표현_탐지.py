# -*- coding: utf-8 -*-
"""욕설/혐오표현 탐지.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1uzrMg5wdijFb_DXB_jxc2NlxJ6XiPzEE
"""

!pip install transformers

from transformers import BertForSequenceClassification, TrainingArguments, Trainer, AutoTokenizer
import torch
import numpy as np

from transformers import TextClassificationPipeline, BertForSequenceClassification, AutoTokenizer

model_name = 'smilegate-ai/kor_unsmile'

model = BertForSequenceClassification.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

pipe = TextClassificationPipeline(
model=model,
tokenizer=tokenizer,
device=-1,     # cpu: -1, gpu: gpu number
return_all_scores=True,
function_to_apply='sigmoid'
     )

for result in pipe("시발새끼")[0]:
    print(result)

