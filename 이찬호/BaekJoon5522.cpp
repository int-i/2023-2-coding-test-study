#include <iostream>

using namespace std;

int main() {
	int score[5] = { };
	int sum = 0;

	for (int i = 0; i < 5; i++)
	{
		cin >> score[i];
		sum += score[i];
	}
	printf("%d", sum);
}