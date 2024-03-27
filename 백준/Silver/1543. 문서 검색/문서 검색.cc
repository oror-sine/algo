#include <iostream>
#include <string>
using namespace std;

int main() {
	string s, p;
	getline(cin, s);
	getline(cin, p);
	int cnt = 0;
	int pos = s.find(p);
	while (pos != -1) {
		++cnt;
		pos = s.find(p, pos + p.size());
	}
	cout << cnt;
	return 0;
}