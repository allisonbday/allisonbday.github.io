import math
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import matplotlib.colors as mcolors


def tile_array(array, desired_length, blank_between=True, cutoff=True):

    if blank_between:  # Add a blank column
        blank_column = np.zeros([len(array), 1])
        array = np.append(array, blank_column, 1)

    num_repeats = math.ceil(desired_length / array.shape[1])
    array_tile = np.tile(array, (1, num_repeats))

    if cutoff:
        array_tile = array_tile[:, :desired_length]

    array_return = np.fliplr(array_tile)
    return array_return


# https://matplotlib.org/stable/users/explain/colors/colormap-manipulation.html
cmap = mcolors.ListedColormap(["white", "gray", "black"])

# Small flower example
small_flower_array = np.array(
    [
        [0, 0, 1, 1, 0, 0, 0, 0],
        [1, 1, 1, 1, 0, 2, 2, 0],
        [1, 1, 0, 1, 1, 0, 2, 2],
        [0, 1, 1, 1, 1, 0, 0, 0],
        [0, 1, 1, 0, 0, 0, 0, 0],
    ]
)

small_flower_df = pd.DataFrame(
    tile_array(
        small_flower_array,
        desired_length=24,
        cutoff=True,
    )
).iloc[::-1]

fig, ax = plt.subplots()
ax.imshow(
    small_flower_df,
    cmap,
    aspect="equal",
    origin="lower",
)
ax.invert_xaxis()

plt.show()


# Large flower example

large_flower_array = np.array(
    [
        [0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 1, 1, 1, 0, 0, 0],
        [1, 1, 0, 1, 0, 1, 1, 0],
        [0, 1, 1, 0, 1, 1, 0, 0],
        [0, 1, 1, 0, 1, 1, 0, 0],
        [0, 1, 1, 1, 1, 1, 0, 0],
        [0, 0, 1, 1, 1, 0, 0, 0],
        [2, 0, 0, 2, 0, 0, 2, 2],
        [2, 2, 0, 2, 0, 2, 2, 0],
        [0, 2, 2, 2, 2, 2, 0, 0],
        [0, 0, 2, 2, 2, 0, 0, 0],
        [2, 2, 2, 2, 2, 2, 2, 2],
    ]
)

large_flower_df = pd.DataFrame(
    tile_array(
        large_flower_array,
        blank_between=False,
        desired_length=24,
        cutoff=True,
    )
).iloc[::-1]

fig, ax = plt.subplots()
ax.imshow(
    large_flower_df,
    cmap,
    aspect="equal",
    origin="lower",
)
ax.invert_xaxis()


plt.show()


# Combine list of patterns


def combine_patterns(patterns, include_blank=True):

    if include_blank:
        blank_row = pd.DataFrame([[0] * 24])

        result = []
        for e in patterns:
            result.append(e)
            result.append(blank_row)
        result.pop()

        return pd.concat(result[::-1], axis=0)

    return pd.concat(patterns[::-1], axis=0)


both_patterns = combine_patterns([small_flower_df, large_flower_df])

fig, ax = plt.subplots()
ax.imshow(
    both_patterns,
    cmap,
    aspect="equal",
    origin="lower",
)
ax.invert_xaxis()

plt.show()
