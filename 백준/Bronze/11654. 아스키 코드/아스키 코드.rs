use std::io::stdin;

fn main() {
    let mut buf = String::new();
    stdin().read_line(&mut buf).unwrap();

    for char in buf.trim().chars() {
        println!("{}", char as u8);
    }
}
