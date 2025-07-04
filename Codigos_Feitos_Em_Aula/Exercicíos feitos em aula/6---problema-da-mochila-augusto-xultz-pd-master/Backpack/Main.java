public class Main {
    public static void main(String[] args) {
        Mesa mesa = new Mesa();
        Mochila mochila = new Mochila(190);
        mesa.cria2();
        System.out.println(mesa.toString());

        mochila.guardarDinamica(mesa);


        System.out.println(mochila.toString());
    }
}