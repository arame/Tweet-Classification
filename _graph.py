import seaborn as sns
import matplotlib.pyplot as plt
import logging, os
from _utility import gl
save_only = False

def histplot_count(title, df, x):
    p = sns.histplot(data=df, x=x, stat='count')
    plt.title(title)

def histplot_range_count(title, df, x, range):
    p = sns.histplot(data=df, x=x, stat='count', binrange=range)
    plt.title(title)

def plot_dict(dict_sse, title, x_label, y_label, fname):
    plt.figure(figsize = (10, 8))
    plt.plot(list(dict_sse.keys()), list(dict_sse.values()))
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    if save_only:
        output_image(fname)
    else:
        plt.show()

def plot_silhouette_avg(dict_sse, title, x_label, y_label, tag):
    plt.figure(figsize = (10, 8))
    plt.plot(list(dict_sse.keys()), list(dict_sse.values()))
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    if save_only:
        fname = f"elbow_plot_for_{tag}.png"
        output_image(fname)
    else:
        plt.show()

def output_image(fname):
    folder = "Images_tfidf" if gl.from_tfidf_file else "Images"
    img = os.path.join(folder, fname)
    if os.path.exists(img):
        os.remove(img)
    plt.savefig(img)
    logging.info(f"Saved image: {img}")
    plt.close()
