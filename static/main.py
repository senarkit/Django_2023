######### CONFIG ###########
 # Linear-Regression, Ridge-Regression, 'Random-Forest',


########## CODE #########
features = ["age", "sex", "bmi", "children", "smoker", "region"]
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_absolute_percentage_error, mean_absolute_error
from sklearn.model_selection import train_test_split

def func(method = "Ridge-Regression"):
    # Get Data
    data = pd.read_csv("./data.csv")

    # clean data if any duplicates
    data = data.drop_duplicates()
    data.describe(include="all")


    # Manual LABEL ENCODING
    data_cleaned = data.copy()
    data_cleaned["sex"] = data["sex"].map({"female": 0,
                                            "male": 1})
    data_cleaned["region"] = data["region"].map(
        {
            "southwest": 0,
            "southeast": 1,
            "northwest": 2,
            "northeast": 3,
        }
    )
    data_cleaned["smoker"] = data["smoker"].map({"yes": 1,
                                                "no": 0})


    # train test split
    X_col = list(set(data_cleaned.columns.tolist()) - set(["expenses"]))
    target_col = ["expenses"]
    X = data_cleaned[X_col]
    X = X[features]
    y = data_cleaned[target_col]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=123)



    # build Model
    if method.lower() == "linear-regression":
        model = LinearRegression()
        model.fit(X_train, y_train["expenses"])
        y_pred = model.predict(X_test)

    if method.lower() == "ridge-regression":
        model = Ridge(alpha=0.05)
        model.fit(X_train, y_train["expenses"])
        y_pred = model.predict(X_test)

    if method.lower() == "random-forest":
        model = RandomForestRegressor()
        model.fit(X_train, y_train["expenses"])
        y_pred = model.predict(X_test)

        # Features
        feats = {}
        for i, j in zip(model.feature_names_in_, model.feature_importances_):
            feats[i] = round(j, 2)
        print("Feature Importance :\n ", feats)

    ### Save Model
    import joblib
    joblib.dump(model, './model.joblib')

    # prediction metric
    print("Model :",method)
    print(f"R2 Score {r2_score(y_test, y_pred)}")
    print(f"MAPE Score {round(mean_absolute_percentage_error(y_test, y_pred) * 100,2)}%")
    print(f"MAE Score {round(mean_absolute_error(y_test, y_pred),2)}")

    ### Predicted Dataframe
    _tmp = y_test.copy().reset_index(drop=True)
    _tmp.columns = ["actual"]
    pred_df = pd.concat([_tmp, pd.Series(y_pred, name="predicted")], axis=1)


# import joblib
# import pandas as pd
# m = joblib.load("model.joblib")
# print(m.predict(pd.DataFrame({"age":19, "sex":0, "bmi":27.9, "children":0,
#                                   "smoker":1, "region":0}
#                                   , index=[0]))[0])








