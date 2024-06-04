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
adicionaCliente = []
adicionaVeiculos = []
adicionarAgendamentoOficina = []
adicionaOrcamentoPagamento = []

# --- Funções do Menu ---

def exibeMenu():
    # Exibe o menu principal do sistema.
    os.system('cls')  # Limpa a tela
    print(Fore.BLUE + "**************************************** PORTO SEGURO / OFICINA ON-LINE ****************************************" + Style.RESET_ALL)
    print(Fore.BLUE + "*                                                                                                              *" + Style.RESET_ALL)
    print(Fore.BLUE + "*                                                                                                              *" + Style.RESET_ALL)
    print(Fore.BLUE + "*" + Style.RESET_ALL, "MENU PRINCÍPAL                                                                  *")
    print(Fore.BLUE + "*                                                                                                              *" + Style.RESET_ALL)
    print(Fore.BLUE + "*                                                                                                              *" + Style.RESET_ALL)
    print(Fore.BLUE + "*" + Style.RESET_ALL, "1 - CADASTRAR NOVOS CLIENTES")
    print(Fore.BLUE + "*                                                                                                              *" + Style.RESET_ALL)
    print(Fore.BLUE + "*" + Style.RESET_ALL, "2 - CADASTRAR VEÍCULOS")
    print(Fore.BLUE + "*                                                                                                              *" + Style.RESET_ALL)
    print(Fore.BLUE + "*" + Style.RESET_ALL, "3 - AGENDAMENTO / OFICINA ON-LINE")
    print(Fore.BLUE + "*                                                                                                              *" + Style.RESET_ALL)
    print(Fore.BLUE + "*" + Style.RESET_ALL, "4 - ORÇAMENTO / PAGAMENTO")
    print(Fore.BLUE + "*                                                                                                              *" + Style.RESET_ALL)
    print(Fore.BLUE + "*                                                                                                              *" + Style.RESET_ALL)
    print(Fore.BLUE + "*" + Style.RESET_ALL, "LISTAR DADOS")
    print(Fore.BLUE + "*                                                                                                              *" + Style.RESET_ALL)
    print(Fore.BLUE + "*                                                                                                              *" + Style.RESET_ALL)
    print(Fore.BLUE + "*" + Style.RESET_ALL, "5 - LISTA DE CLIENTES CADASTRADOS")
    print(Fore.BLUE + "*                                                                                                              *" + Style.RESET_ALL)
    print(Fore.BLUE + "*" + Style.RESET_ALL, "6 - LISTA DE VEÍCULOS CADASTRADOS")
    print(Fore.BLUE + "*                                                                                                              *" + Style.RESET_ALL)
    print(Fore.BLUE + "*" + Style.RESET_ALL, "7 - LISTA DE AGENDAMENTO / OFICINA CADASTRADOS")
    print(Fore.BLUE + "*                                                                                                              *" + Style.RESET_ALL)
    print(Fore.BLUE + "*" + Style.RESET_ALL, "8 - LISTA DE ORÇAMENTO / PAGAMENTOS CADASTRADOS")
    print(Fore.BLUE + "*                                                                                                              *" + Style.RESET_ALL)
    print(Fore.BLUE + "*                                                                                                             *" + Style.RESET_ALL)
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
        cadastrarNovosClientes()
    elif opcao_escolhida == 2:
        cadastrarNovosVeiculos()
    elif opcao_escolhida == 3:
        cadastrarNovosAgendamentoOficina()
    elif opcao_escolhida == 4:
        cadastraNovosOrcamentoPagamento()
    elif opcao_escolhida == 5:
        listarClientes()
    elif opcao_escolhida == 6:
        listarVeiculos()
    elif opcao_escolhida == 7:
        listarAgendaOficina()
    elif opcao_escolhida == 8:
        listarOrcacamentoPagamento()
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

