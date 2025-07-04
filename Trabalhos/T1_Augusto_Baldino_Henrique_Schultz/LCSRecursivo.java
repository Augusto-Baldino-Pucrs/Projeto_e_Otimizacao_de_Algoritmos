public class LCSRecursivo{

    static int chamadas = 0;

    public static int lcsRecursivo(String s1, String s2,int m, int n){
        chamadas++;

        if(m==0 || n==0){
            return 0;
        }

        if(s1.charAt(m-1) == s2.charAt(n-1)){
            return 1 + lcsRecursivo(s1,s2,m-1,n-1);
        } else{
            return Math.max(lcsRecursivo(s1, s2, m-1, n), lcsRecursivo(s1, s2, m, n-1));
        }
    }
}