import pandas as pd


def time_to_integer(time):
    """Extracts days from datetime object
    :param time:
        datetime object
    :return:
        days of datetime object
    """
    time = str(time)
    t, _, _ = time.split(" ")
    return int(t)


def prepare_df(df):
    """Function to drop prepare the initial dataframe. This includes dropping NA's in confirmed_data, released_date
    and afterwards transforming these columns to datetime objects. After that a new feature "duration" is created and
    unnecessary columns are being dropped
    :param df:
        dataframe to be prepared
    :return:
        prepared dataframe
    """
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
            "released_date",
            "city",
        ],
        axis=1,
    )

    return df


def create_test_train(df):
    """
    Creates dummy columns for categoric features and splits into test and train for X and y.
    :param df:
        dataframe with categoric columns
    :return:
        X_train and y_train to be used for Regression fit and X_test and y_Test for testing the model on unseen data
    """
    cat_vars = df.select_dtypes(include=["object"]).copy().columns
    for var in cat_vars:
        df = pd.concat(
            [
                df.drop(var, axis=1),
                pd.get_dummies(df[var], prefix=var, prefix_sep="_", drop_first=True),
            ],
            axis=1,
        )

    X = df.drop("duration", axis=1)
    y = df["duration"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    return X_train, X_test, y_train, y_test


def coef_weights(coefficients, X_train):
    """
    Provides a dataframe that can be used to understand the most influential coefficients
    in a linear model by providing the coefficient estimates along with the name of the
    variable attached to the coefficient.
    :param coefficients
        the coefficients of the linear model
    :param X_train
        the training data, so the column names can be used
    :return:
        coefs_df - a dataframe holding the coefficient, estimate, and abs(estimate)
    """
    coefs_df = pd.DataFrame()
    coefs_df["est_int"] = X_train.columns
    coefs_df["coefs"] = model.coef_
    coefs_df["abs_coefs"] = np.abs(model.coef_)
    coefs_df = coefs_df.sort_values("abs_coefs", ascending=False)
    return coefs_df
