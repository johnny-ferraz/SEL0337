# Prática 6: Introdução às Interfaces de Visão Computacional, Sistemas de Versionamento de Arquivos e Controle de Acesso via Tags

Este projeto consiste na integração de periféricos embarcados na Raspberry Pi, empregando o módulo de câmera, tags RFID e técnicas de aprendizado de máquina, abrangendo aplicações práticas, tais como sistemas de controle de acesso baseados em tags e reconhecimento facial em bancos de dados e servidores.

## Controle de acesso via Tag RFID

Neste projeto foi desenvolvido um código em Python que se concentra na integração de uma tag RFID. O programa realiza a leitura do ID associado a essa tag e, por meio de um sistema de verificação, compara seu valor com o ID esperado. Para interação com o usuário, um LED verde é aceso se o ID for coincidente (acesso liberado) e um LED vermelho é aceso caso os IDs sejam distintos (acesso negado).

Para possibilitar tal operação, o código faz uso do módulo ```SimpleMFRC522```, importado da biblioteca ```mfrc522```, que permite a interação com o ID de uma tag. São também configurados os pinos GPIO, utilizando o canal BCM da Broadcom (pinos GPIO) e os warnings são desativados para evitar mensagens indesejadas.

O programa define variáveis para os pinos dos LEDs verde e vermelho, configurando-os como saídas inicialmente apagados. Em seguida, é criado um objeto ```leitor``` da classe ```SimpleMFRC522()``` para possibilitar a interação com o leitor RFID.

O loop principal é responsável por exibir a mensagem "Aproxime a tag do leitor" no terminal, chamar a função ```leitor.read()```, utilizada para obter o ID e o texto da tag, para assim verificar a compatibilidade do ID identificado, com o cartão previamente escolhido para este projeto, e realizar o controle dos LEDs. Os dados da tag, incluindo ID e texto, são impressos no terminal. Há um atraso de 3 segundos antes da próxima leitura, proporcionando um intervalo entre as operações.

![Circuito RFID](https://raw.githubusercontent.com/johnny-ferraz/SEL0337/main/Pr%C3%A1tica%206/Imagens/RFID.jpg)

## Reconhecimento Facial utilizando Visão Computacional e Algoritmo Haar Cascade

Nesta etapa foi implementado um sistema de reconhecimento facial utilizando a câmera da Raspberry Pi e o algoritmo `Haar Cascade`, classificador em cascata pré-treinado para a detecção facial. O código realiza a captura da imagem no momento em que um push-button é pressionado e logo em seguida o algoritmo é aplicado. Para interação com o usuário, um LED verde é aceso durante o processamento da imagem. Os rostos detectados pelo classificador são armazenados em um diretório ```detected_faces```. 

Inicialmente, são importados ao código bibliotecas essenciais, como ```cv2``` para visão computacional, ```os``` para interação com o sistema operacional, ```RPi.GPIO``` para controle dos pinos GPIO, ```time``` para manipulação de tempo e ```picamera2``` para controle da câmera da Raspberry Pi.

Em seguida, são configurados os pinos GPIO, sendo o botão associado ao pino 18 e o LED ao pino 20. Esses pinos são inicializados como entrada e saída, respectivamente. O botão é configurado com pull-up, ativado em borda de descida com chamada da função ```photo``` e mecanismo de `debounce` de 50 ms para evitar leituras instáveis do botão. Já o LED é definido como inicialmente desligado.

A câmera da Raspberry Pi é inicializada e configurada para criar uma visualização com resolução de 640x480 pixels. O diretório ```detected_faces``` é definido para armazenar as imagens dos rostos detectados e é criado caso ainda não exista.

A função ```photo()``` é definida para lidar com a detecção facial quando o botão é pressionado. Quando o botão é acionado, um quadro é capturado pela câmera, convertido para escala de cinza e o classificador em cascata é aplicado para detectar rostos na imagem. As faces detectadas são destacadas na imagem original com retângulos verdes e as porções contendo os rostos são salvas como arquivos JPEG no diretório definido anteriormente. Além disso, a imagem com os retângulos desenhados é exibida em uma janela com o título ```Camera```. O LED também é aceso durante a detecção facial e apagado após a conclusão.

O programa entra em um loop principal que é interrompido apenas quando o usuário pressiona `CTRL+C`. Dentro desse loop, não há operações específicas, apenas uma instrução vazia que mantém o programa em execução. Se o programa for interrompido, os pinos GPIO são limpos antes do encerramento.

![Circuito RFID](https://raw.githubusercontent.com/johnny-ferraz/SEL0337/main/Pr%C3%A1tica%206/Imagens/C%C3%A2mera.jpg)
