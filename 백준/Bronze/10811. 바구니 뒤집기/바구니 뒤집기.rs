use std::io::stdin;

fn main() {
    let mut nm = String::new();
    stdin().read_line(&mut nm).unwrap();

    let mut nm = nm
        .split_ascii_whitespace()
        .map(|x| x.parse::<u8>().unwrap());
    let n = nm.next().unwrap();
    let _ = nm.next().unwrap();

    let mut baskets: Vec<_> = (0..=n).map(|x| x.to_string()).collect();

    for line in stdin().lines() {
        let ij = line.unwrap();
        let mut ij = ij
            .split_ascii_whitespace()
            .map(|x| x.parse::<usize>().unwrap());
        let i = ij.next().unwrap();
        let j = ij.next().unwrap();
        (&mut baskets[i..=j]).reverse();
    }

    print!("{}", baskets[1..].join(" "));
}
