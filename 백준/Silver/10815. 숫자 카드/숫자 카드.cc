#include <iostream>
#include <map>
using namespace std;

int main(){
	ios::sync_with_stdio(0); cin.tie(0);

	int N, buf; 
	map<int, int> m;
	
	cin >> N;
	for (; N > 0; --N) {
		cin >> buf;
		++m[buf];
	}

	cin >> N;
	for (; N > 0; --N) {
		cin >> buf;
		cout << (m[buf] ? 1 : 0) << ' ';
	}

	return 0;
}