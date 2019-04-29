package gestionpedidos.transportes;

import gestionpedidos.mapa.Mapa;

public class FurgonetaPropia extends Furgoneta {
	
	double velocidadMedia;
	private final double EUROS_P_HORA = 40.0;
	private final double MaxTara = 500.0; //Tara maxima. Se usa en el metodo "coste"
	
	public FurgonetaPropia(String codigo, Mapa mapa, double tara) {
		super(codigo, mapa, tara);
		this.velocidadMedia = 30;
	}
	
	public double coste(String codIni, String codFin) {
		/*
		 * Devuelve el coste de ir desde su ubicacion hasta la
		 * ubicacion del objeto con codigo "codPosDestino"
		 */
		
		double resultado;
		if(this.tara < this.MaxTara) {
			resultado = this.mapa.distancia(codIni, codFin) * this.EUROS_P_HORA / this.velocidadMedia;
		}else {
			resultado = this.mapa.distancia(codIni, codFin) * this.EUROS_P_HORA / (this.velocidadMedia * 1.10);
		}
		
		return resultado;
	}
	
	public void setVelocidadMedia(double vel) {
		this.velocidadMedia = vel;
	}

}
