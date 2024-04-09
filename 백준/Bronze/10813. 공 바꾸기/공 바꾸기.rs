use std::io::stdin;

fn main() {
    let mut buf = String::new();
    stdin().read_line(&mut buf).unwrap();

    let mut nm = buf
        .split_ascii_whitespace()
        .map(|x| x.parse::<u8>().unwrap());

    let n = nm.next().unwrap();
    let _ = nm.next().unwrap();

    let mut balls: Vec<_> = (0..=n).map(|x| x.to_string()).collect();

    for line in stdin().lines() {
        let buf = line.unwrap();
        let mut buf = buf
            .split_ascii_whitespace()
            .map(|x| x.parse::<usize>().unwrap());
        let i = buf.next().unwrap();
        let j = buf.next().unwrap();

        balls.swap(i, j);
    }

    print!("{}", balls[1..].join(" "));
}
