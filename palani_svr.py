import math
import pandas as pd
import tensorflow as tf
import matplotlib.pyplot as plt
from tensorflow import keras
from tensorflow.keras import layers
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
from sklearn.linear_model import LinearRegression
from sklearn.multioutput import MultiOutputRegressor
from sklearn.svm import SVR

def predict(file_path,angle_in,t_in):
    laser=pd.read_csv(file_path)

    x= laser[['Angle','Thickness']]
    laser=laser.drop('Angle',axis=1)
    laser=laser.drop("Thickness",axis=1)
    y=laser

    x_train, x_test, y_train, y_test = train_test_split(x,y, train_size=0.8, random_state=42)


    svm_multi = MultiOutputRegressor(SVR(kernel="rbf", C=100, gamma=0.1, epsilon=0.1))
    svm_multi.fit(x_train,y_train)
    x_pred=pd.DataFrame([[angle_in,t_in]],columns=['Angle','Thickness'])
    ys_pred=svm_multi.predict(x_pred)
    ys_pred=pd.DataFrame(ys_pred)
    return ys_pred