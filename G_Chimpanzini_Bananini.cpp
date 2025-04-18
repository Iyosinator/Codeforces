#include <iostream>
#include <deque>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin >> t;
    while (t--)
    {
        int q;
        cin >> q;
        deque<int> dq;
        bool reversed = false;
        long long sum = 0, R = 0;

        while (q--)
        {
            int s;
            cin >> s;
            if (s == 3)
            {
                int k;
                cin >> k;
                int m = dq.size();
                R += (long long)k * (m + 1);
                sum += k;
                if (!reversed)
                    dq.push_back(k);
                else
                    dq.push_front(k);
                cout << R << "\n";
            }
            else if (s == 1)
            {
                int m = dq.size();
                if (m == 0)
                {
                    cout << 0 << "\n";
                    continue;
                }
                int x;
                if (!reversed)
                {
                    x = dq.back();
                    dq.pop_back();
                    dq.push_front(x);
                }
                else
                {
                    x = dq.front();
                    dq.pop_front();
                    dq.push_back(x);
                }
                R = R + sum - (long long)m * x;
                cout << R << "\n";
            }
            else if (s == 2)
            {
                int m = dq.size();
                R = (long long)(m + 1) * sum - R;
                reversed = !reversed;
                cout << R << "\n";
            }
        }
    }

    return 0;
}
