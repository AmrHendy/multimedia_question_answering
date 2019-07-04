from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
import os
import tensorflow as tf

__path__ = os.path.abspath(os.path.dirname(__file__))
LSMDC_DATA_PATH = os.path.normpath(os.path.join(__path__, "../dataset/LSMDC"))

"""
we tried these changes:
1- added squeeze links to the 3 conv layers in the fusion. (done)
2. change the lstm_cell type which is used in both video embedding and caption embedding building. (done)
3. change the hidden units of the lstm_cell. (done)
4. change the value of self.dropout_keep_prob instead of 0.5 (TODO)
5. change the learning rate from 0.0001 to 0.00001. (done)
6. change the self.optimizer from 'Adam' to 'Adamax' and 'Nadam'. (TODO)
7. change the num_layers from 1. (TODO)
"""

class ModelConfig(object):

    def __init__(self):
        self.batch_size = 16
        self.ret_batch_size = 10

        self.video_height = 299
        self.video_width = 299
        self.video_steps = 40
        self.caption_length = 40

        self.attr_length = 10

        self.word_dim = 300
        self.num_layers = 1
        # hidden dim = hidden units for the lstm cell for both video and caption
        self.hidden_dim = 512
        self.video_embedding_size = 1024

        self.image_feature_net = 'resnet'
        self.layer = 'pool5'

        self.dropout_keep_prob = 0.5
        self.lstm_cell = 'BasicLSTM'
        self.loss_weight = 0.1


        self.wav_data = False


class TrainConfig(object):

    def __init__(self):
        self.learning_rate = 0.0001
        self.train_dir = None
        # as dataset is 26052 video caption pair
        self.max_steps = 65130
        self.last_step_taken = 35000
        self.num_epochs = 10

        self.learning_rate_decay_steps = 500000
        self.learning_rate_decay_factor = 0.5
        self.optimizer = 'Adam'
        self.max_grad_norm = 5.0

        self.steps_per_logging = 1000
        self.steps_per_evaluate = 2500
        self.train_tag = 'RET'

        #'/content/checkpoint/RET_/model.ckpt-35000'
        self.load_from_ckpt = '/content/checkpoint/RET_/model.ckpt-35000'
        self.print_evaluate = False
