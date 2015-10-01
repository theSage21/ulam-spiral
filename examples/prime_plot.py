from painter import paint_image


def get_prime():
    with open('PR', 'r') as fl:
        lines = map(int, fl.readlines())
        prime = tuple(lines)
    return prime


def plot_prime():
    prime = get_prime()
    img = paint_image(prime)
    print('Saving the masterpiece')
    img.save('plots/prime_plot.jpg')


if __name__ == '__main__':
    plot_prime()
