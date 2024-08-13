package br.com.fiap.gs.beans;

public class Pessoas extends Enderecos {

	@SuppressWarnings("unused")
	private int codigoPessoa;
	
	private String nome;
	private String dataNascimento;
	private String ocupacao;
	private String observacao;

	public Pessoas() {
		super();
		// TODO Auto-generated constructor stub
	}

	public Pessoas(String logradouro, int numeroLogradouro, String cep, String observacao, String nome,
			String dataNascimento, String ocupacao, String observacao2) {
		super(logradouro, numeroLogradouro, cep, observacao);
		this.nome = nome;
		this.dataNascimento = dataNascimento;
		this.ocupacao = ocupacao;
		observacao = observacao2;
	}

	public String getNome() {
		return nome;
	}

	public void setNome(String nome) {
		this.nome = nome;
	}

	public String getDataNascimento() {
		return dataNascimento;
	}

	public void setDataNascimento(String dataNascimento) {
		this.dataNascimento = dataNascimento;
	}

	public String getOcupacao() {
		return ocupacao;
	}

	public void setOcupacao(String ocupacao) {
		this.ocupacao = ocupacao;
	}

	public String getObservacao() {
		return observacao;
	}

	public void setObservacao(String observacao) {
		this.observacao = observacao;
	}

	@Override
	public String toString() {
		return "Pessoas [nome=" + nome + ", dataNascimento=" + dataNascimento + ", ocupacao=" + ocupacao
				+ ", observacao=" + observacao + ", getNome()=" + getNome() + ", getDataNascimento()="
				+ getDataNascimento() + ", getOcupacao()=" + getOcupacao() + ", getObservacao()=" + getObservacao()
				+ ", getLogradouro()=" + getLogradouro() + ", getNumeroLogradouro()=" + getNumeroLogradouro()
				+ ", getCep()=" + getCep() + "]";
	}

}
