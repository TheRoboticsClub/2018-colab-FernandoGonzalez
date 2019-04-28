package gestionpedidos.transportes;

import gestionpedidos.mapa.Mapa;

public abstract class Transporte {
	protected String codigo;
	protected Mapa mapa;
	
	public Transporte(String cod, Mapa mapa) {
		this.codigo = cod;
		this.mapa = mapa;
	}

	public double coste(String codPosDestino) {
		/*
		 * Devuelve el coste de ir desde su ubicacion hasta la
		 * ubicacion del objeto con codigo "codPosDestino"
		 */
		
		return this.coste(this.codigo, codPosDestino);
	}
	
	public String getCodigo() {
		//Devuelve el codigo del transporte
		return this.codigo;
	}
	
	public abstract double coste(String codIni, String codFin);

}
