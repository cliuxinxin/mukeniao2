import tensorflow as tf
import numpy as np
from tensorflow import keras
from dataset import generate_dataset
from orms import Train,Tran

tran_name = 'generate_train'
dataset = generate_dataset(name=tran_name)
dataset = dataset.shuffle(buffer_size=100).batch(64)


class_names = ["T-shirt/top", "Trouser", "Pullover", "Dress", "Coat",
               "Sandal", "Shirt", "Sneaker", "Bag", "Ankle boot"]

keras.backend.clear_session()
np.random.seed(42)
tf.random.set_seed(42)

model = keras.models.Sequential([
    keras.layers.Flatten(input_shape=[28, 28]),
    keras.layers.Dense(300, activation="relu"),
    keras.layers.Dense(100, activation="relu"),
    keras.layers.Dense(10, activation="softmax")
])

model.compile(loss="sparse_categorical_crossentropy",
              optimizer="sgd",
              metrics=["accuracy"])

train = Train.first_or_create(name='test_train')
tran = Tran.where('name','=',tran_name).first()
history = model.fit(dataset,epochs=1)

test_name = 'generate_test'
dataset = generate_dataset(name=tran_name)
dataset = dataset.batch(64)

loss,precise = model.evaluate(dataset)
train.trans().attach(tran,{'result':precise})

print(history)