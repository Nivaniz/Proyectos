#include <stdio.h>
#include <stdlib.h>

int main (void){
	int n;
	
	printf("Escriba un numero");
	scanf("%d",&n);
	if (n==0){
		printf("es nulo");	
	}
	else{
	if (n<0){
		printf("Es negativo");
	}
	else{
		printf("Es positivo");
	}	
	}
	return 0;
	
}

