# Automation-Testing-using-BDD-and-Behave-Python-
Automação de Teste utilizando BDD e Behave, validações na API https://jsonplaceholder.typicode.com/users 

Tutorial para execução do teste no windows:

No Windows abrir o terminal e digitar o seguinte comando para instalar o PIP (Gerenciador de pacotes de softwares):
$ curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py

Instalar a versão mais atual do Python no link https://www.python.org/downloads/ e após a instalação do Python, inserir o seguinte comando no terminal para finalizar a instalação do pip:
$ python get-pip.py

Istalar o behave com o pip, inserir o seguinte comando no terminal:
$pip install behave

Se for de sua prefência, também é possível instalar o behave usando o github repository:
$ pip install git+https://github.com/behave/behave

Criar uma pasta em uma área no computador de sua preferencia e clonar o projeto:
$ git clone https://github.com/NicolasYoshioka07/Automation-Testing-using-BDD-and-Behave-Python-.git

Após clonar o projeto entrar no terminal e percorrer até o diretório de features do projeto, exemplo em que clonei o projeto em uma pasta chamada "automation" no desktop:
$ cd /c/Users/{SeuUsuarioAqui}/desktop/automation/Automation-Testing-using-BDD-and-Behave-Python-/features/

Instalar a dependencia necessária para a execução do cenário de teste
$ pip install requests

Executar o cenário de teste com o simples comando "behave"
$ behave



Tutorial para execução do teste no macbook:

Instalar o xCode Command Line Tools via terminal 
$ xcode-select --install

Instalar o Homebrew no terminal
$ ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

Instalar o Python3 via homebrew:
$ brew install python3

Instalar o PIP(Gerenciador de pacotes de software) ou atualiza-lo:
$ sudo easy_install pip

Instalar o behave via terminal:
$ pip install behave

Criar uma pasta em uma área no computador de sua preferencia e clonar o projeto:
Git clone https://github.com/NicolasYoshioka07/Automation-Testing-using-BDD-and-Behave-Python-.git

Após clonar o projeto entrar no terminal e percorrer até o diretório de features do projeto, exemplo em que clonei o projeto em uma pasta chamada “automation” no desktop:
$ cd /Users/{SeuUsuarioAqui}/desktop/automation/Automation-Testing-using-BDD-and-Behave-Python-/features

Instalar a dependência necessária para a execução do cenário de teste:
$ pip install requests

Executar o cenário de teste com o simples comando “behave”
$ behave
