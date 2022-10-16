import java.util.Scanner;



public class WhileNest {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);  
        System.out.print("Please enter n: "); 
        int n = sc.nextInt(); 

        int row = 1;
        while(row <= n){
            int column = 1;
            while (column <= row){
                System.out.print("*");
                column++;
            }

            System.out.print("\n");
            row++;
            
        }
        
    }
}




