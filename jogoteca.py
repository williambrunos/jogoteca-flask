from flask import Flask, render_template, request, redirect, session, flash, url_for

app = Flask(__name__)
app.secret_key = 'vingardionleviosa'


class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console


jogo1 = Jogo('Tetris', 'Puzzle', 'Atari')
jogo2 = Jogo('God of War', 'Rack n Slash', 'ps2')
jogo3 = Jogo('Mortal Kombat', 'Luta', 'PS5')
jogos = [jogo1, jogo2, jogo3]


@app.route('/')
def index():
    return render_template('lista.html', titulo='Jogos', jogos=jogos)


@app.route('/novo')
def novo_jogo():
    if not session.get("usuario_logado", ""):
        return redirect(url_for('login', proximo=url_for('novo_jogo')))
    return render_template('novo.html', titulo='Novo Jogo')


@app.route('/criar', methods=['POST'])
def criar_jogo():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']

    jogo = Jogo(nome, categoria, console)
    jogos.append(jogo)

    return redirect(url_for('index'))


@app.route('/login')
def login():
    proximo = request.args.get('proximo')
    return render_template('login.html', proximo=proximo)


@app.route('/autenticar', methods=['POST'])
def autenticar():
    if request.form['senha'] == 'alohomora':
        session['usuario_logado'] = request.form['nome']
        flash("Usuário logado com sucesso!")

        proxima_pagina = request.form['proximo']
        return redirect(proxima_pagina)
    else:
        flash('Usuário não logado!')
        return redirect(url_for('login'))


@app.route('/logout')
def logout():
    if session.get('usuario_logado', ''):
        session['usuario_logado'] = None

    flash("Logout feito com sucesso!")

    return redirect(url_for('index'))


app.run(debug=True)
