import numpy as np
import pandas as pd


def bass_t(t, c1, c2, c3, t_decrease):
    return c1*np.exp(power_t(t, c2, c3, t_decrease)*t)


def power_t(t, c2, c3, t_decrease):
    if t < t_decrease:
        return c2
    else:
        return power_t(t - 1, c2, c3, t_decrease) - decrease_t(t, c3,
                                                               t_decrease)


def decrease_t(t, c3, t_decrease):
    if t < t_decrease:
        return 0
    else:
        return c3*np.log10(10 + (t - t_decrease))


def fit_c1_c2(days, values):
    coefs = np.polyfit(days, np.log(values), 1)
    return np.exp(coefs[1]), coefs[0]


def init_decrease_date(days, values):
    # compute acceleration
    accel = pd.Series(data=values[15:], index=days[15:]).diff().diff()

    # set negative accelerations to 1
    neg_indices = accel.apply(lambda x: 0 if x > 0 or pd.isnull(x) else 1)

    # extract consecutive sequences of negative accelerations
    from scipy.ndimage import label
    neg_labels, _ = label(neg_indices.values)

    # select first sequence of more than 2 consecutive negative accelerations
    neg_sequences = np.bincount(neg_labels)
    c_init = 1
    for i, c in enumerate(neg_sequences[1:]):
        if c > 2:
            c_init = i + 1
            break
    indices = np.argwhere(neg_labels == c_init)
    if len(indices) > 0:
        selected_index = indices[0]
    # return first index of the decrease
    return accel.index[selected_index][0]
