package br.com.fiap.gs.main;

import java.util.InputMismatchException;
import java.util.Scanner;

import br.com.fiap.gs.beans.Alunos;

import br.com.fiap.gs.beans.Escolas;
import br.com.fiap.gs.beans.Jogos;
import br.com.fiap.gs.beans.Materiais;

public class TesteGs {
	
	

	public static void main(String[] args) {
		
		Scanner scanner = new Scanner(System.in);

		Alunos alunos = new Alunos();
		Escolas escolas = new Escolas();
		Jogos jogos = new Jogos();
		Materiais materiais = new Materiais();
		
		
		
		int opcao = 0;

		while (true) {
			System.out.println("\u001B[36m******************** BLUE OCEAN - JOGOS ********************");
			System.out.println("*");
			System.out.println("* 1 - CADASTRA ALUNOS");
			System.out.println("* 2 - CADASTRA ESCOLAS");
			System.out.println("* 3 - JOGOS");
			System.out.println("* 4 - MATERIAIS");
			System.out.println("* 6 - SAIR");
			System.out.println("*");
			System.out.print("************************************************************\u001B[0m");
			System.out.println();
			System.out.print("\nDIGITE UMA DAS OPÇOES ACIMA: ");

			try {
				opcao = scanner.nextInt();
				scanner.nextLine(); 

				switch (opcao) {
				case 1: {
					System.out.println();
					System.out.println("******************** 1 - CADASTRA ALUNOS ********************");
					System.out.println();
					System.out.print("Nome:.................: ");
					alunos.setNome(scanner.nextLine());
					System.out.print("Sobrenome.............: ");
					alunos.setSobrenome(scanner.nextLine());
					System.out.print("Data de nascimento....: ");
					alunos.setDataNascimento(scanner.nextLine());
					System.out.print("Telefone..............: ");
					alunos.setTelefone(scanner.nextLine());
					System.out.print("Email.................: ");
					alunos.setEmail(scanner.nextLine());
					System.out.print("Contato...............: ");
					alunos.setContato(scanner.nextLine());
					System.out.print("Observacão............: ");
					alunos.setObservacao(scanner.nextLine());
					System.out.print("Logradouro............: ");
					alunos.setLogradouro(scanner.nextLine());
										
					// Validação do número do logradouro
                    while (true) {
                        System.out.print("Número................: ");
                        try {
                            alunos.setNumeroLogradouro(scanner.nextInt());
                            scanner.nextLine(); 
                            scanner.nextLine(); 
                            break; 
                        } catch (InputMismatchException e) {
                            System.err.println("Por favor, digite um número válido.");
                            scanner.nextLine();
                            scanner.nextLine(); 
                        }
                    }
					
					scanner.nextLine();
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
					System.out.println();
					
					System.out.println("\u001B[33m-------------------- DADOS DO ALUNOS - SALVOS COM SUCESSO! --------------------" 
					                 + "\n"
					                 + "\nNome...................: "+ alunos.getNome() 
					                 + "\nSobrenome..............: "+ alunos.getSobrenome()
					                 + "\nData de Nascimento.....: " + alunos.getDataNascimento()
					                 + "\n"
					                 + "\nTelefone...............: " + alunos.getTelefone()
					                 + "\nEmail..................: " + alunos.getEmail()
					                 + "\nContato................: " + alunos.getContato()
					                 + "\nObservacao.............: " + alunos.getObservacao()
					                 + "\n"
					                 + "\nLogradouro.............: " + alunos.getLogradouro()
					                 + "\nNúmero.................: " + alunos.getNumeroLogradouro()
					                 + "\nBairro.................: " + alunos.getBairro()
					                 + "\nCidade.................: " + alunos.getCidade()
					                 + "\nEstado.................: " + alunos.getEstado()
					                 + "\nCEP....................: " + alunos.getCep()
					                 + "\nComplemento............: " + alunos.getComplemento()
					                 + "\nObservação.............: " + alunos.getObservacao()
					                 + "\n"
					                 + "\n-------------------------------------------------------------------------------\u001B[0m");
					break;
				}

				case 2: {
					System.out.println();
					System.out.println("******************** 2 - CADASTRA ESCOLAS ********************");
					System.out.println();
					System.out.print("Nome da escola........: ");
					escolas.setNomeEscola(scanner.nextLine());
					System.out.print("Tipo da escola........: ");
					escolas.setTipoEscola(scanner.nextLine());
					System.out.print("Telefone..............: ");
					escolas.setTelefone(scanner.nextLine());
					System.out.print("E-mail................: ");
					escolas.setEmail(scanner.nextLine());
					System.out.print("Contato...............: ");
					escolas.setContato(scanner.nextLine());
					System.out.print("Observações...........: ");
					escolas.setObservacao(scanner.nextLine());
					System.out.print("Logradouro............: ");
					escolas.setLogradouro(scanner.nextLine());
				
                    while (true) {
                        System.out.print("Número................: ");
                        try {
                        	escolas.setNumeroLogradouro(scanner.nextInt());
                            scanner.nextLine(); 
                            break; 
                        } catch (InputMismatchException e) {
                            System.err.println("Por favor, digite um número válido.");
                            scanner.nextLine(); 
                        }
                    }
					
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
					System.out.println();
					
					System.out.println("\u001B[33m-------------------- DADOS DA ESCOLA - SALVOS COM SUCESSO! --------------------" 
			                 		 + "\n"
			                 		 + "\nNome da escola.........: "+ escolas.getNomeEscola()
			                 		 + "\nData de Nascimento.....: " + escolas.getTipoEscola()
			                 		 + "\n"
			                 		 + "\nTelefone...............: " + escolas.getTelefone()
			                 		 + "\nEmail..................: " + escolas.getEmail()
			                 		 + "\nContato................: " + escolas.getContato()
			                 		 + "\nObservacao.............: " + escolas.getObservacao()
			                 		 + "\n"
			                 		 + "\nLogradouro.............: " + escolas.getLogradouro()
			                 		 + "\nNúmero.................: " + escolas.getNumeroLogradouro()
			                 		 + "\nBairro.................: " + escolas.getBairro()
			                 		 + "\nCidade.................: " + escolas.getCidade()
			                 		 + "\nEstado.................: " + escolas.getEstado()
			                 		 + "\nCEP....................: " + escolas.getCep()
			                 		 + "\nComplemento............: " + escolas.getComplemento()
			                 		 + "\nObservação.............: " + escolas.getObservacao()
			                 		 + "\n"
			                 		 + "\nCadastro feito para: " + escolas.exiibeEscola()
			                 		 + "\n"
			                 		 + "\n-------------------------------------------------------------------------------\u001B[0m");
					System.out.println();
					break;
					
				}

				case 3: {
					System.out.println();
					System.out.println("******************** 3 - JOGOS ********************");

					System.out.println();
                    while (true) {
                        System.out.print("Pontos do jogador...........: ");
                        try {
                        	jogos.setPontos(scanner.nextInt());
                            scanner.nextLine(); 
                            break; 
                        } catch (InputMismatchException e) {
                            System.err.println("Por favor, digite um número válido.");
                            scanner.nextLine(); 
                        }
                    }
					
					while (true) {
                        System.out.print("Quantidade de participações.: ");
                        try {
                        	jogos.setQuantidadeParticipacoes(scanner.nextInt());
                            scanner.nextLine(); 
                            break; 
                        } catch (InputMismatchException e) {
                            System.err.println("Por favor, digite um número válido.");
                            scanner.nextLine(); 
                        }
                    }
					
					while (true) {
                        System.out.print("Total de ponto..............: ");
                        try {
                        	jogos.setTotalPontos(scanner.nextInt());
                            scanner.nextLine().replace(',', '.'); 
                            break; 
                        } catch (InputMismatchException e) {
                            System.err.println("Por favor, digite um número válido.");
                            scanner.nextLine(); 
                        }
                    }
					System.out.print("Data da participação........: ");
					jogos.setDataParticipacao(scanner.nextLine());
					System.out.print("Observação..................: ");
					jogos.setObservacao(scanner.nextLine());
					System.out.println();
					
					System.out.println();
					System.out.println("\u001B[33m-------------------- DADOS DO JOGO - SALVOS COM SUCESSO! --------------------" 
			                 		 + "\n"
			                 		 + "\nPontos do jogador...........: " + jogos.getPontos()
			                 		 + "\nQuantidade de participações.: " + jogos.getQuantidadeParticipacoes()
			                 		 + "\nTotal de Ponto..............: " + jogos.getTotalPontos()
			                 		 + "\nData da Participação........: " + jogos.getDataParticipacao()
			                 		 + "\nObservação..................: " + jogos.getObservacao()
			                 		 + "\n"
			                 		 + "\nTotal de pontos feito pelo jogador é de: " + jogos.calculaPontos()
			                 		 + "\n"
			                 		 + "\n-----------------------------------------------------------------------------\u001B[0m");
					System.out.println();
					
					break;
				}

				case 4: {
					System.out.println();
					System.out.println("******************** 4 - MATERIAIS ********************");
					System.out.println();
					System.out.print("Tipo de material....: ");
					materiais.setTipoMaterial(scanner.nextLine());
					
					while (true) {
                        System.out.print("Peso do material..: ");
                        try {
                            materiais.setPesoMaterial(scanner.nextInt());
                            scanner.nextLine().replace(',', '.'); 
                            break; 
                        } catch (InputMismatchException e) {
                            System.err.println("Por favor, digite um número válido.");
                            scanner.nextLine(); 
                        }
                    }
					
					while (true) {
                        System.out.print("Total de meteiais.: ");
                        try {                        	
                        	materiais.setTotal(scanner.nextInt());
                            scanner.nextLine().replace(',', '.'); 
                            break; 
                        } catch (InputMismatchException e) {
                            System.err.println("Por favor, digite um número válido.");
                            scanner.nextLine(); 
                        }
                    }
					
					System.out.println();
					System.out.println("\u001B[33m-------------------- DADOS DOS MATERIAIS - SALVOS COM SUCESSO --------------------" 
			                 		 + "\n"
			                 		 + "\nTipo de material...: " + materiais.getTipoMaterial()
			                 		 + "\nPeso do material...: " + materiais.getPesoMaterial()
			                 		 + "\nTotal de materiais.: " + materiais.getTotal()
			                 		 + "\n"
			                 		 + "Total de materiais trazido pelo jogador é de: " + materiais.totalMateriais()
			                 		 + "\n"
			                 		 + "\n----------------------------------------------------------------------------------\u001B[0m");
										
					break;
				}

				case 6: {
					System.out.println();
					System.err.println("SAIR DO SISTEMA");
					System.out.println();
					scanner.close();
					System.exit(0);
					break;
				}

				default:
					System.out.println();
					System.err.println("Opção inválida. Tente novamente.");
					System.out.println();
				}

			} catch (InputMismatchException e) {
				System.out.println();
				System.err.println("Entrada inválida. Digite um número inteiro.");
				System.out.println();
				scanner.next(); 

			}
		}

	}

}
