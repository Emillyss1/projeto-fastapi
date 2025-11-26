from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from dependencies import pegar_sessao, verificar_token
from schemas import PedidoSchema, ItemPedidoSchema
from models import Pedido, Usuario, ItensPedido

order_router = APIRouter(prefix="/pedidos", tags=["pedidos"], dependencies=[Depends(verificar_token)])

@order_router.get("/lista")
async def pedidos():
    """
        Essa é a rota padrão de pedidos
        """
    return {"mensagem": "Você acessou a rota de pedidos"}

@order_router.post("/pedido")
async def criar_pedido(pedido_schema: PedidoSchema, session: Session = Depends(pegar_sessao)):
    novo_pedido = Pedido(usuario=pedido_schema.usuario)
    session.add(novo_pedido)
    session.commit()
    return {"mensagem": f"Pedido criado com sucesso. ID do pedido: {novo_pedido.id}"}

@order_router.post("/pedido/cancelar/{id_pedido}")
async def cancelar_pedido(id_pedido: int, session: Session = Depends(pegar_sessao), usuario: Usuario = Depends(verificar_token)):
    pedido = session.query(Pedido).filter(Pedido.id==id_pedido).first()
    if not pedido:
        raise HTTPException(status_code=400, detail="Pedido não encontrado")
    if not usuario.admin and usuario.id != pedido.usuario:
        raise HTTPException(status_code=401, detail="Você não possui autorização para fazer esta modificação")
    pedido.status = "CANCELADO"
    session.commit()
    return {
        "mensagem": f"Pedido {pedido.id} cancelado consucesso!",
        "Pedido": pedido
    }

@order_router.get("/listar")
async def listar_pedidos(session: Session = Depends(pegar_sessao), usuario: Usuario = Depends(verificar_token)):
    if not usuario.admin:
        raise HTTPException(status_code=401, detail="Você não possui autorização para realizar esta operação")
    else:
        pedidos = session.query(Pedido).all()
    return {
        "Pedidos": pedidos
    }

@order_router.post("pedido/adicionar-item/{id_pedido")
async def adicionar_item(id_pedido: int,
                         item_pedido_schema: ItemPedidoSchema,
                         session: Session = Depends(pegar_sessao),
                         usuario: Usuario = Depends(verificar_token)):
    pedido = session.query(Pedido).filter(Pedido.id==id_pedido).first()
    if not pedido:
        raise HTTPException(status_code=400, detail="Pedido inexistente")
    if not usuario.admin and usuario.id != pedido.usuario:
        raise HTTPException(status_code=401, detail="Você não possui autorização para realizar esta operação")
    itens_pedido = ItensPedido(item_pedido_schema.quantidade, item_pedido_schema.sabor,
                               item_pedido_schema.tamanho, item_pedido_schema.preco_unitario), id_pedido
    pedido.calcular_preco()
    session.add(itens_pedido)
    session.commit()
    return {
        "mensagem": "Item criado com sucesso",
        "item-id": itens_pedido.id,
        "preco_pedido": pedido.preco
    }

