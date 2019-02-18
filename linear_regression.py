'''

linear regression exercise for y=3*x +1

'''


import tensorflow as tf
import numpy as np

max_val=100

x=np.linspace(1.0,1.0+max_val,max_val,endpoint=False)
x=x/max_val

y=3*x+1+0.0033*np.random.randn(max_val)

# print("x shape is {}".format(x.shape))
# print("y shape is {}".format(y.shape))

batchsize=5
iteration=max_val//batchsize

X=tf.placeholder(tf.float32,shape=[None])
Y=tf.placeholder(tf.float32,shape=[None])

weight=tf.Variable(0.0)
bias=tf.Variable(0.0)

predict=tf.add(tf.multiply(X,weight),bias)
loss=tf.square(tf.subtract(predict,Y))
loss=tf.reduce_sum(loss)/batchsize
optimizer=tf.train.GradientDescentOptimizer(learning_rate=0.01).minimize(loss)


with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for epoch in range(200):
        random_index=np.random.permutation(iteration*batchsize)
        for step in range(iteration):
            x_input=x[random_index[step*batchsize:step*batchsize+batchsize]]
            y_input=y[random_index[step*batchsize:step*batchsize+batchsize]]
            opt,l,w,b=sess.run([optimizer,loss,weight,bias],feed_dict={X:x_input,Y:y_input})
            print("epoch is {},step is {}, loss is {:.3f},  weight is {:.3f}, bias is {:.3f}".format(epoch,step,l,w,b))
