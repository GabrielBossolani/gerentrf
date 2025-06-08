from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
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

@app.route('/editar/<titulo>', methods=['GET', 'POST'])
def editar(titulo):
    tarefa = next((t for t in tarefas if t['titulo'] == titulo), None)
    if not tarefa:
        return redirect(url_for('index'))
    if request.method == 'POST':
        tarefa['titulo'] = request.form['titulo']
        tarefa['descricao'] = request.form['descricao']
        return redirect(url_for('index'))
    return render_template('editar_tarefa.html', tarefa=tarefa)

@app.route('/excluir/<titulo>')
def excluir(titulo):
    global tarefas
    tarefas = [t for t in tarefas if t['titulo'] != titulo]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
