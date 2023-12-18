# Prática 6: Introdução às Interfaces de Visão Computacional, Sistemas de Versionamento de Arquivos e Controle de Acesso via Tags

Este projeto consiste na integração de periféricos embarcados na Raspberry Pi, empregando o módulo de câmera, tags RFID e técnicas de aprendizado de máquina, abrangendo aplicações práticas, tais como sistemas de controle de acesso baseados em tags e reconhecimento facial em bancos de dados e servidores.

## Controle de acesso via Tag RFID

Neste projeto foi desenvolvido um código em Python que se concentra na integração de uma tag RFID. O programa permite a leitura eficiente de dados e identificadores (IDs) associados a essas tags. Posteriormente, foi implementada uma etapa para a criação de um sistema de verificação. Esse sistema, baseado em um circuito básico e no código elaborado, possibilita a comparação entre o ID de uma tag RFID e a base de dados de IDs armazenada no próprio código. Essa abordagem oferece uma solução eficaz para a identificação e validação de tags RFID.

Para possibilitar a utilização destas tags, o código faz uso do módulo ```SimpleMFRC522```, importado da biblioteca ```mfrc522```, que permite a interação com a ID de uma tag. Inicialmente, são configurados os pinos GPIO, utilizando o canal BCM da Broadcom, e os warnings são desativados para evitar mensagens indesejadas.

O programa define variáveis para os pinos dos LEDs verde e vermelho, os configura como saídas e os inicializa apagados. Em seguida, é criado um objeto ```leitor``` da classe ```SimpleMFRC522()``` para facilitar a interação com o leitor RFID.

No loop principal, exibe a mensagem "Aproxime a tag do leitor" e entra em um loop infinito. Dentro desse loop, a função ```leitor.read()``` é utilizada para obter o ID e o texto da tag, para assim verificar a compatibilidade do ID identificado, com o cartão previamente escolhido para este projeto.

Para controlar os LEDs, se o ID for correspondente, o LED verde é aceso e o vermelho é apagado. Caso contrário, o LED verde é apagado, e o vermelho é aceso.

Os dados da tag, incluindo ID e texto, são impressos no terminal. Há um atraso de 3 segundos antes da próxima leitura, proporcionando um intervalo entre as operações. Este código exemplifica a utilização prática do módulo ```SimpleMFRC522``` para ler e verificar tags RFID na Raspberry Pi, demonstrando a interação física com o ambiente por meio dos LEDs.

![Circuito RFID](https://raw.githubusercontent.com/johnny-ferraz/SEL0337/main/Pr%C3%A1tica%206/Imagens/RFID.jpg)

## Reconhecimento Facial via Visão Computacional

Nesta estapa que visa implementar um sistema de Reconhecimento Facial utilizando visão computacional, é implementado ao código bibliotecas essenciais, como ```cv2``` para processamento de imagem, ```os``` para interação com o sistema operacional, ```RPi.GPIO``` para controle dos pinos GPIO, ```time``` para manipulação de tempo e ```picamera2``` para controle da câmera da Raspberry Pi.

Em seguida, são configurados os pinos GPIO, sendo o botão associado ao pino 18 e o LED ao pino 20. Esses pinos são inicializados como entrada e saída, respectivamente. O botão é configurado com pull-up, e um LED é inicialmente desligado.

O programa carrega um classificador em cascata pré-treinado para a detecção facial. Esse classificador é essencial para identificar rostos nas imagens capturadas.

A câmera da Raspberry Pi é inicializada e configurada para criar uma visualização com resolução de 640x480 pixels. Um diretório chamado ```detected_faces``` é definido para armazenar as imagens contendo rostos detectados. Caso esse diretório não exista, ele é criado.

A função ```photo``` é definida para lidar com a detecção facial quando o botão é pressionado. Quando o botão é acionado, um quadro é capturado pela câmera, convertido para escala de cinza e o classificador em cascata é aplicado para detectar rostos na imagem. Os rostos detectados são destacados na imagem original com retângulos verdes, e as porções contendo os rostos são salvas como arquivos JPEG no diretório definido anteriormente.

Além disso, a imagem com os retângulos desenhados é exibida em uma janela com o título ```Camera```. O LED também é aceso durante a detecção facial e apagado após a conclusão.

A configuração do botão inclui a detecção de borda de descida, o que significa que a função ```photo``` é chamada quando o botão é pressionado. Há também um mecanismo de "debounce" com um tempo de 50 milissegundos para evitar leituras instáveis do botão.

O programa entra em um loop principal que é interrompido apenas quando o usuário pressiona `CTRL+C`. Dentro desse loop, não há operações específicas, apenas uma instrução vazia que mantém o programa em execução. Se o programa for interrompido, os pinos GPIO são limpos antes do encerramento.

