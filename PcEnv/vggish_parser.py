# Copyright 2017 The TensorFlow Authors All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# =============================================================================

# 使う前にルードディレクトリで以下を実行（ファイルが重すぎてpushできん）
# mkdir PcEnv/checkpoint; cd PcEnv/checkpoint; curl -O https://storage.googleapis.com/audioset/vggish_model.ckpt; curl -O https://storage.googleapis.com/audioset/vggish_pca_params.npz

import os
import tensorflow as tf

from PcEnv.models.research.audioset.vggish \
    import vggish_input, vggish_postprocess, vggish_slim, vggish_params


path_to_checkpoint = os.path.join('.', 'checkpoints', 'vggish_model.ckpt')
path_to_pca = os.path.join('.', 'checkpoints', 'vggish_pca_params.npz')


def parse_with_vggish(wav_file):
    examples_batch = vggish_input.wavfile_to_examples(wav_file)
    print(examples_batch)
    pproc = vggish_postprocess.Postprocessor(path_to_pca)
    with tf.Graph().as_default(), tf.compat.v1.Session() as sess:
        # Define the model in inference mode, load the checkpoint, and
        # locate input and output tensors.
        vggish_slim.define_vggish_slim(training=False)
        vggish_slim.load_vggish_slim_checkpoint(sess, path_to_checkpoint)
        features_tensor = sess.graph.get_tensor_by_name(
            vggish_params.INPUT_TENSOR_NAME)
        embedding_tensor = sess.graph.get_tensor_by_name(
            vggish_params.OUTPUT_TENSOR_NAME)

        # Run inference and postprocessing.
        [embedding_batch] = sess.run([embedding_tensor],
                                     feed_dict={features_tensor: examples_batch})
        print(embedding_batch)
        postprocessed_batch = pproc.postprocess(embedding_batch)
        print(postprocessed_batch)
    return postprocessed_batch

        # Write the postprocessed embeddings as a SequenceExample, in a similar
        # format as the features released in AudioSet. Each row of the batch of
        # embeddings corresponds to roughly a second of audio (96 10ms frames), and
        # the rows are written as a sequence of bytes-valued features, where each
        # feature value contains the 128 bytes of the whitened quantized embedding.
        # seq_example = tf.train.SequenceExample(
        #     feature_lists=tf.train.FeatureLists(
        #         feature_list={
        #             vggish_params.AUDIO_EMBEDDING_FEATURE_NAME:
        #                 tf.train.FeatureList(
        #                     feature=[
        #                         tf.train.Feature(
        #                             bytes_list=tf.train.BytesList(
        #                                 value=[embedding.tobytes()]))
        #                         for embedding in postprocessed_batch
        #                     ]
        #                 )
        #         }
        #     )
        # )
    # return [[embedding.tobytes()] for embedding in postprocessed_batch]