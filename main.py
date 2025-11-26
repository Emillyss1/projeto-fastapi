from  fastapi import FastAPI
from passlib.context import CryptContext
from dotenv import load_dotenv
from fastapi.security import OAuth2PasswordBearer
import os

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))

bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_schema = OAuth2PasswordBearer(tokenUrl="auth/login-form")

#Para executar, digitar: uvicorn main:app --reload

app = FastAPI()

print(">>>IMPORTANDO ROTAS")
from auth_routes import auth_router
print(">>>ROTAS DE AUTENTICACAO IMPORTADAS COM SUCESSO")
from order_routes import order_router
print(">>>ROTAS DE PEDIDO IMPORTADAS COM SUCESSO")

app.include_router(auth_router)
app.include_router(order_router)
print("API configurada e pronta")
