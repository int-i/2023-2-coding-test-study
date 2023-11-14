#include <iostream>
#include <algorithm>

using namespace std;

int nums[1000001];

int main() {
	nums[1] = 0;
	nums[2] = 1;
	nums[3] = 1;
	int n;
	cin >> n;
	for (int i = 4; i < n + 1; i++) {
		int blank = n, blank_1 = n, blank_2 = n;
		if (i % 2 == 0)
			blank = nums[i / 2];
		if (i % 3 == 0)
			blank_1 = nums[i / 3];
		blank_2 = nums[i - 1];
		nums[i] = min(min(blank, blank_1), blank_2) + 1;
	}
	cout << nums[n] << "\n";

}
