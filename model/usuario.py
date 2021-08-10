from config import db

class Usuario(db.Model):
    __tablename__ = 'usuarios'
    id      = db.Column(db.Integer, primary_key=True)
    nome    = db.Column(db.String(250))
    email   = db.Column(db.String(128), unique=True)
    senha   = db.Column(db.String(16))

    def __init__(self, nome, email, senha):
        self.nome   = nome
        self.email  = email
        self.senha  = senha

    def __repr__(self):
        return 'Usuario: ' + self.nome + ' | ' + self.email