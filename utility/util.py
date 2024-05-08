# -*- coding: utf-8 -*-
import io
import warnings
import itertools
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

from os.path import exists
from contextlib import redirect_stdout

output_files = {
    'fizzbuzz': ('fizzbuzz.txt', [100]),
    'hailstone': ('hailstone.txt', [15])
}


# # check that reference output files exist
# assert all([exists(f'utility/outputs/{target}.txt') for target in output_files.keys()]), \
#     'Reference output files are missing -- please contact instructors.'

def checked(fn):
    function_name = fn.__name__
    reference_file, test_args = output_files[function_name]

    with open(f'utility/outputs/{reference_file}', 'r') as f:
        expected = f.read()

        f = io.StringIO()
        with redirect_stdout(f):
            fn(*test_args)
        given = f.getvalue()

        print(f'Checking {function_name}...{"✅" if given == expected else "❌"}\n')

    return lambda *args, **kwargs: fn(*args, **kwargs)


def load_image(path):
    '''Loads image at PATH'''
    return plt.imread(path)

def show_array_as_image(arr):
    plt.imshow(arr, cmap='gray')
    plt.clim(0, 1)
