#include<bits/stdc++.h>
using namespace std;

//sorts the array in descending order
bool comparePbyW(pair <int, int> a, pair<int, int> b) {
    double r1 = (double)a.first / (double)a.second;
    double r2 = (double)b.first / (double)b.second;
    return r1 > r2;
}

//sort on basis of min weight
bool compareByWeight(pair<int, int> a, pair<int, int> b) {
    int w1 = a.second;
    int w2 = b.second;
    return w2>w1; 
}

//sort on basis of max profit
bool compareByProfit(pair <int, int> a, pair<int, int> b) {
    int p1= a.first;
    int p2 = b.first;
    return p1>p2;
} 

//first -> value/profit
//second -> weight
double fractionalKnapsack(int Weight, pair <int, int> arr[], int N) {
    //sort on basis of ratio
    sort(arr, arr + N, comparePbyW);
    //sort(arr, arr + N, compareByWeight);
    //sort(arr, arr + N, compareByProfit);

//to print the profits and weights arranged in descending order of (P/W)
//     cout<<endl;
//    for(int i = 0; i < N; i++) {
//     cout<<arr[i].first << " " << arr[i].second << endl;
//    }

    //declare the final result
    double finalValue = 0;

    //looping through all items
    for(int i=0; i<N; i++){

        //if adding item wont overflow then add it completely
        if(arr[i].second <= Weight) {
            Weight -= arr[i].second;
            finalValue += arr[i].first;
        }

        //if we cant add it completely add the fractional part
        else {
            finalValue += arr[i].first * ((double) Weight / (double)arr[i].second);
            break;
        }
    }
    return finalValue;
}

int main() {
    int N = 5;
    pair <int, int> arr[] = {
        make_pair(40,80),
        make_pair(10,10),
        make_pair(50,40),
        make_pair(30,20),
        make_pair(60,90)
    };
    int weight = 110;
    cout << "Maximum profit that we can obtain is " << fractionalKnapsack(weight, arr, N);
    return 0;
}