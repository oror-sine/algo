use std::io;

fn main() {
    let mut buf = String::new();
    io::stdin().read_line(&mut buf).unwrap();

    let mut cnts = [0; 9];

    for num in buf.trim().chars() {
        let num = num.to_digit(10).unwrap() as usize;
        match num {
            9 => cnts[6] += 1,
            num => cnts[num] += 1,
        }
    }
    cnts[6] = (cnts[6] + 1) >> 1;

    let ans = *cnts.iter().max().unwrap();
    println!("{ans}");
}
