
# Eventex

Sistema de Eventos encomendado pela Morena.

## Índice

- [Como desenvolver](#como-desenvolver)
- [Como fazer o deploy](#como-fazer-o-deploy)

## Como desenvolver

Siga os passos abaixo para configurar o ambiente de desenvolvimento da aplicação:

1. **Clone o repositório**:
   ```bash
   git clone git@github.com:matheuspdf/eventex.git
   cd eventex
   ```

2. **Crie um ambiente virtual** usando o `pipenv` e instale as dependências:
   ```bash
   pipenv install --ignore-pipfile
   ```

3. **Ative o ambiente virtual**:
   ```bash
   pipenv shell
   ```

4. **Configure as variáveis de ambiente** copiando o arquivo de exemplo:
   ```bash
   cp contrib/env-sample .env
   ```

5. **Execute os testes** para garantir que tudo está funcionando corretamente:
   ```bash
   python manage.py test
   ```

6. **Rode as migrações** para configurar o banco de dados:
   ```bash
   python manage.py migrate
   ```

7. **Inicie o servidor**:
   ```bash
   python manage.py runserver
   ```
8. Para criar um super usuário e utilizar o admin do Django
   ```bash
   python manage.py createsuperuser
   ```

Agora você pode acessar o sistema em `http://localhost:8000`.

---

## Como fazer o deploy

Siga estes passos para realizar o deploy da aplicação no **Fly.io**:

1. **Instale o Fly.io CLI**:
   ```bash
   curl -L https://fly.io/install.sh | sh
   ```

2. **Crie uma conta no Fly.io** (se você ainda não tiver):
   ```bash
   fly auth signup
   ```

3. **Faça login** na sua conta Fly.io:
   ```bash
   fly auth login
   ```

4. **Inicialize e configure a aplicação** para Fly.io:
   ```bash
   fly launch
   ```
   - Escolha um nome para a aplicação quando solicitado.
   - Selecione a região desejada.
   - Não crie o banco de dados agora (a menos que precise).

5. **Defina as variáveis de ambiente** na instância Fly.io. Por exemplo:
   ```bash
   flyctl secrets set SECRET_KEY=$(python contrib/secret_gen.py) DEBUG=False
   ```

6. **Faça o deploy da aplicação**:
   ```bash
   flyctl deploy
   ```

---