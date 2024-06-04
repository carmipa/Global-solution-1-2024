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


# Listas globais
adicionaAlunos = []
adicionaEscolas = []
materiais = []  
adicionaJogos = []

# --- Funções do Menu ---

def exibeMenu():
    # Exibe o menu principal do sistema.
    os.system('cls')  # Limpa a tela
    print("""                               ＧＬＯＢＡＬ ＳＯＬＵＴＩＯＮ － ＢＬＵＥ ＯＣＥＡＮ""")
    print(Fore.BLUE + "**************************************** GLOABAL SOLUTION / BLUE OCEAN *****************************************" + Style.RESET_ALL)
    print(Fore.BLUE + "*                                                                                                              *" + Style.RESET_ALL)
    print(Fore.BLUE + "*                                                                                                              *" + Style.RESET_ALL)
    print(Fore.BLUE + "*" + Style.RESET_ALL, "MENU PRINCÍPAL                                                                          *")
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
    print(Fore.BLUE + "*" + Style.RESET_ALL, "LISTAR DADOS")
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
        cadastraJogos()
    elif opcao_escolhida == 5:
        listarAlunos()
    elif opcao_escolhida == 6:
        listarEscolas()
    elif opcao_escolhida == 7:
        listarMateriais()
    elif opcao_escolhida == 8:
        listarJogos()
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

# Funções de Cadastro

def cadastrarAlunos():
    # Cadastra um novo cliente.
    os.system('cls')
    print(Fore.BLUE + "**************************************** CADASTRAR ALUNOS ****************************************" + Style.RESET_ALL)
    alunos = []
    print(Fore.BLUE + "DADOS DO ALUNO" + Style.RESET_ALL)
    alunos.append(input("NOME...............: "))
    alunos.append(input("SOBRENOME..........: "))
    alunos.append(input("DATA DE NASCIMENTO.: "))
    print(Fore.BLUE + "CONTATOS DO ALUNO" + Style.RESET_ALL)
    alunos.append(input("NÚMERO DE TELEFÔNE.: "))
    alunos.append(input("E-MAIL.............: "))
    alunos.append(input("CONTATO............: "))
    alunos.append(input("OBSERVAÇÃO.........: "))
    print(Fore.BLUE + "ENDEREÇO DO CLIENTE" + Style.RESET_ALL)
    alunos.append(input("LOGRADOURO.........: "))
    alunos.append(input("NÚMERO.............: "))
    alunos.append(input("BAIRRO.............: "))
    alunos.append(input("CIDADE.............: "))
    alunos.append(input("CEP................: "))
    alunos.append(input("ESTADO.............: "))
    alunos.append(input("COMPLEMENTO........: "))
    alunos.append(input("OBSERVAÇÃO.........: "))

    adicionaAlunos.append(alunos)
    print("\n")
    print("\n")
    print(Fore.YELLOW + "**************************************** DADOS DO ALUNO CADASTRADOS COM SUCESSO ****************************************" + Style.RESET_ALL)
    print("\n")
    print("\n")
    voltarMenuPrincipal()

def cadastrarEscolas():
    # Cadastra um novo veículo.
    os.system('cls')
    print(Fore.BLUE + "**************************************** CADASTRAR NOVAS ESCOLAS ****************************************" + Style.RESET_ALL)
    escolas = []
    print(Fore.BLUE + "DADOS DA ESCOLA" + Style.RESET_ALL)
    escolas.append(input("NOME DA ESCOLA.....: "))
    escolas.append(input("TIPO DE ESCOLA.....: "))
    print(Fore.BLUE + "CONTATOS DA ESCOLA" + Style.RESET_ALL)
    escolas.append(input("NÚMERO DE TELEFÔNE.: "))
    escolas.append(input("E-MAIL.............: "))
    escolas.append(input("CONTATO............: "))
    escolas.append(input("OBSERVAÇÃO.........: "))
    print(Fore.BLUE + "ENDEREÇO DA ESCOLA" + Style.RESET_ALL)
    escolas.append(input("LOGRADOURO.........: "))
    escolas.append(input("NÚMERO.............: "))
    escolas.append(input("BAIRRO.............: "))
    escolas.append(input("CIDADE.............: "))
    escolas.append(input("CEP................: "))
    escolas.append(input("ESTADO.............: "))
    escolas.append(input("COMPLEMENTO........: "))
    escolas.append(input("OBSERVAÇÃO.........: "))
    adicionaEscolas.append(escolas)
    print("\n")
    print("\n")
    print(Fore.YELLOW + "**************************************** DADOS DA ESCOLA CADASTRADOS COM SUCESSO ****************************************" + Style.RESET_ALL)
    print("\n")
    print("\n")
    voltarMenuPrincipal()

