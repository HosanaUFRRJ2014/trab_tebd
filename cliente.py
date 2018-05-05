import requests
import xml.etree.ElementTree as ET
import sys

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
	headers = {'content-type': 'text/xml'}
	resposta = requests.post(url=URL_SERVIDOR,data=conteudoXML, headers=headers)

	##TODO: Trocar isso por uma resposta e parsear e apresentar os dados ao usuário
	print("Resposta: ", resposta.content)


"""
Dado um xml dentro de um parâmentro, o método imprime o xml de resposta.
TODO: Parsear a resposta para apresentar ao usuário
"""
def consultarStatus(xmlcpf):
	headers = {'content-type': 'text/xml'}
	resposta = requests.get(url = URL_SERVIDOR, data = xmlcpf, headers=headers)

	#TODO: Trocar isso por uma resposta e parsear e apresentar os dados ao usuário
	print(resposta.content)


def main():

	
	#conteudoXML_status = lerArquivo("exemplos/consultStatus4.xml")
	#conteudoXML = lerArquivo("exemplos/methodCall.xml")

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

