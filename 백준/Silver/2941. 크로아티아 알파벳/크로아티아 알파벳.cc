#include <iostream>
#include <string>
using namespace std;

int main() {
	string s; cin >> s;
	string dictionary[8] = { "c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z=" };
	for (auto key : dictionary) {
		int pos = s.find(key);
		while (pos != string::npos) {
			s.replace(pos, key.size(), "0");
			pos = s.find(key, pos + 1);
		}
	}
	cout << s.size();
}