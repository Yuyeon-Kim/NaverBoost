# 220215
# Q5

import matplotlib.pyplot as plt
import string

# names = ["group_%s" %i for i in "abc"]
names = ["group_%s" %i for i in string.ascii_lowercase[:3]]
values = [1, 10, 100]

plt.figure(figsize=(9, 3))

plt.subplot(1,3,1)
plt.bar(names, values)

plt.subplot(1,3,2)
plt.scatter(names, values)

plt.subplot(1,3,3)
plt.plot(names, values)

plt.show()