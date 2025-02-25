package br.com.fiap.gs.beans;

import br.com.fiap.gs.interfaces.Ijogos;

public class Jogos implements Ijogos{

	@SuppressWarnings("unused")
	private int codigoJogo;

	private int pontos;
	private int quantidadeParticipacoes;
	private double totalPontos;
	private String dataParticipacao;
	private String observacao;
	private Alunos alunos;
	private Materiais materiais;

	public Jogos() {
		super();
		// TODO Auto-generated constructor stub
	}

	public Jogos(int pontos, int quantidadeParticipacoes, double totalPontos, String dataParticipacao,
			String observacao) {
		super();
		this.pontos = pontos;
		this.quantidadeParticipacoes = quantidadeParticipacoes;
		this.totalPontos = totalPontos;
		this.dataParticipacao = dataParticipacao;
		this.observacao = observacao;
	}

	public int getPontos() {
		return pontos;
	}

	public void setPontos(int pontos) {
		this.pontos = pontos;
	}

	public int getQuantidadeParticipacoes() {
		return quantidadeParticipacoes;
	}

	public void setQuantidadeParticipacoes(int quantidadeParticipacoes) {
		this.quantidadeParticipacoes = quantidadeParticipacoes;
	}

	public double getTotalPontos() {
		return totalPontos;
	}

	public void setTotalPontos(double totalPontos) {
		this.totalPontos = totalPontos;
	}

	public String getDataParticipacao() {
		return dataParticipacao;
	}

	public void setDataParticipacao(String dataParticipacao) {
		this.dataParticipacao = dataParticipacao;
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

	public Materiais getMateriais() {
		return materiais;
	}

	public void setMateriais(Materiais materiais) {
		this.materiais = materiais;
	}

	@Override
	public String toString() {
		return "Jogos [pontos=" + pontos + ", quantidadeParticipacoes=" + quantidadeParticipacoes + ", totalPontos="
				+ totalPontos + ", dataParticipacao=" + dataParticipacao + ", observacao=" + observacao + ", alunos="
				+ alunos + ", materiais=" + materiais + ", getPontos()=" + getPontos()
				+ ", getQuantidadeParticipacoes()=" + getQuantidadeParticipacoes() + ", getTotalPontos()="
				+ getTotalPontos() + ", getDataParticipacao()=" + getDataParticipacao() + ", getObservacao()="
				+ getObservacao() + ", getAlunos()=" + getAlunos() + ", getMateriais()=" + getMateriais() + "]";
	}

	@Override
	public double calculaPontos() {
		// TODO Auto-generated method stub
		return pontos = (int) totalPontos;
	}

}
