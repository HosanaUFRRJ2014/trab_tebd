import requests
import xml.etree.ElementTree as ET
import sys
from lxml import etree
from io import StringIO, BytesIO

#DONE: Colocar como parâmetro de terminal
#URL_SERVIDOR = "http://ruralruby.dlinkddns.com:8011"

URL_SERVIDOR  = str(sys.argv[1])
NOME_METODO   = str(sys.argv[2])
CAMINHO_ARQ   = str(sys.argv[3])
""" 
NOTA: Usar POST para o método submeter 
e GET para o método consultarStatus.


Exemplo de requisição GET que funciona
url = "http://maps.googleapis.com/maps/api/geocode/xml"


location = "delhi technological university"
PARAMS = {'address':location}
 
r = requests.get(url = url, params = PARAMS)

print(r.content)  #necessário parsear o xml depois
"""

def lerArquivo(nomeArquivo):
	arquivo = open(nomeArquivo,'r')
	texto = arquivo.read()
	arquivo.close()
	return texto

"""
Método para a submissao de um Bolhetim
FIXME: Não está funcionando
"""

def submeter(conteudoXML): 

	headers  = {'content-type': 'text/xml'}
	resposta = requests.post(url=URL_SERVIDOR,data=conteudoXML, headers=headers)

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
TODO: Parsear a resposta para apresentar ao usuário
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


def main():

	
	#conteudoXML_status = lerArquivo("exemplos/consultStatus4.xml")
	#conteudoXML 		= lerArquivo("exemplos/methodCall.xml")

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

