import numpy as np
import pandas as pd
from bass.model import bass_t, fit_c1_c2, init_decrease_date
from bass.dataset import prepare_dataset
from sklearn.metrics import mean_absolute_error
import matplotlib.pyplot as plt


def optimize_bass(t_true, y_true, t_decrease, t_values=np.arange(1, 60),
                  c3_values=np.linspace(.001, .003, 5)):
    t0_values = np.arange(t_decrease - 4, t_decrease + 4)
    errors = []
    for c3 in c3_values:
        for t0 in t0_values:
            c1, c2 = fit_c1_c2(t_true[t_true <= t_decrease],
                               y_true[t_true <= t_decrease])

            bass_values = np.array([bass_t(t, c1, c2, c3, t0) for t in t_values])

            idx_ = np.array([i for i, v in enumerate(t_values) if v in t_true])
            errors.append({
                "t0": t0, "c1": c1, "c2": c2, "c3": c3,
                "bass_values": bass_values, "t_values": t_values,
                "error": mean_absolute_error(bass_values[idx_], y_true)})

    df_errors = pd.DataFrame(errors)
    return df_errors[df_errors.error == df_errors.error.min()]


def optimize_region(region="Île-de-France", column="hospitalises",
                    plot_result=True):
    t_true, y_true = prepare_dataset(maille_nom=region, column=column)
    t_decrease = init_decrease_date(t_true, y_true)

    df_optimum = optimize_bass(t_true, y_true, t_decrease)
    if not plot_result:
        return df_optimum

    t0_ = df_optimum["t0"].values[0]
    bass_values_ = df_optimum["bass_values"].values[0]
    c1_ = df_optimum["c1"].values[0]
    c2_ = df_optimum["c2"].values[0]
    c3_ = df_optimum["c3"].values[0]
    t_values_ = df_optimum["t_values"].values[0]

    plt.figure()
    plt.scatter(t_true, y_true)
    plt.scatter(t_true[t_true >= t0_], y_true[t_true >= t0_])
    plt.plot(t_values_, bass_values_)
    plt.title(f"{region}: t0={t0_}, c1={c1_:.4f}, c2={c2_:.4f}, c3={c3_:.4f}")
    import os
    if not os.path.isdir("results"):
        os.makedirs("results")
    plt.savefig(f"results/eval_{region}.png")
    return df_optimum
