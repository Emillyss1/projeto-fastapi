# from sqlalchemy import create_engine, MetaData, Table
#
# # Conectar ao banco .db
# engine = create_engine("sqlite:///banco.db")
#
# # Refletir todas as tabelas existentes
# metadata = MetaData()
# metadata.reflect(bind=engine)
#
# # Mostrar nomes das tabelas
# print(metadata.tables.keys())
#
# # Exemplo: acessar dados de uma tabela
# tabela = Table('usuarios', metadata, autoload_with=engine)
# with engine.connect() as conn:
#     result = conn.execute(tabela.select())
#     for row in result:
#         print(row)
#
#
# # tabela = Table('pedidos', metadata, autoload_with=engine)
# # with engine.connect() as conn:
# #     result = conn.execute(tabela.select())
# #     for row in result:
# #         print(row)
# #
# # tabela = Table('itenspedido', metadata, autoload_with=engine)
# # with engine.connect() as conn:
# #     result = conn.execute(tabela.select())
# #     for row in result:
# #         print(row)
