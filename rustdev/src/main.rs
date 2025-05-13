

fn has3asfactor(num: i32) -> bool {
    num % 3 == 0
}
fn main() {
    let mut counter: i32 = 1;
    while counter <= 100000 {
        if counter % 2 == 0 {
            println!("{} is even", counter);
        } else {
            println!("{} is odd", counter);
        }
        if has3asfactor(counter) {
                println!("Number is divisible by 3");
            }
        counter += 1;
    }
    println!("Ferdig"); 
}