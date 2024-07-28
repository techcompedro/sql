from flask import Flask
from  molde import Pessoas, Veiculos, session
from flask import jsonify

app = Flask(__name__)

@app.route('/usuarios')
def todos_user():
    pessoas = session.query(Pessoas).all()
    if pessoas:
        return jsonify([
            {
                "nome": pessoa.nome,
                "idade": pessoa.idade,
                "endereco": pessoa.endereco,
                "contato": pessoa.contato
            } for pessoa in pessoas
        ])
    else:
        return jsonify({"erro": "Usuário não encontrado"}), 404




@app.route('/usuarios/<nome>')
def buscar_nome(nome):
    pessoa = session.query(Pessoas).filter_by(nome=nome).first()
    if pessoa:
        return jsonify ({
            "idade": pessoa.idade
        })
    else:
        return jsonify({"erro": "Usuário não encontrado"}), 404

@app.route('/usuarios/<nome>/delete')
def delete_nome(nome):
    pessoa = session.query(Pessoas).filter_by(nome=nome).first()
    session.delete(pessoa)
    if pessoa:
        return jsonify ({
            "user": 'deletado'
        })
    else:
        return jsonify({"erro": "Usuário não encontrado"}), 404
        
        

if __name__ == '__main__':
    app.run(debug=True)
