int solution(int num) {
    int ans = 0;
    
    while (ans <= 500){
        if (num == 1) 
            return ans;
        
        int r = num % 2;
        num /= 2;
        ++ans;
        
        if (r == 1){
            num = num*3 + 2;
            ++ans;
        }
    }
    
    return -1;
}