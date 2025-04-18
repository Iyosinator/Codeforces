#include <iostream>
using namespace std;

int main()
{
    int t;
    cin >> t; 

    while (t--)
    {
        int x;
        cin >> x; 

        string str_x = to_string(x);
                
        int n = str_x.length();             
        int ans = (str_x[0] - '0' - 1) * 10;
    
        if (n == 1)
        {
            ans += 1;
        }
        else if (n == 2)
        {
            ans += 3;
        }
        else if (n == 3)
        {
            ans += 6;
        }
        else if (n == 4)
        {
            ans += 10;
        }
        

        cout << ans << endl; 
    }

    return 0;
}
