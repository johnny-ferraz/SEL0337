# Prática 6: Introdução às Interfaces de Visão Computacional, Sistemas de Versionamento de Arquivos e Controle de Acesso via Tags

Este projeto consiste na integração de periféricos embarcados na Raspberry Pi, empregando o módulo de câmera, tags RFID e técnicas de aprendizado de máquina, abrangendo aplicações práticas, tais como sistemas de controle de acesso baseados em tags e reconhecimento facial em bancos de dados e servidores.

## Controle de acesso via Tag RFID

Neste projeto foi desenvolvido um código em Python que se concentra na integração de uma tag RFID. O programa permite a leitura eficiente de dados e identificadores (IDs) associados a essas tags. Posteriormente, foi implementada uma etapa para a criação de um sistema de verificação. Esse sistema, baseado em um circuito básico e no código elaborado, possibilita a comparação entre o ID de uma tag RFID e a base de dados de IDs armazenada no próprio código. Essa abordagem oferece uma solução eficaz para a identificação e validação de tags RFID.

Para possibilitar a utilização destas tags, o código faz uso do módulo ```SimpleMFRC522```, importado da biblioteca ```mfrc522```, que permite a interação com a ID de uma tag. Inicialmente, são configurados os pinos GPIO, utilizando o canal BCM da Broadcom, e os warnings são desativados para evitar mensagens indesejadas.

O programa define variáveis para os pinos dos LEDs verde e vermelho, os configura como saídas e os inicializa apagados. Em seguida, é criado um objeto ```leitor``` da classe ```SimpleMFRC522()``` para facilitar a interação com o leitor RFID.

No loop principal, exibe a mensagem "Aproxime a tag do leitor" e entra em um loop infinito. Dentro desse loop, a função ```leitor.read()``` é utilizada para obter o ID e o texto da tag, para assim verificar a compatibilidade do ID identificado, com o cartão previamente escolhido para este projeto.

Para controlar os LEDs, se o ID for correspondente, o LED verde é aceso e o vermelho é apagado. Caso contrário, o LED verde é apagado, e o vermelho é aceso.

Os dados da tag, incluindo ID e texto, são impressos no terminal. Há um atraso de 3 segundos antes da próxima leitura, proporcionando um intervalo entre as operações. Este código exemplifica a utilização prática do módulo ```SimpleMFRC522``` para ler e verificar tags RFID na Raspberry Pi, demonstrando a interação física com o ambiente por meio dos LEDs.
