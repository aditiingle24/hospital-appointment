#include<iostream>
using namespace std;
int main()
{
	int n;
	cin>>n;
	int a[n];
	for(int i=0;i<n;i++)
	{
		cin>>a[i];
	}
	int c_s=a[0];
	int m_s=a[0];
	for(int i=1;i<=n;i++)
	{
		c_s=max(a[i],c_s+a[i]);
		m_s=max(c_s,m_s);
	}
	cout<<m_s;
}
