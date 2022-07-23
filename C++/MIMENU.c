#include <stdio.h>
#include <stdlib.h>
#include <conio.h>
#include <math.h>

int main (int argc, char *argv []){
	//Declaración de variables
	int OP=0;
	int a,b,c,d,p,hampollo,hamres,hamtoc,hamveg,acumula,comida; //de hamburgesas
	int beb,cocacola,pepsi,fanta,delawarer,sprite,e,f,g,h,i; //Menu bebida
	int pap,papgra,papmed,papchic,papcurl,j,k,l,m;//menu de papas
	int helvan,helcho,helfre,sundae,gallet,n,w,q,r,s,pos;//menu de helados
	char resp='s';//final
	
	do{
		system("cls");
		  printf("\t\t\t\t MENU DE COMIDA \n\n");
		  printf("\t\t\t\t ELIJA LO QUE VA PEDIR \n\n");
		  printf("\t\t 1. Hamburgesa \n\n");
		  printf("\t\t 2. Bebida  \n\n");
		  printf("\t\t 3. Papas \n\n");
		  printf("\t\t 4. Postres \n\n");
		  printf("\t\t 5. Salir \n\n");
		  printf("\t\t\t\t ELIGE UNA OPCION --->");
		  scanf("%d",&OP);
		  switch (OP){
		  	 case 1: system ("cls"); //limpiar la pantalla de ejecución
		  	 a=0; b=0; c=0; d=0; p=0; hampollo=50; hamres=60; hamtoc=70; hamveg=80; acumula=0; comida=0;
		  	 printf("\t\t\t\t MENU DE HAMBURGESA \n\n");
		  	 printf("\t\t\t\t Por favor elija opcion escribiendo el numero de comida\n\n");
		  	 printf("\t\t\t\t 1.- Hamburgesa con Pollo ---------50$ \n\n");
		  	 printf("\t\t\t\t 2.- Hamburgesa de Res ---------60$ \n\n");
		  	 printf("\t\t\t\t 3.- Hamburgersa de tocino ----------70$ \n\n");
		  	 printf("\t\t\t\t 4.- Hamburgesa vegetariana -----------80$ \n\n");
		  	 scanf("%d",&comida);
		  	 switch (comida){
		  	 	 case 1: system ("cls");
		  	 	    printf("\t\t\t\t Ha elegido Hamburgesa con pollo \n\n");
		  	 	    printf("Ingrese la cantidad");
		  	 	    scanf("%d",&a);
		  	 	    acumula= acumula+hampollo*a;
		  	 	    p=p+a;
		  	 	    break;
		  	 	 case 2: system ("cls");
		  	 	    printf("\t\t\t\t Ha elegido Hamburgesa de res \n\n");
		  	 	    printf("Ingrese la cantidad");
		  	 	    scanf("%d",&b);
		  	 	    acumula= acumula+hamres*b;
		  	 	    p=p+b;
		  	 	    break;
		  	 	 case 3: system("cls");
		  	 	    printf("\t\t\t\t Ha elegido Hamburgesa de tocino \n\n");
		  	 	    printf("Ingrese la cantidad");
		  	 	    scanf("%d",&c);
		  	 	    acumula= acumula+hamtoc*c;
		  	 	    p=p+c;
		  	 	    break;
		  	 	case 4: system ("cls");
		  	 	    printf("\t\t\t\t Ha elegido Hamburgesa vegetarina \n\n");
		  	 	    printf("Ingrese la cantidad");
		  	 	    scanf("%d",&d);
		  	 	    acumula= acumula+hamveg*d;
		  	 	    p=p+d;
		  	 	    break;
		  	 	 default:
		  	 	 	printf("\t\t\t\t Opcion no valida elija otro numero \n\n");
		  	 	 	break;
			   }//final de switch para menu de hamburgesa (FINSEGUN)
			 case 2: system ("cls");
			 e=0; f=0; g=0; h=0; i=0; cocacola=49; pepsi=39; fanta=29; delawarer=29; sprite=19; beb=0; acumula=0;
		  	 printf("\t\t\t\t MENU DE BEBIDA \n\n");
		  	 printf("\t\t\t\t Por favor elija opcion escribiendo el numero de comida\n\n");
		  	 printf("\t\t\t\t 1.- Cocacola ---------49$ \n\n");
		  	 printf("\t\t\t\t 2.- Pepsi ---------39$ \n\n");
		  	 printf("\t\t\t\t 3.- Fanta ----------29$ \n\n");
		  	 printf("\t\t\t\t 4.- Delawarer -----------29$ \n\n");
		  	 printf("\t\t\t\t 5.- Sprite -----------19$ \n\n");
		  	 scanf("%d",&beb);
		  	 switch (comida){
		  	 	case 1: system ("cls");
		  	 	    printf("\t\t\t\t Ha elegido COCACOLA \n\n");
		  	 	    printf("Ingrese la cantidad");
		  	 	    scanf("%d",&e);
		  	 	    acumula= acumula+cocacola*e;
		  	 	    p=p+e;
		  	 	    break;
		  	 	 case 2: system ("cls");
		  	 	    printf("\t\t\t\t Ha elegido PEPSI \n\n");
		  	 	    printf("Ingrese la cantidad");
		  	 	    scanf("%d",&f);
		  	 	    acumula= acumula+pepsi*f;
		  	 	    p=p+f;
		  	 	    break;
		  	 	 case 3: system("cls");
		  	 	    printf("\t\t\t\t Ha elegido FANTA \n\n");
		  	 	    printf("Ingrese la cantidad");
		  	 	    scanf("%d",&g);
		  	 	    acumula= acumula+fanta*g;
		  	 	    p=p+g;
		  	 	    break;
		  	 	 case 4: system ("cls");
		  	 	    printf("\t\t\t\t Ha elegido DELAWARER\n\n");
		  	 	    printf("Ingrese la cantidad");
		  	 	    scanf("%d",&h);
		  	 	    acumula= acumula+delawarer*h;
		  	 	    p=p+h;
		  	 	    break;
		  	 	 case 5: system ("cls");
		  	 	    printf("\t\t\t\t Ha elegido SPRITE\n\n");
		  	 	    printf("Ingrese la cantidad");
		  	 	    scanf("%d",&i);
		  	 	    acumula= acumula+sprite*i;
		  	 	    p=p+i;
		  	 	    break;
		  	 	 default:
		  	 		printf("OPCION NO VALIDA ELIGA OTRO NUMERO");
		  	 		break;
			   }//final de switch para menu de bebidad
			 case 3: system ("cls");
			  j=0; k=0; l=0; m=0; papgra=49; papmed=39; papchic=29; papcurl=29; pap=0; acumula=0;
		  	 printf("\t\t\t\t MENU DE PAPAS \n\n");
		  	 printf("\t\t\t\t Por favor elija opcion escribiendo el numero de comida\n\n");
		  	 printf("\t\t\t\t 1.- Papas grandes ------49$ \n\n");
		  	 printf("\t\t\t\t 2.- Papas medianas ---------39$ \n\n");
		  	 printf("\t\t\t\t 3.- Papas chicas ----------29$ \n\n");
		  	 printf("\t\t\t\t 4.- Papas curly -----------29$ \n\n");
		  	 scanf("%d",&pap);
		  	 switch (pap){
		  	 	case 1: system ("cls");
		  	 	    printf("\t\t\t\t Ha elegido PAPAS GRANDES \n\n");
		  	 	    printf("Ingrese la cantidad");
		  	 	    scanf("%d",&j);
		  	 	    acumula= acumula+papgra*j;
		  	 	    p=p+j;
		  	 	    break;
		  	 	 case 2: system ("cls");
		  	 	    printf("\t\t\t\t Ha elegido PAPAS MEDIANAS \n\n");
		  	 	    printf("Ingrese la cantidad");
		  	 	    scanf("%d",&k);
		  	 	    acumula= acumula+papmed*k;
		  	 	    p=p+k;
		  	 	    break;
		  	 	 case 3: system("cls");
		  	 	    printf("\t\t\t\t Ha elegido PAPAS CHICAS \n\n");
		  	 	    printf("Ingrese la cantidad");
		  	 	    scanf("%d",&l);
		  	 	    acumula= acumula+papchic*l;
		  	 	    p=p+l;
		  	 	    break;
		  	 	 case 4: system ("cls");
		  	 	    printf("\t\t\t\t Ha elegido PAPAS CURLY \n\n");
		  	 	    printf("Ingrese la cantidad");
		  	 	    scanf("%d",&m);
		  	 	    acumula= acumula+papcurl*m;
		  	 	    p=p+m;
		  	 	    break;
		  	 	 default:
		  	 	 	printf("OPCION NO VALIDA ELIGA OTRO NUMERO");
		  	 		break;
			   }//final de switch para menu de papas
		  	 case 4: system ("cls");
		  	  n=0; w=0; q=0; r=0; s=0; helvan=19; helcho=29; helfre=15; sundae=39; gallet=49; pos=0; acumula=0; 
		  	 printf("\t\t\t\t MENU DE POSTRES \n\n");
		  	 printf("\t\t\t\t Por favor elija opcion escribiendo el numero de comida\n\n");
		  	 printf("\t\t\t\t 1.- Helado de Vainilla ------19$ \n\n");
		  	 printf("\t\t\t\t 2.- Helado de Chocolate ---------29$ \n\n");
		  	 printf("\t\t\t\t 3.- Helado de Fresa ----------15$ \n\n");
		  	 printf("\t\t\t\t 4.- Sundae -----------39$ \n\n");
		  	 printf("\t\t\t\t 5.- Galletas -----------49$ \n\n");
		  	 scanf("%d",&pos);
		  	 switch (pos){
		  	 	case 1: system ("cls");
		  	 	    printf("\t\t\t\t Ha elegido VAINILLA \n\n");
		  	 	    printf("Ingrese la cantidad");
		  	 	    scanf("%d",&n);
		  	 	    acumula= acumula+helvan*n;
		  	 	    p=p+n;
		  	 	    break;
		  	 	 case 2: system ("cls");
		  	 	    printf("\t\t\t\t Ha elegido CHOCOLATE \n\n");
		  	 	    printf("Ingrese la cantidad");
		  	 	    scanf("%d",&w);
		  	 	    acumula= acumula+helcho*w;
		  	 	    p=p+w;
		  	 	    break;
		  	 	 case 3: system("cls");
		  	 	    printf("\t\t\t\t Ha elegido FRESA \n\n");
		  	 	    printf("Ingrese la cantidad");
		  	 	    scanf("%d",&q);
		  	 	    acumula= acumula+helfre*q;
		  	 	    p=p+q;
		  	 	    break;
		  	 	 case 4: system ("cls");
		  	 	    printf("\t\t\t\t Ha elegido SUNDAE \n\n");
		  	 	    printf("Ingrese la cantidad");
		  	 	    scanf("%d",&r);
		  	 	    acumula= acumula+sundae*r;
		  	 	    p=p+r;
		  	 	    break;
		  	 	 case 5: system ("cls");
		  	 	    printf("\t\t\t\t Ha elegido GALLETAS \n\n");
		  	 	    printf("Ingrese la cantidad");
		  	 	    scanf("%d",&s);
		  	 	    acumula= acumula+gallet*s;
		  	 	    p=p+s;
		  	 	    break;
		  	 	 default: 
		  	 	    printf("OPCION NO VALIDA ELIJA OTRO NUMERO");
		  	 	    break;
			   }//final de switch menu para postres
			 case 5: system ("cls");
			     printf("Gracias, vuelva pronto");
			     break;
			 
			 default:
			 	 printf("OPCION INVALIDA");
			 	 break;
		  }//final de switch para menu de comida general
		  resp=0;
		printf("\t\t\t\t LA CUENTA TOTAL ES DE: %d \n\n", acumula);
		printf("\t\t\t\t EL TOTAL DE PLATOS ES DE: %d \n\n", p);
		printf("\t\t\t\t GRACIAS POR SU COMPRA, ¡VUELVA PRONTO¡\n\n");
		printf("\t\t\t\t Desea continuar S o N \n\n");
		scanf("%s",&resp);
	}while (resp=='s'|| resp== 'S');//final de do
	return 0;
}// final de main
	
