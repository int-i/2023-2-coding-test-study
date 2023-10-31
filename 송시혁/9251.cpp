#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

string s1, s2;


int main()
{
    cin  >> s1 >> s2;
    int length1 = s1.length();
    int length2 = s2.length();
    int dp[1001][1001]={0};
    for(int i=1; i<length1; i++)
    {
        for(int j=1; j<length2; j++){
            if(s1[i-1]==s2[j-1])
                dp[i][j] = dp[i-1][j-1]+1;
            
            else
                dp[i][j] = max(dp[i][j-1],dp[i-1][j]);

        }
    }
    cout << dp[length1][length2];



}