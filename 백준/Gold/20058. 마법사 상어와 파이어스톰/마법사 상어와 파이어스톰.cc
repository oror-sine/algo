#include <iostream>
#include <string.h>
#include <queue>
#define R first
#define C second
using namespace std;


int dr[4] = { -1, 1, 0,0 };
int dc[4] = { 0, 0, -1, 1 };
const int MAX = 1 << 6;
const int MAX_SQUARE = MAX_SQUARE * MAX_SQUARE;
int grid[MAX][MAX];
int tmp[MAX][MAX];

int main(){
	ios::sync_with_stdio(0); cin.tie(0);
	int N, Q; cin >> N >> Q;
	N = 1 << N;
	for (int r = 0; r < N; ++r) {
		for (int c = 0; c < N; ++c) {
			cin >> grid[r][c];
		}
	}
	int left_ice = 0;
	for (int q = 0; q < Q; ++q) {
		left_ice = 0;
		int L; cin >> L;
		int step = 1 << L;
		int half_step = step >> 1;
		for (int start_r = 0; start_r < N; start_r += step) {
			for (int  start_c = 0; start_c < N; start_c += step) {
				for (int r = 0; r < step; ++r) {
					for (int c = 0; c < step; ++c) {
						int nr = c;
						int nc = step - r - 1;
						tmp[start_r + nr][start_c + nc] = grid[start_r+r][start_c + c];
					}
				}
			}
		}
		
		for (int r = 0; r < N; ++r) {
			for (int c = 0; c < N; ++c) {
				grid[r][c] = tmp[r][c];
				int cnt = 0;
				for (int i = 0; i < 4; ++i) {
					int nr = r + dr[i];
					int nc = c + dc[i];
					if (nr < 0 || nr >= N || nc < 0 || nc >= N) continue;
					if (tmp[nr][nc]) ++cnt;
				}
				if (cnt < 3 && grid[r][c]) --grid[r][c];
				left_ice += grid[r][c];
			}
		}

	}
	
	memset(tmp, 0, sizeof(tmp));
	
	int max_size = 0;
	for (int r = 0; r < N; ++r) {
		for (int c = 0; c < N; ++c) {
			if (tmp[r][c] || !grid[r][c]) continue;
			queue<pair<int, int>> Q;
			Q.push({ r, c });
			++tmp[r][c];
			int size = 1;
			while (Q.size()) {
				pair<int, int> coord = Q.front(); Q.pop();
				for (int i = 0; i < 4; ++i) {
					int nr = coord.R + dr[i];
					int nc = coord.C + dc[i];
					if (nr < 0 || nr >= N || nc < 0 || nc >= N) continue;
					if (tmp[nr][nc]) continue;
					if (!grid[nr][nc]) continue;
					++tmp[nr][nc];
					++size;
					Q.push({ nr, nc });
				}
			}
			if (size > max_size) {
				max_size = size;
			}
		}
	}
	cout << left_ice << '\n' << max_size;
	return 0;
}

