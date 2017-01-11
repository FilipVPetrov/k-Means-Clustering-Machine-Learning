import numpy as np

import matplotlib.pyplot as plt
from Point import *
from Canvas import *

KCluster = 2
listPoints = Canvas.createPointsN(20)
listCentroids = Canvas.createCentroidsN(KCluster)
Canvas.plotPoints(KCluster, listPoints,listCentroids)

# for centroid in listCentroids:
#     print str(centroid)

print Canvas.getCloserCentroid(Point(4,8),listCentroids)

plt.show(block=True)