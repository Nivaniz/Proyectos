#include <stdio.h>
#include <stdlib.h>
#include <conio.h>
#include <math.h>

int main (int argc, char *argv []){
	//LA DECLARACIÓN DE VARIABLES DE TODOS LOS EJERCICICIOS
	int OP=0;
	char Resp='s';
	int Num1,Num2,Suma; //algoritmo suma de dos numeros
	float h,area,vol,radio; // algoritmo cilindro
	float Base,H,Area; // algoritmo triángulo
	float Gal, Total; //algoritmo gasolinera
	int Num, Opcion, Val; //algoritmo menu
	int Cont,Fact; //algoritmo factorial
	
	do{
		  system("cls");
		  printf("\t\t\t\t BIENVENIDO \n\n");
		  printf("\t\t\t\t MENU INTEGRADOR \n\n");
		  printf("\t\t 1. ALGORITMO SUMA DE NUMEROS \n\n");
		  printf("\t\t 2. ALGORITMO DE CILINDRO  \n\n");
		  printf("\t\t 3. ALGORITMO AREA DEL TRIANGULO \n\n");
		  printf("\t\t 4. ALGORITMO GASOLINERA \n\n");
		  printf("\t\t 5. MENU \n\n");
	 	  printf("\t\t 6. ALGORITMO FACTORIAL DE UN NUMERO  \n\n");
		  printf("\t\t\t\t ELIGE UNA OPCION --->");
		  scanf("%d",&OP);
		  switch (OP){
		       case 1: system ("cls"); //limpiar la pantalla de ejecución
			 	     Num1=0;Num2=0;Suma=0;
			 	     printf("\t\t\t\t SUMA DE NUMEROS \n\n");
			 	     printf("Dame el numero uno:");
					 scanf("%d",&Num1);
	                 printf("Dame el numero dos:");
	                 scanf("%d",&Num2);
	                 Suma=Num1+Num2;
	                 printf("La suma es: %d+ %d = %d",Num1,Num2,Suma);
	                 break;
	           case 2: system ("cls");
	                 radio=0;h=0;area=0;vol=0;
	                 printf("\t\t\t\t CILINDRO \n\n");
					 printf("\n Dame el valor del Radio");
				     scanf("%f",&radio);
			         printf("\n Dame el valor de la Altura");
				     scanf("%f",&h);
				     area=2*3.1416*radio*(radio+h);
				     vol=3.1416*pow(radio,2)*h;
				     printf("\n El valor de Area es:%.2f",area);
				     printf("\n El valor de Volumen es: %.2f",vol);
				     break;	
			   case 3: system ("cls");
			         Base=0;
			         H=0;
			         Area=0;
			         printf("\t\t\t\t AREA DE TRIANGULO\n\n");
			         printf ("Dame el valor de la Base");
	                 scanf("%f",&Base);
	                 printf("Dame el valor de la altura");
	                 scanf("%f",&H);
	                 Area=Base*H/2;
	                 printf("el resultado de la superficie es:%2.f",Area);
	                 break;
	           case 4: system ("cls");
	                 Gal=0;
	                 Total=0;
	                 printf("\t\t\t\t GASOLINERA \n\n");
	                 printf("¿Cuantos galones?:");
	                 scanf("%f",&Gal);
	                 Total=Gal*3.785*8,20;
	                 printf("El total a pagar es: %f",Total);
	                 break;
	           case 5: system ("cls");
	                 Num=0;
	                 Val=0;
	                 Opcion=0;
	                 printf("\t\t\t\t MENU \n\n");
	                 printf("\t\t\t\tOPCION 1: 100 * NUMERO");
	                 printf("\t\t\t\t MENU PARA ESCOGER\n\n");
	                 printf("\t\t\t\tOPCION 2: 100 ^ NUMERO\n\n");
	                 printf("\t\t\t\tOPCION 3: 100 / NUMERO\n\n");
	                 printf("\t\t\t\tOPCION 0: CERO\n\n");
	                 printf("\t\t\t\t ELIGE UNA OPCION:\n\n");
	                 scanf("%d",&Opcion);
	                 printf("DAME EL NUMERO A EVALUAR:");
	                 scanf("%d",&Num);
	                 if (Opcion==1){
	                 	Val=100*Num;
					 }
	                 else{
	                 	if(Opcion==2){
	                 		Val=pow(100,Num);
						 }
						 else{
						 	if(Opcion==3){
						 		if(Num==0){
						 			printf("NO EXISTE LA DIVISION ENTRE 0");
								 }
								 else{
								 	Val=100/Num;
								 }
							 }
							 else{
							 	if(Opcion==0)
							 	Val=0;
							 }
						 }
					 }
					 printf("El valor es :%d",Val);
					 break;
				case 6: system("cls");
				     printf("\t\t\t\t FACTORIAL \n\n");
					 printf("Dame el numero a calcular:");
					 scanf("%d",&Num);
					 
					 Cont=1;
					 Fact=1;
					 while(Cont<=Num){
					 	Fact=Fact*Cont;
					 	Cont++;
					 	printf("\n\tCONTADOR--- %d       \t\t ACUMULADOR---%d",Cont,Fact);
					 }
					 printf("EL FACTORIAL DEL NUMERO %d es %d",Num,Fact);
					 break;	
					 default: printf("OPCION INVALIDA");
					 break;	
			}
			printf("\t\t\t\t Desea continuar S o N \n\n");
			scanf("%s",&Resp);
	}while(Resp=='s'|| Resp== 'S');
	return 0;
}
