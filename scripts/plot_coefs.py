import numpy as np
from bass.model import decrease_t, power_t
import matplotlib.pyplot as plt

# Let's look at power coef (C2) and decrease coef (C3)
c1 = 99.924
c2 = 0.145
c3 = .003
t0 = 34

t_values = np.arange(1, 50)
decrease_values = [decrease_t(t, c3, t0) for t in t_values]
plt.plot(t_values, decrease_values, label='decrease_t')

c2 = 0.1
c3 = .003
t0 = 34

t_values = np.arange(50)
power_values = [power_t(t, c2, c3, t0) for t in t_values]
plt.plot(t_values, power_values, label='power_t')
plt.legend()
