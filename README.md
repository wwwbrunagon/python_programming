https://cursos.alura.com.br/course/introducao-ao-python/
instrutor: Flávio Almeida

Básico
listas: Estrutura de dados que guardam valores de qualquer tipo conhecido do python.

tuplas: Tuplas são imutáveis e por isso se comportam como listas estáticas, é muito bom para evitar que alguem altere a lista depois de criada. Em resumo isso significa que não podemos alterar um mesmo objeto tupla, ou seja, mudar uma de suas referências internas (seus valores), nem adicionar ou remover elemento. Quanto à sintaxe, a tupla se diferencia por substituir os colchetes ([]) das listas por parênteses (())
exemplo: 
>>> tipos_de_convite = ('vip', 'normal', 'meia', 'cortesia')
>>> tipos_de_convite[1]
>>> 'normal'

dictionary:  Nos permite criar facilmente uma associação chave e  valor. 
exemplo
>>> convites_com_valor = {'vip' : 60, 'normal' : 40, 'meia' : 30, 'cortesia' : 0 } 
>>> convites_com_valor
{'meia': 30, 'vip': 60, 'cortesia': 0, 'normal': 40}
>>> convites_com_valor['vip']
60

podemos imprimir todas as chaves e valores de um dicionário:
>>> convites_com_valor.keys()
['meia', 'vip', 'cortesia', 'normal']
>>> convites_com_valor.values()
[30, 60, 0, 40]

Funções
O primeiro passo para definirmos uma função que poderá ser reutilizada por qualquer desenvolvedor é criarmos um arquivo com a extensão .py pois é neste arquivo que definiremos nossa função. Usamos a palavra chave def (define em inglês) seguido do nome da função terminando com dois pontos:

# python/biblioteca.py

def gera_nome_convite():

def gera_nome_convite(convite):
  posicao_final = len(convite)
  posicao_inicial = posicao_final - 4
  parte1 = convite[0:4]
  parte2 = convite[ posicao_inicial:posicao_final]
  return parte1 + ' ' + parte2

>>> info = gera_nome_convite('Flavio Almeida')
>>> print 'O código gerado foi %s' % (info)
O código gerado foi Flav eida

_usando funções dentro de funções
exemplo: uma rotina que o desenvolvedor sempre faz é chamar primeiro o gera_nome_convite e depois o envia_convite. Ou seja ele sempre tem que lembrar de formatar o nome do convidado para depois enviar. No console normalmente temos o seguinte procedimento:

def gera_nome_convite(nome_convidado):
    posicao_final = len(nome_convidado)
    posicao_inicial = posicao_final - 4
    parte1 = nome_convidado[0:4]
    parte2 = nome_convidado[posicao_final-4:posicao_final]
    return parte1 + ' ' + parte2


def envia_convite(nome_convidado):
    print "Enviando convite para %s" %(nome_convidado)


def processa_convite(nome_convidado):
    nome_formatado = gera_nome_convite(nome_convidado)
    envia_convite(nome_formatado)



Expressões Regulares ou simplesmente regex
Pesquisar por critério numa string 
O módulo RE (Lib regex python)

>>> import re

Meta caracteres
ex.:
Queremos todas as palavras que começam com expressão [A-Za-z]y. O truque é definirmos uma faixa ainda maior de caracteres, indicado pelo operador +. Este operador significa um ou mais caracteres. Vamos adicionar a expressão [A-Za-z]+ após a já existente:

>>> resultados = re.findall('([A-Za-z]y[A-Za-z]+)','Python ou jython ou PyPy')
>>> resultados 
['Python', 'jython', 'PyPy']
Caso queiramos buscar qualquer caractere, podemos usar [A-Za-z0-9] como faixa. Porém, por ser uma necessidade tão comum, podemos optar pelo atalho \w. 
>>> resultados = re.findall('(\wy\w+)','Python ou jython ou PyPy')
>>> resultados
['Python', 'jython', 'PyPy']
o \w também incorpora números, porém não leva em consideração acentos.
>>> resultados = re.findall('(\wy\w+)','Python3 ou jython2 ou PyPy')
>>> resultados
['Python3', 'jython2', 'PyPy']
devemos configurar esses caracteres separadamente, como por exemplo: 
\w|á|é (\w ou á ou é).
Existem outros atalhos como o \d que identifica apenas números ou \s para whitespaces como espaço ou tabulação.
Raw String (para declarar expressões regulares)
Para definir uma raw string devemos prefixar a string com a letra r, por exemplo r'[A-Z]+'.
Não confunda o r com regex, r significa raw.
Com expressões regulares procuramos pelo início através do caractere ^ (circunflexo). Por exemplo, para pegar um texto que começa com # (tralha) usaremos a expressão r'^#'

Analogamente podemos usar o caractere $ para buscar pelo final da string. Para saber se uma string termina com br podemos usar a expressão: r'.*br$'. Repare o $ no final da expressão. br deve estar no final ($) e antes do br podem vir quaisquer caracteres, zero ou mais vezes (.*):

