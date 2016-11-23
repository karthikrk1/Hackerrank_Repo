import java.io.*;
import java.util.*;

public class ProjectEuler2 {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner in = new Scanner(System.in);
        int T = in.nextInt(); //Number of test cases stored as int for convinience.
        for(int i=0;i<T;i++){ //Looping over the test cases
            long N = in.nextLong(); //The limit until to loop
            long f1=1L, f2=2L;
            long sum=0L, output=2L;
            while((f1+f2)<N){
                sum=f1+f2;
                f1=f2;
                f2=sum;
                if(sum%2==0)
                    output+=sum;
            }
            //sum=0L;
            System.out.println(output);
        }
    }
}