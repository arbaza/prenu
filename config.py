from easydict import EasyDict as edict
import json
import os

config = edict()
config.TRAIN = edict()

config.TRAIN.batch_size = 25
config.TRAIN.early_stopping_num = 10
config.TRAIN.lr = 0.0001
config.TRAIN.lr_decay = 0.5
config.TRAIN.decay_every = 5
config.TRAIN.beta1 = 0.5  # beta1 in Adam optimiser
config.TRAIN.n_epoch = 2
config.TRAIN.sample_size = 50
config.TRAIN.g_alpha = 15  # weight for pixel loss
config.TRAIN.g_gamma = 0.0025  # weight for perceptual loss
config.TRAIN.g_beta = 0.1  # weight for frequency loss
config.TRAIN.g_adv = 1  # weight for frequency loss

config.TRAIN.seed = 100
config.TRAIN.epsilon = 0.000001


config.TRAIN.VGG16_path = os.path.join('../../input/vgg16p/', 'VGG16', 'vgg16_weights.npz')
config.TRAIN.training_data_path = os.path.join('../../input/pickles/', 'testing.pickle')
config.TRAIN.val_data_path = os.path.join('../../input/pickles/', 'validation.pickle')
config.TRAIN.testing_data_path = os.path.join('../../input/pickles/', 'testing.pickle')
config.TRAIN.mask_Gaussian1D_path = os.path.join('../../input/maskkk', 'Gaussian1D')
config.TRAIN.mask_Gaussian2D_path = os.path.join('../../input/maskkk', 'Gaussian2D')
config.TRAIN.mask_Poisson2D_path = os.path.join('../../input/maskkk', 'Poisson2D')

def log_config(filename, cfg):
    with open(filename, 'w') as f:
        f.write("================================================\n")
        f.write(json.dumps(cfg, indent=4))
        f.write("\n================================================\n")
