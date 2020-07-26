# pylint: disable=no-name-in-module
from behave import given, when, then
import requests

@given(u'que realizo uma requisicao na api de usuários')
def requisicao(context):
  response = requests.get('https://jsonplaceholder.typicode.com/users')
  context.response_body = response.json()
  context.status_code = response.status_code

@when(u'obter a resposta com sucesso e o status code ok')
def validar_status_code(context):
  assert context.status_code == 200

@then(u'Validar os dados do usuario')
def validar_retorno_usuarios(context):
  #Bloco para percorrer o array de usuarios e mapear a posicao do usuario com o ID 7, dessa forma, caso a API retorne o usuario em uma posicao diferente de [6] no array o codigo sera dinamico para fazer a validacao assertiva da mesma forma.
  index = 0
  while(index < len(context.response_body)):
    user_id = context.response_body[index]['id']
    if user_id == 7:
      break
    index +=1
  assert context.response_body[index]['id'] == 7
  assert context.response_body[index]['name'] == 'Kurtis Weissnat'
  assert context.response_body[index]['username'] == 'Elwyn.Skiles'
  assert context.response_body[index]['email'] == 'Telly.Hoeger@billy.biz'
