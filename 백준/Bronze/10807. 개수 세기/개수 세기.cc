#include <stdio.h>

main(){
	int n,v,cnt=0;
	scanf("%d",&n);
	int L[n];
	for(int i=0;i<n;i++)
	{
		scanf("%d",&L[i]);
	}
	scanf("%d",&v);
	for(int i=0;i<n;i++)
	{
		if(L[i]==v)
			cnt++;
	}
	printf("%d",cnt);
}