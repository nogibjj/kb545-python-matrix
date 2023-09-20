import pandas as pd


def getDescStats():
    df = pd.read_csv(
        "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
    )
    answer = df["sepal_length"].describe()
    return answer
