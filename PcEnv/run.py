# import
from __future__ import absolute_import, division, print_function, unicode_literals
# 標準モジュール
import os
import sys
import argparse
import time
import logging
from sklearn import metrics
import csv
import random
# 要インストール
import tensorflow as tf
import h5py
import numpy as np
import keras
from keras.models import Model
from keras.layers import (Input, Dense, BatchNormalization, Dropout, Lambda,
                          Activation, Concatenate)
import keras.backend as K
from keras.optimizers import Adam


# 下準備
# 関数の宣言
def attention_pooling(inputs, **kwargs):
    [out, att] = inputs

    epsilon = 1e-7
    att = K.clip(att, epsilon, 1. - epsilon)
    normalized_att = att / K.sum(att, axis=1)[:, None, :]

    return K.sum(out * normalized_att, axis=1)


def pooling_shape(input_shape):
    if isinstance(input_shape, list):
        (sample_num, time_steps, freq_bins) = input_shape[0]

    else:
        (sample_num, time_steps, freq_bins) = input_shape

    return sample_num, freq_bins


def get_layer(input_layer):
    drop_rate = 0.5
    hidden_units = 1024

    layer = tf.keras.layers.Dense(hidden_units)(input_layer)
    layer = tf.keras.layers.BatchNormalization()(layer)
    layer = tf.keras.layers.Activation('relu')(layer)
    layer = tf.keras.layers.Dropout(drop_rate)(layer)
    return layer


def get_model():
    # モデルの構成
    time_steps = 10
    freq_bins = 128

    classes_num = 527

    input_l = tf.keras.layers.Input(shape=(time_steps, freq_bins))

    layer1 = get_layer(input_l)

    layer2 = get_layer(layer1)

    # なんかここ並列して繋がってるっぽい？
    da1 = tf.keras.layers.Dense(classes_num, activation='sigmoid')(layer2)
    da2 = tf.keras.layers.Dense(classes_num, activation='softmax')(layer2)

    lamb2 = tf.keras.layers.Lambda(attention_pooling, output_shape=pooling_shape)([da1, da2])

    layer3 = get_layer(layer2)

    db1 = tf.keras.layers.Dense(classes_num, activation='sigmoid')(layer3)
    db2 = tf.keras.layers.Dense(classes_num, activation='softmax')(layer3)

    lamb3 = tf.keras.layers.Lambda(attention_pooling, output_shape=pooling_shape)([db1, db2])

    con = tf.keras.layers.Concatenate(axis=-1)([lamb2, lamb3])
    con = tf.keras.layers.Dense(classes_num)(con)

    out = tf.keras.layers.Activation('sigmoid')(con)

    model = tf.keras.Model(input_l, out)

    model.summary()

    model.load_weights("final_weights.h5")  # パスは必要に応じて変更

    return model


def get_label():
    ##ラベルリストの生成
    label = []
    with open("class_labels_indices.csv")as f:
        read = csv.reader(f)
        for i in read:
            label.append(i[2])
    label.pop(0)
    return label
