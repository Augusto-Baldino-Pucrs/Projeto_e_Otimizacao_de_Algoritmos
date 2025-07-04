import java.util.ArrayList;
import java.util.List;

public class Mochila {
    double capacidade;
    ArrayList<Item> mochila = new ArrayList<>();

    public Mochila(int capacidade) {
        this.capacidade = capacidade;
    }

    public List<Item> guardarGuloso(Mesa mesa) {
        
        int iteracoes = 0;

        while (mesa.itens.size() > 0) {
            Item maiorValor = mesa.itens.get(0);
            for (Item i : mesa.itens) {
                if ((i.valor / i.peso) >= maiorValor.valor / maiorValor.peso) {
                    maiorValor = i;
                }
                iteracoes++;
            }
        
            if (capacidade >= maiorValor.peso) {
                mochila.add(maiorValor);
                capacidade = capacidade - maiorValor.peso;
            }
        
            mesa.itens.remove(maiorValor);
        }
        
        double valorTotal = 0;
        double pesoTotal = 0;
        for (Item item : mochila) {
            valorTotal += item.valor;
            pesoTotal += item.peso;
        }
        System.out.println("Iterações (Gulosa): " + iteracoes);
        System.out.println("Valor total (Gulosa): " + valorTotal);
        System.out.println("Peso total (Gulosa): " + pesoTotal);
        
        
        return mochila;
    }
    public List<Item> guardarForcaBruta(Mesa mesa) {
        int n = mesa.itens.size();
        double melhorValor = 0;
        List<Item> melhorCombo = new ArrayList<>();
    
        int iteracoes = 0;
    
        for (int i = 0; i < (int)Math.pow(2, n); i++) {
            double pesoTotal = 0;
            double valorTotal = 0;
            List<Item> comboAtual = new ArrayList<>();
    
            for (int j = 0; j < n; j++) {
                if ((i / (int)Math.pow(2, j)) % 2 == 1){
                    Item item = mesa.itens.get(j);
                    pesoTotal += item.peso;
                    valorTotal += item.valor;
                    comboAtual.add(item);  
                }
                iteracoes++;
            }
    
            if (pesoTotal <= capacidade && valorTotal > melhorValor) {
                melhorValor = valorTotal;
                melhorCombo = comboAtual;
            }
        }
    
        System.out.println("Iteraçoes: " + iteracoes);
        mochila = new ArrayList<>(melhorCombo);
        mochila = new ArrayList<>(melhorCombo);

        double pesoTotal = 0;
        double valorTotal = 0;
        for (Item item : mochila) {
            pesoTotal += item.peso;
            valorTotal += item.valor;
        }

        System.out.println("Iterações (Força Bruta): " + iteracoes);
        System.out.println("Valor total (Força Bruta): " + valorTotal);
        System.out.println("Peso total (Força Bruta): " + pesoTotal);

        return mochila;
    }
    public List<Item> guardarDinamica(Mesa mesa) {
        int N = mesa.itens.size();
        int C = (int)capacidade;
        int[][] maxTab = new int[N + 1][C + 1];
        int iteracoes = 0;
    
        for (int i = 1; i <= N; i++) {
            Item item = mesa.itens.get(i - 1);
            for (int j = 1; j <= C; j++) {
                if (item.peso <= j) {
                    maxTab[i][j] = Math.max(
                        maxTab[i - 1][j],
                        (int)item.valor + maxTab[i - 1][j - (int)item.peso]
                    );
                } else {
                    maxTab[i][j] = maxTab[i - 1][j];
                }
                iteracoes++;
            }
        }
    
        mochila.clear();
        int j = C;
        for (int i = N; i > 0 && j > 0; i--) {
            if (maxTab[i][j] != maxTab[i - 1][j]) {
                Item item = mesa.itens.get(i - 1);
                mochila.add(item);
                j -= (int)item.peso;
            }
        }
    
        double valorTotal = 0;
        double pesoTotal = 0;
        for (Item item : mochila) {
            valorTotal += item.valor;
            pesoTotal += item.peso;
        }

        System.out.println("Iterações (Programação Dinâmica): " + iteracoes);
        System.out.println("Valor total (Programação Dinâmica): " + valorTotal);
        System.out.println("Peso total (Programação Dinâmica): " + pesoTotal);

        return mochila;
    }

    public String toString() {
        StringBuilder sb = new StringBuilder();
        for (Item item : mochila) {
            sb.append(item.id + ",");
        }
        return sb.toString();
    }
}