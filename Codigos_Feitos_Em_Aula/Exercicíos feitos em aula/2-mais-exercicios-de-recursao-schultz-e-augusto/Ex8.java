import java.util.ArrayList;
import java.util.List;

public class Ex8 {
    public int findBiggest(List<Integer> array){
        if(array.size() < 2){
            return array.get(0);
        }
        int n0 = array.get(0);
        int n1 = array.get(1);
        if(n0 < n1){
            return findBiggest(array.subList(1, array.size()));
        }
        else{
            List<Integer> newArray = new ArrayList<>(array);
            newArray.set(1, n0);
            return findBiggest(newArray.subList(1, newArray.size()));
        }
    }
}

//[4, 5, 2, 8, 3, 9, 1]
