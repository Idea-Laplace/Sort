import os
from time import sleep, time

def insertion_sort(x: list):
    # for visual purpose
    position = 0
    count = 0

    def graphical_list(x: list[int]):
        for i, value in enumerate(x):
            if i == position:
                print('O' * value + " <")
            else:
                print('O' * value)
        print("="*30)

    # Actual process
    for i in range(1, len(x)):
        j = i
        position = j
        graphical_list(x)
        sleep(1)
        os.system('cls')
        while x[j] < x[j-1] and j > 0:
            x[j], x[j-1] = x[j-1], x[j]
            position -= 1
            j -= 1
            count += 1
            graphical_list(x)
            sleep(1)
            os.system('cls')
    graphical_list(x)
    print(f"Total steps: {count}")
    print(f"The maximum steps for length {len(x)} lists: {len(x)}*({len(x)}-1)/2 = {int(len(x)*(len(x)-1)/2)}")


if __name__ == '__main__':
    x = [4, 7, 2, 1, 9, 6, 5, 3, 8]
    y = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    insertion_sort(x)
    input()
    os.system('cls')
    insertion_sort(y)
    input()