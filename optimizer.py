import tensorflow as tf 

# Model parameters
w = tf.Variable([.3], tf.float32)
b = tf.Variable([-.3], tf.float32)

#inputs and outputs
x = tf.placeholder(tf.float32)
linear_model = w * x + b
y = tf.placeholder(tf.float32)

#loss
squared_delta = tf.square(linear_model-y)
loss = tf.reduce_sum(squared_delta)

#optimize
optimizer = tf.train.GradientDescentOptimizer(0.01)
train = optimizer.minimize(loss)

init = tf.global_variables_initializer()


sess = tf.Session()
sess.run(init)


for i in range(1000):
	sess.run(train, {x:[1,2,3,4], y:[0, -1, -2, -3]})

print(sess.run([w, b]))

#print(sess.run(loss, {x:[1,2,3,4], y:[0, -1, -2, -3]}))


#output: [array([-0.9999969], dtype=float32), array([ 0.99999082], dtype=float32)]
#The optimizer optimizes loss and gives us efficient 
#value as near to -1 for w and 1 for b. If we use those values
#loss will be zero. 