>>> resultado = re.match(r'.*br$','http://alura.com.br')
>>> resultado.group()
'http://alura.com.br'

Qual é o resultado da execução?
1)
>>> import re
>>> resultados = re.findall(r'([JP]\w+)','Java JavaScript Python')
>>> resultados
Imprime: ['Java', 'JavaScript', 'Python']
Criamos uma string crua (raw string) com o prefixo r' '. Dentro das aspas vem a expressão regular em parêntesis - r'( )'.
Definimos um grupo com dois caracteres: [JP] Ou seja, a string deve começar com J ou P. Em seguida deve vir qualquer word caracter uma ou mais vezes - \w+. Um word caracter é uma letra ou número.
\w é um dos meta caracteres do mundo de expressões regulares e significa word. Em outras palavras letras e números (igual à [a-zA-Z0-9]). Tem muito mais meta caracteres como \d para representar números decimais (igual a [0-9]) ou \s que representa um whitespace que seria um tabulador ou return.


2)
>>> resultado = re.match(AQUI,'Python3')
>>> resultado.group()
r'(\w+\d$)'. Ou seja, qualquer word char (\w) um ou mais vez (+) seguindo pelo número decimal (\d) no fim ($) da palavra!

Função construtora e self
Precisamos definir quais serão as características de nossa classe através do construtor __init__, que recebe como parâmetro um self. Utilizamos o termo construtor porque ele é chamado toda vez que criamos um objeto a partir de uma classe.
class Perfil():
   'Classe padrão para perfis de usuários'
   def __init__(self, nome, telefone, empresa):
      self.nome = nome
      self.telefone = telefone
      self.empresa = empresa

class Data(object):
   def __init__(self, dia, mes, ano):
      self.dia = dia
      self.mes = mes
      self.ano = ano

   def imprime(self):
      print '%s/%s/%s' % (self.dia, self.mes, self.ano)

---
>>> from models import Data
>>> d = Data(21,11,2007)
>>> d.imprime()
21/11/2007



Um pouco mais sobre classes: old style X new style
https://cursos.alura.com.br/course/introducao-ao-python/task/7013

Aprendemos a declarar classes em Python garantindo assim que todos os nossos perfis tenham a mesma estrutura. Inclusive aprendemos a criar métodos e entendemos como o Python lida com atributos privados.
Porém, há duas maneiras de declararmos classes em Python. A primeira, chamada old style é a que utilizamos. Mas qual a razão de terem criado uma segunda forma? Para entendermos isso mais facilmente, faremos um teste. Podemos perguntar para a instância de uma classe qual é seu tipo. Porém, há duas maneiras de fazer isso. A primeira é através da função type(), e a segunda é através da propriedade __class__, da própria instância:

>>> perfil = Perfil('Flávio Almeida', 'não informado', 'Caelum')
>>> type(perfil)
<type 'instance'>
>>> perfil.__class__
<class models.Perfil at 0x10f3b4870>
Hm, o resultado da função type() é instance, o que nos informa muito pouco sobre qual o tipo do objeto. Porém, o atributo __class__ nos diz exatamente seu tipo. Essa discrepância foi um dos motivos para o novo estilo de declaração de classes, o new style:

# -*- coding: UTF-8 -*-
class Perfil(object):
   'Classe padrão para perfis de usuários'
   def __init__(self, nome, telefone, empresa):
      self.nome = nome
      self.telefone = telefone
      self.empresa = empresa

   def imprimir(self):
      print "Nome : %s, Telefone: %s, Empresa %s" % (self.nome, self.telefone, self.empresa)   

Repare que o nome da classe agora recebe um parâmetro, um object. Pronto, estamos no novo estilo de declaração de variáveis do Python, fácil assim? Você deve estar se perguntando o que ganhamos com uma alteração tão ínfima como essa, certo? Vamos recarregar o arquivo .py e realizar o mesmo teste que fizemos antes:

>>> perfil = Perfil('Flávio Almeida', 'não informado', 'Caelum')
>>> type(perfil)
<class 'models.Perfil'>
>>> perfil.__class__
<class 'models.Perfil'>
Repare que a função type() e a propriedade __class__ retornam agora um mesmo valor, o nome da classe. Esta é apenas uma das diferenças, pois o novo estilo de declaração de classes adiciona novos recursos na linguagem. Veremos alguns deles durante o curso.


Como seria feito a instanciação de um objeto da classe Perfil?
class Perfil():
   'Classe padrão para perfis de usuários'
   def __init__(self, nome, telefone, empresa):
      self.nome = nome
      self.telefone = telefone
      self.empresa = empresa
Diferente de outras linguagens orientadas a objetos a sintaxe do Python para a criação de um objeto é sem a palavra new.
Logo a alternativa correta seria a que indica:Perfil('Fabio Pimentel', '2222-3333', 'Caelum

