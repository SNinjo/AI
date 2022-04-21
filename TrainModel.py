import numpy as np
from keras.models import Sequential
from keras.layers.core import Dense

# load training data
data = np.loadtxt("./BMI.csv", dtype=float, delimiter=',', skiprows=1)
x_train = data[0:19, (0, 1)]
y_train = data[0:19, (2)]
x_test = data[20:29, (0, 1)]
y_test = data[20:29, (2)]

# define network structure
model = Sequential()
model.add( Dense( input_dim = 2, units = 5, kernel_initializer = 'normal', activation = 'sigmoid'))
model.add( Dense( units = 1, kernel_initializer = 'normal', activation = 'linear'))

# Configures the model for training
model.compile(loss = 'mse', optimizer = 'adam', metrics = ['mse'])

# train model
model.fit(x_train, y_train, batch_size = 10, epochs = 100)

# evaluate the model and output the accuracy
result_train = model.evaluate(x_train, y_train)
result_test = model.evaluate(x_test, y_test)
print('Train Acc:', result_train[0], result_train[1])
print('Test Acc:', result_test[0], result_test[1])

"""
內部效度: Train Acc
外部效度: Test Acc

evaluate:
    Returns the loss value & metrics values for the model in test mode.

"""
