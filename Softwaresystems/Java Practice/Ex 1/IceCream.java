//package Ex 1;

public class IceCream {

    public static double calcPrice(int vanilla, int chocolate){
        double cone = 0.70;
        double pricePerScoopVanilla = 1.00;
        double pricePerScoopChocolate = 1.10;
        double x = (vanilla * pricePerScoopVanilla)+(chocolate * pricePerScoopChocolate)+cone;
        //System.out.println(x);
    
        return Math.round(x * 2) / 2.0;
    }
    public static void main(String[] args) {
        int i = 3;
        int j = 5;
    
        System.out.println(calcPrice(i, j));
    
    }
    
    }
