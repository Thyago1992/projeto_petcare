# 🐾 PetCare - Atendimento

Sistema web para gerenciamento de atendimentos de um pet shop, desenvolvido com Django 6.1 e Python.

## 🎯 Sobre o Projeto

Aplicação completa para o dia a dia de um pet shop que permite:

- ✅ Cadastro e gerenciamento de tutores
- ✅ Cadastro de pets vinculados a tutores
- ✅ Catálogo de serviços com preço
- ✅ Registro de atendimentos (pet + serviço + data)
- ✅ Painel com os atendimentos do dia e valor total faturado
- ✅ Autenticação de usuários (login, cadastro e logout)

## ✨ Funcionalidades

### Painel

- ✅ Lista apenas os atendimentos do dia atual
- ✅ Exibe a quantidade de atendimentos e a soma dos valores cobrados
- ✅ Mostra hora, tutor, pet, serviço e valor de cada atendimento

### Tutores

- ✅ Cadastro com nome e telefone
- ✅ Edição dos dados
- ✅ Listagem ordenada por nome

### Pets

- ✅ Cadastro de pets vinculados a um tutor existente
- ✅ Definição de nome e espécie
- ✅ Listagem com o nome do tutor

### Serviços

- ✅ Cadastro com nome e preço
- ✅ Edição dos dados

### Atendimentos

- ✅ Registro de atendimento com pet, serviço, data e hora
- ✅ Preço cobrado opcional: se ficar em branco, usa automaticamente o preço do serviço
- ✅ Listagem do mais recente para o mais antigo

### Interface

- ✅ Tema escuro com layout responsivo
- ✅ Menu com destaque da página atual
- ✅ Saudação ao usuário logado e botão de sair no cabeçalho

## 🛠 Tecnologias Utilizadas

### Backend

- ✅ Python 3.12+
- ✅ Django 6.1
- ✅ Class-Based Views (ListView, CreateView, UpdateView)
- ✅ Django ORM
- ✅ Django Forms (ModelForm)
- ✅ Django Auth — autenticação de usuários
- ✅ Django Admin

### Frontend

- ✅ Django Templates
- ✅ HTML5
- ✅ CSS3 (variáveis CSS, Flexbox e Grid)

### Banco de Dados

- ✅ SQLite

### Testes

- ✅ Django TestCase
- ✅ Django Test Client

## 🏗 Arquitetura

O projeto segue o padrão MTV (Model-Template-View) do Django, dividido em dois apps:

```
projeto_petcare
├── setup/                    # Configurações do projeto (settings, urls, wsgi)
├── servico/                  # App do catálogo de serviços (model Servico)
└── atendimento/              # App principal
    ├── migrations/           # Migrações do banco de dados
    ├── static/atendimento/   # Arquivos estáticos (CSS)
    ├── templates/atendimento/# Templates HTML
    ├── admin.py              # Registro no Django Admin
    ├── forms.py              # Formulários (ModelForm)
    ├── models.py             # Models Tutor, Pet e Atendimento
    ├── tests.py              # Testes automatizados
    ├── urls.py               # Rotas da aplicação
    └── views.py              # Views e regras de exibição
```

## 🚀 Instalação

### Pré-requisitos

- Python 3.12+
- pip
- Git

### 1. Clone o repositório

```bash
git clone https://github.com/Thyago1992/projeto_petcare.git
cd projeto_petcare
```

### 2. Crie e ative o ambiente virtual

```bash
python -m venv venv
```

Windows (PowerShell):

```bash
venv\Scripts\activate
```

Linux / macOS:

```bash
source venv/bin/activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Crie o banco de dados

```bash
python manage.py migrate
```

### 5. Crie um usuário administrador (opcional)

```bash
python manage.py createsuperuser
```

### 6. Execute o servidor

```bash
python manage.py runserver
```

A aplicação estará disponível em: `http://127.0.0.1:8000`

## ⚙ Configuração

As configurações sensíveis podem ser definidas por variáveis de ambiente:

| Variável            | Padrão                         | Descrição                           |
|---------------------|--------------------------------|-------------------------------------|
| `DJANGO_SECRET_KEY` | `chave-so-para-desenvolvimento`| Chave secreta do Django             |
| `DJANGO_DEBUG`      | `True`                         | Ativa/desativa o modo de depuração  |

Outras configurações relevantes em `setup/settings.py`:

```python
LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Recife'

LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = 'painel'
LOGOUT_REDIRECT_URL = 'login'
```

> ⚠ Em produção, defina uma `DJANGO_SECRET_KEY` própria e use `DJANGO_DEBUG=False`.

## 🔌 Rotas da Aplicação

Todas as rotas, exceto login e cadastro, exigem usuário autenticado. Quem não estiver logado é redirecionado para `/login/`.

### Autenticação

| Rota          | Método    | Descrição                       |
|---------------|-----------|---------------------------------|
| `/login/`     | GET, POST | Tela de login                   |
| `/cadastro/`  | GET, POST | Cadastro de novo usuário        |
| `/sair/`      | POST      | Encerra a sessão                |

### Painel

| Rota        | Método | Descrição                           |
|-------------|--------|-------------------------------------|
| `/`         | GET    | Painel com os atendimentos do dia   |
| `/painel/`  | GET    | Painel com os atendimentos do dia   |

