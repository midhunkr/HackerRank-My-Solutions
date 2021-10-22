void bonAppetit(int bill_count, int* bill, int k, int b) {
	int i;
	int sum=0;
	int net_sum;
	for(i=0;i<bill_count;i++){
		sum+=bill[i];
	}
	//printf("Sum is %d\n",sum);
	net_sum=(sum-bill[k])/2;
	//printf("Net sum is %d\n",net_sum);
	if(net_sum==b){
		printf("Bon Appetit\n");
	}
	else if(net_sum!=b){
		int difference;
		difference=(sum/2)-net_sum;
		printf("%d\n",difference);
	}
}