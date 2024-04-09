use std::io::stdin;

fn main() {
    let mut input = String::new();
    stdin().read_line(&mut input).unwrap();

    let input: usize = input.trim().parse().unwrap();

    print!("{}", "long ".repeat(input / 4) + "int");
}
