from pysimplesoap.client import SoapClient, SoapFault

# create a simple consumer
client = SoapClient(
    location = "http://localhost:8008/",
    action = 'http://localhost:8008/', # SOAPAction
   # namespace = "http://example.com/sample.wsdl", 
    soap_ns='soap',
    trace = True, #mudar para False para não imprimir o log no terminal
    ns = False)

# call the remote method

#response = client.Adder(a=1, b=2)
#resposta = client.criarAluno(cpf="5485",nome="hosana",universidade="ufrrj", curso="ccomp")

resposta = client.consultaStatus(cpf="00000000000")


# extract and convert the returned value

#result = response.AddResult
#objAluno = resposta.Aluno

resultado = resposta.value

#print (int(result))

print("*****************************")
#print(objAluno)
print(int(resultado))


