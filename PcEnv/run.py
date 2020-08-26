# The MIT License
#
# Copyright (c) 2010-2017 Google, Inc. http://angularjs.org
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

# Copied and changed from keras/core.py of https://github.com/IBM/audioset-classification/tree/master/audioset_classify

# import
from __future__ import absolute_import, division, print_function, unicode_literals
# 標準モジュール
import csv
import os
# 要インストール
import tensorflow as tf
import keras.backend as K


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

    classes_num = 3

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

    model_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'AudioSetModel.5.0019.ckpt')
    model.load_weights(model_path)  # パスは必要に応じて変更

    return model


def get_label():
    # ラベルリストの生成
    return {0: 'water', 1: 'impact', 2: 'else'}
