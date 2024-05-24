package projetocofrinho;

public class Euro extends Moedas {

	public Euro (double va) {
		this.va = va;
	}

	@Override
	// método info
	public void info() {
		System.out.println("Euro:" + va);
		
	}

	@Override
	// método conerter
	public double converter() {
		return this.va*5.1;
		
	}
	// identifica e remove apenas uma moeda com o valor selecionado
	@Override
	public boolean equals(Object objeto) {
		if (this.getClass()!= objeto.getClass()) {
			return false;
		}
		Euro objEuro = (Euro) objeto;
		if (this.va != objEuro.va) {
			return false;
		}
		return true;
	}
		
	}
	


