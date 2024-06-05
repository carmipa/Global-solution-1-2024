#########################################################################################################################################
#
#     INSTRUÇÕES DE USO:
#
# 1 - quando houver uma opção de pesquisa no menu use as seguinte opções:
#     ex: 1 ou 2 ou 3 - "sempre um destes 3 código"
#
# 2 - O programa usa a biblioteca "COLORAMA", como visto no importe, para que funcione corretamente use
#     o seguinte comando no console abaixo antes de rodar o programa:
#     "pip install colorama"
#     OBS: se a biblioteca já estiver instalada, não é necessário a instalar
#
#########################################################################################################################################

# importa bibiotecas de cores e para limpesa de tela

import os
from colorama import Fore, Style
from datetime import datetime

# Listas globais
alunos = []
escolas = []
materiais = []
jogos = []

# --- Funções do Menu ---

def exibeMenu():
    # Exibe o menu principal do sistema.
    os.system('cls')  # Limpa a tela
    print("""                               ＧＬＯＢＡＬ ＳＯＬＵＴＩＯＮ － ＢＬＵＥ ＯＣＥＡＮ""")
    print(Fore.BLUE + "**************************************** GLOABAL SOLUTION / BLUE OCEAN *****************************************" + Style.RESET_ALL)
    print(Fore.BLUE + "*                                                                                                              *" + Style.RESET_ALL)
    print(Fore.BLUE + "*                                                                                                              *" + Style.RESET_ALL)
    print(Fore.BLUE + "*" + Style.RESET_ALL, " MENU PRINCÍPAL                                                                          *")
    print(Fore.BLUE + "*                                                                                                              *" + Style.RESET_ALL)
    print(Fore.BLUE + "*                                                                                                              *" + Style.RESET_ALL)
    print(Fore.BLUE + "*" + Style.RESET_ALL, "1 - CADASTRAR ALUNOS")
    print(Fore.BLUE + "*                                                                                                              *" + Style.RESET_ALL)
    print(Fore.BLUE + "*" + Style.RESET_ALL, "2 - CADASTRAR ESCOLAS")
    print(Fore.BLUE + "*                                                                                                              *" + Style.RESET_ALL)
    print(Fore.BLUE + "*" + Style.RESET_ALL, "3 - CADASTRA MATERIAIS")
    print(Fore.BLUE + "*                                                                                                              *" + Style.RESET_ALL)
    print(Fore.BLUE + "*" + Style.RESET_ALL, "4 - CADASTRA JOGADAS")
    print(Fore.BLUE + "*                                                                                                              *" + Style.RESET_ALL)
    print(Fore.BLUE + "*                                                                                                              *" + Style.RESET_ALL)
    print(Fore.BLUE + "*" + Style.RESET_ALL, " LISTAR DADOS")
    print(Fore.BLUE + "*                                                                                                              *" + Style.RESET_ALL)
    print(Fore.BLUE + "*                                                                                                              *" + Style.RESET_ALL)
    print(Fore.BLUE + "*" + Style.RESET_ALL, "5 - LISTA DE ALUNOS CADASTRADOS")
    print(Fore.BLUE + "*                                                                                                              *" + Style.RESET_ALL)
    print(Fore.BLUE + "*" + Style.RESET_ALL, "6 - LISTA DE ESCOLAS CADASTRADAS")
    print(Fore.BLUE + "*                                                                                                              *" + Style.RESET_ALL)
    print(Fore.BLUE + "*" + Style.RESET_ALL, "7 - LISTA DE MATERIAIS CADASTRADOS")
    print(Fore.BLUE + "*                                                                                                              *" + Style.RESET_ALL)
    print(Fore.BLUE + "*" + Style.RESET_ALL, "8 - LISTA DE JOGADAS")
    print(Fore.BLUE + "*                                                                                                              *" + Style.RESET_ALL)
    print(Fore.BLUE + "*                                                                                                              *" + Style.RESET_ALL)
    print(Fore.BLUE + "*                                                                                                              *" + Style.RESET_ALL)
    print(Fore.BLUE + "*" + Style.RESET_ALL, "0 - SAIR DO SISTEMA")
    print(Fore.BLUE + "*                                                                                                              *" + Style.RESET_ALL)
    print(Fore.BLUE + "*                                                                                                              *" + Style.RESET_ALL)
    print(Fore.BLUE + "****************************************************************************************************************" + Style.RESET_ALL)

