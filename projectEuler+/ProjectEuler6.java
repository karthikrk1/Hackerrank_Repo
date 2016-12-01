import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class ProjectEuler6{

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner in = new Scanner(System.in);
        int T = in.nextInt(); // This is the number of test cases
        for(int i=0;i<T;i++){
            long N = in.nextLong(); //This is the limit of the series
            long sum = N*(N+1)/2;
            long sumSq = sum*sum;
            long sqSum = (((2*N)+1)*sum)/3;
            long diff = Math.abs(sqSum-sumSq);
            System.out.println(diff);
        }
    }
}