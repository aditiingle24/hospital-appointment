#include<iostream>
using namespace std;
int main() {
    int n;
    cin >> n;
    int a[n];
    for (int i = 0; i < n; i++) cin >> a[i];
    int t;
    cin >> t;
    int l = 0, h = n - 1, m;
    while (l <= h) {
        m = l + (h - l) / 2;
        if (a[m] < t) l = m + 1;
        else if (a[m] > t) h = m - 1;
        else {
            cout << m << endl;
            return 0;
        }
    }
    return 0;
}

