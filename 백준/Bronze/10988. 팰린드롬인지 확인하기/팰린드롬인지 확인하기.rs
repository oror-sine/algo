use std::io::stdin;

fn main() {
    let mut buf = String::new();
    stdin().read_line(&mut buf).unwrap();
    let buf = buf.trim();

    for (a, b) in buf.chars().zip(buf.chars().rev()).take(buf.len() / 2) {
        if a != b {
            print!("{}", 0);
            return;
        }
    }

    print!("{}", 1);
}
