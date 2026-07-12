package Java;

import java.util.Scanner; 
import java.util.Random;

class HotOrCold {
  public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);
    Random random = new Random();

    int upper = random.nextInt(0,10000);
    int lower = random.nextInt(0, upper);
    int ans = random.nextInt(lower, upper);
    int guesses_left = 10;

    System.out.print("Welcome to Hot or Cold!");
    System.out.println(String.format("Guess the number that I am thinking of. Hint: It is between %s and %s", lower, upper));

    while (true) {
        System.out.println("What is your guess?");
        int guess = scanner.nextInt();

        guesses_left -= 1;

        if (guess > ans) {
            System.out.println("Too Hot!");
            System.out.println(String.format("You have %s guesses left", guesses_left));
        } else if (guess < ans) {
            System.out.println("Too Cold!");
            System.out.println(String.format("You have %s guesses left", guesses_left));
        } else {
            System.out.println("Correct!");
            System.out.println(String.format("You used %s guesses", 10 - guesses_left));
            break;
        }

        if (guesses_left == 0) {
            System.out.println(String.format("You lost! Answer was %s", ans));
            break;
        }
    }
    
    scanner.close();
    
  }
}