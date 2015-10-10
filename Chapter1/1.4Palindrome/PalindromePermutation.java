import java.util.*;

public class PalindromePermutation{
     static ArrayList<String> perms = new ArrayList<String>() ;
     static ArrayList<String> permsNew = new ArrayList<String>() ;

     public static void permutation(String str) {
      permutation("", str);
  }

  private static void permutation(String prefix, String str) {
      int n = str.length();
      if (n == 0)
          perms.add(prefix);
      else {
          for (int i = 0; i < n; i++){

              permutation(prefix + str.charAt(i), str.substring(0, i) + str.substring(i+1, n));
          }
      }
  }
  public static boolean checkPalin(String s){
      for(int j = 0; j < s.length()  ; ++j){
        //   System.out.println(s);
        //     System.out.println("s: "+s.charAt(j));
        //     System.out.println("s2: "+s.charAt(s.length() -1-j));
          if((s.charAt(j) != s.charAt(s.length() -1-j))){
              return false;
          }

    }
        return true;

  }

    public static void main(String[] args) {
        permutation("tet");
        for(int i = 0; i < perms.size(); ++i){
            if(checkPalin(perms.get(i))){
            
                permsNew.add(perms.get(i));
            }
        }
        for(int i = 0 ; i < permsNew.size();i++)
            System.out.println(permsNew.get(i));
    }
}
