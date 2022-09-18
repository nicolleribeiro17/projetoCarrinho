<h1 align="center">projetoCarrinho</h1> 

## Objetivos: 
Desenvolvimento de um carrinho de compras como projeto do bootcamp LuizaCode utilizando a linguagem Python e o framework FastAPI.

Tabela de conteúdos
=================
<!--ts-->
   * ## Sobre
      * Primeira etapa do projeto - consiste na criação das persistência, das classes e das rotas necessárias para ao desenvolvimento do projeto e para a comunicação da API Rest.  A elaboração dessa primeira fase não possui regras e nem aplicações de bancos de dados, portanto o projeto será aprimorado ao longo do bootcamp. 

   * ## Como utilizar

### Configurações iniciais
    
Antes de começar, você deve ter instalado em sua máquina as seguintes ferramentas: [Git](https://git-scm.com), [Python](https://python.org.br/instalacao-windows/)

Além disto é bom ter um editor para trabalhar com o código como [VSCode](https://code.visualstudio.com/)

Para a visualização das requisições web diretamente no VSCode, indico instalar a extensão [RESTClient](https://marketplace.visualstudio.com/items?itemName=humao.rest-client)

### 🎲 Rodando o Back End (servidor)
    # Clone este repositório
    $ git clone https://github.com/nicolleribeiro17/projetoCarrinho.git
    
    # Acesse a pasta do projeto no terminal do visual code
    
    # Ative a máquina virtual
    $ .\ambientevirtual\Scripts\activate
    
    # Acesse o repositório projeto_testado onde estará o código revisado
    $ cd projeto_testado
    
    # Execute o comando
    $ uvicorn rotas:app --reload
    
    # O servidor iniciára na porta 8000 - acesse <http://localhost:8000/>
    
    # Para ver o funcionamento do código, acessar o arquivo casos_teste.http. 
    # Neste arquivo irá conter os dados de entrada que irão ser utilizados para teste.
    # Para testar as requisições feitas nas rotas foi acessado o caminho .<http://localhost:8000/docs>
    
<!--te-->

