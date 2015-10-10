
import java.util.Arrays;
public class TripleJump{
    //something to keep track of the steps taken

    public static int  TripleJump(int n){ // n being the number of stairs
        // path so count the bottom nodes
        if(n < 0)
            return 0;
        else if(n == 1)
            return 1;
        else
            return TripleJump(n -1) + TripleJump(n-2)+TripleJump(n-3);
    }

    public static int Trip(int n){
            int[] memo = new int [n +1];
            Arrays.fill(memo,-1);
            return n;
    }
    public static int TripT(int n, int[] memo){
        if  ( n < 0)
            return 0;
        else if( n == 0)
            return 1;
        else if (memo[n] > -1)
            return memo[n];
        else{
            memo[n] = TripT(n-1, memo)+ TripT(n-2, memo) + TripT(n-3, memo);
            return memo[n];
        }

    }
    public static void main(String[] args) {
            System.out.println(Trip(4));
    }
}
