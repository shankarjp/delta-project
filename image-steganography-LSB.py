from PIL import Image

def generate_data(data):
    byte = []
    for info in data:
        byte_list = [format(i, '08b') for i in info]
        for i in byte_list:
                byte.append(i)
    return(byte)

def modify_pixel(pixel, data):
    data_list = generate_data(data)
    len_data = len(data_list)
    image_data = iter(pixel)
    for i in range(len_data):
        pixel = [value for value in image_data.__next__()[:3] + image_data.__next__()[:3] + image_data.__next__()[:3]]
        for j in range(0,8):
            if(data_list[i][j] == '0' and pixel[j]%2 != 0):
                pixel[j] -= 1
            elif(data_list[i][j] == '1' and pixel[j]%2 == 0):
                if(pixel[j] != 0):
                    pixel[j] -= 1
                else:
                    pixel[j] += 1
        if(i == len_data-1):
            if(pixel[-1]%2 == 0):
                if(pixel[-1] != 0):
                    pixel[-1] -= 1
                else:
                    pixel[-1] += 1
        else:
            if(pixel[-1]%2 != 0):
                pixel[-1] -= 1
        pixel = tuple(pixel)
        yield pixel[0:3]
        yield pixel[3:6]
        yield pixel[6:9]

def encode_data(new_image, data):
    width = new_image.size[0]
    (x,y) = (0,0)
    for pixel in modify_pixel(new_image.getdata(), data):
        new_image.putpixel((x,y), pixel)
        if(x == width-1):
            x=0
            y+=1
        else:
            x+=1

def encode(image_name, file_name, new_image_name):
    image = Image.open(image_name, 'r')
    data = open(file_name, 'rb')
    new_image = image.copy()
    encode_data(new_image, data)
    new_image.save(new_image_name, str(new_image_name.split(".")[1].upper()))

def decode(image_name, new_file_name):
    image = Image.open(image_name, 'r')
    f = open(new_file_name, 'wb')
    image_data = iter(image.getdata())
    while(True):
        pixel = [value for value in image_data.__next__()[:3] + image_data.__next__()[:3] + image_data.__next__()[:3]]
        binary_string = ''
        for i in pixel[:8]:
            if(i%2 == 0):
                binary_string += '0'
            else:
                binary_string += '1'
        f.write(bytes([int(i) for i in binary_string]))
        if(pixel[-1]%2 != 0):
            f.close()
            break

def main():
    response = input()
    res_list = response.split()
    if(len(res_list) < 3):
        print("insert <image_name> <file_name> <new_image_name>")
        print("extract <image_name> <new_file_name>")
    elif(res_list[0] == "insert"):
        encode(image_name = res_list[1], file_name = res_list[2], new_image_name = res_list[3])
    elif(res_list[0] == "extract"):
        decode(image_name = res_list[1], new_file_name = res_list[2])
    else:
        print("Invalid Entry!")

if(__name__ == "__main__"):
    main()
