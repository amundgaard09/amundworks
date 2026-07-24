
#include <unordered_map>
#include <iostream>
#include <string>
#include <vector>

int _int_clip(int value, int upper, int lower) {
    if (value > upper) { return upper; }
    else if (value < lower) { return lower; }
    else { return value; }
}

int main() {
    int diff;
    int n_guesses = 0;
    int n_incorrect_guesses = 0;
    bool complete = false;
    char guessed_char;

    std::string guessed_word;
    std::string actual_word;
    std::unordered_map<int, std::vector<std::string>> word_db = {
        {3, {"cat", "dog", "sun", "hat", "run", "big", "cup"}},
        {4, {"tree", "frog", "jump", "wind", "fire", "lamp", "duck"}},
        {5, {"apple", "brick", "cloud", "flame", "grape", "piano", "stone"}},
        {6, {"bridge", "candle", "flight", "jungle", "mirror", "rocket", "castle"}},
        {7, {"battery", "blanket", "captain", "dolphin", "emperor", "fantasy", "lantern"}},
        {8, {"aircraft", "backpack", "calendar", "dinosaur", "elephant", "firework", "goldfish"}},
        {9, {"adventure", "bookshelf", "chocolate", "dandelion", "evergreen", "flagstone", "grassland"}},
        {10,{"strawberry", "accomplish", "birthplace", "changeable", "discretion", "earthquake", "floorboard"}}
    };

    std::cout << "Welcome to Hangman!" << std::endl;
    std::cout << "Select the Word Length (3 - 10): " << std::endl;
    std::cin >> diff;

    diff = _int_clip(diff, 10, 3);

    std::string guessed_letters;
    std::vector<std::string>& word_list = word_db[diff];
    actual_word = word_list[rand() % word_list.size()];
    std::string guess_word(actual_word.length(), '_');

    while (!complete) {
        std::cout << "Input your guess letter: " << std::endl;
        std::cin >> guessed_char;

        guessed_letters += guessed_char;

        if (actual_word.find(guessed_char) != std::string::npos) {
            for (int i = 0; i < actual_word.length(); i++) {
                if (actual_word[i] == guessed_char) {
                    guess_word[i] = guessed_char;
                }
            }

            std::cout << "Correct Guess!"  << std::endl;
            std::cout << "Word: " << guess_word << std::endl;
            std::cout << "Guessed Letters: " << guessed_letters << std::endl;

        } else {
            n_incorrect_guesses += 1;
            std::cout << "Incorrect Guess!"  << std::endl;
            std::cout << "Word: " << guess_word << std::endl;
            std::cout << "Guessed Letters: " << guessed_letters << std::endl;
        }

        if (guess_word == actual_word && n_incorrect_guesses < 7) {
            std::cout << "You won! Word was: " << actual_word << std::endl;
            complete = true;
        }

        if (n_incorrect_guesses > 6) {
            std::cout << "Game Over!" << std::endl;
            complete = true;
        }

        n_guesses++;
    }

    return 0;
}
