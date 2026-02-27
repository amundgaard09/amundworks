

import random
import matplotlib.pyplot as plt

x = [x for x in random.choices(range(1, 100), k=1000)]
y = [y for y in random.choices(range(1, 50), k=1000)]

plt.scatter(x, y)
plt.show()