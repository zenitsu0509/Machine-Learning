import pandas as pd
data = pd.read_csv("/content/project_9_sample_dataset.csv")
height = "Height"
weight = "Weight"
train,target = data[[height]],data[weight]
data
from sklearn.linear_model import LinearRegression
linear_regression = LinearRegression()
linear_regression.fit(train,target)
weight_flipper_height = linear_regression.coef_[0]
weight_flipper_height
intercept_body_mass = linear_regression.intercept_
intercept_body_mass
import numpy as np
flipper_length_range = np.linspace(train.min(), train.max(), num=10)
predicted_body_mass = (
    weight_flipper_height * flipper_length_range + intercept_body_mass
)
import matplotlib.pyplot as plt
import seaborn as sns
sns.scatterplot(x=train[height], y=target, color="black", alpha=0.5)
plt.plot(flipper_length_range, predicted_body_mass)
_ = plt.title("Model using LinearRegression from scikit-learn")
from sklearn.metrics import mean_squared_error

inferred_body_mass = linear_regression.predict(train)
model_error = mean_squared_error(target, inferred_body_mass)
print(f"The mean squared error of the optimal model is {model_error:.2f}")
from sklearn.metrics import mean_absolute_error

model_error = mean_absolute_error(target, inferred_body_mass)
print(f"The mean absolute error of the optimal model is {model_error:.2f} g")
