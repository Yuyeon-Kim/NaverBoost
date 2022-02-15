# 220215
# Q4

import numpy as np
import matplotlib.pyplot as plt

t = np.arange(0., 5., 0.2)

# 사용 마커 : red dashes, green squares, blue triangles
# 문제 주석 오류 : blue suares     -> green squares 
#                 green triangles -> blue triangles
plt.plot(t, t, "--r", t, t**2, "sg", t, t**3, "^b")
plt.show()