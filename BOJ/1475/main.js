const input = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "./BOJ/1475/input.txt")
  .toString()
  .trim();

const cnts = Array(9).fill(0);
for (num of input) {
  cnts[num === "9" ? 6 : Number(num)]++;
}
cnts[6] = (cnts[6] + 1) >> 1;

console.log(Math.max(...cnts));
