const input = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "./BOJ/2583/input.txt")
  .toString()
  .split("\n");

let line = 0;
const [M, N, K] = input[line++].split(" ").map(Number);
const arr = Array.from(Array(M), () => Array(N).fill(0));

while (line <= K) {
  const [sc, sr, ec, er] = input[line++].split(" ").map(Number);
  for (let r = sr; r < er; r++) {
    for (let c = sc; c < ec; c++) {
      arr[r][c] = true;
    }
  }
}

const dr = [0, 0, -1, 1];
const dc = [-1, 1, 0, 0];
const areas = [];

for (let r = 0; r < M; r++) {
  for (let c = 0; c < N; c++) {
    if (arr[r][c]) continue;

    const stack = [{ r, c }];
    arr[r][c] = true;
    let area = 1;

    while (stack.length > 0) {
      const { r, c } = stack.pop();
      for (let i = 0; i < 4; i++) {
        const nr = r + dr[i];
        const nc = c + dc[i];
        if (!(nr <= -1 || M <= nr || nc <= -1 || N <= nc) && !arr[nr][nc]) {
          stack.push({ r: nr, c: nc });
          arr[nr][nc] = true;
          area++;
        }
      }
    }
    areas.push(area);
  }
}

console.log(`${areas.length}\n${areas.sort((a, b) => a - b).join(" ")}`);
