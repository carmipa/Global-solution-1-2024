package br.com.fiap.gs.beans;

import br.com.fiap.gs.interfaces.Imateriais;

public class Materiais implements Imateriais{

	@SuppressWarnings("unused")
	private int codigoMaterial;
	
	private String tipoMaterial;
	private double pesoMaterial;
	private Enderecos endereco;

	public Materiais() {
		super();
		// TODO Auto-generated constructor stub
	}

	public Materiais(String tipoMaterial, double pesoMaterial) {
		super();
		this.tipoMaterial = tipoMaterial;
		this.pesoMaterial = pesoMaterial;
	}

	public String getTipoMaterial() {
		return tipoMaterial;
	}

	public void setTipoMaterial(String tipoMaterial) {
		this.tipoMaterial = tipoMaterial;
	}

	public double getPesoMaterial() {
		return pesoMaterial;
	}

	public void setPesoMaterial(double pesoMaterial) {
		this.pesoMaterial = pesoMaterial;
	}

	public Enderecos getEndereco() {
		return endereco;
	}

	public void setEndereco(Enderecos endereco) {
		this.endereco = endereco;
	}

	@Override
	public String toString() {
		return "Materiais [tipoMaterial=" + tipoMaterial + ", pesoMaterial=" + pesoMaterial + ", endereco=" + endereco
				+ ", getTipoMaterial()=" + getTipoMaterial() + ", getPesoMaterial()=" + getPesoMaterial()
				+ ", getEndereco()=" + getEndereco() + "]";
	}

	@Override
	public double calculaPeso() {
		// TODO Auto-generated method stub
		return 0;
	}

	@Override
	public int quantidadeMateriais() {
		// TODO Auto-generated method stub
		return 0;
	}

}
