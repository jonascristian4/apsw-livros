from typing import Counter
from flask import Flask, render_template, request, Blueprint
from config import db
from model.usuario import Usuario

TEMPLATES = './view'
STATIC = './static'

usuario_blueprint = Blueprint('usuarios', __name__, static_url_path='',  template_folder=TEMPLATES, static_folder=STATIC)


@usuario_blueprint.route('/cadastrarUsuario', methods=['POST'])
def cadastrarUsuario():
    nome = request.form.get('nome')
    email = request.form.get('email')
    senha = request.form.get('senha')

    usuario = Usuario(nome, email, senha)

    usuarios = Usuario.query.all()
    for u in usuarios:
        if u.email == email:
            return 'Email já cadastrado!, tente novamente com outro endereço de email.'
    db.session.add(usuario)
    db.session.commit()
    return render_template('index.html')


@usuario_blueprint.route('/consultarUsuarios')
def consultarUsuarios():
    usuarios = Usuario.query.all()
    return render_template('index.html', usuarios=usuarios)

@usuario_blueprint.route('/usuarios/form')
def adicionarUsuarios():
    usuarios = Usuario.query.all()
    return render_template('cadastrarUsuarios.html')