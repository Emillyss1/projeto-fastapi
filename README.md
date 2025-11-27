# 🍕 Projeto FastApi - Simulação de Serviço de Delivery

API de back-end desenvolvida com **FastAPI** e **SQLAlchemy** (usando Alembic para migrações) para simular o ciclo de vida de um serviço de delivery. A aplicação inclui funcionalidades como autenticação de usuários, gerenciamento de pedidos e catálogo de produtos.

---

## 🛠️ Pré-requisitos

Para executar este projeto localmente, você precisará ter instalado:

* **Python 3.10** ou versão superior.
* **pip** (gerenciador de pacotes do Python).

## ⚙️ Instalação e Configuração

Siga os passos abaixo para configurar o ambiente de desenvolvimento e instalar as dependências.

### 1. Clonar o Repositório

```bash
# Navegue até a pasta onde deseja salvar o projeto
git clone [https://github.com/Emillyss1/projeto_fastapi.git](https://github.com/Emillyss1/projeto_fastapi.git)
cd projeto-fastapi

2. Criar e Ativar o Ambiente Virtual
É essencial usar um ambiente virtual para isolar as dependências do projeto.

# Cria o ambiente virtual (.venv)
python -m venv .venv

Para ativar o ambiente:Sistema OperacionalComando de AtivaçãoWindows (CMD/PowerShell).\.venv\Scripts\activateLinux/macOSsource ./.venv/bin/activate

▶️ Executando a API
1. Aplicar Migrações do Banco de Dados
Este projeto utiliza Alembic para gerenciar o esquema do banco de dados (seu arquivo banco.db). Certifique-se de que o banco está atualizado:

alembic upgrade head

2. Iniciar o Servidor
Inicie o servidor Uvicorn para rodar a aplicação FastAPI:

uvicorn main:app --reload

📖 Documentação da API
O FastAPI gera documentação interativa automaticamente. Use-a para testar os endpoints da API:

Swagger UI: http://127.0.0.1:8000/docs

Redoc: http://127.0.0.1:8000/redoc


