'''
nlp-with-tensorflow.py

Natural Language Processing (NLP) with TensorFlow
-------------------------------------------------

Inspired by work from the Stanford University course
CS224N, we will explore some of the currently common
techniques associated with Natural Language
Processing and Deep Learning.
'''

# Header
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

# Imports
import pandas as pd
import tensorflow as tf
import matplotlib.pyplot as plt
import seaborn as sns

from numpy import array
from numpy import argmax
from nltk.tokenize import wordpunct_tokenize
from gensim import corpora
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

# Getting the data
ENCODING = 'ISO-8859-1'
USECOLS = ['text', 'user']

# Text corpus
def create_document_corpus(df, column):
    '''Creates document corpus.'''
    return [i for i in df[column]]

# Removing common words and tokenize
def tokenise(document_corpus):
    '''Tokenises text.'''
    return [[word for word in doc.lower().split()] for doc in document_corpus]

# Labels
def encode(dataset):
    '''Encodes labels.'''
    print(f'Shape before encoding: {len(dataset)}')
    encoded = tf.keras.utils.to_categorical(dataset)
    print(f'Shape after encoding: {encoded.shape}')
    return encoded

if __name__ == '__main__':
    # Get data
    # Trump
    trump = pd.read_csv('../data/realDonaldTrump.csv',
                        encoding=ENCODING,
                        usecols=USECOLS)
    #Obama
    obama = pd.read_csv('../data/BarackObama.csv',
                        encoding=ENCODING,
                        usecols=USECOLS)
    # Senators
    senartors = pd.read_csv('../data/senators.csv',
                            encoding=ENCODING,
                            usecols=USECOLS)

    # Concatenate
    df = pd.concat([trump, obama, senators])

    # Formatting text
    document = create_document_corpus(df, 'text')
    tokenised_doc = tokenise(document)
    dictionary = corpora.Dictionary(tokenised_doc)

    # Feature data
    data = list(map(lambda item: dictionary.doc2idx(tokenised_doc[item]),
                    range(len(tokenised_doc))))

    values = array(df['user'].values)
    label_encoder = LabelEncoder()
    integer_encodings = label_encoder.fit_transform(values)
    labels = encode(integer_encodings)

    # Train-test split
    x_train, x_test, y_train, y_test = train_test_split(data,
                                                        labels,
                                                        test_size=.25,
                                                        shuffle=True)
    print(f'X-train: {len(x_train)}, Y-train: {len(y_train)}')
    print(f'X-test: {len(x_test)}, Y-test: {len(y_test)}')

    # Pad the data
    x_train = tf.keras.preprocessing.sequence.pad_sequences(x_train,
                                                            value=0,
                                                            padding='post',
                                                            maxlen=45)
    x_test = tf.keras.preprocessing.sequence.pad_sequences(x_test,
                                                        value=0,
                                                        padding='post',
                                                        maxlen=45)

    # Create validation set
    # Feature set
    x_val, partial_x_train = x_train[:10000], x_train[10000:]
    # Label set
    y_val, partial_y_train = y_train[:10000], y_train[10000:]

    # Build model
    vocab_size = 458047
    model = tf.keras.Sequential()
    model.add(tf.keras.layers.Embedding(vocab_size, 128))
    model.add(tf.keras.layers.GlobalAveragePooling1D())
    model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))
    model.add(tf.keras.layers.Flatten())
    model.add(tf.keras.layers.Dense(102, activation=tf.nn.softmax))
    # model.summary()

    # Compile
    model.compile(optimizer='adam',
                loss='categorical_crossentropy',
                metrics=['acc'])

    # Train
    history = model.fit(partial_x_train,
                        partial_y_train,
                        epochs=10,
                        batch_size=512,
                        validation_data=(x_val, y_val),
                        verbose=1)

    # Evaluate
    results = model.evaluate(x_test, y_test)
    print(results)

    # Plotting
    history_dict = history.history
    acc = history_dict['acc']
    val_acc = history_dict['val_acc']
    loss = history_dict['loss']
    val_loss = history_dict['val_loss']
    epochs = range(1, len(acc) + 1)

    f, (ax1, ax2) = plt.subplots(2, 1, figsize=(20, 20), dpi=80, sharex=True)
    sns.lineplot(epochs, acc, label='Training', color='navy', ax=ax1)
    sns.lineplot(epochs, val_acc, label='Validation', color='brown', ax=ax1)
    sns.lineplot(epochs, loss, label='Loss', color='navy', ax=ax2)
    sns.lineplot(epochs, val_loss, label='Validation', color='brown', ax=ax2)
    ax1.set_title('Training & Validation Accuracy', fontsize=22)
    ax2.set_title('Training & Validation Loss', fontsize=22)
    ax1.set_ylabel('Accuracy', fontsize=14)
    ax2.set_ylabel('Loss', fontsize=14)
    ax1.legend(), ax2.legend()
    plt.xlabel('Epochs', fontsize=14)
    plt.show()
