import tensorflow as tf
print("test")
print(tf.__version__)
print("TensorFlow version:", tf.__version__)
print("Num GPUs Available: ", len(tf.config.list_physical_devices('GPU')))
# Num GPUs Available:  0 means not supported GPU
print("Physical devices:", tf.config.list_physical_devices())