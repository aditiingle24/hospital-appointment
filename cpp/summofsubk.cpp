#include<iostream>
using namespace std;
int main() {
    int n, k;
    cin >> n >> k;
    int a[n];

    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }

    int max_sum = 0, current_sum = 0;

    for (int i = 0; i < k; i++) {
        current_sum += a[i];
    }
    max_sum = current_sum;

    for (int i = k; i < n; i++) {
        current_sum += a[i]; 
        current_sum -= a[i - k];  
        max_sum = max(max_sum, current_sum);
    }

    cout << max_sum;
    return 0;
}

