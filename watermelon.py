import matplotlib
import matplotlib.pyplot as plt
data1 = [[10,10,10,10,10,10,10,6,10,10,10],
        [10,10,10,10,10,10,9,4,5,10,10],
        [10,10,10,10,10,9,9,9,4,5,10],
        [10,10,10,10,9,9,9,9,4,5,6],
        [10,10,10,9,9,9,9,9,4,5,6],
        [10,10,9,9,9,9,9,9,4,5,5],
        [10,9,9,9,9,9,9,9,4,5,5],
        [10,10,9,9,9,9,9,9,4,5,5],
        [10,10,10,9,9,9,9,9,4,5,5],
        [10,10,10,10,9,9,9,9,4,5,5],
        [10,10,10,10,10,9,9,9,4,5,5]]
plt.imshow(data1,cmap="nipy_spectral")
plt.show()