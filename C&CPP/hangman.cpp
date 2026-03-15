
#include <unordered_map>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main() {
    int Difficulty;
    int GuessCount = 0;
    int IncorrectGuessCount = 0;

    bool GameComplete = false;

    char GuessedLetter;

    string GuessedWord;
    string ActualWord;
    unordered_map<int, vector<string>> WordDatabase = {
        {3, {"cat", "dog", "sun", "hat", "run", "big", "cup"}},
        {4, {"tree", "frog", "jump", "wind", "fire", "lamp", "duck"}},
        {5, {"apple", "brick", "cloud", "flame", "grape", "piano", "stone"}},
        {6, {"bridge", "candle", "flight", "jungle", "mirror", "rocket", "castle"}},
        {7, {"battery", "blanket", "captain", "dolphin", "emperor", "fantasy", "lantern"}},
        {8, {"aircraft", "backpack", "calendar", "dinosaur", "elephant", "firework", "goldfish"}},
        {9, {"adventure", "bookshelf", "chocolate", "dandelion", "evergreen", "flagstone", "grassland"}},
        {10, {"strawberry", "accomplish", "birthplace", "changeable", "discretion", "earthquake", "floorboard"}}
    };

    cout << "Welcome to Hangman!\n";
    cout << "Select the Word Length (3 - 10): ";
    cin >> Difficulty;

    string GuessedLetters;
    vector<string>& WordList = WordDatabase[Difficulty];
    ActualWord = WordList[rand() % WordList.size()];
    string GuessWord(ActualWord.length(), '_');

    while (!GameComplete) {
        cout << "Input your guess letter: ";
        cin >> GuessedLetter;

        GuessedLetters += GuessedLetter;

        if (ActualWord.find(GuessedLetter) != string::npos) {
            for (int i = 0; i < ActualWord.length(); i++) {
                if (ActualWord[i] == GuessedLetter) {
                    GuessWord[i] = GuessedLetter;
                }
            }

            cout << "Correct Guess!\n";
            cout << "Word: " << GuessWord << "\n";
            cout << "Guessed Letters: " << GuessedLetters << "\n";


        } else {
            IncorrectGuessCount += 1;
            cout << "Incorrect Guess!\n";
            cout << "Word: " << GuessWord << "\n";
            cout << "Guessed Letters: " << GuessedLetters << "\n";
        }

        if (GuessWord == ActualWord && IncorrectGuessCount < 7) {
            cout << "You won! Word was: " << ActualWord;
            GameComplete = true;
        }

        if (IncorrectGuessCount > 6) {
            cout << "Game Over!\n";
            GameComplete = true;
        }

        GuessCount++;
    }

    return 0;
}

