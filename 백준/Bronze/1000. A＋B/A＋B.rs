use std::io::stdin;

fn main() {
    let mut buf = String::new();
    stdin().read_line(&mut buf).unwrap();

    let mut inputs = buf
        .split_ascii_whitespace()
        .map(|x| x.parse::<u8>().unwrap());
    
    let a = inputs.next().unwrap();
    let b = inputs.next().unwrap();

    print!("{}", a + b);
}
