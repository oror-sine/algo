use std::io::stdin;

fn main() {
    let mut buf = String::new();
    stdin().read_line(&mut buf).unwrap();

    let year: i16 = buf.trim().parse().unwrap();

    let ans = if (year % 400 == 0) || (year % 4 == 0 && year % 100 != 0) {
        1
    } else {
        0
    };

    print!("{}", ans);
}
