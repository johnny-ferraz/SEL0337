# Prática 6 - Projetos em Sistemas Embarcados
# Davi Daniel da Silva - 12567029
# João Lucas Almeida Caldas Ferraz - 12609651

# Importação das bibliotecas

import cv2 
import os
import RPi.GPIO as GPIO 
import time
from picamera2 import Picamera2

GPIO.setmode(GPIO.BCM) # Define os pinos GPIO pelo canal do SoC da Broadcom
GPIO.setwarnings(False) # Desativa os warnings

BUTTON = 18 # Variável para o pino do botão (pino 18)
LED = 20 # Variável para o pino do LED (pino 20)

GPIO.setup(LED, GPIO.OUT) # Define o pino do LED como saída
GPIO.setup(BUTTON, GPIO.IN, GPIO.PUD_UP) # Define o pino do botão como entrada e com pull-up

GPIO.output(LED, False) # LED inicialmente apagado

face_detector = cv2.CascadeClassifier("/home/sel/haarcascade_frontalface_default.xml") # Carrega o classificador para 
                                                                                       # detecção facial
cv2.startWindowThread() # Inicia uma thread para gerenciar janelas de visualização
picam2 = Picamera2() # Inicializa a câmera da Raspberry Pi
picam2.configure(picam2.create_preview_configuration(main={"format":'XRGB8888', "size": (640, 480)})) 
# Configura a câmera para criar uma visualização com formato de representação de cores 32 bits “XRGB8888” e resolução
# de 640x480 pixels
picam2.start() # Inicia a câmera
output_directory = "detected_faces" # Define o diretório onde as imagens com rostos detectados serão armazenadas
os.makedirs(output_directory, exist_ok=True) # Cria o diretório, se ele não existir

def photo(pin): # Função para detecção facial
    if not GPIO.input(pin): # Verifica se o botão foi pressionado
        GPIO.output(LED, True) # Acende o LED
        im = picam2.capture_array() # Captura um quadro da câmera e armazena na variável
        grey = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY) # Converte a imagem colorida para escala de cinza
        faces = face_detector.detectMultiScale(grey, 1.1, 5) # Usa o classificador em cascata para detectar rostos
                                                             # na imagem em escala de cinza
        for (x, y, w, h) in faces: # Loop para processar cada rosto detectado
            cv2.rectangle(im, (x, y), (x + w, y + h), (0, 255, 0)) # Desenha um retângulo verde ao redor do rosto
                                                                   # na imagem original
            timestamp = int(time.time()) # Gera um nome de arquivo único com base no carimbo de data/hora
            filename = os.path.join(output_directory, f"face_{timestamp}.jpg")
            cv2.imwrite(filename, im[y:y+h, x:x+w]) # Salva apenas a porção da imagem que contém o rosto detectado
                                                    # como um arquivo JPEG

        cv2.imshow("Camera", im) # Exibe a imagem com os retângulos desenhados em uma janela com o título "Camera"
        cv2.waitKey(500) # Aguarda 500 ms

    else: # Se o botão não for pressionado
        time.sleep(2) # Delay de 2 s
        GPIO.output(LED, False) # Apaga o LED

GPIO.add_event_detect(BUTTON, GPIO.FALLING, callback=photo, bouncetime=50) # Configura o pino do botão com interrupção em 
# borda de descida, chamada da função photo com o acionamento da interrupção e tratamento do efeito bounce do botão

try: # Execução normal do programa
    while True: # Loop
        pass # Mantém o programa em execução (instrução vazia)
except KeyboardInterrupt: # Executado quando o usuário interrompe a execução do programa apertando CTRL+C
    GPIO.cleanup() # Limpa os pinos GPIO antes de encerrar o programa