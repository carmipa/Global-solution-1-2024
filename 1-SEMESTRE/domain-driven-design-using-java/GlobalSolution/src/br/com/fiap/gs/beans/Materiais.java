package br.com.fiap.gs.beans;

import br.com.fiap.gs.interfaces.Imateriais;

public class Materiais implements Imateriais{

	@SuppressWarnings("unused")
	private int codigoMaterial;

	private String tipoMaterial;
	private double pesoMaterial;
	private double total;

	public Materiais() {
		super();
		// TODO Auto-generated constructor stub
	}

	public Materiais(String tipoMaterial, double pesoMaterial, double total) {
		super();
		this.tipoMaterial = tipoMaterial;
		this.pesoMaterial = pesoMaterial;
		this.total = total;
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

	public double getTotal() {
		return total;
	}

	public void setTotal(double total) {
		this.total = total;
	}

	@Override
	public String toString() {
		return "Materiais [tipoMaterial=" + tipoMaterial + ", pesoMaterial=" + pesoMaterial + ", total=" + total
				+ ", getTipoMaterial()=" + getTipoMaterial() + ", getPesoMaterial()=" + getPesoMaterial()
				+ ", getTotal()=" + getTotal() + "]";
	}

	@Override
	public double totalMateriais() {
		
		return pesoMaterial = totalMateriais();
	}

	



}
