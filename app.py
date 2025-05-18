from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Lista de tarefas simulando um banco de dados em memória
tarefas = []

@app.route('/')
def index():
    return render_template('index.html', tarefas=tarefas)

@app.route('/criar', methods=['GET', 'POST'])
def criar():
    if request.method == 'POST':
        titulo = request.form['titulo']
        descricao = request.form['descricao']
        tarefas.append({'titulo': titulo, 'descricao': descricao})
        return redirect(url_for('index'))
    return render_template('criar_tarefa.html')

@app.route('/editar/<int:indice>', methods=['GET', 'POST'])
def editar(indice):
    if request.method == 'POST':
        tarefas[indice]['titulo'] = request.form['titulo']
        tarefas[indice]['descricao'] = request.form['descricao']
        return redirect(url_for('index'))
    return render_template('editar_tarefa.html', indice=indice, tarefa=tarefas[indice])

@app.route('/excluir/<int:indice>')
def excluir(indice):
    tarefas.pop(indice)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)