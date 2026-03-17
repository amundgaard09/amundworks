
#include <iostream>
#include <SFML/Graphics.hpp>

int main() {
    std::cout << "Program started\n" << std::endl;
    sf::RenderWindow window(sf::VideoMode({800, 600}), "Particle Sim");

    while (window.isOpen()) {
        while (const std::optional event = window.pollEvent()) {
            if (event->is<sf::Event::Closed>()) {
                window.close();
            }   
        }

        window.clear(sf::Color::Black);
        window.display();
    }
}