use std::io::stdin;

fn main() {
    let mut buf = String::new();
    stdin().read_line(&mut buf).unwrap();

    let v: Vec<i8> = buf
        .split_ascii_whitespace()
        .map(|x| x.parse().unwrap())
        .collect();

    if let [h, m] = v[..] {
        let (h, m) = match () {
            _ if m >= 45 => (h, m - 45),
            _ if h > 0 => (h - 1, m + 15),
            _ => (23, m + 15),
        };

        print!("{} {}", h, m);
    }
}
