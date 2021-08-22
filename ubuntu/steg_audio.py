import wave

def encode(input_audio_name, output_audio_name, file_name):
    pass

def decode(encoded_audio_name, extracted_file_name):
    pass

def main():
    response = int(input("Welcome to Audio Stego\n1. Encode\t2.Decode\nChoose an option: "))
    if(response == 1):
        input_audio_name = input("Input Audio Name : ")
        output_audio_name = input("Output Audio Name : ")
        file_name = input("File to be encoded : ")
        encode(input_audio_name, output_audio_name, file_name)
    elif(response == 2):
        encoded_audio_name = input("Encoded Audio Name : ")
        extracted_file_name = input("Extracted File Name : ")
        decode(encoded_audio_name, extracted_file_name)
    else:
        pass

if __name__ == "__main__":
    main()