def escolherOpcao():
    # Lê a opção do usuário e chama a função correspondente.
    while True:
        try:
            opcao_escolhida = int(input("Escolha uma opção: "))
            if 0 <= opcao_escolhida <= 8:
                break
            else:
                opcaoInvalida()
        except ValueError:
            opcaoInvalida()

    if opcao_escolhida == 1:
        cadastrarAlunos()
    elif opcao_escolhida == 2:
        cadastrarEscolas()
    elif opcao_escolhida == 3:
        cadastrarMateriais()
    elif opcao_escolhida == 4:
        cadastrarJogadas()
    elif opcao_escolhida == 5:
        listarAlunos(alunos)
    elif opcao_escolhida == 6:
        listarEscolas(escolas)
    elif opcao_escolhida == 7:
        listarMateriais(materiais)
    elif opcao_escolhida == 8:
        listarJogos(jogos)
    elif opcao_escolhida == 0:
        finalizarSistema()
    return opcao_escolhida

def opcaoInvalida():
    # Exibe uma mensagem de erro para opção inválida.
    print(Fore.RED + "**************************************** OPÇÃO INVÁLIDA ****************************************" + Style.RESET_ALL)
    voltarMenuPrincipal()

def voltarMenuPrincipal():
    # Retorna ao menu principal.
    input("\nDigite uma tecla para voltar ao menu: ")

# --- Funções de Cadastro ---

def cadastrarAlunos():
    # Cadastra um novo aluno.
    os.system('cls')
    print(Fore.BLUE + "**************************************** CADASTRAR ALUNOS ****************************************" + Style.RESET_ALL)

    while True:
        aluno = {}
        print(Fore.BLUE + "DADOS DO ALUNO" + Style.RESET_ALL)
        aluno["nome"] = input("NOME...............: ")
        aluno["sobrenome"] = input("SOBRENOME..........: ")
        aluno["data_nascimento"] = input("DATA DE NASCIMENTO.: ")
        print(Fore.BLUE + "CONTATOS DO ALUNO" + Style.RESET_ALL)
        aluno["telefone"] = input("NÚMERO DE TELEFÔNE.: ")
        aluno["email"] = input("E-MAIL.............: ")
        aluno["contato"] = input("CONTATO............: ")
        aluno["observacao"] = input("OBSERVAÇÃO.........: ")
        print(Fore.BLUE + "ENDEREÇO DO ALUNO" + Style.RESET_ALL)
        aluno["logradouro"] = input("LOGRADOURO.........: ")
        aluno["numero"] = input("NÚMERO.............: ")
        aluno["bairro"] = input("BAIRRO.............: ")
        aluno["cidade"] = input("CIDADE.............: ")
        aluno["cep"] = input("CEP................: ")
        aluno["estado"] = input("ESTADO.............: ")
        aluno["complemento"] = input("COMPLEMENTO........: ")
        aluno["observacao_endereco"] = input("OBSERVAÇÃO.........: ")

        alunos.append(aluno)
        print("\n")
        print("\n")
        print(Fore.YELLOW + "**************************************** DADOS DO ALUNO CADASTRADOS COM SUCESSO ****************************************" + Style.RESET_ALL)
        print("\n")
        print("\n")

        # Pergunta se o usuário quer cadastrar outro aluno
        continuar = input("Deseja cadastrar outro aluno? (s/n): ").lower()
        os.system('cls')
        if continuar != 's':
            break

    voltarMenuPrincipal()