def cadastrarMateriais():
    # Cadastra um novo agendamento de oficina.
    os.system('cls')
    print(Fore.BLUE + "**************************************** CADASTRAR NOVOS MATERIAIS ****************************************" + Style.RESET_ALL)
    total_materiais = 0

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
        total_materiais += 1

        # Pergunta se o usuário deseja cadastrar mais materiais
        continuar = input("Deseja cadastrar mais materiais? (S/N): ").upper()
        if continuar != 'S':
            break

    print("\n")
    print(Fore.YELLOW + "**************************************** DADOS DOS MATERIAIS CADASTRADOS COM SUCESSO ****************************************" + Style.RESET_ALL)
    print("\n")
    print(Fore.YELLOW + "TOTAL DE MATERIAIS CADASTRADOS: " + Style.RESET_ALL, total_materiais)
    print("\n")

    # Imprime os materiais cadastrados
    for i, material in enumerate(materiais):
        print(Fore.YELLOW + f"Material {i+1}:" + Style.RESET_ALL)
        print(Fore.YELLOW + f"  Tipo: {material['tipo']}" + Style.RESET_ALL)
        print(Fore.YELLOW + f"  Peso: {material['peso']} kg" + Style.RESET_ALL)
        print("\n")

    voltarMenuPrincipal()

def cadastraJogos():
# Cadastra uma nova jogada.
os.system('cls')
print(Fore.BLUE + "**************************************** CADASTRAR NOVAS JOGADAS ****************************************" + Style.RESET_ALL)
print("\n")
jogos = []
jogos.append(input("PONTOS DO JOGADOR.......................: "))
jogos.append(input("QUANTIDADE DE PARTICIPAÇÕES.............: "))
jogos.append(input("TOTAL DE PONTO..........................: "))
jogos.append(input("DATA DA PARTICIPAÇÃO....................: "))
jogos.append(input("OBSERVAÇÃO..............................: "))

adicionaJogos.append(jogos)
print("\n")
print("\n")
print(Fore.YELLOW + "**************************************** DADOS DO JOGADOR CADASTRADOS COM SUCESSO ****************************************" + Style.RESET_ALL)
print("\n")
print("\n")
voltarMenuPrincipal()

# Lista global para armazenar os dados dos jogos
adicionaJogos = []

# Funções de Listagem 

def listarAlunos():
    # Lista todos os clientes cadastrados.
    os.system('cls')
    print(Fore.YELLOW + "**************************************** LISTA DE ALUNOS ****************************************" + Style.RESET_ALL)
    if adicionaAlunos:
        for i, alunos in enumerate(adicionaAlunos):
            print(Fore.CYAN + f"Alunos {i+1}:\n" + Style.RESET_ALL)
            print(Fore.CYAN + "----------------------------------------------------------------------------------------------------" + Style.RESET_ALL)
            print(Fore.CYAN + "NOME...............: " + Style.RESET_ALL, alunos[0])
            print(Fore.CYAN + "SOBRENOME..........: " + Style.RESET_ALL, alunos[1])
            print(Fore.CYAN + "DATA DE NASCIMENTO.: " + Style.RESET_ALL, alunos[2])
            print(Fore.CYAN + "NÚMERO DE TELEFÔNE.: " + Style.RESET_ALL, alunos[3])
            print(Fore.CYAN + "E-MAIL.............: " + Style.RESET_ALL, alunos[4])
            print(Fore.CYAN + "CONTATO............: " + Style.RESET_ALL, alunos[5])
            print(Fore.CYAN + "OBSERVAÇÃO.........: " + Style.RESET_ALL, alunos[6])
            print(Fore.CYAN + "LOGRADOURO.........: " + Style.RESET_ALL, alunos[7])
            print(Fore.CYAN + "NÚMERO.............: " + Style.RESET_ALL, alunos[8])
            print(Fore.CYAN + "BAIRRO.............: " + Style.RESET_ALL, alunos[9])
            print(Fore.CYAN + "CIDADE.............: " + Style.RESET_ALL, alunos[10])
            print(Fore.CYAN + "CEP................: " + Style.RESET_ALL, alunos[11])
            print(Fore.CYAN + "ESTADO.............: " + Style.RESET_ALL, alunos[12])
            print(Fore.CYAN + "COMPLEMENTO........: " + Style.RESET_ALL, alunos[13])
            print(Fore.CYAN + "OBSERVAÇÃO.........: " + Style.RESET_ALL, alunos[14])
            print(Fore.CYAN + "----------------------------------------------------------------------------------------------------" + Style.RESET_ALL)
    else:
        print("\n")
        print(Fore.RED + "**************************************** ! NENHUM ALUNO CADASTRADO ! ****************************************" + Style.RESET_ALL)
        print("\n")
    voltarMenuPrincipal()

