import java.util.ArrayList;

class Mesa {
    public ArrayList<Item> itens;

    public Mesa() {
        this.itens = new ArrayList<>();
    }

    public void cria1() {
        // Pesos:  23, 31, 29, 44, 53, 38, 63, 85, 89, 82
        // Valores: 92, 57, 49, 68, 60, 43, 67, 84, 87, 72
        
        Item item1 = new Item(1, 23, 92);
        Item item2 = new Item(2, 31, 57);
        Item item3 = new Item(3, 29, 49);
        Item item4 = new Item(4, 44, 68);
        Item item5 = new Item(5, 53, 60);
        Item item6 = new Item(6, 38, 43);
        Item item7 = new Item(7, 63, 67);
        Item item8 = new Item(8, 85, 84);
        Item item9 = new Item(9, 89, 87);
        Item item10 = new Item(10, 82, 72);
        
        itens.add(item1);
        itens.add(item2);
        itens.add(item3);
        itens.add(item4);
        itens.add(item5);
        itens.add(item6);
        itens.add(item7);
        itens.add(item8);
        itens.add(item9);
        itens.add(item10);
    }

    public void cria2(){
        // Pesos:  56, 59, 80, 64, 75, 17
        // Valores: 50, 50, 64, 46, 50, 05

        Item item1 = new Item(1, 56, 50);
        Item item2 = new Item(2, 59, 50);
        Item item3 = new Item(3, 80, 64);
        Item item4 = new Item(4, 64, 46);
        Item item5 = new Item(5, 75, 50);
        Item item6 = new Item(6, 17, 05);

        itens.add(item1);
        itens.add(item2);
        itens.add(item3);
        itens.add(item4);
        itens.add(item5);
        itens.add(item6);
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        for (Item item : itens) {
            sb.append("(").append(item.peso).append("/").append(item.valor).append(") ");
        }
        return sb.toString();
    }
}