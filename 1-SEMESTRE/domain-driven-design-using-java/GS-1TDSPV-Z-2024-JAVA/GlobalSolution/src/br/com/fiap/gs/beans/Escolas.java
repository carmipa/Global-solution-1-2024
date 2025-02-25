package br.com.fiap.gs.beans;

import br.com.fiap.gs.interfaces.Iescola;

public class Escolas extends Enderecos implements Iescola{

	@SuppressWarnings("unused")
	private int codigoEscola;

	private String nomeEscola;
	private String tipoEscola;
	private String telefone;
	private String email;
	private String contato;
	private String observacao;
	private Alunos alunos;

	public Escolas() {
		super();
		// TODO Auto-generated constructor stub
	}

	public Escolas(String logradouro, int numeroLogradouro, String bairro, String cidade, String estado, String cep,
			String complemento, String observacao, String nomeEscola, String tipoEscola, String telefone, String email,
			String contato, String observacao2) {
		super(logradouro, numeroLogradouro, bairro, cidade, estado, cep, complemento, observacao);
		this.nomeEscola = nomeEscola;
		this.tipoEscola = tipoEscola;
		this.telefone = telefone;
		this.email = email;
		this.contato = contato;
		observacao = observacao2;
	}

	public String getNomeEscola() {
		return nomeEscola;
	}

	public void setNomeEscola(String nomeEscola) {
		this.nomeEscola = nomeEscola;
	}

	public String getTipoEscola() {
		return tipoEscola;
	}

	public void setTipoEscola(String tipoEscola) {
		this.tipoEscola = tipoEscola;
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

	public Alunos getAlunos() {
		return alunos;
	}

	public void setAlunos(Alunos alunos) {
		this.alunos = alunos;
	}

	@Override
	public String toString() {
		return "Escolas [nomeEscola=" + nomeEscola + ", tipoEscola=" + tipoEscola + ", telefone=" + telefone
				+ ", email=" + email + ", contato=" + contato + ", observacao=" + observacao + ", alunos=" + alunos
				+ ", getNomeEscola()=" + getNomeEscola() + ", getTipoEscola()=" + getTipoEscola() + ", getTelefone()="
				+ getTelefone() + ", getEmail()=" + getEmail() + ", getContato()=" + getContato() + ", getObservacao()="
				+ getObservacao() + ", getAlunos()=" + getAlunos() + "]";
	}

	@Override
	public String exiibeEscola() {
		
		return "Escola " + nomeEscola + " , uma escola da rede " + tipoEscola;
	}

}
