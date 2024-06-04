from flask import Flask, render_template, request, redirect, url_for
from colorama import Fore, Style

app = Flask(__name__)

# Listas globais
adicionaAlunos = []
adicionaEscolas = []
materiais = []
adicionaOrcamentoPagamento = []

# --- Funções do Menu ---

def exibeMenu():
    # Exibe o menu principal do sistema.
    menu_html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>GLOBAL SOLUTION - BLUE OCEAN</title>
        <style>
            body {
                background-color: #f0f0f0;
                font-family: sans-serif;
            }
            .container {
                width: 80%;
                margin: 0 auto;
                padding: 20px;
                background-color: #fff;
                border-radius: 5px;
                box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
            }
            h1 {
                text-align: center;
                color: #333;
            }
            .menu-item {
                margin-bottom: 10px;
                padding: 10px;
                background-color: #eee;
                border-radius: 3px;
                cursor: pointer;
                text-align: center;
            }
            .menu-item:hover {
                background-color: #ddd;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>GLOBAL SOLUTION - BLUE OCEAN</h1>
            <div class="menu-item" onclick="window.location.href='/cadastrar_alunos'">1 - CADASTRAR ALUNOS</div>
            <div class="menu-item" onclick="window.location.href='/cadastrar_escolas'">2 - CADASTRAR ESCOLAS</div>
            <div class="menu-item" onclick="window.location.href='/cadastrar_materiais'">3 - CADASTRA MATERIAIS</div>
            <div class="menu-item" onclick="window.location.href='/orcamento_pagamento'">4 - ORÇAMENTO / PAGAMENTO</div>
            <div class="menu-item" onclick="window.location.href='/listar_alunos'">5 - LISTA DE ALUNOS CADASTRADOS</div>
            <div class="menu-item" onclick="window.location.href='/listar_escolas'">6 - LISTA DE ESCOLAS CADASTRADAS</div>
            <div class="menu-item" onclick="window.location.href='/listar_materiais'">7 - LISTA DE MATERIAIS CADASTRADOS</div>
            <div class="menu-item" onclick="window.location.href='/listar_orcamentos'">8 - LISTA DE ORÇAMENTO / PAGAMENTOS CADASTRADOS</div>
            <div class="menu-item" onclick="window.location.href='/sair'">0 - SAIR DO SISTEMA</div>
        </div>
    </body>
    </html>
    """
    return menu_html

@app.route('/')
def index():
    return exibeMenu()

# Funções de Cadastro

@app.route('/cadastrar_alunos', methods=['GET', 'POST'])
def cadastrarAlunos():
    if request.method == 'POST':
        alunos = [
            request.form['nome'],
            request.form['sobrenome'],
            request.form['data_nascimento'],
            request.form['telefone'],
            request.form['email'],
            request.form['contato'],
            request.form['observacao'],
            request.form['logradouro'],
            request.form['numero'],
            request.form['bairro'],
            request.form['cidade'],
            request.form['cep'],
            request.form['estado'],
            request.form['complemento'],
            request.form['observacao_endereco'],
        ]
        adicionaAlunos.append(alunos)
        return redirect(url_for('index'))
    return render_template('cadastrar_alunos.html')

@app.route('/cadastrar_escolas', methods=['GET', 'POST'])
def cadastrarEscolas():
    if request.method == 'POST':
        escolas = [
            request.form['nome_escola'],
            request.form['tipo_escola'],
            request.form['telefone_escola'],
            request.form['email_escola'],
            request.form['contato_escola'],
            request.form['observacao_escola'],
            request.form['logradouro_escola'],
            request.form['numero_escola'],
            request.form['bairro_escola'],
            request.form['cidade_escola'],
            request.form['cep_escola'],
            request.form['estado_escola'],
            request.form['complemento_escola'],
            request.form['observacao_endereco_escola'],
        ]
        adicionaEscolas.append(escolas)
        return redirect(url_for('index'))
    return render_template('cadastrar_escolas.html')

@app.route('/cadastrar_materiais', methods=['GET', 'POST'])
def cadastrarMateriais():
    if request.method == 'POST':
        tipo_material = request.form['tipo_material']
        peso_material = float(request.form['peso_material'])
        materiais.append({"tipo": tipo_material, "peso": peso_material})
        return redirect(url_for('index'))
    return render_template('cadastrar_materiais.html')

@app.route('/orcamento_pagamento', methods=['GET', 'POST'])
def cadastraNovosOrcamentoPagamento():
    if request.method == 'POST':
        orcamentoPagamento = [
            request.form['preco_pecas'],
            request.form['valor_hora'],
            float(request.form['horas_trabalhadas']),
            None,  # Mão de obra será calculada
            None,  # Valor total será calculado
            request.form['tipo_pagamento'],
            request.form['desconto'],
            request.form['parcelamento'],
            request.form['quantidade_parcelas'],
            None,  # Valor com desconto será calculado
            None,  # Valor da parcela será calculado
        ]
        # Calcule o valor da mão de obra
        valorHora = float(orcamentoPagamento[1])
        maoDeObra = valorHora * orcamentoPagamento[2]
        orcamentoPagamento[3] = maoDeObra

        # Calcule o valor total
        precoPecas = float(orcamentoPagamento[0])
        valorTotal = precoPecas + maoDeObra
        orcamentoPagamento[4] = valorTotal

        # Calcule o desconto
        desconto = float(orcamentoPagamento[6])
        valorComDesconto = valorTotal - (valorTotal * (desconto / 100))
        orcamentoPagamento[9] = valorComDesconto

        # Calcule o valor da parcela
        quantidadeParcelas = int(orcamentoPagamento[8])
        if quantidadeParcelas > 1:
            valorParcela = valorComDesconto / quantidadeParcelas
            orcamentoPagamento[10] = valorParcela
        else:
            orcamentoPagamento[10] = valorComDesconto

        adicionaOrcamentoPagamento.append(orcamentoPagamento)
        return redirect(url_for('index'))
    return render_template('orcamento_pagamento.html')

# Funções de Listagem 

@app.route('/listar_alunos')
def listarAlunos():
    return render_template('listar_alunos.html', alunos=adicionaAlunos)

@app.route('/listar_escolas')
def listarEscolas():
    return render_template('listar_escolas.html', escolas=adicionaEscolas)

@app.route('/listar_materiais')
def listarMateriais():
    return render_template('listar_materiais.html', materiais=materiais)

@app.route('/listar_orcamentos')
def listarOrcacamentoPagamento():
    return render_template('listar_orcamentos.html', orcamentos=adicionaOrcamentoPagamento)

# Funções de Encerramento 

@app.route('/sair')
def finalizarSistema():
    return "Saindo do sistema..."

if __name__ == '__main__':
    app.run(debug=True)