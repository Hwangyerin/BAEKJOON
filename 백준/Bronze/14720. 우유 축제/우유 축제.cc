#include <stdio.h>
main(){
	int n,cnt=0,temp=0;
	scanf("%d",&n);
	int L[n]={0};
	for(int i=0;i<n;i++){
		scanf("%d",&L[i]);
	}
	
	for(int i=0;i<n;i++){
		if (L[i]==temp){
			cnt++;
			if (temp==2)
				temp=0;
			else
				temp++;
		}
		else
			continue;
		
	}
	printf("%d",cnt);
}