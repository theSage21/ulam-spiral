from painter import paint_image


def table_of(n):
    " Generate multiplication table "
    current = 0
    while True:
        current += n
        yield current


def table_plot(n):
    "Paint the table"
    print('Painting table of ', n)
    t = table_of(n)
    img = paint_image(t)
    print('Saving masterpiece')
    img.save('plots/table_of_' + str(n) + '.jpg')


if __name__ == '__main__':
    table_plot(2)
    table_plot(3)
    table_plot(5)
    table_plot(7)
    table_plot(11)
