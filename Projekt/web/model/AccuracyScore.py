import numpy as np 
import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.neural_network import MLPClassifier

 
df = pd.read_csv("https://sebkaz.github.io/teaching/PrzetwarzanieDanych/data/polish_names.csv")

def to(string): return int(string == 'm')
def ost_a(string): return int(string[-1] == 'a')

def getAccuracyScore():

    df['to'] = df['gender'].map(to)
    df['ost_a'] = df['name'].map(ost_a)

    y = df['to'].values
    x = df[['ost_a']].values

    model = MLPClassifier (solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(5, 2), random_state=1)
    model.fit(x, y)

    y_pred = model.predict(x)
    return accuracy_score(y, y_pred)
