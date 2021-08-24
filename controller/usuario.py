from typing import Counter
from flask import Flask, render_template, request, Blueprint
from config import db
from model.usuario import Usuario

TEMPLATES = './view'
STATIC = './static'

usuario_blueprint = Blueprint('usuarios', __name__, template_folder=TEMPLATES, static_folder=STATIC)


@usuario_blueprint.route('/cadastrarUsuario', methods=['POST'])
def cadastrarUsuario():
    nome = request.form.get('nome')
    email = request.form.get('email')
    senha = request.form.get('senha')

    usuario = Usuario(nome, email, senha)

    usuarios = Usuario.query.all()
    for u in usuarios:
        if u.email == email:
            return 'Email já cadastrado!'
    db.session.add(usuario)
    db.session.commit()
    return 'Usuario cadastrado!'


@usuario_blueprint.route('/consultarUsuarios')
def consultarUsuarios():
    usuarios = Usuario.query.all()
    return render_template('listarUsuarios.html', usuarios=usuarios)


#@usuario_blueprint.route('/index')
#def contarUsuarios():
#    usuarios = Usuario.query.all()
#    q = Counter(usuarios)
#    return render_template('index.html', quantidade = q)
