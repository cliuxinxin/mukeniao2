from collections import OrderedDict
import tensorflow as tf
import numpy as np
from tensorflow import keras
from dataset import generate_dataset
from orms import Train,Tran,Result
from utils import RunBuilder

params = OrderedDict(
    batch_size = [32,64], 
    epochs = [1,2]
)

results = []

keras.backend.clear_session()
np.random.seed(42)
tf.random.set_seed(42)

class_names = ["T-shirt/top", "Trouser", "Pullover", "Dress", "Coat",
                "Sandal", "Shirt", "Sneaker", "Bag", "Ankle boot"]

for run in RunBuilder.get_runs(params):
    
    for k,v in run._asdict().items(): results.append(Result(key=k,value=v))

    tran_name = 'generate_train'
    dataset = generate_dataset(name=tran_name)
    dataset = dataset.shuffle(buffer_size=100).batch(run.batch_size)

    model = keras.models.Sequential([
        keras.layers.Flatten(input_shape=[28, 28]),
        keras.layers.Dense(300, activation="relu"),
        keras.layers.Dense(100, activation="relu"),
        keras.layers.Dense(10, activation="softmax")
    ])

    model.compile(loss="sparse_categorical_crossentropy",
                optimizer="sgd",
                metrics=["accuracy"])

    
    history = model.fit(dataset,epochs=run.epochs)

    test_name = 'generate_test'
    dataset = generate_dataset(name=tran_name)
    dataset = dataset.batch(64)

    loss,precise = model.evaluate(dataset)
    
    results.append(Result(key='eval_result',value=precise))
    train = Train.first_or_create(name='test_train')
    tran = Tran.where('name','=',tran_name).first()
    train.trans().attach(tran,{'result':precise})
    train.results().save_many(results)

    print(history)