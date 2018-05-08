import pandas


def read_csv():
    url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
    names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
    dataset = pandas.read_csv(url, names=names)
    print(dataset.head(20))
    print(dataset.shape)
    print(dataset.describe())


read_csv()