def cadastrarEscolas():
    # Cadastra uma nova escola.
    os.system('cls')
    print(Fore.BLUE + "**************************************** CADASTRAR NOVAS ESCOLAS ****************************************" + Style.RESET_ALL)

    while True:
        escola = {}
        print(Fore.BLUE + "DADOS DA ESCOLA" + Style.RESET_ALL)
        escola["nome"] = input("NOME DA ESCOLA.....: ")
        escola["tipo"] = input("TIPO DE ESCOLA.....: ")
        print(Fore.BLUE + "CONTATOS DA ESCOLA" + Style.RESET_ALL)
        escola["telefone"] = input("NÚMERO DE TELEFÔNE.: ")
        escola["email"] = input("E-MAIL.............: ")
        escola["contato"] = input("CONTATO............: ")
        escola["observacao"] = input("OBSERVAÇÃO.........: ")
        print(Fore.BLUE + "ENDEREÇO DA ESCOLA" + Style.RESET_ALL)
        escola["logradouro"] = input("LOGRADOURO.........: ")
        escola["numero"] = input("NÚMERO.............: ")
        escola["bairro"] = input("BAIRRO.............: ")
        escola["cidade"] = input("CIDADE.............: ")
        escola["cep"] = input("CEP................: ")
        escola["estado"] = input("ESTADO.............: ")
        escola["complemento"] = input("COMPLEMENTO........: ")
        escola["observacao_endereco"] = input("OBSERVAÇÃO.........: ")

        escolas.append(escola)
        print("\n")
        print("\n")
        print(Fore.YELLOW + "**************************************** DADOS DA ESCOLA CADASTRADOS COM SUCESSO ****************************************" + Style.RESET_ALL)
        print("\n")
        print("\n")

        # Pergunta se o usuário quer cadastrar outra escola
        continuar = input("Deseja cadastrar outra escola? (s/n): ").lower()
        os.system('cls')
        if continuar != 's':
            break

    voltarMenuPrincipal()

def cadastrarMateriais():
    # Cadastra um novo material.
    os.system('cls')
    print(Fore.BLUE + "**************************************** CADASTRAR NOVOS MATERIAIS ****************************************" + Style.RESET_ALL)
    while True:
        print("\n")
        print(Fore.BLUE + "DETALHES DO MATERIAL" + Style.RESET_ALL)

        tipo_material = input("TIPO DO MATERIAL.......: ")
        while True:
            try:
                peso_material = float(input("PESO DO MATERIAL.......: "))
                break
            except ValueError:
                print(Fore.RED + "Peso inválido. Digite um número válido." + Style.RESET_ALL)

        materiais.append({"tipo": tipo_material, "peso": peso_material})

        # Pergunta se o usuário deseja cadastrar mais materiais
        continuar = input("Deseja cadastrar mais materiais? (S/N): ").upper()
        if continuar != 'S':
            break

    print("\n")
    print(Fore.YELLOW + "**************************************** DADOS DOS MATERIAIS CADASTRADOS COM SUCESSO ****************************************" + Style.RESET_ALL)
    print("\n")
    print(Fore.YELLOW + "TOTAL DE MATERIAIS CADASTRADOS: " + Style.RESET_ALL, len(materiais))
    print("\n")

    # Imprime os materiais cadastrados
    for i, material in enumerate(materiais):
        print(Fore.YELLOW + f"Material {i+1}:" + Style.RESET_ALL)
        print(Fore.YELLOW + f"  Tipo: {material['tipo']}" + Style.RESET_ALL)
        print(Fore.YELLOW + f"  Peso: {material['peso']} kg" + Style.RESET_ALL)
        print("\n")

    voltarMenuPrincipal()

def cadastrarJogadas():
    # Cadastra uma nova jogada.
    os.system('cls')
    print(Fore.BLUE + "**************************************** CADASTRAR NOVAS JOGADAS ****************************************" + Style.RESET_ALL)
    print("\n")

    jogada = []
    total_pontos = 0
    numero_participacoes = 1

    while True:
        try:
            pontos = float(input("PONTOS DO JOGADOR.......................: "))
            total_pontos += pontos
            jogada.append({"pontos": pontos, "participacao": numero_participacoes, "total_pontos": total_pontos})
            
            # Obtém a data atual e formata como string
            data_atual = datetime.now().strftime("%Y-%m-%d")  
            jogada[-1]["data"] = data_atual
            
            jogada[-1]["observacao"] = input("OBSERVAÇÃO..............................: ")

            # Pergunta se o usuário quer adicionar mais jogos
            continuar = input("Deseja adicionar mais jogos? (s/n): ").lower()
            if continuar != 's':
                break

            numero_participacoes += 1
        except ValueError:
            print(Fore.RED + "Erro! Por favor, insira um valor numérico válido para os pontos." + Style.RESET_ALL)

    jogos.append(jogada)
    print("\n")
    print("\n")
    print(Fore.YELLOW + "**************************************** DADOS DO JOGADOR CADASTRADOS COM SUCESSO ****************************************" + Style.RESET_ALL)
    print("\n")
    print("\n")
    voltarMenuPrincipal()

