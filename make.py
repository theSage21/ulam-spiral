from painter import paint_image


def get_prime():
    with open('PR', 'r') as fl:
        lines = map(int, fl.readlines())
        prime = tuple(lines)
    return prime


def plot_prime(start=0, base='./', count=[]):
    prime = get_prime()
    img = paint_image(prime)
    print('Saving the masterpiece')
    count.append(True)
    c = str(len(count))
    img.save(base + 'prime_plot' + c + '.jpg')


def make_movie(base, no_of_frames=20, steps=100):
    for i in range(steps):
        for frame in range(no_of_frames):
            plot_prime(frame * i, base)
            print('-'*10)

if __name__ == '__main__':
    plot_prime()
    # make_movie('movie/')
