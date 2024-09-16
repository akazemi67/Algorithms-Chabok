// Problem's Link: https://quera.org/problemset/170167

#include <iostream>
#include <vector>
#include <iomanip>
#include <cmath>

using namespace std;

int main() {
    int n;

    cin >> n;
    vector<long double> nums(n, 0);
	for(int i=0; i<n; i++){
        cin >> nums[i];
		nums[i] *= pow(10, 12);
	}

    long double prev = 0;
    for(int i=n-1; i>=0; i--){
        nums[i] += prev;

        if(i > 0){
            long double part = nums[i]/i;
            prev += part;
        }
    }

    for(int i=0; i<n; i++){
        cout << std::fixed << std::showpoint << std::setprecision(5) << nums[i]/pow(10, 12) << " ";
    }

    return 0;
}