# --- Funções de Listagem ---

def listarAlunos(alunos):
    # Lista todos os alunos cadastrados.
    os.system('cls')
    print(Fore.YELLOW + "**************************************** LISTA DE ALUNOS ****************************************" + Style.RESET_ALL)
    if alunos:
        for i, aluno in enumerate(alunos):
            print(Fore.CYAN + f"Aluno {i+1}:\n" + Style.RESET_ALL)
            print(Fore.CYAN + "----------------------------------------------------------------------------------------------------" + Style.RESET_ALL)
            print(Fore.CYAN + "NOME...............: " + Style.RESET_ALL, aluno["nome"])
            print(Fore.CYAN + "SOBRENOME..........: " + Style.RESET_ALL, aluno["sobrenome"])
            print(Fore.CYAN + "DATA DE NASCIMENTO.: " + Style.RESET_ALL, aluno["data_nascimento"])
            print(Fore.CYAN + "NÚMERO DE TELEFÔNE.: " + Style.RESET_ALL, aluno["telefone"])
            print(Fore.CYAN + "E-MAIL.............: " + Style.RESET_ALL, aluno["email"])
            print(Fore.CYAN + "CONTATO............: " + Style.RESET_ALL, aluno["contato"])
            print(Fore.CYAN + "OBSERVAÇÃO.........: " + Style.RESET_ALL, aluno["observacao"])
            print(Fore.CYAN + "LOGRADOURO.........: " + Style.RESET_ALL, aluno["logradouro"])
            print(Fore.CYAN + "NÚMERO.............: " + Style.RESET_ALL, aluno["numero"])
            print(Fore.CYAN + "BAIRRO.............: " + Style.RESET_ALL, aluno["bairro"])
            print(Fore.CYAN + "CIDADE.............: " + Style.RESET_ALL, aluno["cidade"])
            print(Fore.CYAN + "CEP................: " + Style.RESET_ALL, aluno["cep"])
            print(Fore.CYAN + "ESTADO.............: " + Style.RESET_ALL, aluno["estado"])
            print(Fore.CYAN + "COMPLEMENTO........: " + Style.RESET_ALL, aluno["complemento"])
            print(Fore.CYAN + "OBSERVAÇÃO.........: " + Style.RESET_ALL, aluno["observacao_endereco"])
            print(Fore.CYAN + "----------------------------------------------------------------------------------------------------" + Style.RESET_ALL)
    else:
        print("\n")
        print(Fore.RED + "**************************************** ! NENHUM ALUNO CADASTRADO ! ****************************************" + Style.RESET_ALL)
        print("\n")
    voltarMenuPrincipal()

def listarEscolas(escolas):
    # Lista todas as escolas cadastradas.
    os.system('cls')
    print(Fore.YELLOW + "**************************************** LISTA DE ESCOLAS ****************************************" + Style.RESET_ALL)
    if escolas:
        for i, escola in enumerate(escolas):
            print(Fore.CYAN + f"Escola {i+1}:\n" + Style.RESET_ALL)
            print(Fore.CYAN + "----------------------------------------------------------------------------------------------------" + Style.RESET_ALL)
            print(Fore.CYAN + "NOME...............: " + Style.RESET_ALL, escola["nome"])
            print(Fore.CYAN + "TIPO DE ESCOLA.....: " + Style.RESET_ALL, escola["tipo"])
            print(Fore.CYAN + "NÚMERO DE TELEFÔNE.: " + Style.RESET_ALL, escola["telefone"])
            print(Fore.CYAN + "E-MAIL.............: " + Style.RESET_ALL, escola["email"])
            print(Fore.CYAN + "CONTATO............: " + Style.RESET_ALL, escola["contato"])
            print(Fore.CYAN + "OBSERVAÇÃO.........: " + Style.RESET_ALL, escola["observacao"])
            print(Fore.CYAN + "LOGRADOURO.........: " + Style.RESET_ALL, escola["logradouro"])
            print(Fore.CYAN + "NÚMERO.............: " + Style.RESET_ALL, escola["numero"])
            print(Fore.CYAN + "BAIRRO.............: " + Style.RESET_ALL, escola["bairro"])
            print(Fore.CYAN + "CIDADE.............: " + Style.RESET_ALL, escola["cidade"])
            print(Fore.CYAN + "CEP................: " + Style.RESET_ALL, escola["cep"])
            print(Fore.CYAN + "ESTADO.............: " + Style.RESET_ALL, escola["estado"])
            print(Fore.CYAN + "COMPLEMENTO........: " + Style.RESET_ALL, escola["complemento"])
            print(Fore.CYAN + "OBSERVAÇÃO.........: " + Style.RESET_ALL, escola["observacao_endereco"])
            print(Fore.CYAN + "----------------------------------------------------------------------------------------------------" + Style.RESET_ALL)
    else:
        print("\n")
        print(Fore.RED + "**************************************** ! NENHUMA ESCOLA CADASTRADA ! ****************************************" + Style.RESET_ALL)
        print("\n")
    voltarMenuPrincipal()

