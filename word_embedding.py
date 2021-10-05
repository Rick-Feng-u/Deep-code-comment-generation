from xml_to_seq import xml_to_prufer

from tensorflow.keras.preprocessing.text import one_hot

from tensorflow.keras.layers import Embedding
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential

import numpy as np

generated_sequence = xml_to_prufer('test.xml')
voc_size = 171476

onehot_repr=[one_hot(words,voc_size)for words in generated_sequence] 
print(onehot_repr)

# TODO would sentences size too large effect outcome?
item_size = 28
embedded_docs=pad_sequences(onehot_repr,padding='post',maxlen=item_size)
print(embedded_docs)

# TODO research deep on accurate dimensions
dimensions = 15

model=Sequential()
model.add(Embedding(voc_size,dimensions,input_length=item_size))
model.compile('adam','mse')

model.summary()

print(model.predict(embedded_docs)[0])