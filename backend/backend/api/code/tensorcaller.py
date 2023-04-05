from keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import tensorflow as tf
import numpy as np
# import os


def getTensorModelPred(text):
    tokenizer=Tokenizer()
    x = tokenizer.texts_to_sequences([text])
    x = pad_sequences(x, maxlen=100)
    model = tf.keras.models.load_model('api/code/reviewtestbackendmodel.h5')
    y_pred = model.predict(x)
    pred_call=np.argmax(y_pred[0])
    class_names = ['Fake', 'Genuine']
    # pred = { 'pred': class_names[pred_call]}
    # print(pred)
    return class_names[pred_call]