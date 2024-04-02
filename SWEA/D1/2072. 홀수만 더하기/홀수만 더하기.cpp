#include <iostream>
using namespace std;

int main(){
	ios::sync_with_stdio(0); cin.tie(0);
	int T; cin >> T;

	for (int t = 1; t <= T; ++t) {
		cout << '#' << t << ' ';

		int ans = 0;

		for (int i = 0; i < 10; ++i) {
			int N; cin >> N;

			if (N % 2 == 1) 
				ans += N;
		}

		cout << ans << '\n';
	}

	return 0;
}
