import java.io.*;
import java.util.*;

public class ProjectEuler3 {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
         Scanner in = new Scanner(System.in);
		int T = in.nextInt(); // The number of test cases given
		for(int z=0;z<T;z++){
			long N = in.nextLong(); //Given number for which we need to find the largest prime
			long i=0L;
			while(N%2==0){
				N/=2;
			}
			if(N==1){
				System.out.println(2);
			}
			for( i=3;i<=Math.sqrt(N);i+=2){
				while(N%i==0){
					N/=i;
				}
			}
			if(N>=2){
				System.out.println(N);
			}
			else
				System.out.println(i-2);
		}
		in.close();
    }
}