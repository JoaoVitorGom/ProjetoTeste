package projetocofrinho;

public class Real extends Moedas{
	public Real (double va) {
		this.va = va;
	}

	@Override
	// método info 
	public void info() {
		System.out.println("Real:" + va);
		
	}

	@Override
	// método converter
	public double converter() {
		return this.va;
		
	}
	@Override
	// identifica e remove apenas uma moeda com o valor selecionado
	public boolean equals(Object objeto) {
		if (this.getClass()!= objeto.getClass()) {
			return false;
		}
		Real objReal = (Real) objeto;
		if (this.va != objReal.va) {
			return false;
		}
		return true;
	}

}
