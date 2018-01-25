import tensorflow as tf 


############Constant#################
node1 = tf.constant(3.0, tf.float32)
node2 = tf.constant(4.0)

print(node1, node2)


###########Placeholder##############

a = tf.placeholder(tf.float32)
b = tf.placeholder(tf.float32)

adder_node = a + b 

sess = tf.Session()
print(sess.run(adder_node, {a: [1, 2], b: [3, 4]}))

sess.close()