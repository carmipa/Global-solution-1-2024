package br.com.fiap.gs.beans;

public abstract class Enderecos {

	@SuppressWarnings("unused")
	private int codigoEndereco;
	
	private String logradouro;
	private int numeroLogradouro;
	private String cep;
	private String observacao;

	public Enderecos() {
		super();
		// TODO Auto-generated constructor stub
	}

	public Enderecos(String logradouro, int numeroLogradouro, String cep, String observacao) {
		super();
		this.logradouro = logradouro;
		this.numeroLogradouro = numeroLogradouro;
		this.cep = cep;
		this.observacao = observacao;
	}

	public String getLogradouro() {
		return logradouro;
	}

	public void setLogradouro(String logradouro) {
		this.logradouro = logradouro;
	}

	public int getNumeroLogradouro() {
		return numeroLogradouro;
	}

	public void setNumeroLogradouro(int numeroLogradouro) {
		this.numeroLogradouro = numeroLogradouro;
	}

	public String getCep() {
		return cep;
	}

	public void setCep(String cep) {
		this.cep = cep;
	}

	public String getObservacao() {
		return observacao;
	}

	public void setObservacao(String observacao) {
		this.observacao = observacao;
	}

}