def cadastrarNovosClientes():
    # Cadastra um novo cliente.
    os.system('cls')
    print(Fore.BLUE + "**************************************** CADASTRAR NOVOS CLIENTES ****************************************" + Style.RESET_ALL)
    cliente = []
    print(Fore.BLUE + "DADOS DO CLIENTE" + Style.RESET_ALL)
    cliente.append(input("NOME...............: "))
    cliente.append(input("DATA DE NASCIMENTO.: "))
    cliente.append(input("PROFISÃO...........: "))
    cliente.append(input("CPF................: "))
    cliente.append(input("NASCIONALIDADE.....: "))
    print(Fore.BLUE + "CONTATOS DO CLIENTE" + Style.RESET_ALL)
    cliente.append(input("NÚMERO DE TELEFÔNE.: "))
    cliente.append(input("NÚMERO DE CELUAR...: "))
    cliente.append(input("E-MAIL.............: "))
    print(Fore.BLUE + "ENDEREÇO DO CLIENTE" + Style.RESET_ALL)
    cliente.append(input("LOGRADOURO.........: "))
    cliente.append(input("Número.............: "))
    cliente.append(input("CEP................: "))
    cliente.append(input("ESTADO.............: "))
    cliente.append(input("COMPLEMENTO........: "))

    adicionaCliente.append(cliente)
    print("\n")
    print("\n")
    print(Fore.YELLOW + "**************************************** DADOS DO CLIENTE CADASTRADOS COM SUCESSO ****************************************" + Style.RESET_ALL)
    print("\n")
    print("\n")
    voltarMenuPrincipal()

def cadastrarNovosVeiculos():
    # Cadastra um novo veículo.
    os.system('cls')
    print(Fore.BLUE + "**************************************** CADASTRAR NOVOS VEÍCULOS ****************************************" + Style.RESET_ALL)
    veiculo = []
    print(Fore.BLUE + "DADOS DO VEÍCULO" + Style.RESET_ALL)
    veiculo.append(input("MODELO............: "))
    veiculo.append(input("MONTADORA.........: "))
    veiculo.append(input("MOTOR.............: "))
    veiculo.append(input("ANO DE FABRICAÇÃO.: "))
    veiculo.append(input("PLACA.............: "))
    veiculo.append(input("PROPRIETÁRIO......: "))
    veiculo.append(input("OBSERVAÇÃO........: "))

    adicionaVeiculos.append(veiculo)
    print("\n")
    print("\n")
    print(Fore.YELLOW + "**************************************** DADOS DO VEÍCULO CADASTRADOS COM SUCESSO ****************************************" + Style.RESET_ALL)
    print("\n")
    print("\n")
    voltarMenuPrincipal()

def cadastrarNovosAgendamentoOficina():
    # Cadastra um novo agendamento de oficina.
    os.system('cls')
    print(Fore.BLUE + "**************************************** CADASTRAR NOVO AGENDAMENTO / OFICINA ON-LINE ****************************************" + Style.RESET_ALL)
    agendamentoOficina = []
    print("\n")
    print(Fore.BLUE + "AGENDAMENTO" + Style.RESET_ALL)
    agendamentoOficina.append(input("DATA.....................................: "))
    print("\n")
    print(Fore.BLUE + "DETALHES DO SERVIÇO" + Style.RESET_ALL)
    agendamentoOficina.append(input("DESCRIÇÃO DO PROBLEMA DO VEÍCULO.........: "))
    agendamentoOficina.append(input("DIAGNOSTICO DO VEÍCULO...................: "))
    agendamentoOficina.append(input("PARTES AFETADAS..........................: "))
    agendamentoOficina.append(input("PEÇAS USADAS.............................: "))
    agendamentoOficina.append(input("HORAS TRABALHADAS........................: "))

    adicionarAgendamentoOficina.append(agendamentoOficina)
    print("\n")
    print("\n")
    print(Fore.YELLOW + "**************************************** DADOS DO AGENDAMENTO CADASTRADOS COM SUCESSO ****************************************" + Style.RESET_ALL)
    print("\n")
    print("\n")
    voltarMenuPrincipal()

