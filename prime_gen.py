from collections import deque
import pickle


def read_existing():
    try:
        f=open('data/primenumbers','rb')
        prime=pickle.load(f)
        f.close()
        primenumbers=deque(prime)
        current=primelist[-1]+1
    except:
        primenumbers=deque([2,3,5,7,11,13])
        current=14
    return primenumbers,current

def save(primelist):
    "Save primelist"
    f=open('data/primenumbers','wb')
    pickle.dump(list(primelist),f)
    f.close()
def create_primes():
    primelist,current=read_existing()
    while True:
        #check if prime
        root=current**0.5
        prime=True
        for p in primelist:
            if p>root:break
            if current%p==0:
                prime=False
                break
        #--------------
        if prime:primelist.append(current)
        current+=1
        if current%1e5==0:
            save(primelist)
            print(len(primelist),end='\r')
if __name__=='__main__':
    create_primes()
