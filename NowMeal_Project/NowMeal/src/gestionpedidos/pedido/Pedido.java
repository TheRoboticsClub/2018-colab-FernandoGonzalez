package gestionpedidos.pedido;

import gestionpedidos.transportes.Transporte;

public class Pedido {
	// CÓDIGO DE APOYO
	private Cliente cliente;
	private PlatoComida[] comidas;
	private Restaurante restaurante;
	private double importe;	
	private Transporte transporte;
	private double peso;
	
	public Pedido(Cliente cliente, PlatoComida[] comidas, Restaurante restaurante) {		
		//Constructor
		this.cliente = cliente;
		this.comidas = comidas;
		this.restaurante = restaurante;
		this.calcularImporte(this.comidas);
		this.calcularPeso(this.comidas);
	}
	
	private void calcularImporte(PlatoComida[] comidas) {
		int size = comidas.length; //Guardo la longitud del array
		double precio = 0.0;
		for(int i = 0; i < size; i++) {
			precio = precio + comidas[i].getPrecio();
		}
		this.importe = precio;
	}
	
	private void calcularPeso(PlatoComida[] comidas) {
		int size = comidas.length; //Guardo la longitud del array
		double peso = 0.0;
		for(int i = 0; i < size; i++) {
			peso = peso + comidas[i].getPeso();
		}
		this.peso = peso;
	}

	
	public double getPeso(){
		//Devuelve el peso total de los platos de comida
		return this.peso;
	}
	
	
	public double coste(Transporte transporte){
		//Devuelve el coste del pedido
		//1.Calculo el coste del transporte desde su ubicacion a la del restaurante
		
		double coste1 = this.transporte.coste(this.restaurante.getCodigo());
		
		//2.Calculo el coste del transporte desde el restaurante al cliente
		double coste2 = this.transporte.coste(this.restaurante.getCodigo(),this.cliente.getCodigo());
		
		return this.importe + coste1 + coste2;
	}
	
	// CÓDIGO DE APOYO
	public double getImporte(){
		return importe;
	}	

	// CÓDIGO DE APOYO
	public Transporte getTransporte() {
		return transporte;
	}

	// CÓDIGO DE APOYO
	public void setTransporte(Transporte transporte) {
		this.transporte = transporte;
	}
	
	// CÓDIGO DE APOYO
	public Cliente getCliente(){
		return cliente;
	}
	
	// CÓDIGO DE APOYO
	public Restaurante getRestaurante(){
		return restaurante;
	}
}