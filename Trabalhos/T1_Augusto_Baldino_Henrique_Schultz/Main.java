import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Entrada das duas strings
        System.out.println("Digite a primeira string:");
        String s1 = scanner.nextLine();

        System.out.println("Digite a segunda string:");
        String s2 = scanner.nextLine();

        System.out.println("\n=== Executando LCS Recursivo ===");
        executarRecursivo(s1, s2);

        System.out.println("\n=== Executando LCS Dinâmico ===");
        executarDinamico(s1, s2);

        scanner.close();
    }

    private static void executarRecursivo(String s1, String s2) {
        LCSRecursivo.chamadas = 0;
        long inicio = System.nanoTime();
        int resultado = LCSRecursivo.lcsRecursivo(s1, s2, s1.length(), s2.length());
        long fim = System.nanoTime();
    
        double tempoSegundos = (fim - inicio) / 1e9;
    
        System.out.println("Comprimento da LCS (Recursivo): " + resultado);
        System.out.println("Número de chamadas recursivas: " + LCSRecursivo.chamadas);
        System.out.printf("Tempo de execução: %.6f segundos\n", tempoSegundos);
    }
    
    private static void executarDinamico(String s1, String s2) {
        long inicio = System.nanoTime();
        int resultado = LCSDinamico.lcsDinamico(s1, s2);
        long fim = System.nanoTime();
    
        double tempoSegundos = (fim - inicio) / 1e9;
    
        System.out.println("Comprimento da LCS (Dinâmico): " + resultado);
        System.out.println("Número de iterações: " + LCSDinamico.iteracoes);
        System.out.printf("Tempo de execução: %.6f segundos\n", tempoSegundos);
    }
    
}
