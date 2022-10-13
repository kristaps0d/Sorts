# py modules
import numpy as np

# local modules
from algorithms import bubblesort_visualised
from misc import keyboardExceptionExitHandler

# unsorted data
data = np.random.randint(30, size=80)

keyboardExceptionExitHandler(bubblesort_visualised, (data))