### Tutores

| Rota                       | Método    | Descrição          |
|----------------------------|-----------|--------------------|
| `/tutores/`                | GET       | Lista os tutores   |
| `/tutores/novo/`           | GET, POST | Cadastra um tutor  |
| `/tutores/{id}/editar/`    | GET, POST | Edita um tutor     |

### Pets

| Rota           | Método    | Descrição        |
|----------------|-----------|------------------|
| `/pets/`       | GET       | Lista os pets    |
| `/pets/novo/`  | GET, POST | Cadastra um pet  |

### Serviços

| Rota                        | Método    | Descrição            |
|-----------------------------|-----------|----------------------|
| `/catalogo/`                | GET       | Lista os serviços    |
| `/servicos/novo/`           | GET, POST | Cadastra um serviço  |
| `/servicos/{id}/editar/`    | GET, POST | Edita um serviço     |

### Atendimentos

| Rota                   | Método    | Descrição                  |
|------------------------|-----------|----------------------------|
| `/atendimentos/novo/`  | GET, POST | Registra um atendimento    |

### Administração

| Rota       | Descrição                                            |
|------------|------------------------------------------------------|
| `/admin/`  | Django Admin com Tutor, Pet, Serviço e Atendimento   |

## 🗄 Estrutura do Banco de Dados

### Tabela: servico

| Campo  | Tipo          | Restrições          |
|--------|---------------|---------------------|
| id     | BIGINT        | PK, AUTO_INCREMENT  |
| nome   | VARCHAR(100)  | NOT NULL            |
| preco  | DECIMAL(6,2)  | NOT NULL            |

### Tabela: tutor

| Campo     | Tipo          | Restrições          |
|-----------|---------------|---------------------|
| id        | BIGINT        | PK, AUTO_INCREMENT  |
| nome      | VARCHAR(100)  | NOT NULL            |
| telefone  | VARCHAR(20)   | NOT NULL            |

### Tabela: pet

| Campo     | Tipo          | Restrições                         |
|-----------|---------------|------------------------------------|
| id        | BIGINT        | PK, AUTO_INCREMENT                 |
| nome      | VARCHAR(100)  | NOT NULL                           |
| especie   | VARCHAR(50)   | NOT NULL                           |
| tutor_id  | BIGINT        | FK (tutor.id), NOT NULL, PROTECT   |

### Tabela: atendimento

| Campo          | Tipo          | Restrições                           |
|----------------|---------------|--------------------------------------|
| id             | BIGINT        | PK, AUTO_INCREMENT                   |
| data           | DATETIME      | NOT NULL                             |
| preco_cobrado  | DECIMAL(8,2)  | NOT NULL (preenchido automaticamente)|
| pet_id         | BIGINT        | FK (pet.id), NOT NULL, PROTECT       |
| servico_id     | BIGINT        | FK (servico.id), NOT NULL, PROTECT   |

### Relacionamentos

```
pet.tutor_id           → tutor.id    (N:1)
atendimento.pet_id     → pet.id      (N:1)
atendimento.servico_id → servico.id  (N:1)
```

## ✔ Validações e Regras de Negócio

### Tutores

- ✅ Nome é obrigatório
- ✅ Telefone é obrigatório
- ✅ Não é possível excluir um tutor que possui pets cadastrados

### Pets

- ✅ Nome e espécie são obrigatórios
- ✅ Tutor vinculado deve existir no sistema
- ✅ Não é possível excluir um pet que possui atendimentos

### Serviços

- ✅ Nome e preço são obrigatórios
- ✅ Não é possível excluir um serviço que possui atendimentos

### Atendimentos

- ✅ Pet, serviço e data são obrigatórios
- ✅ Se o preço cobrado não for informado, assume o preço atual do serviço
- ✅ O preço fica gravado no atendimento, então mudanças futuras no preço do serviço não alteram o histórico

### Acesso

- ✅ Todas as páginas internas exigem login
- ✅ Usuário já logado que acessa a tela de login é redirecionado ao painel
- ✅ Senhas validadas pelos validadores padrão do Django

## 🧪 Testes

O projeto possui 19 testes automatizados cobrindo models, autenticação, painel e cadastros, com cenários de sucesso e de erro.

### Executar os testes

```bash
python manage.py test
```

O Django cria um banco temporário para os testes, então os dados do `db.sqlite3` não são alterados.

### Cobertura

| Grupo                  | Cenários testados                                                                                       |
|------------------------|---------------------------------------------------------------------------------------------------------|
| `AtendimentoModelTests`| preço automático do serviço, preço informado mantido, representação em texto, proteção ao excluir tutor |
| `AcessoTests`          | páginas exigem login, páginas abrem logado, login, logout, cadastro de usuário                          |
| `PainelTests`          | painel vazio, filtro por atendimentos de hoje, soma do valor total                                      |
| `CadastrosTests`       | criação de tutor, pet, serviço e atendimento, edição de tutor, tutor sem nome não é salvo               |

## 📝 Licença

Este projeto foi desenvolvido para fins educacionais.

## 👤 Autor

Desenvolvido por **Thyago Antonio Sampaio Valadares** como projeto de portfólio.

[![GitHub](https://img.shields.io/badge/GitHub-Thyago1992-181717?style=flat&logo=github)](https://github.com/Thyago1992)
