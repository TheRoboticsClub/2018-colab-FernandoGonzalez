package gestionpedidos.transportes;

import gestionpedidos.mapa.Mapa;

public class FurgonetaSubcontratada extends Furgoneta {
	
	double eurosPKm;
	private final double MaxTara = 1000.0; //Tara maxima. Se usa en el metodo "coste"
	
	public FurgonetaSubcontratada(String codigo, Mapa mapa, double tara) {
		super(codigo, mapa, tara);
		this.eurosPKm = 1.0;
	}
	
	public double coste(String codIni, String codFin) {
		/*
		 * Devuelve el coste de ir desde su ubicacion hasta la
		 * ubicacion del objeto con codigo "codPosDestino"
		 */
		
		double resultado;
		if(this.tara < this.MaxTara) {
			resultado = this.mapa.distancia(codIni, codFin) * this.eurosPKm;
		}else {
			resultado = this.mapa.distancia(codIni, codFin) * this.eurosPKm * 1.10;
		}
		
		return resultado;
	}
	
	public void setEurosPKm(double euros) {
		this.eurosPKm = euros;
	}

}
