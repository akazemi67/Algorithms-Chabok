//Problem's Link: https://quera.org/problemset/10168

#include <iostream>
#include <vector>
#include <algorithm>

#define MAX 10000000

using namespace std;

int main() {
    long a, b, nn, num, p;
    cin >> a >> b;

    vector<int> dp(b+1, MAX);
    dp[a] = 0;
    if(a==2 || a==3)
        dp[2*a] = 1; 

    for(num=a; num<=b; num++){
        if(dp[num]>=MAX)
            continue;            

        p = 2;
        while(p*p<=num){
            if (num%p==0){
                nn = num+p;
                if(nn<=b)
                    dp[nn] = min(dp[nn], 1+dp[num]);

                nn = num+num/p;
                if(nn<=b)
                    dp[nn] = min(dp[nn], 1+dp[num]);
            }
            p++;
        }
    }

    if(dp[b]<MAX)
        cout << dp[b] << endl;
    else
        cout << -1 << endl;

    return 0;
}

