# -*- coding: utf-8 -*-
# Implementation of Wang et al 2017: Automatic Brain Tumor Segmentation using Cascaded Anisotropic Convolutional Neural Networks. https://arxiv.org/abs/1709.00382

# Author: Guotai Wang
# Copyright (c) 2017-2018 University College London, United Kingdom. All rights reserved.
# http://cmictig.cs.ucl.ac.uk
#
# Distributed under the BSD-3 licence. Please see the file licence.txt
# This software is not certified for clinical use.
#
import tensorflow as tf

def rename(checkpoint_from, checkpoint_to, replace_from, replace_to):
    checkpoint = tf.train.get_checkpoint_state(checkpoint_from)
    with tf.Session() as sess:
        for var_name, _ in tf.contrib.framework.list_variables(checkpoint_from):
            print(var_name)
            # Load the variable
            var = tf.contrib.framework.load_variable(checkpoint_from, var_name)

            # Set the new name
            new_name = var_name
            if None not in [replace_from, replace_to]:
                new_name = new_name.replace(replace_from, replace_to)
            var = tf.Variable(var, name=new_name)

        # Save the variables
        saver = tf.train.Saver()
        sess.run(tf.global_variables_initializer())
        saver.save(sess, checkpoint_to)

if __name__ == '__main__':
    net_name   = ['wt', 'tc', 'en']
    net_name_c = ['WT', 'TC', 'EN']
    num_pretrain = [1000, 1000, 1000]
    for i in range(3):
        for view in ['sg', 'cr']:
            checkpoint_from = "model/msnet_{0:}32_{1:}.ckpt".format(net_name[i], num_pretrain[i])
            checkpoint_to   = "model/msnet_{0:}32{1:}_init".format(net_name[i], view)
            replace_from   = "MSNet_32".format(net_name_c[i])
            replace_to     = "MSNet_32{0:}".format(net_name_c[i], view)
            rename(checkpoint_from, checkpoint_to, replace_from, replace_to)