def cadastraNovosOrcamentoPagamento():
    # Cadastra um novo orçamento e pagamento.
    os.system('cls')
    print(Fore.BLUE + "**************************************** CADASTRAR NOVO ORÇAMENTO / PAGAMENTO ****************************************" + Style.RESET_ALL)
    print("\n")
    print(Fore.BLUE + "ORÇAMENTO DO SERVIÇO" + Style.RESET_ALL)

    orcamentoPagamento = []
    
    orcamentoPagamento.append(input("PREÇO DAS PEÇAS................................R$: ")) # 0
    orcamentoPagamento.append(input("VALOR DA HORA DO TRABALHO......................R$: ")) # 1

    #  Gerenciamento de erro para entrada de horas trabalhadas
    while True:
        try:
            horasTrabalhadas = float(input("QUANTIDADE DE HORAS TRABALHADAS................:   "))  # 2
            break  # Sai do loop se a entrada for válida
        except ValueError:
            print("Entrada inválida. Digite um número válido para as horas trabalhadas.")

    # Calcule o valor da mão de obra
    valorHora = float(orcamentoPagamento[1])
    maoDeObra = valorHora * horasTrabalhadas
    orcamentoPagamento.append(maoDeObra)  # 3

    # Calcule o valor total
    precoPecas = float(orcamentoPagamento[0])
    valorTotal = precoPecas + maoDeObra
    orcamentoPagamento.append(valorTotal)  # 4

    print("\n")
    print(Fore.BLUE + "PAGAMENTO" + Style.RESET_ALL)
    orcamentoPagamento.append(input("TIPO DE PAGAMENTO..............................:   "))  # 5
    orcamentoPagamento.append(input("DESCONTO.......................................:   "))  # 6
    orcamentoPagamento.append(input("PARCELAMENTO...................................:   "))  # 7
    orcamentoPagamento.append(input("QUANTIDADE DE PARCELAS.........................:   "))  # 8

    # Calcule o desconto
    desconto = float(orcamentoPagamento[6])
    valorComDesconto = valorTotal - (valorTotal * (desconto / 100))
    orcamentoPagamento.append(valorComDesconto)  # 9

    # Calcule o valor da parcela
    quantidadeParcelas = int(orcamentoPagamento[7])
    if quantidadeParcelas > 1:
        valorParcela = valorComDesconto / quantidadeParcelas
        orcamentoPagamento.append(valorParcela)  # 10
    else:
        orcamentoPagamento.append(valorComDesconto)  # Se for 1 parcela, o valor é o total com desconto

    adicionaOrcamentoPagamento.append(orcamentoPagamento)
    print("\n")
    print("\n")
    print(Fore.YELLOW + "**************************************** DADOS DO ORÇAMENTO CADASTRADOS COM SUCESSO ****************************************" + Style.RESET_ALL)
    print("\n")
    print("\n")
    voltarMenuPrincipal()

# Funções de Listagem 

def listarClientes():
    # Lista todos os clientes cadastrados.
    os.system('cls')
    print(Fore.YELLOW + "**************************************** LISTA DE CLIENTES ****************************************" + Style.RESET_ALL)
    if adicionaCliente:
        for i, cliente in enumerate(adicionaCliente):
            print(Fore.CYAN + f"Cliente {i+1}:\n" + Style.RESET_ALL)
            print(Fore.CYAN + "----------------------------------------------------------------------------------------------------" + Style.RESET_ALL)
            print(Fore.CYAN + "NOME...............: " + Style.RESET_ALL, cliente[0])
            print(Fore.CYAN + "DATA DE NASCIMENTO.: " + Style.RESET_ALL, cliente[1])
            print(Fore.CYAN + "PROFISÃO...........: " + Style.RESET_ALL, cliente[2])
            print(Fore.CYAN + "CPF................: " + Style.RESET_ALL, cliente[3])
            print(Fore.CYAN + "NASCIONALIDADE.....: " + Style.RESET_ALL, cliente[4])
            print(Fore.CYAN + "NÚMERO DE TELEFÔNE.: " + Style.RESET_ALL, cliente[5])
            print(Fore.CYAN + "NÚMERO DE CELUAR...: " + Style.RESET_ALL, cliente[6])
            print(Fore.CYAN + "E-MAIL.............: " + Style.RESET_ALL, cliente[7])
            print(Fore.CYAN + "LOGRADOURO.........: " + Style.RESET_ALL, cliente[8])
            print(Fore.CYAN + "Número.............: " + Style.RESET_ALL, cliente[9])
            print(Fore.CYAN + "CEP................: " + Style.RESET_ALL, cliente[10])
            print(Fore.CYAN + "ESTADO.............: " + Style.RESET_ALL, cliente[11])
            print(Fore.CYAN + "COMPLEMENTO........: " + Style.RESET_ALL, cliente[12])
            print(Fore.CYAN + "----------------------------------------------------------------------------------------------------" + Style.RESET_ALL)
    else:
        print("\n")
        print(Fore.RED + "**************************************** ! NENHUM CLIENTE CADASTRADO ! ****************************************" + Style.RESET_ALL)
        print("\n")
    voltarMenuPrincipal()

