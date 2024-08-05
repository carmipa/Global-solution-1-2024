from flask import Flask, render_template, request, redirect, url_for
from colorama import Fore, Style
from datetime import datetime

app = Flask(__name__)

# Listas globais
alunos = []
escolas = []
materiais = []
jogos = []

# --- Funções de Cadastro ---

def cadastrar_alunos():
    # Cadastra um novo aluno.
    aluno = {}
    aluno["nome"] = request.form.get("nome")
    aluno["sobrenome"] = request.form.get("sobrenome")
    aluno["data_nascimento"] = request.form.get("data_nascimento")
    aluno["telefone"] = request.form.get("telefone")
    aluno["email"] = request.form.get("email")
    aluno["contato"] = request.form.get("contato")
    aluno["observacao"] = request.form.get("observacao")
    aluno["logradouro"] = request.form.get("logradouro")
    aluno["numero"] = request.form.get("numero")
    aluno["bairro"] = request.form.get("bairro")
    aluno["cidade"] = request.form.get("cidade")
    aluno["cep"] = request.form.get("cep")
    aluno["estado"] = request.form.get("estado")
    aluno["complemento"] = request.form.get("complemento")
    aluno["observacao_endereco"] = request.form.get("observacao_endereco")

    alunos.append(aluno)
    return redirect(url_for('cadastrar_alunos'))

def cadastrar_escolas():
    # Cadastra uma nova escola.
    escola = {}
    escola["nome"] = request.form.get("nome")
    escola["tipo"] = request.form.get("tipo")
    escola["telefone"] = request.form.get("telefone")
    escola["email"] = request.form.get("email")
    escola["contato"] = request.form.get("contato")
    escola["observacao"] = request.form.get("observacao")
    escola["logradouro"] = request.form.get("logradouro")
    escola["numero"] = request.form.get("numero")
    escola["bairro"] = request.form.get("bairro")
    escola["cidade"] = request.form.get("cidade")
    escola["cep"] = request.form.get("cep")
    escola["estado"] = request.form.get("estado")
    escola["complemento"] = request.form.get("complemento")
    escola["observacao_endereco"] = request.form.get("observacao_endereco")

    escolas.append(escola)
    return redirect(url_for('cadastrar_escolas'))

def cadastrar_materiais():
    # Cadastra um novo material.
    tipo_material = request.form.get("tipo_material")
    peso_material = request.form.get("peso_material")

    if tipo_material and peso_material:
        try:
            peso_material = float(peso_material)
            materiais.append({"tipo": tipo_material, "peso": peso_material})
        except ValueError:
            return "Peso inválido. Digite um número válido."
    return redirect(url_for('cadastrar_materiais'))

def cadastrar_jogadas():
    # Cadastra uma nova jogada.
    jogada = []
    total_pontos = 0
    numero_participacoes = 1

    while True:
        try:
            pontos = float(request.form.get("pontos"))
            total_pontos += pontos
            jogada.append({"pontos": pontos, "participacao": numero_participacoes, "total_pontos": total_pontos})
            data_atual = datetime.now().strftime("%Y-%m-%d")
            jogada[-1]["data"] = data_atual
            jogada[-1]["observacao"] = request.form.get("observacao")

            continuar = request.form.get("continuar")
            if continuar != 's':
                break

            numero_participacoes += 1
        except ValueError:
            return "Erro! Por favor, insira um valor numérico válido para os pontos."

    jogos.append(jogada)
    return redirect(url_for('cadastrar_jogadas'))

# --- Funções de Listagem ---

def listar_alunos():
    # Lista todos os alunos cadastrados.
    return render_template('listar_alunos.html', alunos=alunos)

def listar_escolas():
    # Lista todas as escolas cadastradas.
    return render_template('listar_escolas.html', escolas=escolas)

def listar_materiais():
    # Lista todos os materiais cadastrados.
    return render_template('listar_materiais.html', materiais=materiais)

def listar_jogos():
    # Lista todas as jogadas cadastradas.
    return render_template('listar_jogos.html', jogos=jogos)

# --- Rotas ---

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cadastrar_alunos', methods=['GET', 'POST'])
def cadastrar_alunos():
    if request.method == 'POST':
        return cadastrar_alunos()
    return render_template('cadastrar_alunos.html')

@app.route('/cadastrar_escolas', methods=['GET', 'POST'])
def cadastrar_escolas():
    if request.method == 'POST':
        return cadastrar_escolas()
    return render_template('cadastrar_escolas.html')

@app.route('/cadastrar_materiais', methods=['GET', 'POST'])
def cadastrar_materiais():
    if request.method == 'POST':
        return cadastrar_materiais()
    return render_template('cadastrar_materiais.html')

@app.route('/cadastrar_jogadas', methods=['GET', 'POST'])
def cadastrar_jogadas():
    if request.method == 'POST':
        return cadastrar_jogadas()
    return render_template('cadastrar_jogadas.html')

@app.route('/listar_alunos')
def listar_alunos():
    return listar_alunos()

@app.route('/listar_escolas')
def listar_escolas():
    return listar_escolas()

@app.route('/listar_materiais')
def listar_materiais():
    return listar_materiais()

@app.route('/listar_jogos')
def listar_jogos():
    return listar_jogos()

if __name__ == '__main__':
    app.run(debug=True)

