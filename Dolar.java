package projetocofrinho;

public class Dolar extends Moedas {
	public Dolar (double va) {
		this.va = va;
	}

	@Override
	// método info
	public void info() {
		System.out.println("Dólar:" + va);
		
	}

	@Override
	// método converter
	public double converter() {
		return this.va*5.2;
		
	}
	@Override
	// identifica e remove apenas uma moeda com o valor selecionado
	public boolean equals(Object objeto) {
		if (this.getClass()!= objeto.getClass()) {
			return false;
		}
		Dolar objDolar = (Dolar) objeto;
		if (this.va != objDolar.va) {
			return false;
		}
		return true;
	}

}
