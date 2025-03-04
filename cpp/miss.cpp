#include<iostream>
using namespace std;
int main()
{
	int n,s=0;
	cin>>n;
	int a[n];
	for(int i=0;i<n;i++)
	{
		cin>>a[i];
	}
	for(int i=0;i<n;i++)
	{
 	 	s+=a[i];
	}
	int num;
	num=(n*(n+1))/2;
	int d;
	if(num!=s)
	{
		d=num-s;
	}
	cout<<d;
}
