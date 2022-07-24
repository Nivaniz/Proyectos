#include <stdio.h>

/* run this program using the console pauser or add your own getch, system("pause") or input loop */

int main(int argc, char** argv) {
	//Declaración de variables
    int num1,num2,suma;  
    
	printf("Dame el numero uno:");
	scanf("%d",&num1);
	printf("Dame el numero dos:");
	scanf("%d",&num2);
	suma=num1+num2;
	printf("La suma es: %d", suma);
	return 0;
}
