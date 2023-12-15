let line = 0;
const input = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "./BOJ/1406/input.txt")
  .toString()
  .split("\n");

const stack_l = Array.from(input[line++]);
const stack_r = [];
const M = input[line++];

while (line < input.length) {
  const command = input[line++];
  switch (command) {
    case "L":
      if (stack_l.length) stack_r.push(stack_l.pop());
      break;
    case "D":
      if (stack_r.length) stack_l.push(stack_r.pop());
      break;
    case "B":
      if (stack_l.length) stack_l.pop();
      break;
    default:
      stack_l.push(command[2]);
      break;
  }
}
while (stack_r.length > 0) stack_l.push(stack_r.pop());

console.log(stack_l.join(""));
