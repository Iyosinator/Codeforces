#include <iostream>
using namespace std;

int main()
{
    int n;
    cin >> n;
    int cards[n];

    for (int i= 0; i <n; i++){
        cin >> cards[i];
    }

    int left = 0 ,right = n-1;
    int sereja = 0,dima = 0;
    int choosen = 0,turn = 0;


    while (left <= right)
    {
        if (cards[left] > cards[right] ){
            choosen = cards[left];
            left ++;
        }
        else{
            choosen = cards[right];
            right --;
        }

        if (turn % 2 == 0){
            sereja += choosen;
        }
        else{
            dima += choosen;
        }
        turn += 1;
    }

   

    cout << sereja << " " << dima << endl;
    
    return 0;
}
