# Trabalho de TEBD - Cliente que se comunica por XML 

Este trabalho foi apresentado à disciplina de Tópicos Especiais em Banco de Dados (TEBD) no semestre 2018.1.
O objetivo do repositório é apresentar uma estrutura de Cliente que utiliza protocolo XML para se comunicar com um servidor remoto. Toda a troca de informação entre Cliente e Servidor ocorre apenas via XML. XSDs são usados para a validação e verificação dos XMLs usados nas trocas de informações do sistema do lado do servidor.


## Organização do repositório

Esta seção objetiva explicar resumidamente o esquema e a organização do repositório da aplicação.

- A pasta *exemplos* contém exemplos de teste de xml que serão consumidos pela aplicação;
- O arquivo *cliente.py* é a aplicação do cliente. 




## Como configurar o ambiente de desenvolvimento:

O sistema foi desenvolvido em **Python3** e utiliza a biblioteca **Requests** para as requisições GET E POST.

### Instalando a biblioteca de Requests GET e POST:    

Em um terminal Linux, execute o seguinte comando:

    sudo pip install requests



## Executando a aplicação:


A aplicação recebe como parâmetro a url de um servidor (**<URL_SERVIDOR>**) que aceite requisições do cliente, o método que se deseja executar (**<NOME_MÉTODO_APLICAÇÃO>**), isto é, ```submeter``` ou ```consultarStatus```, e o nome do arquivo XML o qual será enviado o conteúdo (**<NOME_ARQUIVO_XML>**).

Abaixo, segue o formato de uma execução do cliente:

	python3 <URL_SERVIDOR> <NOME_MÉTODO_APLICAÇÃO> <NOME_ARQUIVO_XML>