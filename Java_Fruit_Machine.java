/*
Java version of the fruit machine project
My first java project, so hopefully doesn't go too badly
*/

import java.util.Random;
import java.util.Scanner;
import java.util.Arrays;

public class Java_Fruit_Machine {
    static int countRepeats(String[] itemsRolled, String toCheck) {
        int count = 0;
        for (int i = 0; i < itemsRolled.length; i++){
            if (itemsRolled[i] == toCheck) {
                count++;
            }
        }
        return count;
    }
    static int winningsCalc(String[] itemsRolled, int winnings, int numberOfReels) {
        int numberOfRepeats = 1;
        String repeatedSymbol = "";
        for (int i = 0; i < itemsRolled.length-1; i++) {
            numberOfRepeats = countRepeats(itemsRolled, itemsRolled[i]);
            if (numberOfRepeats >= numberOfReels-1) {
                repeatedSymbol = itemsRolled[i];
            }
        }
        if (numberOfRepeats == numberOfReels) {
            if (repeatedSymbol == "Skull"){
                return 0;
            }
            else if (repeatedSymbol == "Bell") {
                return winnings + 500;
            }
            else {
                return winnings + 100;
            }
        }
        else if (numberOfRepeats == numberOfReels-1) {
            if (repeatedSymbol == "Skull") {
                return winnings - 100;
            }
            else {
                return winnings + 50;
            }
        }
        else{
            return winnings;
        }
    }
    static String[] spinFruitMachine(String[] symbols, int numberOfReels) {
        String[] itemsArray = {};
        for (int i = 0; i < numberOfReels; i++) {
            Random rand = new Random();
            int x = rand.nextInt(symbols.length);
            itemsArray = Arrays.copyOf(itemsArray, itemsArray.length+1);
            itemsArray[itemsArray.length-1] = symbols[x];
        }
        return itemsArray;
    }
    static int playFruitMachine(int winnings, String[] symbols, int numberOfReels) {
        String[] itemsRolled = spinFruitMachine(symbols, numberOfReels);
        for (int i = 0; i < itemsRolled.length; i++) {
            System.out.println(itemsRolled[i]);
        }
        winnings = winningsCalc(itemsRolled, winnings, numberOfReels);
        return winnings - 20;
    }
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.println("Enter a number of reels:");
        int numberOfReels = input.nextInt();
        int winnings = 100;     // had to do it in pennies because i couldnt get the decimal to round correctly
        String[] symbols = {"Cherry","Bell","Lemon","Orange","Star","Skull"};
        System.out.println("Press enter to play (20p), press any other key then enter to quit");
        String playAgain = input.nextLine();
        while (playAgain == "") {
            winnings = playFruitMachine(winnings, symbols, numberOfReels);
            if (winnings >= 20) {
                System.out.println("You have "+winnings+"p");
                System.out.println("Press enter to play (20p), press any other key then enter to quit");
                playAgain = input.nextLine();
            }
            else {
                System.out.println("You lose");
                playAgain = "nope";
            }
        System.out.println("thank you for playing, you won "+winnings+"p in total!");
        }
    }
}