import tensorflow as tf 
from tensorflow.examples.tutorials.mnist import input_data

mnist = input_data.read_data_sets("/tmp/data/", one_hot=True) #one_hot means one is on and other off

# we have 10 classes, 0-9
n_nodes_hiddenlayer1 = 500
n_nodes_hiddenlayer2 = 500
n_nodes_hiddenlayer3 = 500

n_classes = 10
batch_size = 100

x = tf.placeholder('float', [None, 784])
y = tf.placeholder('float')

def neural_network_model(data):

	#(input_data * weight) + biases

	hidden_1_layer = {'weights' : tf.Variable(tf.random_normal([784, n_nodes_hiddenlayer1])),
	                 'biases' : tf.Variable(tf.random_normal([n_nodes_hiddenlayer1])) } 

	hidden_2_layer = {'weights' : tf.Variable(tf.random_normal([n_nodes_hiddenlayer1, n_nodes_hiddenlayer2])),
	                 'biases' : tf.Variable(tf.random_normal([n_nodes_hiddenlayer2])) } 

	hidden_3_layer = {'weights' : tf.Variable(tf.random_normal([n_nodes_hiddenlayer2, n_nodes_hiddenlayer3])),
	                 'biases' : tf.Variable(tf.random_normal([n_nodes_hiddenlayer3])) } 

	output_layer = {'weights' : tf.Variable(tf.random_normal([n_nodes_hiddenlayer3, n_classes])),
	                 'biases' : tf.Variable(tf.random_normal([n_classes])) } 
	l1 = tf.add(tf.matmul(data, hidden_1_layer['weights']) , hidden_1_layer['biases'])
	l1 = tf.nn.relu(l1)

	l2 = tf.add(tf.matmul(l1, hidden_2_layer['weights']) , hidden_2_layer['biases'])
	l2 = tf.nn.relu(l2)

	l3 = tf.add(tf.matmul(l2, hidden_3_layer['weights']) , hidden_3_layer['biases'])
	l3 = tf.nn.relu(l3)
	output = tf.matmul(l3, output_layer['weights']) + output_layer['biases']
	return output


def train_neural_network(x):
	prediction = neural_network_model(x)
	cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=prediction, labels=y))

	#learning_rate = .0001 default
	optimizer = tf.train.AdamOptimizer().minimize(cost)

	epochs_number = 10

	with tf.Session() as sess:
		sess.run(tf.initialize_all_variables())

		for epoch in range(epochs_number):
			epoch_loss = 0
			for a in range(int(mnist.train.num_examples/batch_size)):
				epoch_x, epoch_y = mnist.train.next_batch(batch_size)
				a, c = sess.run([optimizer, cost], feed_dict={x: epoch_x, y: epoch_y})
				epoch_loss += c
			print('Epoch', epoch, 'completed out of', epochs_number, 'loss:', epoch_loss)

		correct = tf.equal(tf.argmax(prediction, 1), tf.argmax(y, 1))
		accuracy = tf.reduce_mean(tf.cast(correct, 'float'))
		print('Accuracy:', accuracy.eval({x:mnist.test.images, y:mnist.test.labels}))

train_neural_network(x)


'''
Process we follow:

- input > weight > hidden layer 1 (activation function) > weights >
hidden layer 2 (activation function) > weights > output layer

- Compare output to intended output > cost function (cross entropy)
- Optimization function (optimizer) > minimize cost (AdamOptimize, 
stochastic Gradient descent, AdaGrab, ...)
- Backpropagation

-feed forward + backprop = epoch

'''