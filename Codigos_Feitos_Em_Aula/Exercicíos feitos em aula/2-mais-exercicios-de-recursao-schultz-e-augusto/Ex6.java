public class Ex6 {
    public String intToBinary(int n){
        if(n == 1){
            return "1";
        }
        return intToBinary(n/2) + "" + n%2;
    }
}
