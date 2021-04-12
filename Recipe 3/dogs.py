__author__ = "Siddharth Gabu"
__license__ = "MIT"
__version__ = "1.0"
__credits__ = "Josh Gordon - Google Developers"
__maintainer__ = "Siddharth Gabu"
__status__ = "Practice"

import numpy as np
import matplotlib.pyplot as plt

greyhounds = 500
labs = 500

grey_height = 28 + 4 * np.random.randn(greyhounds)
lab_height = 24 + 4  * np.random.randn(labs)

plt.hist([grey_height, lab_height],stacked=True,color=['r','b'])
plt.show()