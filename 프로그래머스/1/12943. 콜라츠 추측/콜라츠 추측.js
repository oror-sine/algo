function solution(num) { 
    let ans = 0;
    
    while (ans <= 500){
        if (num == 1) 
            return ans;
        
        if (num%2) {
            num = (num*3 + 1) / 2;
            ans += 2;
        } else {
            num /= 2;
            ans += 1;
        } 
    }
    
    return -1;
}