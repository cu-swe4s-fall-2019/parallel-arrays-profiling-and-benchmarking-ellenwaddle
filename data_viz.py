import sys
import math_lib as ml
import matplotlib.pyplot as plt
import pathlib
import matplotlib
matplotlib.use('Agg')

def boxplot(L, out_file_name, x_axis, y_axis, title, groups = None):

    file = pathlib.Path(out_file_name)

    if L is None:
        raise ValueError('empty list, nothing to graph')

    if L == []:
        raise ValueError('empty list, nothing to graph')

    if file.exists():

        return ('this file name is taken, choose another.')
        sys.exit(1)

    else:

        ticks = []
        j = 1

        if groups is not None:
            for i in groups:
                ticks.append(j)
                j += 1

        width = 3
        height = 3

        fig = plt.figure(figsize=(width, height), dpi=300)

        ax = fig.add_subplot(1, 1, 1)
        ax.boxplot(L)

        if x_axis is not None:
            ax.set_xlabel(x_axis)
        if y_axis is not None:
            ax.set_ylabel('frequency')
        if title is not None:
            ax.set_title(title)

        if groups is not None:
            plt.xticks(ticks, groups, rotation='vertical')

        plt.savefig(out_file_name, bbox_inches='tight')

    if not file.exists():
        print('the plot did not save successfully.')
