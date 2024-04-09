use std::io::stdin;

fn main() {
    let mut buf = String::new();
    stdin().read_line(&mut buf).unwrap();

    let v: Vec<i32> = buf
        .split_ascii_whitespace()
        .map(|x| x.parse().unwrap())
        .collect();

    if let [a, b] = v[..] {
        let ans = match a {
            a if a > b => ">",
            a if a < b => "<",
            _ => "==",
        };

        print!("{}", ans);
    }
}
