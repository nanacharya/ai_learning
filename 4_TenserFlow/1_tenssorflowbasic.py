import tensorflow as tf
print("test")
print(tf.__version__)
print("TensorFlow version:", tf.__version__)
print("Num GPUs Available: ", len(tf.config.list_physical_devices('GPU')))
# Num GPUs Available:  0 means not supported GPU
print("Physical devices:", tf.config.list_physical_devices())

# Disable eager excution
tf.compat.v1.disable_eager_execution()

tensor = tf.constant("hello, Trensor flow")

with tf.compat.v1.Session() as sess:
    result = sess.run(tensor)
    print(result.decode())


#without session
# print(tensor.numpy().decode())


# operations
a= tf.constant(5)
b= tf.constant(10)

add_op = tf.add(a, b)
with tf.compat.v1.Session() as sess:
    result =  sess.run(add_op)
    print("Result : " , result)



print("float placeholder.... ")

x= tf.compat.v1.placeholder(tf.float32, shape = (None,))
square_op = tf.square(x)

with tf.compat.v1.Session() as sess:
    result = sess.run(square_op, feed_dict = {x: [1,2,3]})
    print("Result : ", result)

