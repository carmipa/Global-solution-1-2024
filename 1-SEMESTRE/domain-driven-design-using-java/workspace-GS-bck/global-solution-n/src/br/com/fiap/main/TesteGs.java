package br.com.fiap.main;

import javax.swing.JOptionPane;

public class TesteGs {
	
	public static String texto(String t) {
		
		return JOptionPane.showInputDialog(t);
		
	}
	
	public static int numero(String n) {
		
		return Integer.parseInt(JOptionPane.showInputDialog(n));
		
	}
	
	public static double real(String r) {
		
		return Double.parseDouble(JOptionPane.showInputDialog(r));
		
	}

	public static void main(String[] args) {
		
		
		

	}

}
