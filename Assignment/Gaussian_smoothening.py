import matplotlib.pyplot as plt
from scipy import misc, ndimage
brain = plt.imread("Brain.jpg")
brain.shape
plt.imshow(brain, cmap='Greys_r')
plt.show()
plt.hist(neuro, bins = 10)
plt.show()
