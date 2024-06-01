# Importando bibliotecas
from qreader import QReader
import cv2


# URL's
caminhoPastaProcessar_IN = "/Users/murilomedeiros/Library/CloudStorage/OneDrive-Pessoal/RPA/Ambiente de Testes/Download de Notas e Cupons Fiscais/Processar/"
caminhoImagem_IN = ""


def main():

    try:
        # Create a QReader instance
        qreader = QReader()

        # Get the image that contains the QR code
        image = cv2.cvtColor(cv2.imread(caminhoPastaProcessar_IN + "image2.jpeg"), cv2.COLOR_BGR2RGB)

        # Use the detect_and_decode function to get the decoded QR data
        decoded_text = qreader.detect_and_decode(image=image)

        # Tratativa de limpar a string para capturar apenas a chave de acesso
        decoded_text = decoded_text[0]
        decoded_text = decoded_text.split("|")
        decoded_text = decoded_text[0]
        decoded_text = decoded_text.split("=")
        decoded_text = decoded_text[1]
        print(f"Chave de acesso extraída: {decoded_text}")

    
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