def listarVeiculos():
    # Lista todos os veículos cadastrados.
    os.system('cls')
    print(Fore.YELLOW + "**************************************** LISTA DE VEÍCULOS ****************************************" + Style.RESET_ALL)
    if adicionaVeiculos:
        for i, veiculo in enumerate(adicionaVeiculos):
            print(Fore.CYAN + f"Veículo {i+1}:\n" + Style.RESET_ALL)
            print(Fore.CYAN + "----------------------------------------------------------------------------------------------------" + Style.RESET_ALL)
            print(Fore.CYAN + "MODELO............: " + Style.RESET_ALL, veiculo[0])
            print(Fore.CYAN + "MONTADORA.........: " + Style.RESET_ALL, veiculo[1])
            print(Fore.CYAN + "MOTOR.............: " + Style.RESET_ALL, veiculo[2])
            print(Fore.CYAN + "ANO DE FABRICAÇÃO.: " + Style.RESET_ALL, veiculo[3])
            print(Fore.CYAN + "PLACA.............: " + Style.RESET_ALL, veiculo[4])
            print(Fore.CYAN + "PROPRIETÁRIO......: " + Style.RESET_ALL, veiculo[5])
            print(Fore.CYAN + "OBSERVAÇÃO........: " + Style.RESET_ALL, veiculo[6])
            print(Fore.CYAN + "----------------------------------------------------------------------------------------------------" + Style.RESET_ALL)
    else:
        print("\n")
        print(Fore.RED + "**************************************** ! NENHUM VEÍCULO CADASTRADO ! ****************************************" + Style.RESET_ALL)
        print("\n")
    voltarMenuPrincipal()

def listarAgendaOficina():
    # Lista todos os agendamentos de oficina.
    os.system('cls')
    print(Fore.YELLOW + "**************************************** LISTA DE AGENDAMENTOS / OFICINA ****************************************" + Style.RESET_ALL)
    if adicionarAgendamentoOficina:
        for i, agendamentoOficina in enumerate(adicionarAgendamentoOficina):
            print(Fore.CYAN + f"Agendamento {i+1}:\n" + Style.RESET_ALL)
            print(Fore.CYAN + "----------------------------------------------------------------------------------------------------" + Style.RESET_ALL)
            print(Fore.CYAN + "DATA.....................................: " + Style.RESET_ALL, agendamentoOficina[0])
            print(Fore.CYAN + "DESCRIÇÃO DO PROBLEMA DO VEÍCULO.........: " + Style.RESET_ALL, agendamentoOficina[1])
            print(Fore.CYAN + "DIAGNOSTICO DO VEÍCULO...................: " + Style.RESET_ALL, agendamentoOficina[2])
            print(Fore.CYAN + "PARTES AFETADAS..........................: " + Style.RESET_ALL, agendamentoOficina[3])
            print(Fore.CYAN + "PEÇAS USADAS.............................: " + Style.RESET_ALL, agendamentoOficina[4])
            print(Fore.CYAN + "HORAS TRABALHADAS........................: " + Style.RESET_ALL, agendamentoOficina[5])
            print(Fore.CYAN + "----------------------------------------------------------------------------------------------------" + Style.RESET_ALL)
    else:
        print("\n")
        print(Fore.RED + "**************************************** ! NENHUM AGENDAMENTO / OFICINA CADASTRADO ! ****************************************" + Style.RESET_ALL)
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