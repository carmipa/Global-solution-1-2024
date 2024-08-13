package br.com.fiap.gs.beans;

public class Escola extends Enderecos {

	@SuppressWarnings("unused")
	private int codigoEscola;
	
	private String nomeEscola;
	private String telefone;
	private String email;
	private String tipoEscola;
	private String observacao;

	public Escola() {
		super();
		// TODO Auto-generated constructor stub
	}

	public Escola(String logradouro, int numeroLogradouro, String cep, String observacao, String nomeEscola,
			String telefone, String email, String tipoEscola, String observacao2) {
		super(logradouro, numeroLogradouro, cep, observacao);
		this.nomeEscola = nomeEscola;
		this.telefone = telefone;
		this.email = email;
		this.tipoEscola = tipoEscola;
		observacao = observacao2;
	}

	public String getNomeEscola() {
		return nomeEscola;
	}

	public void setNomeEscola(String nomeEscola) {
		this.nomeEscola = nomeEscola;
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

	public String getTipoEscola() {
		return tipoEscola;
	}

	public void setTipoEscola(String tipoEscola) {
		this.tipoEscola = tipoEscola;
	}

	public String getObservacao() {
		return observacao;
	}

	public void setObservacao(String observacao) {
		this.observacao = observacao;
	}

	@Override
	public String toString() {
		return "Escola [nomeEscola=" + nomeEscola + ", telefone=" + telefone + ", email=" + email + ", tipoEscola="
				+ tipoEscola + ", observacao=" + observacao + ", getNomeEscola()=" + getNomeEscola()
				+ ", getTelefone()=" + getTelefone() + ", getEmail()=" + getEmail() + ", getTipoEscola()="
				+ getTipoEscola() + ", getObservacao()=" + getObservacao() + "]";
	}

}
