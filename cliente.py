import requests
import xml.etree.ElementTree as ET



##TODO: Colocar como parâmetro de terminal
URL_SERVIDOR = "http://ruralruby.dlinkddns.com:8011"

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
	resposta = requests.post(url=URL_SERVIDOR,data=conteudoXML)

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
	conteudoXML_status = lerArquivo("consultStatus4.xml")
	consultarStatus(conteudoXML_status)

#	conteudoXML = lerArquivo("methodCall.xml")
#	submeter(conteudoXML)


#Executar função main
if __name__ == '__main__':
	main()

