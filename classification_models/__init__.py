import tensorflow as tf
import tensorflow.keras.applications as ka
from .__version__ import __version__

def get_submodules_from_kwargs(kwargs):
    backend = kwargs.get('backend', None)
    layers = kwargs.get('layers', tf.keras.layers)
    models = kwargs.get('models', tf.keras.models)
    utils = kwargs.get('utils', tf.keras.utils)
    return backend, layers, models, utils
