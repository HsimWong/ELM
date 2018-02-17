import numpy as np
from mnist import MNIST
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data


def MELM_MNIST25(Testcode, TrainDataSize, TotalLayers, HiddernNeurons, C1, rhoValue, sigpara, sigpara1, TrainingData_File, TestingData_File) :

	# Basic tf setting
	tf.set_random_seed(2016)
	sess = tf.Session()

	# Get data
	mnist = input_data.read_data_sets("/tmp/data/", one_hot=True)

	train_x = mnist.train.images
	train_y = mnist.train.labels
	
	test_x = mnist.test.images
	test_y = mnist.test.labels

	


	return TrainingTime, TestingTime, TrainingAccuracy, TestingAccuracy