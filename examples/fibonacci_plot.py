from painter import paint_image


def fibo():
    x, y = None, None
    while True:
        if x is None:
            x = 1
            yield 1
        if y is None:
            y = 1
            yield 1
        z = x + y
        y = x
        x = z
        yield z


def fibo_plot():
    fibonacci = fibo()
    img = paint_image(fibonacci)
    print('Saving the masterpiece')
    img.save('plots/fibo_plot.jpg')

if __name__ == '__main__':
    fibo_plot()
