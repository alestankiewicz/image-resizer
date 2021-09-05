from PIL import Image
from math import floor

def main():
    n = 5
    im = Image.open("kotek.jpg")
    resized_kotek = resize(im, n)
    resized_kotek.show()
    #nowe = Image.new(mode = 'RGB', size = (100, 100))
    #new_size = calc_size(nowe.size)
    #print('new_size', new_size)


def calc_size(old_size: (int, int), n):
    print('old_size: ', old_size)
    width = old_size[0]
    height = old_size[1]
    

    return (floor(width*n), floor(height*n))

def resize(img: Image, n):
    new_size = calc_size(img.size, n)
    new_img = Image.new(mode = 'RGB', size = new_size)

    pixels = new_img.load()
    for i in range(new_size[0]):
        for j in range(new_size[1]):
            pixels[i,j] = img.getpixel((floor(i/n), floor(j/n)))

    return new_img        


if __name__ == "__main__":
    main()
