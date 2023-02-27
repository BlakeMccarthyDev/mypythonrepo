import matplotlib.pyplot as plt
def draw_scatterplot(x_values, y_values):
    plt.scatter(x_values, y_values, s=20)
    plt.title("Scatter Plot")
    plt.xlabel("x values")
    plt.ylabel("y values")
    plt.show()

xval = [1, 2, 3, 4]
yval = [4, 3, 2, 1]

draw_scatterplot(xval, yval)