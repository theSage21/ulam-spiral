from painter import paint_image
import pickle

def get_prime():
        f=open('data/primenumbers','rb')
        prime=pickle.load(f)
        f.close()
        return prime
def plot_prime():
    prime=get_prime()
    img=paint_image(prime)
    print('Saving the masterpiece')
    img.save('plots/prime_plot.jpg')
if __name__=='__main__':
    plot_prime()
       
