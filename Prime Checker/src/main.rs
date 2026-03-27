
use std::{io};

fn main() {
    println!("How many integers do you want to check for primes?:");

    let mut primevector: Vec<i32> = Vec::new();
    let mut input: String = String::new();

    io::stdin()
        .read_line(&mut input)
        .expect("Failed to read line"); 

    let number: i32 = input
        .trim()
        .parse()
        .expect("Invalid integer input");

    for i in 1..=number {
        let prime: bool = are_you_prime(i);
        if prime {
            primevector.push(i);
        }
    }

    for prime in primevector {
        println!("{}", prime);
    }
}

fn are_you_prime(number: i32) -> bool {
    if number <= 1 {
        return false;
    }

    for i in 2..number {
        if number % i == 0 {
            return false;
        } else {
            continue;
        }
    }
    true
}