import tensorflow as tf


##############Build###################
x1 = tf.constant(5)
x2 = tf.constant(6)
result = tf.multiply(x1, x2)
print(result)

#tensorflow version
print(tf.__version__)

##################Run#################
sess = tf.Session()
print(sess.run(result))
sess.close()

#using with statement that doesn't need close

with tf.Session() as sess:
	print(sess.run(result))
