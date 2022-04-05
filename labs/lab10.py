######################################################
# Name   : Rashmika Batra
# Pledge : I pledge my honor that I have abided by the Stevens Honor System. 
######################################################
from cs5png import PNGImage

def mult(c,n):
    '''Given numbers c and n, return c*n, using only addition and lööps'''
    result=0
    for i in range(n):
        result= result+c
    return result 

print(mult(6,7))
print (mult(1.5,28))
def update(c,n):
    '''Given numbers c and n,
    return z where z(0, c) = z and z(n, c) = z(n-1, c)**2 + c,
    absolutely no recursion'''
    z=0
    for i in range(n):
        z=z**2+c
    return z 
        
print(update(1,3))
print(update(-1,3))
print(update(1,10))

def inMSet(c,n):
    '''Given a complex c and a number n, return if the magnitude of z
    never goes above 2 in the process of doing update(...). Don't(!)
    call update'''
    z=0
    for i in range(n):
        z=z**2+c
        if abs(z)>2:
            return False
    return True 
print(inMSet(3+4j,25))
print(inMSet(.3+-.5j,25))
print(inMSet(-.7+.3j,25))
print(inMSet(.42+-.2j,25))
print(inMSet(.42+-.2j,50))


   

def scale(pix, pixelMax, floatMin, floatMax):
    a=(floatMax-floatMin)
    b=(pix/pixelMax)
    return (b*a)+floatMin
print(scale(100,200,-2.0,1.0))
print(scale(100,200,-1.5,1.5))
print(scale(100,300,-2.0,1.0))
print(scale(25,300,-2.0,1.0))
print(scale(299,300,-2.0,1.0))


def mset(n):
    '''Creates a 300x200 image of the Mandelbrot set, where
    the image is of the complex plane with x real [-2, 1] and y imaginary, [-i, i]'''
    width = 300
    height = 200
    image = PNGImage(width, height)

    for col in range(width):
        for row in range(height):
            x= scale(width,height,-2,1)
            y=scale(width,height,-1,1)
            c=x+y*1j
            if inMSet(c,n):
                image.plotPoint(col,row)
    image.saveFile()

if __name__ == "__main__":
    iterations = 100 # Change this to play with the picture, once everything's working
    mset(iterations)
