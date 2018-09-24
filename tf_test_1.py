import tensorflow as tf
import numpy as np
w = 3.7
b = 5.2
x_data = np.random.rand(100).astype(np.float32)
y_data = x_data*w + b
Weights = tf.Variable(tf.random_uniform([1], -10, 10))
biases = tf.Variable(tf.zeros([1]))
y = Weights*x_data + biases
loss = tf.reduce_mean(tf.square(y-y_data))
optimizer = tf.train.GradientDescentOptimizer(0.5)
train = optimizer.minimize(loss)
init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)
print('y=', w, '*x+', b)
for step in range(2001):
    sess.run(train)
    if step % 100 == 0:
        print(step, sess.run(Weights), sess.run(biases))
print('y=', sess.run(Weights), '*x+', (sess.run(biases)))
