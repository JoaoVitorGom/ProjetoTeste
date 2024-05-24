package projetocofrinho;
import java.util.ArrayList;
public class Cofrinho {
	private ArrayList<Moedas> listaMoedas;
	public Cofrinho() {
		this.listaMoedas = new ArrayList<>();
		
	}
	// método de adicionar moedas
	public void adicionar(Moedas moeda) {
		this.listaMoedas.add(moeda);
	
		
	}
	// método de remover moedas
	public void remover(Moedas moeda) {
		this.listaMoedas.remove(moeda);
	}
	// método de listar moedas
	public void listagemMoedas() {
		
		if (this.listaMoedas.isEmpty()) {
			System.out.print("Cofrinho vazio");
		return ;
	}
	
		for(Moedas moeda : this.listaMoedas) {
		moeda.info();	
		}
	}
	// método de converter o valor total para reais 
	public double valorConvertido() {
		if(this.listaMoedas.isEmpty()) {
			return 0;	
			
		}
		double ValorSomado = 0;
		for (Moedas moeda : this.listaMoedas) {
			ValorSomado = ValorSomado + moeda.converter();
		}
		return ValorSomado;
	}

}

	


