import os
from sklearn.metrics import accuracy_score
from keras.datasets import cifar,mnist,imdb
import numpy as np
import itertools

import matplotlib.pyplot as plt
from sklearn.metrics import f1_score,precision_recall_fscore_support
import BuildModel
from sklearn.feature_extraction.text import CountVectorizer
from itertools import chain
from keras.callbacks import ModelCheckpoint

def plot_RMDL(history_):
    Number_of_models = len(history_)
    plt.legend(['RDL 1', 'RDL 2', 'RDL 3', 'RDL 4', 'RDL 5', 'RDL 6', 'RDL 7', 'RDL 8', 'RDL 9', 'RDL 10',
                'RDL 11', 'RDL 12', 'RDL 13', 'RDL 14', 'RDL 15'], loc='upper right')
    for i in range(0, Number_of_models):
        plt.plot(history_[i].history['acc'])
        plt.title('model accuracy')
        plt.ylabel('accuracy')
        plt.xlabel('epoch')
    plt.legend(['RDL 1', 'RDL 2', 'RDL 3', 'RDL 4', 'RDL 5', 'RDL 6', 'RDL 7', 'RDL 8', 'RDL 9', 'RDL 10',
                'RDL 11', 'RDL 12', 'RDL 13', 'RDL 14', 'RDL 15'], loc='upper right')
    plt.show()



    for i in range(0, Number_of_models):
        plt.plot(history_[i].history['val_acc'])
        plt.title('model accuracy')
        plt.ylabel('accuracy')
        plt.xlabel('epoch')

    plt.show()
    plt.legend(['RDL 1', 'RDL 2', 'RDL 3', 'RDL 4', 'RDL 5', 'RDL 6', 'RDL 7', 'RDL 8', 'RDL 9', 'RDL 10',
                'RDL 11', 'RDL 12', 'RDL 13', 'RDL 14', 'RDL 15'], loc='upper right')
    for i in range(0, Number_of_models):
        # summarize history for loss
        plt.plot(history_[i].history['loss'])

        plt.title('model loss train')
        plt.ylabel('loss')
        plt.xlabel('epoch')

    plt.legend(['RDL 1', 'RDL 2', 'RDL 3', 'RDL 4', 'RDL 5', 'RDL 6', 'RDL 7', 'RDL 8', 'RDL 9', 'RDL 10',
                'RDL 11', 'RDL 12', 'RDL 13', 'RDL 14', 'RDL 15'], loc='upper right')
    plt.show()
    plt.legend(
        ['RDL 1', 'RDL 2', 'RDL 3', 'RDL 4', 'RDL 5', 'RDL 6', 'RDL 7', 'RDL 8', 'RDL 9', 'RDL 10', 'RDL 11',
         'RDL 12', 'RDL 13', 'RDL 14', 'RDL 15'], loc='upper right')
    for i in range(0, Number_of_models):
        # summarize history for loss
        plt.plot(history_[i].history['val_loss'])

        plt.title('model loss test')
        plt.ylabel('loss')
        plt.xlabel('epoch')
    plt.legend(['RDL 1', 'RDL 2', 'RDL 3', 'RDL 4', 'RDL 5', 'RDL 6', 'RDL 7', 'RDL 8', 'RDL 9', 'RDL 10',
                'RDL 11', 'RDL 12', 'RDL 13', 'RDL 14', 'RDL 15'], loc='upper right')
    plt.show()


def plot_confusion_matrix(cm, classes,
                          normalize=False,
                          title='Confusion matrix',
                          cmap=plt.cm.Blues):
    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=45)
    plt.yticks(tick_marks, classes)

    fmt = '.2f' if normalize else 'd'
    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, format(cm[i, j], fmt),
                 horizontalalignment="center",
                 color="white" if cm[i, j] > thresh else "black")

    plt.tight_layout()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')
    plt.show()




def accuracy(y_test,final_y):
    np.set_printoptions(precision=2)
    y_test_temp = np.argmax(y_test, axis=1)
    F_score = accuracy_score(y_test_temp, final_y)
    F1 = precision_recall_fscore_support(y_test_temp, final_y, average='micro')
    F2 = precision_recall_fscore_support(y_test_temp, final_y, average='macro')
    F3 = precision_recall_fscore_support(y_test_temp, final_y, average='weighted')
    print(F_score)
    print(F1)
    print(F2)
    print(F3)