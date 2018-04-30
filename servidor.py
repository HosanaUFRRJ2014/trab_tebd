from pysimplesoap.server import SoapDispatcher, SOAPHandler
from http.server import HTTPServer

#TODO: Colocar as classes em arquivos separados

class Materia(object):
    """docstring for Materia"""
    def __init__(self, codigo, nome, creditos, conceito, situacao):
        #super(Materia, self).__init__()
        self.codigo = codigo
        self.nome = nome
        self.creditos = creditos
        self.conceito = conceito
        self.situacao = situacao
        




#FIXME Periodo tem uma lista de matérias. Pode ser necessário especificar isso.
class Periodo(object):
    """docstring for Periodo"""
    def __init__(self, ano, semestre, materia):
        #super(Periodo, self).__init__()
        self.ano = ano
        self.semestre = semestre
        self.materia = materia
        



#FIXME: historico tem uma lista de periodos. Talves seja necessário especificar isso aqui.
class Historico(object):
    """docstring for Historico"""
    def __init__(self, periodo):
        #super(Historico, self).__init__()
        self.periodo = periodo




class Aluno(object):
    """docstring for Aluno"""
    def __init__(self, cpf, nome, universidade, curso):
        #super(Aluno, self).__init__()
        self.cpf = cpf
        self.nome = nome
        self.universidade = universidade
        self.curso = curso



    def getNome(self):
        return self.nome

                 




class Bolhetim(object):
    """docstring for Bolhetim"""
    def __init__(self, aluno, historico):
        #super(Bolhetim, self).__init__()
        self.aluno = aluno
        self.historico = historico

                        



def criarAluno(cpf,nome,universidade,curso):
    return Aluno(cpf,nome,universidade,curso)



def adder(a,b):
    "Add two values"
    return a+b


#def submeter(bolhetim):
 #   pass


def consultaStatus(cpf):
    """consulta o status da inscrição do candidato com o CPF informado como parâmetro. 
    Possíveis retornos: 
    0 - Candidato não encontrado, 
    1 - Em processamento, 
    2 - Candidato Aprovado e Selecionado, 
    3 - Candidato Aprovado e em Espera, 
    4 - Candidato Não Aprovado.
    TODO: NOT IMPLEMENTED YET"""

    return 0


dispatcher = SoapDispatcher(
    'my_dispatcher',
    location = "http://localhost:8008/",
    action = 'http://localhost:8008/', # SOAPAction
    namespace = "http://example.com/sample.wsdl", prefix="ns0",
    trace = True,
    ns = True)

# register the user function
dispatcher.register_function('Adder', adder,
    returns={'AddResult': int}, 
    args={'a': int,'b': int})


dispatcher.register_function('consultaStatus', consultaStatus,
    returns={'value': int}, 
    args={'cpf': str})




dispatcher.register_function('criarAluno', criarAluno,
    returns={'Aluno': {'cpf':str,'nome':str,'universidade':str,'curso':str}}, 
    args={'cpf':str,'nome':str,'universidade':str,'curso':str})

dispatcher.register_function('Aluno.getNome', Aluno.getNome,
    returns={'nome': str}, 
    args={})



print("Starting server...")
httpd = HTTPServer(("", 8008), SOAPHandler)
httpd.dispatcher = dispatcher

print(dispatcher.list_methods())

#aluno = Aluno("1981","meu nome","universidade", "curso")


httpd.serve_forever()
