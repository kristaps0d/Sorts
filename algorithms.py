# py modules
import time

# local modules
from cli import cliDrawBars

def bubblesort(data:list) -> list:
    iterations = len(data)

    # recursive loop
    while True:
        if iterations == 0:
            break

        for n in range(len(data) - 1):
            # if d[n] > d[n+1] then
            # switch them around
            if data[n] > data[n+1]:
                t1, t2 = data[n+1], data[n]
                data[n], data[n+1] = t1, t2

        iterations -= 1

    return data

def bubblesort_visualised(data:list, sleep_time:float=0.2) -> list:
    iterations = len(data)

    # recursive loop
    while True:
        print('\n'*30)

        title = f'Bubble sort: info: iter: [{len(data) - iterations}] left: [{iterations}] [{(iterations / len(data))*100}%]'

        cliDrawBars(data, '\n' + '\t'*int(len(data)*4.4 / len(title)) + title)
        time.sleep(sleep_time)

        if iterations == 0:
            break
            
        for n in range(len(data) - 1):
            # if d[n] > d[n+1] then
            # switch them around
            if data[n] > data[n+1]:
                t1, t2 = data[n+1], data[n]
                data[n], data[n+1] = t1, t2

        iterations -= 1

    return data