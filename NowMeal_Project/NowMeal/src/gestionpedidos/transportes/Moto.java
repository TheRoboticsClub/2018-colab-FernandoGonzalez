package gestionpedidos.transportes;

import gestionpedidos.mapa.Mapa;

public class Moto extends Transporte {
	
	private final double eurosPKm = 2.0;
	
	public Moto(String cod, Mapa mapa) {
		super(cod, mapa); //Llamo al construnctor de la clase padre
	}
	
	public double coste(String codIni, String codFin) {
		/*
		 * Devuelve el coste de ir desde su ubicacion hasta la
		 * ubicacion del objeto con codigo "codPosDestino"
		 */
		
		return this.mapa.distancia(codIni, codFin) * this.eurosPKm;
	}

}
