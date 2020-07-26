# language:pt

Funcionalidade: Validar os dados do usuário na api https://jsonplaceholder.typicode.com/users
  Eu como um automatizador de testes
  Quero poder realizar uma busca de usuários em uma api
  Para que seja possível validar o id, nome, username e email do usuário

  Cenário: Validar os dados do usuário
    Dado que realizo uma requisicao na api de usuários
    Quando obter a resposta com sucesso e o status code ok
    Então Validar os dados do usuario
