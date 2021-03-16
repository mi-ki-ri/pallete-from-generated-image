import numpy as np
from PIL import Image 
import glob
import os

# see. https://stackoverflow.com/questions/18801218/build-a-color-palette-from-image-url

def palette(img):
    """
    Return palette in descending order of frequency
    """
    arr = np.asarray(img)
    palette, index = np.unique(asvoid(arr).ravel(), return_inverse=True)
    palette = palette.view(arr.dtype).reshape(-1, arr.shape[-1])
    count = np.bincount(index)
    order = np.argsort(count)
    return palette[order[::-1]]

def asvoid(arr):
    """View the array as dtype np.void (bytes)
    This collapses ND-arrays to 1D-arrays, so you can perform 1D operations on them.
    http://stackoverflow.com/a/16216866/190597 (Jaime)
    http://stackoverflow.com/a/16840350/190597 (Jaime)
    Warning:
    >>> asvoid([-0.]) == asvoid([0.])
    array([False], dtype=bool)
    """
    arr = np.ascontiguousarray(arr)
    return arr.view(np.dtype((np.void, arr.dtype.itemsize * arr.shape[-1])))


for MYFILE in glob.glob("./img/*"):


    FILENAME = os.path.basename(MYFILE)
    FILEPATH = "./img/" +  FILENAME
    PALLETEPATH = "./pallete/" + FILENAME



    img = Image.open(FILEPATH, 'r').convert('RGB')

    stacks = []

    for col in palette(img)[:5]:
        stacks.append( np.full((120,120,3), col))

    stack = np.hstack(stacks)

    fromarr = Image.fromarray(stack).save( PALLETEPATH )