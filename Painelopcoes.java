package projetocofrinho;

import java.util.Scanner;

public class Painelopcoes {
private Scanner scan;
private Cofrinho cofrinho;

public Painelopcoes() {
	scan = new Scanner(System.in);
	cofrinho = new Cofrinho();
	
}
// Painel de opções indicando as opções de escolha
public void mostrarPainel() {
	System.out.println("Cofrinho");
	System.out.println("1-Adicionar Moedas");
	System.out.println("2-Remover Moedas");
	System.out.println("3-Listagem de Moedas");
	System.out.println("4-Total convertido em real");
	System.out.println("5-Encerrar o programa");
	String op = scan.next();
	switch(op) {
	// caso a opção 5 seja escolhida o programa será encerrado
	case "5" :
		System.out.println("O Sistema foi encerrado");
		break;
	// caso a opção 1 seja escolhida o programa irá adicionar moedas
	case "1":
	// Menu com as opções de qual tipo de moeda será adicionada
		System.out.println("Escolha Moeda");
		System.out.println("1-Real");
		System.out.println("2-Dólar");
		System.out.println("3-Euro");
		int opMoeda = scan.nextInt();
		// Opção para saber qual o valor da moeda
		System.out.println("Digite o Valor");
		String valorMoeda = scan.next();
		double ValorMoeda = Double.valueOf(valorMoeda);
		Moedas moeda = null;
		// identifica a qual classe, euro, dólar ou real a moeda pertencerá
		if(opMoeda == 1) {
			moeda = new Real(ValorMoeda);
		}else if (opMoeda == 2) {
			moeda = new Dolar(ValorMoeda);
		}else if (opMoeda == 3) {
			moeda = new Euro(ValorMoeda);
		}else {
			System.out.println("Não existe essa opção");
			mostrarPainel();
		}
		// adiciona a moeda escolhida no cofrinho
		cofrinho.adicionar(moeda);
		System.out.println("Moeda adicionada");
		mostrarPainel();
		break;
	case "2":
		// caso a opção 2 seja escolhida o programa irá remover as moedas
		System.out.println("Escolha Moeda");
		System.out.println("1-Real");
		System.out.println("2-Dólar");
		System.out.println("3-Euro");
		int opMoedar = scan.nextInt();
		// identifica qual o valor da moeda a ser removida
		System.out.println("Digite o Valor");
		String valorMoedar = scan.next();
		double ValorMoedar = Double.valueOf(valorMoedar);
		Moedas moedar = null;
		// identifica a qual classe, euro, dólar ou real será a moeda removida
		if(opMoedar == 1) {
			moedar = new Real(ValorMoedar);
		}else if (opMoedar == 2) {
			moedar = new Dolar(ValorMoedar);
		}else if (opMoedar == 3) {
			moedar = new Euro(ValorMoedar);
		}else {
			System.out.println("Não existe essa opção");
			mostrarPainel();
		}
		// remove a moeda do cofrinho
		cofrinho.remover(moedar);
		System.out.println("Moeda removida");
		
		mostrarPainel();
		break;
	// se a opção 3 for escolhida será feita a listagem das moedas
	case "3":
		// exibe a lista de todas as moedas adicionadas
		cofrinho.listagemMoedas();
		mostrarPainel();
		break;
   // se a opção 4 for escolhida será feita a conversão do valor total para reais 
	case "4":
		// converte para reais e mostra o valor total
		double valorConvertido = cofrinho.valorConvertido(); 
		System.out.print("O valor total convertido para real é: " + valorConvertido );
		
		
		mostrarPainel();
		break;
		default:
			System.out.println("Opção Inválida");
			mostrarPainel();
			break;
	}
}
}
