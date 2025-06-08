from flask import Flask, rendertemplate, request, redirect, urlfor

from flask_sqlalchemy import SQLAlchemy

app = Flask(name)

app.config['SQLALCHEMYDATABASEURI'] = 'sqlite:///tarefas.db'

app.config['SQLALCHEMYTRACKMODIFICATIONS'] = False

db = SQLAlchemy(app)

class Tarefa(db.Model):

id = db.Column(db.Integer, primary_key=True)
titulo = db.Column(db.String(100), nullable=False)
descricao = db.Column(db.String(500), nullable=False)
def __repr__(self):
    return f'<Tarefa {self.titulo}>'
@app.beforefirstrequest

def cria_bd():

db.create_all()
@app.route('/')

def index():

tarefas = Tarefa.query.all()
return render_template('index.html', tarefas=tarefas)
@app.route('/criar', methods=['GET', 'POST'])

def criar():

if request.method == 'POST':
    titulo = request.form['titulo']
    descricao = request.form['descricao']
    nova_tarefa = Tarefa(titulo=titulo, descricao=descricao)
    db.session.add(nova_tarefa)
    db.session.commit()
    return redirect(url_for('index'))
return render_template('criar_tarefa.html')
@app.route('/editar/', methods=['GET', 'POST'])

def editar(id):

tarefa = Tarefa.query.get_or_404(id)
if request.method == 'POST':
    tarefa.titulo = request.form['titulo']
    tarefa.descricao = request.form['descricao']
    db.session.commit()
    return redirect(url_for('index'))
return render_template('editar_tarefa.html', tarefa=tarefa)
@app.route('/excluir/')

def excluir(id):

tarefa = Tarefa.query.get_or_404(id)
db.session.delete(tarefa)
db.session.commit()
return redirect(url_for('index'))
if name == 'main':

app.run(debug=True)