def listarMateriais(materiais):
    # Lista todos os materiais cadastrados.
    os.system('cls')
    print(Fore.YELLOW + "**************************************** LISTA DE MATERIAIS ****************************************" + Style.RESET_ALL)
    if materiais:
        for i, material in enumerate(materiais):
            print(Fore.CYAN + f"Material {i+1}:\n" + Style.RESET_ALL)
            print(Fore.CYAN + "----------------------------------------------------------------------------------------------------" + Style.RESET_ALL)
            print(Fore.CYAN + "TIPO MATERIAL............: " + Style.RESET_ALL, material["tipo"])
            print(Fore.CYAN + "PESO DO MATERIAL.........: " + Style.RESET_ALL, material["peso"])
            print(Fore.CYAN + "----------------------------------------------------------------------------------------------------" + Style.RESET_ALL)
    else:
        print("\n")
        print(Fore.RED + "**************************************** ! NENHUM MATERIAL CADASTRADO ! ****************************************" + Style.RESET_ALL)
        print("\n")
    voltarMenuPrincipal()

def listarJogos(jogos):
    
    os.system('cls')  # Limpa a tela

    print(Fore.YELLOW + "**************************************** LISTA DE JOGADAS ****************************************" + Style.RESET_ALL)

    if jogos:
        for i, jogada in enumerate(jogos, start=1):  # Começa a enumeração em 1
            print(Fore.CYAN + f"Jogada {i}:\n" + Style.RESET_ALL)
            print(Fore.CYAN + "----------------------------------------------------------------------------------------------------" + Style.RESET_ALL)
            total_pontos_jogador = 0

            for j, dado in enumerate(jogada, start=1):  # Começa a enumeração em 1
                print(Fore.CYAN + f"Dado {j}:\n" + Style.RESET_ALL)
                print(Fore.CYAN + "PONTOS..................................: " + Style.RESET_ALL, dado["pontos"])
                print(Fore.CYAN + "QUANTIDADE DE PARTICIPAÇÕES.............: " + Style.RESET_ALL, dado["participacao"])
                print(Fore.CYAN + "TOTAL DE PONTOS.........................: " + Style.RESET_ALL, dado["total_pontos"])
                print(Fore.CYAN + "DATA DA PARTICIPAÇÃO....................: " + Style.RESET_ALL, dado["data"])
                print(Fore.CYAN + "OBSERVAÇÃO..............................: " + Style.RESET_ALL, dado["observacao"])
                total_pontos_jogador += dado["pontos"]
            print(Fore.CYAN + "----------------------------------------------------------------------------------------------------" + Style.RESET_ALL)
            print(Fore.CYAN + f"TOTAL DE PONTOS DO JOGADOR.............: {total_pontos_jogador}" + Style.RESET_ALL)
            print("\n") 

    else:
        print("\n")
        print(Fore.RED + "**************************************** ! NENHUMA JOGADA CADASTRADA ! ****************************************" + Style.RESET_ALL)
        print("\n")

    voltarMenuPrincipal()


# --- Funções de Encerramento ---

def finalizarSistema():
    # Finaliza o programa com uma mensagem de despedida.
    os.system('cls')
    print(Fore.YELLOW + "**************************************** ! SAINDO DO SISTEMA ! ****************************************" + Style.RESET_ALL)
    exit()

# --- Função Principal ---

def main():
    # Função principal do programa.
    while True:
        exibeMenu()
        escolherOpcao()

if __name__ == '__main__':
    main()