![Banner_project](readme-images/banner-project.png)

## TO DO LIST API - É uma API REST criada para um Sistema de Gerenciamento de Tarefas.  
![Concluído](https://img.shields.io/static/v1?label=STATUS&message=CONCLUÍDO&color=GREEN&style=for-the-badge)


### Descrição
Essa API ajuda no gerenciamento de uma lista de tarefas (to-do list). A API permite que os usuários criem, atualizem, excluam e visualizem tarefas. Cada tarefa possue um Titulo, uma Descrição, um Prazo (data planejada para conclusão), uma Data da Conclusão, e uma Situação que pode ser (nova, em andamento, concluída ou cancelada).

- ### Tecnologias Utilizadas.
  ![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
  ![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray)
  ![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)

### Passos Iniciais.
- ### O que é uma API ?
  API é um termo para designar uma interface de comunicação que um sistema oferece para que outros acessem suas funções, dados e recursos sem que o software ou plataforma externa precise saber como eles foram implementados. Trata-se de um conjunto de rotinas e padrões muito utilizados na web para facilitar a integração entre diferentes sites e aplicativos.

- ### Como Funciona uma API RESTFUL ?
  Uma API RESTful funciona através da manipulação de recursos e representações. Essas representações são trocadas entre os usuários e o servidor através de uma interface padronizada e de um protocolo de comunicação específico — geralmente o HTTP. Assim, quando um usuário deseja usar uma funcionalidade da aplicação, seu dispositivo envia uma solicitação via HTTP ao servidor. O servidor localiza o recurso e comunica a representação do estado dele na resposta ao usuário através do mesmo protocolo. E são essas representações que podem ser feitas em diversos formatos.

  Caso ainda tenha duvidas de como uma API RESTFUL funciona, recomendo a leitura do site: (https://www.hostinger.com.br/tutoriais/api-restful)

### Como Instalar o Projeto.
- #### Clone esse Reposítorio em sua maquina, isso pode ser feito via git com o comando:
  ``` git clone https://github.com/kaiquevieirasoares/api-to-do-list.git```


  ou diretamente do Github:


  ![Captura de tela 2024-05-15 150552](https://github.com/kaiquevieirasoares/api-to-do-list/assets/123115955/25e31f9f-6e82-4691-b8ea-daef2f1e7c39)

- ### Com o projeto em mãos você terá acesso a essa estrutura de codigo:
  ![Diretorio do projeto](api-to-do-list/readme-images/Configuração do diretório.png)
  
  



| Tecnologia | Versão | Comando para instalar |
|:----------|------|---------------------|
|NodeJS| 12.18.2| ``` brew install node ``` |
|Yarn  |  1.17.3 | ```npm install -g yarn``` |
|Expo  |  3.23.1 |  ```yarn add global expo-cli```|




### Como Utilizar a API ?
Primeiramente vamos entender o que significa os termos técnicos da aplicação.

- ### END-POINTS:
  O URL do endpoint é a localização exata do recurso solicitado ao servidor de API, permitindo que dois programas interajam. No endpoint, a API acessará os recursos necessários de um servidor para executar uma tarefa especificada, como recuperar determinados dados ou informações. As APIs enviam solicitações para acessar dados de um servidor com uma resposta enviada de volta. O local da resposta é o endpoint.
  
  - Nossa API possui 5  END_POINTS, ou seja, 5 endereços com diferentes funções de requisição, sendo elas:
  
  









