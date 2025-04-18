#include <iostream>
#include <vector>
#include <string>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin >> t;
    while (t--)
    {
        int n;
        cin >> n;
        string s;
        cin >> s;

        int cntL = 0, cntI = 0, cntT = 0;
        for (char ch : s)
        {
            if (ch == 'L')
                cntL++;
            else if (ch == 'I')
                cntI++;
            else if (ch == 'T')
                cntT++;
        }

        int m_found = -1, k = 0;
        for (int m = 0; m <= 2 * n; m++)
        {
            if ((n + m) % 3 == 0)
            {
                k = (n + m) / 3;
                if (cntL <= k && cntI <= k && cntT <= k)
                {
                    m_found = m;
                    break;
                }
            }
        }

        if (m_found == -1)
        {
            cout << -1 << "\n";
            continue;
        }

        if (m_found == 0)
        {
            cout << 0 << "\n";
            continue;
        }

        int deficitL = k - cntL;
        int deficitI = k - cntI;
        int deficitT = k - cntT;
        vector<int> ops;

        while (deficitL > 0 || deficitI > 0 || deficitT > 0)
        {
            bool opPerformed = false;
            for (int i = 0; i < (int)s.size() - 1; i++)
            {
                if (s[i] != s[i + 1])
                {
                    char cand;
                    if ((s[i] == 'L' && s[i + 1] == 'I') || (s[i] == 'I' && s[i + 1] == 'L'))
                        cand = 'T';
                    else if ((s[i] == 'L' && s[i + 1] == 'T') || (s[i] == 'T' && s[i + 1] == 'L'))
                        cand = 'I';
                    else
                        cand = 'L';

                    if ((cand == 'L' && deficitL > 0) ||
                        (cand == 'I' && deficitI > 0) ||
                        (cand == 'T' && deficitT > 0))
                    {
                        ops.push_back(i + 1);
                        if (cand == 'L')
                            deficitL--;
                        else if (cand == 'I')
                            deficitI--;
                        else if (cand == 'T')
                            deficitT--;
                        s.insert(s.begin() + i + 1, cand);
                        opPerformed = true;
                        break;
                    }
                }
            }
            if (!opPerformed)
                break;
        }

        if (deficitL || deficitI || deficitT)
            cout << -1 << "\n";
        else
        {
            cout << ops.size() << "\n";
            for (int op : ops)
                cout << op << "\n";
        }
    }

    return 0;
}
