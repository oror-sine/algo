use std::{fmt::Write, io::stdin};

fn draw_line(buf: &mut String, i: usize, n: usize) {
    writeln!(buf, "{}{}", " ".repeat(n - i), "*".repeat(1 + (i - 1) * 2)).unwrap();
}

fn main() {
    for line in stdin().lines().take(1) {
        let n: usize = line.unwrap().trim().parse().unwrap();
        let mut output = String::new();

        for i in 1..n {
            draw_line(&mut output, i, n);
        }

        draw_line(&mut output, n, n);

        for i in (1..n).rev() {
            draw_line(&mut output, i, n);
        }

        print!("{}", output);
    }
}
