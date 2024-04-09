# authors: Mert Erol, Ishana Rana
# environment: Python 3.12.0, numpy 1.26.1, gensim 4.3.2
# encoding: utf-8

import numpy as np
from gensim.models import KeyedVectors

full_path = "/Users/merterol/Downloads"
model = KeyedVectors.load_word2vec_format(f"{full_path}/cc.en.300.vec.gz", binary=False, limit=500000)

v_animalkingdom, v_adorable, v_deadly = (model["animal"] + model["kingdom"]) / 2, model["adorable"], model["deadly"]

print(f"Similarity between Animal Kingdom and Adorable: {np.dot(v_animalkingdom, v_adorable) / (np.linalg.norm(v_animalkingdom) * np.linalg.norm(v_adorable))}")
print(f"Similarity between Animal Kingdom and Deadly: {np.dot(v_animalkingdom, v_deadly) / (np.linalg.norm(v_animalkingdom) * np.linalg.norm(v_deadly))}")