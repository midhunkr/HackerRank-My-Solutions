
//April 8 2021
char* catAndMouse(int x, int y, int z) {

	char *str;
	// int catA=int x;
	// int catB=int y;
	int catAMouse=abs(z-x);
	int catBMouse=abs(z-y);
	if(catAMouse<catBMouse){
		str="Cat A";
	}else if((catAMouse>catBMouse)){
		str="Cat B";
	}else{
		str="Mouse C";
	}
	return str;

}
int main(int argc, char const *argv[])
{
	char *result;
	result=catAndMouse(1,3,2);
	printf("%s\n",result);
}