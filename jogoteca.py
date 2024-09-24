from flask import Flask, render_template, request, redirect

app = Flask(__name__)


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
    return render_template('novo.html', titulo='Novo Jogo')


# TODO: Transformar esta rota /criar em middleware para que não fique carregando a lista apenas em /criar,
#  deve ser ilustrada também no /
@app.route('/criar', methods=['POST'])
def criar_jogo():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']

    jogo = Jogo(nome, categoria, console)
    jogos.append(jogo)

    return redirect('/')


app.run(debug=True)
