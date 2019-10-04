import sys
import math_lib as ml
import matplotlib.pyplot as plt
import pathlib
import matplotlib
matplotlib.use('Agg')


def histogram(L, out_file_name, groups):

    file = pathlib.Path(out_file_name)

    if file.exists():

        return ('this file name is taken, choose another.')
        sys.exit(1)

    if L is None:
        raise ValueError('empty list, nothing to graph')

    if L is []:
        raise ValueError('empty list, nothing to graph')

    else:
        ticks = []
        j = 1

        for i in groups:
            ticks.append(k)
            j += 1

        width = 3
        height = 3
        mean = ml.list_mean(L)
        stdev = ml.list_stdev(L)
        title = 'mean=' + str(mean) + ' stdev=' + str(stdev)

        fig = plt.figure(figsize=(width, height), dpi=300)

        ax = fig.add_subplot(1, 1, 1)
        ax.set_title(title)
        ax.set_xlabel('value')
        ax.set_ylabel('frequency')
        ax.xticks(ticks, groups, rotation='vertical')

        ax.hist(L, 3)

        plt.savefig(out_file_name, bbox_inches='tight')

        if not file.exists():

            print('the plot did not save successfully.')


def boxplot(L, out_file_name, groups):

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

        for i in groups:
            ticks.append(j)
            j += 1

        width = 3
        height = 3

        fig = plt.figure(figsize=(width, height), dpi=300)

        ax = fig.add_subplot(1, 1, 1)
        ax.boxplot(L)
        ax.set_xlabel('value')
        ax.set_ylabel('frequency')
        ax.set_title('[user] add appropriate title here')
        plt.xticks(ticks, groups, rotation='vertical')

        plt.savefig(out_file_name, bbox_inches='tight')

    if not file.exists():
        print('the plot did not save successfully.')


def combo(L, out_file_name):

    file = pathlib.Path(out_file_name)

    if file.exists():
        return ('this file name is taken, choose another.')

    else:
        width = 3
        height = 3
        mean = ml.list_mean(L)
        stdev = ml.list_stdev(L)
        title = 'mean=' + str(mean) + ' stdev=' + str(stdev)

        fig = plt.figure(figsize=(width, height), dpi=300)

        ax = fig.add_subplot(2, 1, 1)
        ax.set_title(title)
        ax.set_ylabel('frequency')
        ax.set_xlabel('value')
        ax.hist(L, 3)

        ax2 = fig.add_subplot(2, 1, 2)
        ax2.set_ylabel('frequency')
        ax2.boxplot(L)

        plt.savefig(out_file_name, bbox_inches='tight')
