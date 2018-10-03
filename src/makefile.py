from PIL import Image
import numpy

DARKNESS=100

def make_monotone_file(v,size):
    
    im = Image.new("RGB",size)
    for x in range(size[0]):
        for y in range(size[1]):
            r,g,b = v,v,v
            im.putpixel((x,y),(r,g,b,0))
    im.save("monotone_"+str(DARKNESS)+".bmp")
    print("make monotone file")
    return im

if __name__ == "__main__":
    print("input_size:a*b")
    size = (int(input("a:")),int(input("b:")))      #make size_tuple
    im = make_monotone_file(DARKNESS,size)
    print(im.format, im.size, im.mode)
    im.show()
        
