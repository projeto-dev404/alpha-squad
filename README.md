# <div align="center"><a href="https://discord.gg/sQYnuvF8uu"><img src="https://media.licdn.com/dms/image/D4D0BAQHE8bsrmJVrYg/company-logo_200_200/0/1695757217802?e=1704931200&v=beta&t=Lz0CsYmhEB8P4C1DU7pFW0wYzJkpd7gwP2tX8LwaWpo" alt="logo" width="180"/></a></div>

# CodeMentor - Backend

Este repositório contém o código-fonte do backend para a aplicação de gerenciamento de squads, stacks e integrantes do projeto de mentoria CodeMentor. A aplicação foi desenvolvida utilizando o framework Django e o Django Rest Framework. Até o momento, a aplicação oferece funcionalidades de cadastro, login, logout e obtenção de dados de usuários específicos.

## Ferramentas Utilizadas

- Django
- Django Rest Framework
- PostgreSQL
- Docker

## Configuração e Execução

O Dockerfile neste repositório é configurado para construir uma imagem com as dependências necessárias para executar o projeto. Você pode criar a imagem e iniciar os contêineres com os seguintes comandos:

```bash
docker-compose build
docker-compose up
```

Certifique-se de definir as variáveis de ambiente adequadas no arquivo .env de acordo com o .env-example antes de executar o contêiner.

### Observações

- Esta é uma API inicial, que será aprimorada no futuro para adequar as necessidades do projeto.

## Endpoints da API
### Criar um usuário

- **Método:** POST
- **Endpoint:** /auth/users
- **Corpo da solicitação (JSON):**
  ```json
  {
      "name": "Novo Usuário",
      "email": "usuario@example.com",
      "password": "1234567890"
  }
  ```
  
- **Resposta (JSON):**
  ```json
  {
      "name": "Novo Usuário",
      "email": "usuario@example.com",
      "id": "sa4f89-4894-asf8-6548-54fsa894f87d"
  }
  ```

### Obter os dados do usuário logado atualmente

- **Método:** GET
- **Endpoint:** /auth/users/me
- **Headers:**

| Chave         | Valor                  |
|---------------|------------------------|
| Authorization | token "auth_token"     |


- **Resposta (JSON):**
```json
{
   "name": "Nome",
   "id": "sa4f89-4894-asf8-6548-54fsa894f87d",
   "email": "usuario@example.com"
}
```

### Obter dados do usuário especificado

- **Método:** GET
- **Endpoint:** /auth/users/:id
- **Headers:**

| Chave         | Valor                  |
|---------------|------------------------|
| Authorization | token "auth_token"     |

- **Resposta (JSON):**
```json
{
   "name": "Nome",
   "id": "sa4f89-4894-asf8-6548-54fsa894f87d",
   "email": "usuario@example.com"
}
```

### Realizar login

- **Método:** POST
- **Endpoint:** /auth/token/login
- **Requisição (JSON):**
```json
{
    "email": "usuario@example.com",
    "password": "1234567890"
}
```

- **Resposta (JSON):**
```json
{
  "HTTP_200_OK",
  "auth_token"
}
```
### Realizar logout

- **Método:** POST
- **Endpoint:** /auth/token/logout
- **Headers:**

| Chave         | Valor                  |
|---------------|------------------------|
| Authorization | token "auth_token"     |

- **Resposta (JSON):**
```json
{
  "HTTP_204_NO_CONTENT"
}
```

## Contribuição

Se você deseja contribuir para este projeto, siga estas etapas:

1. Faça um fork do repositório.

2. Crie uma nova branch para suas alterações:
   ```bash
   git checkout -b minha-feature
   ```
   
3. Faça suas alterações e faça commit delas:
   ```bash
   git commit -m 'Adicione minha feature'
   ```

4. Envie suas alterações para o seu fork:
   ```bash
   git push origin minha-feature
   ```

5. Abra uma solicitação pull para este repositório.