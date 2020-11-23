from orms import Tran,Entry
import imageio
import tensorflow as tf


def generate_dataset(gen_name='generate_train'):
    tran = Tran.where('name','=','generate_train').first()

    def dataset_fn():
        for entry in tran.entries().get():
            imgarr = imageio.imread(entry.location)
            label = entry.label 
            yield imgarr,label

    dataset = tf.data.Dataset.from_generator(dataset_fn,
        (tf.float32,tf.float32),
        (tf.TensorShape([28,28]),tf.TensorShape([]))
        )
    
    return dataset

