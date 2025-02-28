import numpy as np


color_filters = {
    "none": np.array([
        [1.0, 0.0, 0.0],
        [0.0, 1.0, 0.0],
        [0.0, 0.0, 1.0]
    ]),
    "sepia": np.array([
        [0.272, 0.534, 0.131],
        [0.349, 0.686, 0.168],
        [0.393, 0.769, 0.189]
    ]),
    "grayscale": np.array([
        [0.299, 0.587, 0.114],
        [0.299, 0.587, 0.114],
        [0.299, 0.587, 0.114]
    ]),
    "negative": np.array([
        [-1.0,  0.0,  0.0],
        [ 0.0, -1.0,  0.0],
        [ 0.0,  0.0, -1.0]
    ]) + 1,
    "blue_only": np.array([
        [1, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]),
    "green_only": np.array([
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]),
    "red_only": np.array([
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 1]
    ]),
    "cool": np.array([
        [1.2, 0.2, 0.0],
        [0.0, 1.0, 0.0],
        [0.0, 0.0, 0.8]
    ]),
    "warm": np.array([
        [0.8, 0.0, 0.0],
        [0.0, 1.0, 0.1],
        [0.0, 0.2, 1.2]
    ]),
    "invert_red_green": np.array([
        [0.0, 1.0, 0.0],
        [1.0, 0.0, 0.0],
        [0.0, 0.0, 1.0]
    ]),
    "invert_red_blue": np.array([
        [0.0, 0.0, 1.0],
        [0.0, 1.0, 0.0],
        [1.0, 0.0, 0.0]
    ]),
    "invert_green_blue": np.array([
        [1.0, 0.0, 0.0],
        [0.0, 0.0, 1.0],
        [0.0, 1.0, 0.0]
    ]),
    "solarize": np.array([
        [-2.0, 2.0, 2.0],
        [2.0, -2.0, 2.0],
        [2.0, 2.0, -2.0]
    ]) + 1,
}