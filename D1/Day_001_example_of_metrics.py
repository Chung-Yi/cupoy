import numpy as np
import matplotlib.pyplot as plt

w = 3
b = 0.5 

x_lin = np.linspace(0, 100, 101 )
# print(x_lin)
y = (x_lin + np.random.randn(101)*5) * w + b

plt.plot(x_lin, y, 'b.', label = 'data points')
plt.title('Assume we have data points')
plt.legend(loc = 0)
plt.show()
# plt.close()

y_hat = x_lin * w + b
plt.plot(x_lin, y, 'bx', label = 'data')
plt.plot(x_lin, y_hat, 'r--', label = 'prediction')
plt.title("Assume we have data points (And the prediction)")
plt.legend(loc = 2)
plt.show()

def mean_absolute_error(y, yp):
    mae = sum(abs(y-yp))/len(y)
    return mae

MAE = mean_absolute_error(y, y_hat)
print("The Mean absolute error is %.3f" % (MAE))