from PIL import Image
import pickle

def get_coordinates():
    f=open('data/coordinate_list','rb')
    data=pickle.load(f)
    f.close()
    return data


def paint_image(numbers):
    '''Takes in data as a list of tuples dictating the location
    of the numbers. First tuple shows location of 1 and so on.
    Numbers is a list of numbers which are to be painted white

    Returns an PIL.Image object ready to be painted.
    '''
    #get spiral map from disk
    print('Loading spiral from disk')
    data=get_coordinates()
    print('Creating canvas')
    #create an image of appropriate
    #size to contain all the numbers
    #present in data
    size=len(data)**0.5
    if size>int(size):
        size=int(size)+10
    #create img object
    img=Image.new('RGB',(size,size),'black')
    #now make all numbers present in
    #numbers white
    print('Painting')
    #shift the number map to match the image
    center=(int(size/2),int(size/2))
    da=[(point[0]+center[0],point[1]+center[1]) for point in data]
    data=da
    #start plotting
    for index,number in enumerate(numbers):
        if index%5==0:print('=',end='\r')
        else:print('|',end='\r')
        try:
            point=data[number]
            try:
                img.putpixel(point,(255,255,255))
            except IndexError:
                print(point)
                break
        except IndexError:
            break
    print('Cleaning up')
    return img
