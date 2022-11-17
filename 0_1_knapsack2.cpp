#include<iostream>
#include<algorithm>
#include<bits/stdc++.h>
using namespace std;

//0/1 Knapsack function
void knapsack(int p[],int w[],int n,int k_capacity)
{
    int i,j,total_profit;
    int a[n+1][k_capacity+1];     //2-d array for matrix implementation
    for(i=0;i<=n;i++)             //Loop for traversing row
    {
        for(j=0;j<=k_capacity;j++)//Loop for traversing columns
        {
            if(i==0 || j==0)
            {
                a[i][j]=0;        //Initialising first row and first column with zero
            }
            else if(w[i-1]<=j)    //If weight is greater than w[i-1] then use formula
            {
                a[i][j]=max(a[i-1][j],(a[i-1][j-w[i-1]]+p[i-1]));
            }
            else                  //Else copy the above value as it is
            {
                a[i][j]=a[i-1][j];
            }
        }
    }
    //The last box of matrix holds the total profit
    //a[n][k_capacity]=Total Profit
    int profit=a[n][k_capacity];
    cout<<"Total profit: "<<profit<<endl;

    cout<<"Matrix generated for Dynamic Programming: "<<endl;
    for(i=0;i<=n;i++)
    {
    	for(j=0;j<=k_capacity;j++)
    	{
    		cout<<a[i][j]<<"\t";
		}
        cout<<endl;
	} 
	cout<<endl;
}

int main()
{
    int n,k_capacity;
    cout<<"Enter the number of objects: "<<endl;
    cin>>n;
    cout<<"Enter the capacity: "<<endl;
    cin>>k_capacity;
    
    int w[n];    //Weight array
    int p[n];    //Profit array
    
    cout<<"Enter the weights: "<<endl;
    for(int i=0;i<n;i++)
    {
        cin>>w[i];    //Accepting weights values
    }
    
    cout<<"Enter the profit: "<<endl;
    for(int i=0;i<n;i++)
    {
        cin>>p[i];    //Accepting profits values
    }
    knapsack(p,w,n,k_capacity);   //Function call for knapsack
    return 0;
}
