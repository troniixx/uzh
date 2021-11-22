public class arithmetic {
//a - (b^2 / (c - d * (a + b)))`

public static void main(String[] args) {
    int a = 1;
    int b = 2;
    int c = 3;
    int d = 4;

    double x = a-(Math.pow(b, 2) / (c - d * (a + b)));

    System.out.println(x);
}
}
