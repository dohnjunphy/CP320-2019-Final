import tensorflow as tf
import numpy
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

file = open("dictionary.txt", mode='r')
dictlist = [None]*250
for i in range(250):
    dictin = file.readline()
    cutoff = 0
    for j in dictin:
        if(j=='['):
            break;
        cutoff+=1
    dictlist[i] = (dictin[0:cutoff], int(dictin[cutoff+1:len(dictin)-2]))
file.close()

trfe = open("train-features.txt", mode='r')
trla = open("train-labels.txt", mode='r')


tr_mat = [None]*100
tr_mat[0] = [0]*250
for i in range(100):
    while(1==1):
        buf = trfe.readline()
        if(buf == ""):
            break;
        buf = buf.split(" ")
        if(buf[0] == i):
            tr_mat[i][int(buf[1])] = int(buf[2])
        elif(int(buf[0]) > i):
            tr_mat[int(buf[0])] = [0]*250
            tr_mat[int(buf[0])][int(buf[1])] = int(buf[2])
            break;

tr_la = [None]*100
for i in range(100):
    tr_la[i] = int(trla.readline())
    

X_train, X_test, y_train, y_test = train_test_split(tr_mat,tr_la,random_state=42, train_size=0.8, test_size=0.2)    

layer = tf.keras.layers.Dense(units=1, input_shape=[250])
model = tf.keras.Sequential([layer])
model.compile(loss='mean_squared_error', optimizer=tf.keras.optimizers.Adam(0.1))

trained_model = model.fit(X_train, y_train, epochs=1000, verbose=False)
print("Finished training the model")

#get trfe in here
tefe = open("test-features.txt", mode='r')
tela = open("test-labels.txt", mode='r')

te_mat = [None]*260
te_mat[0] = [0]*250
for i in range(260):
    while(1==1):
        buf = tefe.readline()
        if(buf == ""):
            break;
        buf = buf.split(" ")
        if(buf[0] == i):
            te_mat[i][int(buf[1])] = int(buf[2])
        elif(int(buf[0]) > i):
            te_mat[int(buf[0])] = [0]*250
            te_mat[int(buf[0])][int(buf[1])] = int(buf[2])
            break;

te_la = [None]*260
for i in range(260):
    te_la[i] = int(tela.readline())

predictions = model.predict(te_mat)
tp = 0
tn = 0
fp = 0
fn = 0
for i in range(len(predictions)):
    if(te_la[i] != None):
        if(te_la[i] == 1 and predictions[i] > 0):
            tp+=1
        elif(te_la[i] ==1 and predictions[i] <= 0):
            fp+=1
        elif(te_la[i] ==0 and predictions[i] > 0):
            tn+=1
        elif(te_la[i] ==0 and predictions[i] <= 0):
            fn+=1
    print("True Positive: %d | False Positive: %d" %(tp, fp))
    print("True Negative: %d | False Negative: %d" %(tn, fn))
