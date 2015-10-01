from PIL import Image


def get_coordinates(limit=1000000, lines=[]):
    if len(lines) == limit:
        return tuple(lines)
    with open('coordinate_list', 'r') as f:
        for _ in range(limit):
            lines.append(eval(f.readline()))
    data = tuple(lines)
    return data


def paint_image(numbers, background='white', hilight=(0, 0, 0)):
    '''
    Takes in data as a list of tuples dictating the location
    of the numbers. First tuple shows location of 1 and so on.
    Numbers is a list of numbers which are to be painted white

    Returns an PIL.Image object ready to be painted.
    '''
    assert isinstance(numbers, (tuple, list))
    assert isinstance(background, str)
    assert isinstance(hilight, (tuple, list))
    assert len(hilight) == 3
    print('Loading spiral from disk')
    data = get_coordinates()
    print('Creating canvas')

    size = int(len(data)**0.5) + 1
    img = Image.new('RGB', (size, size), background)
    print('Painting')

    center = (int(size/2), int(size/2))
    da = [(point[0]+center[0], point[1]+center[1]) for point in data]
    data = da

    for index, number in enumerate(numbers):
        try:
            point = data[number]
            try:
                img.putpixel(point, hilight)
            except IndexError:
                print(point)
                pass
        except IndexError:
            break
    print('Cleaning up')
    return img
