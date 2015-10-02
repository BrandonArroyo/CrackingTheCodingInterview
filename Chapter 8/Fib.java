public class Fib{

    public static int fib( int x ){
        if( x == 0)
            return 0;
        if( x == 1)
            return 1;
        return fib(x - 1) + fib(x -2);
    }
//---------SMARTER WAYS---------
    public static int fibOne(int n){
        return fibSmart(n, new int[n + 1 ]);
    }
    public static int fibSmart(int x, int[] memo){
        if(x == 0 || x == 1) return x;
        if(memo[x] == 0)
            memo[x] = fibSmart(x - 1, memo) + fibSmart(x -2,memo);

        return memo[x];
    }
//-----------------------------------------------------------------
public static int fibon(int n ){
    if(n == 0 ) return 0;
    else if (n == 1) return 1;

    int[] memo = new int[n];
    memo[0 ] = 0;
    memo[1] = 1;
    for(int i = 2; i < n ; ++ i)
        memo[i] = memo[i-1] + memo[i - 2];
    return memo[n-1] + memo[n-2];
}

    public static void main(String[] args) {
        System.out.println(fib(4));
        System.out.println(fibOne(20));
        System.out.println(fibon(20));

    }
}
