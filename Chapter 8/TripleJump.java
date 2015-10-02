
public class TripleJump{
    //something to keep track of the steps taken

    public static int  TripleJump(int n){ // n being the number of stairs
        //1 step
        //Base cases
        if(n < 0 )
            return 0;
        else if ( n == 0)
            return 1;
        else
            return TripleJump(n-1) +TripleJump(n-2) +TripleJump(n-3);
    }



    public static void main(String[] args) {
            System.out.println(TripleJump(10));





    }
}
