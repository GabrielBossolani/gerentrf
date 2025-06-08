from flask import Flask, render_template, request, redirect, url_for
from models import db, Tarefa

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tarefas.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# Criar banco de dados com as tabelas
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    tarefas = Tarefa.query.all()
    return render_template('index.html', tarefas=tarefas)

@app.route('/criar', methods=['GET', 'POST'])
def criar():
    if request.method == 'POST':
        nova_tarefa = Tarefa(
            titulo=request.form['titulo'],
            descricao=request.form['descricao']
        )
        db.session.add(nova_tarefa)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('criar_tarefa.html')

@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    tarefa = Tarefa.query.get_or_404(id)
    if request.method == 'POST':
        tarefa.titulo = request.form['titulo']
        tarefa.descricao = request.form['descricao']
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('editar_tarefa.html', tarefa=tarefa)

@app.route('/excluir/<int:id>')
def excluir(id):
    tarefa = Tarefa.query.get_or_404(id)
    db.session.delete(tarefa)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
