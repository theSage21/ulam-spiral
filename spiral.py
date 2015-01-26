import sys
import pickle
from collections import deque


#import the already existing data
try:
    f=open('coordinate_list','rb')
    data=pickle.load(f)
    f.close()
    data=deque(data)
except:
    data=deque([(0,0),])#the first number is at 0,0
#set global values
coordinate=(0,0)
index=0
#now start the spiraler
def move(current):
    "moves coordinate in current direction"
    global data,index
    global coordinate
    x,y=coordinate
    d={ 'u':(x,y+1),
        'd':(x,y-1),
        'r':(x+1,y),
        'l':(x-1,y)
        }
    coordinate=d[current]
    data.append(coordinate)
    index+=1
    if index>21e6:
        save()
        sys.exit(0)
def save():
    global data,index
    #create a backup
    try:
        f=open('coordinate_list','rb')
        nd=pickle.load(f)
        f.close()
        f=open('coordinate_list.bak','wb')
        pickle.dump(nd,f)
        f.close()
    except:pass#in case of first file
    #create a new file
    f=open('coordinate_list','wb')
    pickle.dump(data,f)
    f.close()
    print(index,end='\r')
    
def spiral_gen():
    "generate the spiral"
    repeat=0
    current='u'
    nxt={'u':'r',
        'r':'d',
        'd':'l',
        'l':'u'
        }
    while True:
        repeat+=1
        move(current)
        if index%10==0:
            save()
            print(index,end='\r')
        for i in range(2):
            current=nxt[current]
            for j in range(repeat):
                move(current)
if __name__=='__main__':
    spiral_gen()
