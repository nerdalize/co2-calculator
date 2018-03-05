import os
import errno
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

# Save a bar plot to a file
def plot(x, y, x_label, y_label, title, filename):
    x_num = np.arange(len(x))
    nerdalize_orange = '#EB4824'
    nerdalize_gray = '#F2F2F2'

    plt.style.use('ggplot')
    plt.rcParams['axes.facecolor'] = nerdalize_gray
    rects = plt.bar(x_num, y, color=nerdalize_orange)
    plt.xticks(np.arange(len(x)),x)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.savefig(filename, bbox_inches='tight')

# Make a directory and don't raise an exeception if it already exists
def mkdir(dirname):
    try:
        os.mkdir(dirname)
    except OSError as exc:
        if exc.errno != errno.EEXIST:
            raise
        pass
