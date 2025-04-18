#include <iostream>
using namespace std;

int main()
{
    int t, n, m, l, r;
    cin >> t;
    while (t--)
    {
        cin >> n >> m >> l >> r;
        int k = m <= -l ? m : -l;
        cout << -k << ' ' << m - k << '\n';
    }
    return 0;
}
