# Prática 6 - Projetos em Sistemas Embarcados
# Davi Daniel da Silva - 12567029
# João Lucas Almeida Caldas Ferraz - 12609651

# Importação das bibliotecas

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
from time import sleep

GPIO.setmode(GPIO.BCM) # Define os pinos GPIO pelo canal SoC da Broadcom
GPIO.setwarnings(False) # Desativa os warnings

LED_VERDE = 18 # Variável para o pino do LED verde (pino 18)
LED_VERMELHO = 23 # Variável para o pino do LED vermelho (pino 23)

GPIO.setup(LED_VERDE, GPIO.OUT) # Define o LED verde como saída
GPIO.setup(LED_VERMELHO, GPIO.OUT) # Define o LED vermelho como saída

GPIO.output(LED_VERDE, False) # Apaga o LED verde
GPIO.output(LED_VERMELHO, False) # Apaga o LED vermelho

leitor = SimpleMFRC522() # Cria o objeto "leitor" para a instância "SimpleMFRC522" da biblioteca

while True: # Loop
	print("Aproxime a tag do leitor") # Printa a mensagem para aproximar a tag do leitor
	id, texto = leitor.read() # Variáveis que armazenam o ID e o texto presente na tag
	if id == 771459753502: # Verifica se o ID da tag é 771459753502
		GPIO.output(LED_VERDE, True) # Acende o LED verde
		GPIO.output(LED_VERMELHO, False) # Apaga o LED vermelho

	else: # Executado se o ID da tag não for 771459753502
		GPIO.output(LED_VERDE, False) # Apaga o LED verde
		GPIO.output(LED_VERMELHO, True) # Acende o LED vermelho
        
	print("ID: {}\nTexto: {}".format(id, texto)) # Printa o ID e o texto da tag no terminal
	sleep(3) # Delay de 3s
