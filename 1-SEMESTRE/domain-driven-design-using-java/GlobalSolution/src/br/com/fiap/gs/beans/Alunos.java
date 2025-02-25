package br.com.fiap.gs.beans;

public class Alunos extends Enderecos {

	@SuppressWarnings("unused")
	private int codigoAluno;

	private String nome;
	private String sobrenome;
	private String dataNascimento;
	private String telefone;
	private String email;
	private String contato;
	private String observacao;
	private Escolas escolas;
	private Materiais materiais;
	private Jogos jogos;

	public Alunos() {
		super();
		// TODO Auto-generated constructor stub
	}

	public Alunos(String logradouro, int numeroLogradouro, String bairro, String cidade, String estado, String cep,
			String complemento, String observacao, String nome, String sobrenome, String dataNascimento,
			String telefone, String email, String contato, String observacao2) {
		super(logradouro, numeroLogradouro, bairro, cidade, estado, cep, complemento, observacao);
		this.nome = nome;
		this.sobrenome = sobrenome;
		this.dataNascimento = dataNascimento;
		this.telefone = telefone;
		this.email = email;
		this.contato = contato;
		observacao = observacao2;
	}

	public String getNome() {
		return nome;
	}

	public void setNome(String nome) {
		this.nome = nome;
	}

	public String getSobrenome() {
		return sobrenome;
	}

	public void setSobrenome(String sobrenome) {
		this.sobrenome = sobrenome;
	}

	public String getDataNascimento() {
		return dataNascimento;
	}

	public void setDataNascimento(String dataNascimento) {
		this.dataNascimento = dataNascimento;
	}

	public String getTelefone() {
		return telefone;
	}

	public void setTelefone(String telefone) {
		this.telefone = telefone;
	}

	public String getEmail() {
		return email;
	}

	public void setEmail(String email) {
		this.email = email;
	}

	public String getContato() {
		return contato;
	}

	public void setContato(String contato) {
		this.contato = contato;
	}

	public String getObservacao() {
		return observacao;
	}

	public void setObservacao(String observacao) {
		this.observacao = observacao;
	}

	public Escolas getEscolas() {
		return escolas;
	}

	public void setEscolas(Escolas escolas) {
		this.escolas = escolas;
	}

	public Materiais getMateriais() {
		return materiais;
	}

	public void setMateriais(Materiais materiais) {
		this.materiais = materiais;
	}

	public Jogos getJogos() {
		return jogos;
	}

	public void setJogos(Jogos jogos) {
		this.jogos = jogos;
	}

	@Override
	public String toString() {
		return "Alunos [nome=" + nome + ", sobrenome=" + sobrenome + ", dataNascimento=" + dataNascimento
				+ ", telefone=" + telefone + ", email=" + email + ", contato=" + contato + ", observacao=" + observacao
				+ ", escolas=" + escolas + ", materiais=" + materiais + ", jogos=" + jogos + ", getNome()=" + getNome()
				+ ", getSobrenome()=" + getSobrenome() + ", getDataNascimento()=" + getDataNascimento()
				+ ", getTelefone()=" + getTelefone() + ", getEmail()=" + getEmail() + ", getContato()=" + getContato()
				+ ", getObservacao()=" + getObservacao() + ", getEscolas()=" + getEscolas() + ", getMateriais()="
				+ getMateriais() + ", getJogos()=" + getJogos() + "]";
	}

}
