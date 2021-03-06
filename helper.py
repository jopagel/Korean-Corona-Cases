import pandas as pd


def time_to_integer(time):
    time = str(time)
    t, _, _ = time.split(" ")
    return int(t)


def prepare_df(df):
    df = df.dropna(subset=["confirmed_date", "released_date"])
    assert df.confirmed_date.isna().sum != 0 or df.released_date != 0
    df[["confirmed_date", "released_date"]] = df[
        ["confirmed_date", "released_date"]
    ].apply(pd.to_datetime)
    df["duration"] = df["released_date"] - df["confirmed_date"]
    df["duration"] = df["duration"].apply(time_to_integer)
    df = df.drop(
        [
            "symptom_onset_date",
            "deceased_date",
            "patient_id",
            "country",
            "infected_by",
            "state",
            "contact_number",
            "confirmed_date",
            "released_date"
        ],
        axis=1,
    )

    return df
