package br.com.fiap.gs.main;

import java.util.InputMismatchException;
import java.util.Scanner;

import br.com.fiap.gs.beans.Alunos;
import br.com.fiap.gs.beans.Escolas;
import br.com.fiap.gs.beans.Jogos;
import br.com.fiap.gs.beans.Materiais;

public class Teste {

    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);

        Alunos alunos = new Alunos();
        Escolas escolas = new Escolas();
        Jogos jogos = new Jogos();
        Materiais materiais = new Materiais();

        int opcao = 0;

        while (true) {
            // Simplificando a exibição do menu
            System.out.println("******************** BLUE OCEAN - JOGOS ********************");
            System.out.println("* 1 - Cadastrar Alunos");
            System.out.println("* 2 - Cadastrar Escolas");
            System.out.println("* 3 - Jogos");
            System.out.println("* 4 - Materiais");
            System.out.println("* 6 - Sair");
            System.out.println("************************************************************");

            System.out.print("\nDigite uma das opções acima: ");

            try {
                opcao = scanner.nextInt();
                scanner.nextLine(); // Consumir a quebra de linha

                switch (opcao) {
                    case 1:
                        cadastrarAluno(scanner, alunos);
                        break;
                    case 2:
                        cadastrarEscola(scanner, escolas);
                        break;
                    case 3:
                        cadastrarJogo(scanner, jogos);
                        break;
                    case 4:
                        cadastrarMaterial(scanner, materiais);
                        break;
                    case 6:
                        System.err.println("Saindo do sistema...");
                        scanner.close();
                        System.exit(0);
                    default:
                        System.err.println("Opção inválida. Tente novamente.");
                }

            } catch (InputMismatchException e) {
                System.err.println("Entrada inválida. Digite um número inteiro.");
                scanner.next(); // Limpar o buffer do scanner
            }
        }
    }

    // Método para cadastrar alunos
    private static void cadastrarAluno(Scanner scanner, Alunos alunos) {
        System.out.println("\nDADOS DO ALUNO");
        System.out.print("Nome:...................: ");
        alunos.setNome(scanner.nextLine());
        System.out.print("Sobrenome.............: ");
        alunos.setSobrenome(scanner.nextLine());
        System.out.print("Data de nascimento....: ");
        alunos.setDataNascimento(scanner.nextLine());

        System.out.println("\nCONTATO DO ALUNO:");
        System.out.print("Telefone..............: ");
        alunos.setTelefone(scanner.nextLine());
        System.out.print("Email.................: ");
        alunos.setEmail(scanner.nextLine());
        System.out.print("Contato...............: ");
        alunos.setContato(scanner.nextLine());
        System.out.print("Observação............: ");
        alunos.setObservacao(scanner.nextLine());

        System.out.println("\nENDEREÇO DO ALUNO:");
        System.out.print("Logradouro............: ");
        alunos.setLogradouro(scanner.nextLine());
        System.out.print("Número................: ");
        alunos.setNumeroLogradouro(scanner.nextInt());
        scanner.nextLine(); // Consumir a quebra de linha
        System.out.print("Bairro................: ");
        alunos.setBairro(scanner.nextLine());
        System.out.print("Cidade................: ");
        alunos.setCidade(scanner.nextLine());
        System.out.print("Estado................: ");
        alunos.setEstado(scanner.nextLine());
        System.out.print("CEP...................: ");
        alunos.setCep(scanner.nextLine());
        System.out.print("Complemento...........: ");
        alunos.setComplemento(scanner.nextLine());
        System.out.print("Observações...........: ");
        alunos.setObservacao(scanner.nextLine());

        mostrarDadosAluno(alunos);
    }

    // Método para mostrar os dados do aluno
    private static void mostrarDadosAluno(Alunos alunos) {
        System.out.println("\n*************** DADOS DO ALUNO - SALVOS COM SUCESSO! ***************");
        System.out.println("\nDADOS DO ALUNO:");
        System.out.println("Nome...................: " + alunos.getNome());
        System.out.println("Sobrenome..............: " + alunos.getSobrenome());
        System.out.println("Data de Nascimento.....: " + alunos.getDataNascimento());
        System.out.println("\nCONTATOS DO ALUNOS:");
        System.out.println("Telefone...............: " + alunos.getTelefone());
        System.out.println("Email..................: " + alunos.getEmail());
        System.out.println("Contato................: " + alunos.getContato());
        System.out.println("Observacao.............: " + alunos.getObservacao());
        System.out.println("\nENDEREÇO DO ALUNO:");
        System.out.println("Logradouro.............: " + alunos.getLogradouro());
        System.out.println("Número.................: " + alunos.getNumeroLogradouro());
        System.out.println("Bairro.................: " + alunos.getBairro());
        System.out.println("Cidade.................: " + alunos.getCidade());
        System.out.println("Estado.................: " + alunos.getEstado());
        System.out.println("CEP....................: " + alunos.getCep());
        System.out.println("Complemento............: " + alunos.getComplemento());
        System.out.println("Observação.............: " + alunos.getObservacao());
        System.out.println("\n****************************************************************************************");
    }

    // Método para cadastrar escolas
    private static void cadastrarEscola(Scanner scanner, Escolas escolas) {
        System.out.println("\nDADOS DA ESCOLA.");
        System.out.print("Nome da escola....: ");
        escolas.setNomeEscola(scanner.nextLine());
        System.out.print("Tipo da escola....: ");
        escolas.setTipoEscola(scanner.nextLine());

        System.out.println("\nCONTATO DA ESCOLA:");
        System.out.print("Telefone..........: ");
        escolas.setTelefone(scanner.nextLine());
        System.out.print("E-mail............: ");
        escolas.setEmail(scanner.nextLine());
        System.out.print("Contato...........: ");
        escolas.setContato(scanner.nextLine());
        System.out.print("Observações.......: ");
        escolas.setObservacao(scanner.nextLine());

        System.out.println("\nENDEREÇO DA ESCOLA:");
        System.out.print("Logradouro............: ");
        escolas.setLogradouro(scanner.nextLine());
        System.out.print("Número................: ");
        escolas.setNumeroLogradouro(scanner.nextInt());
        scanner.nextLine(); // Consumir a quebra de linha
        System.out.print("Bairro................: ");
        escolas.setBairro(scanner.nextLine());
        System.out.print("Cidade................: ");
        escolas.setCidade(scanner.nextLine());
        System.out.print("Estado................: ");
        escolas.setEstado(scanner.nextLine());
        System.out.print("CEP...................: ");
        escolas.setCep(scanner.nextLine());
        System.out.print("Complemento...........: ");
        escolas.setComplemento(scanner.nextLine());
        System.out.print("Observações...........: ");
        escolas.setObservacao(scanner.nextLine());

        mostrarDadosEscola(escolas);
    }

    // Método para mostrar os dados da escola
    private static void mostrarDadosEscola(Escolas escolas) {
        System.out.println("\n*************** DADOS DA ESCOLA - SALVOS COM SUCESSO! ***************");
        System.out.println("\nDADOS DA ESCOLA:");
        System.out.println("Nome da escola.........: " + escolas.getNomeEscola());
        System.out.println("Data de Nascimento.....: " + escolas.getTipoEscola());
        System.out.println("\nCONTATOS DA ESCOLA:");
        System.out.println("Telefone...............: " + escolas.getTelefone());
        System.out.println("Email..................: " + escolas.getEmail());
        System.out.println("Contato................: " + escolas.getContato());
        System.out.println("Observacao.............: " + escolas.getObservacao());
        System.out.println("\nENDEREÇO DA ESCOLA:");
        System.out.println("Logradouro.............: " + escolas.getLogradouro());
        System.out.println("Número.................: " + escolas.getNumeroLogradouro());
        System.out.println("Bairro.................: " + escolas.getBairro());
        System.out.println("Cidade.................: " + escolas.getCidade());
        System.out.println("Estado.................: " + escolas.getEstado());
        System.out.println("CEP....................: " + escolas.getCep());
        System.out.println("Complemento............: " + escolas.getComplemento());
        System.out.println("Observação.............: " + escolas.getObservacao());
        System.out.println("\n****************************************************************************************");
    }

    // Método para cadastrar jogos
    private static void cadastrarJogo(Scanner scanner, Jogos jogos) {
        System.out.println("\n1 - JOGOS\n");
        System.out.print("Pontos do jogador...........: ");
        jogos.setPontos(scanner.nextInt());
        scanner.nextLine(); // Consumir a quebra de linha
        System.out.print("Quantidade de participações.: ");
        jogos.setQuantidadeParticipacoes(scanner.nextInt());
        scanner.nextLine(); // Consumir a quebra de linha
        System.out.print("Total de ponto..............: ");
        jogos.setTotalPontos(scanner.nextDouble());
        scanner.nextLine(); // Consumir a quebra de linha
        System.out.print("Data da participação........: ");
        jogos.setDataParticipacao(scanner.nextLine());
        System.out.print("Observação..................: ");
        jogos.setObservacao(scanner.nextLine());

        mostrarDadosJogo(jogos);
    }

    // Método para mostrar os dados do jogo
    private static void mostrarDadosJogo(Jogos jogos) {
        System.out.println("\n*************** DADOS DO JOGO - SALVOS COM SUCESSO! ***************");
        System.out.println("Pontos do jogador...........: " + jogos.getPontos());
        System.out.println("Quantidade de participações.: " + jogos.getQuantidadeParticipacoes());
        System.out.println("Total de Ponto..............: " + jogos.getTotalPontos());
        System.out.println("Data da Participação........: " + jogos.getDataParticipacao());
        System.out.println("Observação..................: " + jogos.getObservacao());
        System.out.println("\n****************************************************************************************");
    }

    // Método para cadastrar materiais
    private static void cadastrarMaterial(Scanner scanner, Materiais materiais) {
        System.out.println("4 - MATERIAIS\n");
        System.out.print("Tipo de material....: ");
        materiais.setTipoMaterial(scanner.nextLine());
        System.out.print("Peso do material..: ");
        materiais.setPesoMaterial(scanner.nextDouble());
        scanner.nextLine(); // Consumir a quebra de linha
        System.out.print("Total de meteiais.: ");
        materiais.setTotal(scanner.nextDouble());
        scanner.nextLine(); // Consumir a quebra de linha

        mostrarDadosMaterial(materiais);
    }

    // Método para mostrar os dados do material
    private static void mostrarDadosMaterial(Materiais materiais) {
        System.out.println("\n*************** DADOS DOS MATERIAIS - SALVOS COM SUCESSO! ***************");
        System.out.println("Tipo de material...: " + materiais.getTipoMaterial());
        System.out.println("Peso do material...: " + materiais.getPesoMaterial());
        System.out.println("Total de materiais.: " + materiais.getTotal());
        System.out.println("\n****************************************************************************************");
    }
}