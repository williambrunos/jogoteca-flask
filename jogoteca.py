from flask import Flask, render_template, request, redirect, session, flash

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
        return render_template("/login.html")
    return render_template('novo.html', titulo='Novo Jogo')


@app.route('/criar', methods=['POST'])
def criar_jogo():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']

    jogo = Jogo(nome, categoria, console)
    jogos.append(jogo)

    return redirect('/')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/autenticar', methods=['POST'])
def autenticar():
    if request.form['senha'] == 'alohomora':
        session['usuario_logado'] = request.form['nome']
        flash("Usuário logado com sucesso!")
        return redirect('/')
    else:
        flash('Usuário não logado!')
        return redirect('/login')


@app.route('/logout')
def logout():
    if session.get('usuario_logado', ''):
        session['usuario_logado'] = None

    flash("Logout feito com sucesso!")

    return redirect('/')


app.run(debug=True)
