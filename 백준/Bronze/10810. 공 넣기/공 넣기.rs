use std::io::stdin;

fn main() {
    let mut input = String::new();
    stdin().read_line(&mut input).unwrap();

    let mut input = input
        .split_ascii_whitespace()
        .map(|x| x.parse::<usize>().unwrap());

    let n = input.next().unwrap();
    let _ = input.next().unwrap();

    let mut balls = vec!["0".to_owned(); n + 1];

    for line in stdin().lines() {
        let buf = line.unwrap();
        let mut ijk = buf.split_ascii_whitespace();

        let i: usize = ijk.next().unwrap().parse().unwrap();
        let j: usize = ijk.next().unwrap().parse().unwrap();
        let k = ijk.next().unwrap();

        for idx in i..=j {
            balls[idx] = k.to_owned();
        }
    }

    print!("{}", balls[1..].join(" "));
}
