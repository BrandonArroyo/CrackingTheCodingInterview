
public class TripleJump{
    //something to keep track of the steps taken

    public static int  TripleJump(int n){ // n being the number of stairs
        // path so count the bottom nodes
        if(n < 0)
            return 0;
        if(n == 1)
            return 1;
        return TripleJump(n -1) + TripleJump(n-2)+TripleJump](n-3);
    }



    public static void main(String[] args) {
            System.out.println(TripleJump(10));





    }
}
