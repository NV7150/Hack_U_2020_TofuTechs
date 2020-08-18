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

# Aug. 2020 copied and modified by Dango from vggish_interfere_test.py

# 使う前にルードディレクトリで以下を実行（ファイルが重すぎてpushできん）
# mkdir PcEnv/checkpoint; cd PcEnv/checkpoint; curl -O https://storage.googleapis.com/audioset/vggish_model.ckpt; curl -O https://storage.googleapis.com/audioset/vggish_pca_params.npz

import os
import tensorflow as tf

from PcEnv.vggish \
    import vggish_input, vggish_postprocess, vggish_slim, vggish_params


path_to_checkpoint = os.path.join('.', 'checkpoints', 'vggish_model.ckpt')
path_to_pca = os.path.join('.', 'checkpoints', 'vggish_pca_params.npz')

class vggish_parser:
    def __init__(self):
        self.pproc = vggish_postprocess.Postprocessor(path_to_pca)

    def parse_with_vggish(self, wav_file):
        examples_batch = vggish_input.wavfile_to_examples(wav_file)

        with tf.Graph().as_default(), tf.compat.v1.Session() as sess:
            vggish_slim.define_vggish_slim(training=False)
            vggish_slim.load_vggish_slim_checkpoint(sess, path_to_checkpoint)

            features_tensor = sess.graph.get_tensor_by_name(
                vggish_params.INPUT_TENSOR_NAME)
            embedding_tensor = sess.graph.get_tensor_by_name(
                vggish_params.OUTPUT_TENSOR_NAME)
            [embedding_batch] = sess.run([embedding_tensor],
                                         feed_dict={features_tensor: examples_batch})

            postprocessed_batch = self.pproc.postprocess(embedding_batch)

        return postprocessed_batch