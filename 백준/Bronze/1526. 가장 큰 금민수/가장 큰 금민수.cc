#include <iostream>
using namespace std;


int main() {
	int n;
	cin >> n;
	for (int i = n; i >= 4; i--) {
		int numerator = i;
		int flag = false;
		while (numerator != 0) {
			if (numerator % 10 == 4 || numerator % 10 == 7) {
				numerator /= 10;
			}
			else {
				flag = true;
				break;
			}
		}
		if (!flag) {
			cout << i;
			return 0;
		}
	}
	return 0;
}