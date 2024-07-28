from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.sql.schema import Column
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine('sqlite:///banco.db', echo=True)
Base = declarative_base()

class Pessoas(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True)
    nome = Column(String(100))
    idade = Column(Integer)
    endereco = Column(String(100))
    contato = Column(String(15))
    
class Veiculos(Base):
    __tablename__ = 'veiculos'
    id = Column(Integer, primary_key=True)
    nome = Column(String(100))
    marca = Column(String(100))
    capacidade_tanque = Column(Integer)
    cor = Column(String(10))
    ano_fabricacao = Column(Integer)
 

Session = sessionmaker(bind=engine)
session = Session()


# consuntar todos os item mais tenho que muda id pelo o que eu quero ver
#pessoas = session.query(Pessoas).all()
#for a in pessoas:
#   print(a.id)

#consultarr usuarios pelo o nome
# consultar = str(input('digite o nome do user:'))
# pessoa = session.query(Pessoas).filter_by(nome=consultar).first()
# if pessoa:
#     print(f'Idade da {consultar} {pessoa.idade}')
# else:
#     print(f'{consultar}não encontrada.')

# pessoa = session.query(Pessoas).filter(Pessoas.idade>20)
# for a in pessoa:
#     print(a.idade)
