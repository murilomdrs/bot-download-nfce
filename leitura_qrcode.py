from qreader import QReader
# import cv2


# URL's
caminhoPastaProcessar_IN = "/Users/murilomedeiros/Documents/Processar/"
caminhoImagem_IN = ""


def main():

    try:
        # Create a QReader instance
        qreader = QReader()

        # Get the image that contains the QR code
        image = cv2.cvtColor(cv2.imread(caminhoPastaProcessar_IN + "image.jpeg"), cv2.COLOR_BGR2RGB)

        print(image)

        # Use the detect_and_decode function to get the decoded QR data
        decoded_text = qreader.detect_and_decode(image=image)

        print(decoded_text)
    
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
