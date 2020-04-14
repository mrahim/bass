import pandas as pd


DATASET_URL = "https://raw.githubusercontent.com/opencovid19-fr/data/master/dist/chiffres-cles.csv"


def fetch_dataset(url=DATASET_URL, source_type="opencovid19-fr",
                  granularite="region"):
    data = pd.read_csv(url)
    data = data[(data.source_type == source_type) &
                (data.granularite == granularite)]
    data = data.sort_values(by="date").reset_index(drop=True)
    return data


def prepare_dataset(maille_nom="Île-de-France", column="hospitalises"):
    data = fetch_dataset()
    ytrue = data.loc[(data.maille_nom == maille_nom), column].values
    dates = pd.to_datetime(data.loc[(data.maille_nom == maille_nom),
                                    "date"]) - pd.to_datetime("2020-03-01")
    t_true = dates.dt.days.values + 1
    return t_true, ytrue
