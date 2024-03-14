from PIL import Image


def asciiConvert(image, type, saveas, scale):
    scale = int(scale)
    
    #Open and get image size
    img = Image.open(image)
    w,h = img.size

    #Resize image (Downscale)
    img.resize((w//scale, h//scale)).save("resized.%s" % type)

    #Open new image
    img = Image.open("resized.%s" % type)
    w,h = img.size

def main():
    print("test")


if __name__ == "__main__":
    main()