def listarEscolas():
    # Lista todos os veículos cadastrados.
    os.system('cls')
    print(Fore.YELLOW + "**************************************** LISTA DE ESCOLAS ****************************************" + Style.RESET_ALL)
    if adicionaEscolas:
        for i, escolas in enumerate(adicionaEscolas):
            print(Fore.CYAN + f"Veículo {i+1}:\n" + Style.RESET_ALL)
            print(Fore.CYAN + "----------------------------------------------------------------------------------------------------" + Style.RESET_ALL)
            print(Fore.CYAN + "NOME...............: " + Style.RESET_ALL, escolas[0])
            print(Fore.CYAN + "TIPO DE ESCOLA.....: " + Style.RESET_ALL, escolas[1])
            print(Fore.CYAN + "NÚMERO DE TELEFÔNE.: " + Style.RESET_ALL, escolas[2])
            print(Fore.CYAN + "E-MAIL.............: " + Style.RESET_ALL, escolas[3])
            print(Fore.CYAN + "CONTATO............: " + Style.RESET_ALL, escolas[4])
            print(Fore.CYAN + "OBSERVAÇÃO.........: " + Style.RESET_ALL, escolas[5])
            print(Fore.CYAN + "LOGRADOURO.........: " + Style.RESET_ALL, escolas[6])
            print(Fore.CYAN + "NÚMERO.............: " + Style.RESET_ALL, escolas[7])
            print(Fore.CYAN + "BAIRRO.............: " + Style.RESET_ALL, escolas[8])
            print(Fore.CYAN + "CIDADE.............: " + Style.RESET_ALL, escolas[9])
            print(Fore.CYAN + "CEP................: " + Style.RESET_ALL, escolas[10])
            print(Fore.CYAN + "ESTADO.............: " + Style.RESET_ALL, escolas[11])
            print(Fore.CYAN + "COMPLEMENTO........: " + Style.RESET_ALL, escolas[12])
            print(Fore.CYAN + "OBSERVAÇÃO.........: " + Style.RESET_ALL, escolas[13])
            print(Fore.CYAN + "----------------------------------------------------------------------------------------------------" + Style.RESET_ALL)
    else:
        print("\n")
        print(Fore.RED + "**************************************** ! NENHUMA ESCOLA CADASTRADA ! ****************************************" + Style.RESET_ALL)
        print("\n")
    voltarMenuPrincipal()

def listarMateriais():
    # Lista todos os agendamentos de oficina.
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

def listarOrcacamentoPagamento():
    # Lista todos os orçamentos e pagamentos cadastrados.
    os.system('cls')
    print(Fore.YELLOW + "**************************************** LISTA DE ORÇAMENTOS / PAGAMENTOS ****************************************" + Style.RESET_ALL)
    if adicionaOrcamentoPagamento:
        for i, orcamentoPagamento in enumerate(adicionaOrcamentoPagamento):
            print(Fore.CYAN + f"Orçamento {i+1}:\n" + Style.RESET_ALL)
            print(Fore.CYAN + "----------------------------------------------------------------------------------------------------" + Style.RESET_ALL)
            print(Fore.CYAN + "PREÇO DAS PEÇAS................................R$: " + Style.RESET_ALL, orcamentoPagamento[0])
            print(Fore.CYAN + "VALOR DA HORA DO TRABALHO......................R$: " + Style.RESET_ALL, orcamentoPagamento[1])
            print(Fore.CYAN + "QUANTIDADE DE HORAS TRABALHADAS................:   " + Style.RESET_ALL, orcamentoPagamento[2])
            print(Fore.CYAN + "MÃO DE ÓBRA....................................R$: " + Style.RESET_ALL, orcamentoPagamento[3])
            print(Fore.CYAN + "VALOR TOTAL....................................:   " + Style.RESET_ALL, orcamentoPagamento[4])
            print(Fore.CYAN + "TIPO DE PAGAMENTO..............................:   " + Style.RESET_ALL, orcamentoPagamento[5])
            print(Fore.CYAN + "DESCONTO.......................................:   " + Style.RESET_ALL, orcamentoPagamento[6])
            print(Fore.CYAN + "PARCELAMENTO...................................:   " + Style.RESET_ALL, orcamentoPagamento[7])
            print(Fore.CYAN + "QUANTIDADE DE PARCELAS.........................:   " + Style.RESET_ALL, orcamentoPagamento[8])
            print(Fore.CYAN + "VALOR TOTAL DO SERVIÇO COM DESCONTO............R$: " + Style.RESET_ALL, orcamentoPagamento[9])
            if int(orcamentoPagamento[8]) > 1:
                print(Fore.CYAN + "VALOR DAS PARCELAS.............................R$: " + Style.RESET_ALL, orcamentoPagamento[10])
            print(Fore.CYAN + "----------------------------------------------------------------------------------------------------" + Style.RESET_ALL)
    else:
        print("\n")
        print(Fore.RED + "**************************************** ! NENHUM ORÇAMENTO / PAGAMENTO CADASTRADO ! ****************************************" + Style.RESET_ALL)
        print("\n")
    voltarMenuPrincipal()

# Funções de Encerramento 

def finalizarSistema():
    # Finaliza o programa com uma mensagem de despedida.
    os.system('cls')
    print(Fore.YELLOW + "**************************************** ! SAINDO DO SISTEMA ! ****************************************" + Style.RESET_ALL)
    exit()


# Função Principal 

def main():
    # Função principal do programa.
    while True:
        exibeMenu()
        escolherOpcao()

if __name__ == '__main__':
    main()