import java.io.*;
import java.util.*;

public class ProjectEuler1{

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner in = new Scanner(System.in);
        int T =  in.nextInt();
        for(int i=0;i<T;i++){
            long N = in.nextLong();
            long sum = 0L;
            long p=0L;
            p = (N-1)/3;
            sum = (p*(p+1)*3)/2;
            
            p=(N-1)/5;
            sum = sum + (p*(p+1)*5)/2;
            
            p =(N-1)/15;
            sum = sum - (p*(p+1)*15)/2;
            System.out.println(sum);
            
        }
    }
}