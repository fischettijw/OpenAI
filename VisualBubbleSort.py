import matplotlib.pyplot as plt
import random
import time

def bubble_sort(numbers):
    n = len(numbers)
    for i in range(n):
        for j in range(0, n-i-1):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
                yield numbers

def visualize_sort(numbers):
    fig, ax = plt.subplots()
    ax.bar(range(len(numbers)), numbers)
    
    for numbers in bubble_sort(numbers):
        for i in range(len(numbers)):
            ax.bar(i, numbers[i], color='blue')
        plt.pause(0.2)

if __name__ == '__main__':
    numbers = random.sample(range(1, 101), 50)
    visualize_sort(numbers)
    plt.show()
