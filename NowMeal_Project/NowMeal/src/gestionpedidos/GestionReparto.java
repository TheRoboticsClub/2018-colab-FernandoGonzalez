package gestionpedidos;

import gestionpedidos.mapa.*;
import gestionpedidos.pedido.Pedido;
import gestionpedidos.transportes.Transporte;

public class GestionReparto {
	// CÓDIGO DE APOYO

	private final int NumeroGestores = 4;
	
	private GestionRepartoLocal[] gestoresLocales;
	private Mapa mapa;
	
	public GestionReparto(Mapa mapa){
		//Constructor
		this.mapa = mapa;
		//Creo los cuatro gestores de reparto locales
		this.gestoresLocales = new GestionRepartoLocal[this.NumeroGestores];
	}
	
	//CÓDIGO DE APOYO
	public Mapa getMapa() {
		return mapa;
	}
	
	// CÓDIGO DE APOYO
	public String getEstadoGestorLocal(int i){
		return this.gestoresLocales[i].getDisponibles() + this.gestoresLocales[i].getEsperando();
	}
	
	// CÓDIGO DE APOYO
	public String getEstadoGestorLocalNum(int i){
		return this.gestoresLocales[i].getCodMotosDisponibles().size() + ";" +
				this.gestoresLocales[i].getCodFurgoDisponibles().size() + ";" +
				this.gestoresLocales[i].getCodEsperandoMoto().size() + ";" +
				this.gestoresLocales[i].getCodEsperandoFurgo().size() ;
	}
	
	private int cuadrante(PosicionXY pos) {
		int cuad = -1;
		if(pos.getX() <= this.mapa.getMaxCoordX() / 2) {
			if(pos.getY()<= this.mapa.getMaxCoordY() / 2) {
				cuad = 0;
			}else {
				cuad = 1;
			}
		}else if(pos.getX() > this.mapa.getMaxCoordX() / 2) {
			if(pos.getY() <= this.mapa.getMaxCoordY() / 2) {
				cuad = 2;
			}else {
				cuad = 3;
			}
		}
		return cuad;
	}
	
	//PRE: el transporte no ha sido asignado a ninguna zona
	public void addTransporteLocalidad(Transporte transporte) {
		/*añade el transporte dado al gestor de reparto local que le 
		 * corresponde por su ubicación en el mapa llamando al metodo 
		 * "add" de la clase "GestionRepartoLocal"
		 */
		PosicionXY pos = this.mapa.getPosicion(transporte.getCodigo());
		int cuadrante = this.cuadrante(pos); //Obtengo el cuadrante en el que se encuentra el transporte
		if(cuadrante != -1) {
			this.gestoresLocales[cuadrante].add(transporte);
		}else {
			System.out.println("Error! Cuadrante no calculado correctamente");
		}
	}
		
	//PRE: el pedido no tiene asignado ningún transporte
	public void asignarPedido(Pedido pedido){
		/*
		 *asigna el pedido dado al gestor de reparto local que le corresponde por su ubicación en el mapa
		 *llamando al metodo "asignarPedido" de la clase "GestionRepartoLocal"
		 */
		PosicionXY pos = this.mapa.getPosicion(pedido.getTransporte().getCodigo());
		int cuadrante = this.cuadrante(pos); //Obtengo el cuadrante en el que se encuentra el pedido
		if(cuadrante != -1) {
			this.gestoresLocales[cuadrante].asignarPedido(pedido);
		}else {
			System.out.println("Error! Cuadrante no calculado correctamente");
		}
	}
	
	//PRE: el pedido tiene asignado un transporte
	public void notificarEntregaPedido(Pedido pedido){
		/*
		 *Notifica la entrega del pedido al gestor de reparto local que le
		 *corresponde por su ubicacion en el mapa llamando al metodo
		 *"notificarEntregaPedido" de la clase "GestionRepartoLocal" 
		 */
		PosicionXY pos = this.mapa.getPosicion(pedido.getTransporte().getCodigo());
		int cuadrante = this.cuadrante(pos); //Obtengo el cuadrante en el que se encuentra el pedido
		if(cuadrante != -1) {
			this.gestoresLocales[cuadrante].notificarEntregaPedido(pedido);
		}else {
			System.out.println("Error! Cuadrante no calculado correctamente");
		}
	}
	
}