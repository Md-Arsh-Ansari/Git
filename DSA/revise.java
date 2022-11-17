import java.util.Scanner;



public class WhileNest {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);  
        System.out.print("Please enter a number: "); 
        int num = sc.nextInt(); 

        int dubba = 0;
        int hand = 1;
        while(hand <= num){
            dubba = dubba + hand;
            hand += 1;
            }

            System.out.println("The sum from 1 to " + num + " = " + dubba);
            
        }
        
    }




