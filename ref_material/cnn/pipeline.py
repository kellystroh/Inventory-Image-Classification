import os
from skimage import io
from skimage.transform import resize
import numpy as np

def get_images(dirname):
    """Given directory name, returns a generator of (filename, image) tuples. The image is
    an ndarray with shape (n_rows, n_cols) for monochrome images and (n_rows, n_cols, n_channels)
    for color images."""
    
    for fn in os.listdir(dirname):
        dir_fn = os.path.join( dirname, fn )
        filedata = io.imread( dir_fn )
        
        #encourage consistency by returning ndarrays
        yield fn, np.array( filedata )
        
def get_features( dirname, shape, transform_func=lambda x:x ):
    """Given a directory name, returns a feature matrix `X`, with each
    row corresponding to an image in the directory."""

    imgs = get_images( dirname )
    imgs = [resize(img, shape) for filename, img in imgs]
    imgs = [transform_func(x) for x in imgs]
    
    n = len(imgs)
    return np.stack( imgs ).reshape(n, -1)