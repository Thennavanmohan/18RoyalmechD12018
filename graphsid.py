import matplotlib.pyplot as plt
import numpy as np
label = ['Mechanical','civil','computer','electronic']
Engineering_Students = [60,25,90,55]

def plot_bar_x():
    # this is for plotting purposep
    index = np.arange(len(label))
    plt.bar(index, Engineering_Students,color='red',width=0.8)
    plt.xlabel('Genre', fontsize=8)
    plt.ylabel('Engineering_Students', fontsize=8 )
    plt.xticks(index, label, fontsize=8, rotation=90,color=('black'))
    plt.title('Engineering_Students for Each Genre 1995-2017')
    plt.show()

plot_bar_x()