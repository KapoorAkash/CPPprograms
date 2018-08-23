#include<iostream>
using namespace std;
int mian()
{
int arr[100],j,n,temp,i;
cout<<"Enter size";
cin>>n;
for(i=0;i<=n;i++)
{
    cin>>arr[i];
}
cout<<"sorted array"<<endl;
    for(i=0;i<n;i++)
    {
        for(j=i+1;j<n;j++)
        {
            if(arr[i]>arr[j])
            {
                temp=arr[i];
                arr[i]=arr[j];
                arr[j]=temp;

            }
        }
    }
     for(int i=0;i<n;i++)
    {
        cout<<arr[i]<<" ";
    }

}
