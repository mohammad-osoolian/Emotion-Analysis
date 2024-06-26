# -*- coding: utf-8 -*-
"""PreprocessDataset.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1z8ZEP8bSRQ2cSFVwpyn9C851mblKXmn1
"""

! cd content
! git clone https://github.com/Arman-Rayan-Sharif/arman-text-emotion.git

import numpy as np

classes = ['HAPPY', 'SAD', 'ANGRY', 'FEAR', 'SURPRISE', 'HATE', 'OTHER']
class2id = {classes[i]: i for i in range(len(classes))}
id2class = {i: classes[i] for i in range(len(classes))}

def class2onehot(classname):
  classid = class2id[classname]
  result = np.zeros(len(classes))
  result[classid] = 1
  return result

def preprocess_file(inpath, outpath):
  with open(inpath, 'r') as f:
    lines = f.readlines()
  texts = []
  labels = []
  ids = []

  for i, line in enumerate(lines):
    line = line.strip()
    text, classname = line.split('\t')
    id = i
    texts.append(text)
    labels.append(class2onehot(classname))
    ids.append(id)

  with open(outpath, 'w') as f:
    f.write('ID\tText\tLabel\n')
    for i in range(len(ids)):
      f.write(f'{ids[i]}\t{texts[i]}\t{labels[i]}\n')

preprocess_file('arman-text-emotion/dataset/train.tsv', 'pptrain.tsv')
preprocess_file('arman-text-emotion/dataset/test.tsv', 'pptest.tsv')