public class fizzbuzz {
    public static void main(String[] args) {
        int n = 50;

        if( n % 3 == 0 && n % 5 != 0){
            System.out.println("Fizz");
        }
        else if(n % 5 == 0 && n % 3 != 0){
            System.out.println("Buzz"); 
        }
        else if(n % 3 == 0 && n % 5 == 0){
            System.out.println("FizzBuzz");
        }
        else {System.out.println(n);
        }

    }
}
