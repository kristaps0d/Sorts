import numpy as np

def cliDrawBars(bars_data, chart_name:str=''):
    # bars_data = [3, 2, 1, 10] -> each value will be drawn as a (n) large bar

    w, h = len(bars_data), max(bars_data)

    scene = []

    for y in range(h):
        # add new y line
        scene.append([])

        for x in range(w):

            ret = ' '
            if bars_data[x] >= y+1:
                ret = '█'

            scene[y].append(ret)

    scene = np.flip([np.flip(i) for i in scene])

    for y in scene:
        for x in y:
            print(x, end=' ')

        print(end='\n')

    print(f'{chart_name}\n')