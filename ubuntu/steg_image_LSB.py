import cv2

def encode(input_image, output_image_name, file_name):
    height, width, nbchannels = input_image.shape
    size = width*height
    current_width = 0
    current_height = 0
    current_channel = 0

    maskonevalues = [1, 2, 4, 8, 16, 32, 64, 128]
    maskone = maskonevalues.pop(0)
    maskzerovalues = [254, 253, 251, 247, 239, 223, 191, 127]
    maskzero = maskzerovalues.pop(0)

    data = open(file_name, "rb").read()
    length = len(data)
    if(width*height*nbchannels < length + 64):
        raise Exception("Not enough space to hold all steganographic data")
    binary_value = bin(length)[2:]
    if(len(binary_value) > 64):
        raise Exception("Binary Value larger than expected")
    else:
        while(len(binary_value) < 64):
            binary_value = "0" + binary_value
    for c in binary_value:
        value = list(input_image[current_height, current_width])
        if(int(c) == 1):
            value[current_channel] = int(value[current_channel]) | maskone
        else:
            value[current_channel] = int(value[current_channel]) & maskzero
        input_image[current_height, current_width] = tuple(value)
        if(current_channel == nbchannels-1):
            current_channel = 0
            if(current_width == width-1):
                current_width = 0
                if(current_height == height-1):
                    current_height = 0
                    if maskone == 128:
                        raise Exception("No more space available in image")
                    else:
                        maskone = maskonevalues.pop(0)
                        maskzero = maskzerovalues.pop(0)
                else:
                    current_height += 1
            else:
                current_width += 1
        else:
            current_channel += 1
    for byte in data:
        if(isinstance(byte, int)):
            pass
        else:
            byte = ord(byte)
        binv = bin(byte)[2:]
        if(len(binv) > 8):
            raise Exception("Binary Value larger than expected")
        else:
            while(len(binv) < 8):
                binv = "0" + binv
        for c in binv:
            val = list(input_image[current_height, current_width])
            if(int(c) == 1):
                val[current_channel] = int(val[current_channel]) | maskone
            else:
                val[current_channel] = int(val[current_channel]) & maskzero
            input_image[current_height, current_width] = tuple(val)
            if(current_channel == nbchannels-1):
                current_channel = 0
                if(current_width == width-1):
                    current_width = 0
                    if(current_height == height-1):
                        current_height = 0
                        if maskone == 128:
                            raise Exception("No more space available in image")
                        else:
                            maskone = maskonevalues.pop(0)
                            maskzero = maskzerovalues.pop(0)
                    else:
                        current_height += 1
                else:
                    current_width += 1
            else:
                current_channel += 1
        cv2.imwrite(output_image_name, input_image)

def decode(encoded_image, extracted_file_name):
    height, width, nbchannels = encoded_image.shape
    size = width*height
    current_width = 0
    current_height = 0
    current_channel = 0

    maskonevalues = [1, 2, 4, 8, 16, 32, 64, 128]
    maskone = maskonevalues.pop(0)
    maskzerovalues = [254, 253, 251, 247, 239, 223, 191, 127]
    maskzero = maskzerovalues.pop(0)

    bits = ""
    for i in range(64):
        value = encoded_image[current_height, current_width][current_channel]
        value = int(value) & maskone
        if(current_channel == nbchannels-1):
            current_channel = 0
            if(current_width == width-1):
                current_width = 0
                if(current_height == height-1):
                    current_height = 0
                    if(maskone == 128):
                        raise Exception("No more space available in image")
                    else:
                        maskone = maskonevalues.pop(0)
                        maskzero = maskzerovalues.pop(0)
                else:
                    current_height += 1
            else:
                current_width += 1
        else:
            current_channel += 1
        if(value > 0):
            bits += "1"
        else:
            bits += "0"
    length = int(bits, 2)
    output = b""
    for i in range(length):
        bits = ""
        for i in range(8):
            value = encoded_image[current_height, current_width][current_channel]
            value = int(value) & maskone
            if(current_channel == nbchannels-1):
                current_channel = 0
                if(current_width == width-1):
                    current_width = 0
                    if(current_height == height-1):
                        current_height = 0
                        if(maskone == 128):
                            raise Exception("No more space available in image")
                        else:
                            maskone = maskonevalues.pop(0)
                            maskzero = maskzerovalues.pop(0)
                    else:
                        current_height += 1
                else:
                    current_width += 1
            else:
                current_channel += 1
            if(value > 0):
                bits += "1"
            else:
                bits += "0"
        output += bytearray([int(bits, 2)])
    f = open(extracted_file_name, "wb")
    f.write(output)
    f.close()

def main():
    response = int(input("Welcome to Image Stego using LSB\n1. Encode\t2.Decode\nChoose an option: "))
    if(response == 1):
        input_image_name = input("Input Image Name : ")
        input_image = cv2.imread(input_image_name)
        output_image_name = input("Output Image Name : ")
        file_name = input("File to be encoded : ")
        encode(input_image, output_image_name, file_name)
    elif(response == 2):
        encoded_image_name = input("Encoded Image Name : ")
        encoded_image = cv2.imread(encoded_image_name)
        extracted_file_name = input("Extracted File Name : ")
        decode(encoded_image, extracted_file_name)
    else:
        pass

if __name__ == "__main__":
    main()
        