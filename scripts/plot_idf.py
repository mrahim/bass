import numpy as np
from bass.model import bass_t
import matplotlib.pyplot as plt

c1 = 99.924
c2 = 0.145
c3 = .003
t0 = 34

t_values = np.arange(1, 60)
bass_values = [bass_t(t, c1, c2, c3, t0) for t in t_values]
plt.plot(t_values, bass_values)
plt.title(f"BASS on IdF")
