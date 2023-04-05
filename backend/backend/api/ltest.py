# import tensorflow as tf
# from keras.preprocessing.text import Tokenizer
# from tensorflow.keras.preprocessing.sequence import pad_sequences
# import tensorflow as tf
# import numpy as np
# import os
# print(os.getcwd())
# model = tf.keras.models.load_model('backend/backend/api/reviewtestbackendmodel.h5')

# # print(model.summary())
# tokenizer=Tokenizer()
# x = tokenizer.texts_to_sequences(["I did not received any user manul  wall mount stand and any warranty card for this TV from seller Must be fake information provided by seller"])
# x = pad_sequences(x, maxlen=100)
# #model = tf.keras.models.load_model('api/reviewtestbackendmodel.h5')
# y_pred = model.predict(x)
# pred_call=np.argmax(y_pred[0])
# class_names = ['Fake', 'Genuine']
# pred = { 'pred': class_names[pred_call]}
# print(pred)
import joblib

model=joblib.load(open('backend/backend/api/Adaboost.pkl','rb'))
print(model.predict([["10.4","15.2","12","132","0","123","21","2","1","2","3"]]))

