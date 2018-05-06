import requests
import xml.etree.ElementTree as ET
import sys
from lxml import etree
from io import StringIO, BytesIO


#URL_SERVIDOR = "http://ruralruby.dlinkddns.com:8011" #Angelo. Só funciona o get (consultarStatus)
#URL_SERVIDOR = "http://tebd.000webhostapp.com" #Matheus . Funciona get e post, submeter e consultar


URL_SERVIDOR  = str(sys.argv[1])
NOME_METODO   = str(sys.argv[2])
CAMINHO_ARQ   = str(sys.argv[3])


def lerArquivo(nomeArquivo):
	arquivo = open(nomeArquivo,'r')
	texto = arquivo.read()
	arquivo.close()
	return texto

"""
Método para a submissao de um Bolhetim
FIXME: Não está funcionando

envia um boletim como parâmetro e retorna um número inteiro 
	0 - sucesso, 
	1 - XML inválido, 
	2 - XML mal-formado, 
	3 - Erro Interno

"""
def submeter(conteudoXML): 
	resposta = requests.post(url=URL_SERVIDOR,data= conteudoXML)

	parser 	 	  = etree.XMLParser(remove_blank_text=True)
	iterador 	  = etree.XML(resposta.content, parser)
	#respostateste = etree.XML("<methodReturn> <methodName>submeter</methodName> <value>1</value> </methodReturn>", parser)


	for elemento in iterador.iter("*"):
		if elemento.tag == 'value':
			if 	 elemento.text == '0' or elemento.text == ' 0 ':
				print("Sucesso!")

			elif elemento.text == '1' or elemento.text == ' 1 ':
				print("XML inválido.")

			elif elemento.text == '2' or elemento.text == ' 2 ':
				print("XML mal-formado.")

			elif elemento.text == '3' or elemento.text == ' 3 ':
				print("Erro interno.")

	#DONE: Trocar isso por uma resposta e parsear e apresentar os dados ao usuário
	#print("Resposta: ", resposta.content)


"""
Dado um xml dentro de um parâmentro, o método imprime o xml de resposta.

Possíveis retornos: 
	0 - Candidato não encontrado, 
	1 - Em processamento, 
	2 - Candidato Aprovado e Selecionado, 
	3 - Candidato Aprovado e em Espera, 
	4 - Candidato Não Aprovado.


	00000000000 -> Código 0
	00000000001 -> Código 1
	00000000002 -> Código 2
	00000000003 -> Código 3
	00000000004 -> Código 4

"""
def consultarStatus(xmlcpf):
	headers = {'content-type': 'text/xml'}
	resposta = requests.get(url = URL_SERVIDOR, data = xmlcpf, headers=headers)

	parser 	 	  = etree.XMLParser(remove_blank_text=True)
	iterador 	  = etree.XML(resposta.content, parser)
	#respostateste = etree.XML("<methodReturn><methodName>consultarStatus</methodName><value>4</value></methodReturn>", parser)


	for elemento in iterador.iter("*"):
		if elemento.tag == 'value':
			if 	 elemento.text == '0' or elemento.text == ' 0 ':
				print("Candidato não encontrado.")

			elif elemento.text == '1' or elemento.text == ' 1 ':
				print("Em processamento.")

			elif elemento.text == '2' or elemento.text == ' 2 ':
				print("Candidato aprovado e selecionado.")

			elif elemento.text == '3' or elemento.text == ' 3 ':
				print("Candidato aprovado e em espera.")

			elif elemento.text == '4' or elemento.text == ' 4 ':
				print("Candidato não aprovado.")

	#TODO: Trocar isso por uma resposta e parsear e apresentar os dados ao usuário
	#print(resposta.content)




"""
Para executar a aplicação:

python3 cliente.py URL_SERVIDOR NOME_METODO ARQUIVO_XML

Ex:

python3 cliente.py http://tebd.000webhostapp.com submeter exemplos/methodCall.xml 
python3 cliente.py http://tebd.000webhostapp.com consultarStatus exemplos/consultStatus4.xml 


"""
def main():

	conteudoXML_status = lerArquivo(CAMINHO_ARQ)
	conteudoXML 	   = lerArquivo(CAMINHO_ARQ)

	if NOME_METODO == "consultarStatus":
		consultarStatus(conteudoXML_status)

	elif NOME_METODO == "submeter":
		submeter(conteudoXML)

	else:
		print("Opção inválida!")


#Executar função main
if __name__ == '__main__':
	main()

