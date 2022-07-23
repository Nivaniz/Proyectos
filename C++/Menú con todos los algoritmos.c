#include <stdio.h>
#include <stdlib.h>
#include <conio.h>
#include <math.h>
int main (int argc, char*argv[]){
	
	int OP=0;
	printf("\t\t\t\t BIENVENIDO \n\n");
	printf("\t\t\t\t MENU INTEGRADOR \n\n");
	printf("\t\t 1. ALGORITMO SUMA DE NUMEROS \n\n");
	printf("\t\t 2. ALGORITMO DE CILINDRO  \n\n");
	printf("\t\t 3. ALGORITMO AREA DEL TRIANGULO \n\n");
	printf("\t\t 4. ALGORITMO GASOLINERA \n\n");
    printf("\t\t 5. ALGORITMO FACTORIAL DE UN NUMERO \n\n");
	printf("\t\t 6. MENU \n\n");
	printf("\t\t\t\t ELIGE UNA OPCION --->");
	scanf("%d",&OP);
	
	switch(OP){
		case 1: system("cls");
			    printf("\t\t\t\t SUMA DE NUMEROS \n\n");
                
				float num1,num2,suma;  
            	printf("Dame el numero uno:");
	            scanf("%f",&num1);
	            printf("Dame el numero dos:");
	            scanf("%f",&num2);
	            suma=num1+num2;
	            printf("La suma es: %f+ %f = %f",num1,num2,suma);
	            break;
	    case 2: system ("cls");
	            printf("\t\t\t\t CILINDRO \n\n");
	            
	            const double PI=3.1416;
	            float h,area,vol;
	            float radio;
	            printf("\n Dame el valor del Radio");
				scanf("%f",&radio);
				printf("\n Dame el valor de la Altura");
				scanf("%f",&h);
				area=2*3.1416*radio*(radio+h);
				vol=3.1416*pow(radio,2)*h;
				printf("\n El valor de Area es:%f",area);
				printf("\n El valor de Volumen es: %f",vol);
				break;
	    case 3: system ("cls");
	            printf("\t\t\t\t AREA DE TRIANGULO\n\n");
	            
	            float base,altura,sup;
	            printf ("Dame el valor de la Base");
	            scanf("%f",&base);
	            printf("Dame el valor de la altura");
	            scanf("%f",&altura);
	            sup=base*altura/2;
	            printf("el resultado de la superficie es:%f",sup);
	            break;
	    case 4: system ("cls");
	            printf("\t\t\t\t GASOLINERA \n\n");
	            
	            	float preciolitro,total,galonsurt;
	                //GALON VALE 3.785
	                printf("\n Dame los galones a surtir");
	                scanf("%f",&galonsurt);
	                printf("\n Dame el precio por litro");
	                scanf("%f",&preciolitro);
	                total=galonsurt*3.785*preciolitro;
	                printf("\n El total a pagar es de:%f",total);
	                break;        
	    case 5: system("cls");
		        printf("\t\t\t\t FACTORIAL \n\n"); 
                    int num,cont,fact;
                    num=0;
                    printf("Ingresa el numero a calcular el factorial");
                    scanf("%d",&num); // dato ingresasdo por el usuario
					cont=1; // inicializa el contador  
					fact = 1; // inicializa el contador 
					do { 
					fact= fact*cont;
					cont=cont+1;
					printf("\n Contador: %d",cont);
					printf("\n Acumulador %d",fact);
					}while (cont<num);
					printf("\n El factorial del numero: %d",num, "Es: %d",fact);
				    break;
		case 6: system("cls");
	            printf("\t\t\t\t MENU\n\n");
	            
	                int op=0;
                  printf("\t\t Menu de recomendaciones:\n\n");
                  printf( "\t\t1. LITERATURA\n\n");
                  printf("\t\t2. CINE\n\n");
                  printf("\t\t3. MUSICA\n\n");
                  printf("\t\t4.VIDEOJUEGOS\n\n");
                  printf("\t\t5.SALIR\n\n");
                  //ingresar una opción
                  printf("Elija una opcion (1-5):");
                  scanf("%d",&op); 
                  
                 switch(op){
	                    case 1:
	                  	 printf("\t\tLecturas recomendadas:\n\n");
		                 printf("\t\t+ Homo Deus (Yuval Noah Harari)\n\n");
		                 printf("\t\t+ Un mundo feliz (Aldous Huxley)\n\n");
		                 printf("\t\t+ El alquimista ( Paulo Coelho)\n\n");
		                 printf("\t\t+ 1984 (George Orwell)\n\n");
		                 printf("\t\t+ Todo lo que seriamos tu y yo, si no fueramos tu y yo (Albert Espinosa)\n\n");
		                 break;
	                    case 2:
	                   	 printf("\t\tPeliculas recomendadas:\n\n");
		                 printf("\t\t+Amelie\n\n");
	                     printf("\t\t+ Lucy\n\n");
		                 printf("\t\t+ La odisea de Jaques Costeu\n\n");
	                     printf("\t\t+ Animales fantasticos y donde encontrarlos\n\n");
		                 printf("\t\t+ El castillo del vagabundo\n\n");
	                     break;
	                    case 3:
		                 printf("\t\tCanciones recomendadas\n\n");
		                 printf("\t\t+Por volverte a ver\n\n");
		                 printf("\t\t+Ain´t no sunshine\n\n");
		                 printf("\t\t+Dust in the wind\n\n");
		                 printf("\t\t+Life is ife\n\n");
		                 printf("\t\t+Perdon\n\n");
		                 break;
	                   case 4:
		                 printf("\t\t+Videojuegos recomendados\n\n");
		                 printf("\t\t+GTA V\n\n");
	                     printf("\t\t+Roblox\n\n");
		                 printf("\t\t+Minecraft\n\n");
		                 printf("\t\t+Papers please\n\n");
		                 printf("\t\t+Kitty Powers Matchmaker\n\n");
		                 break;
		               case 5:
		                 printf("\t\t USTED ELIGIO SALIR\n\n");
		                 break;
	                   case 6:
		                 printf("\t\t NUMERO NO VALIDO/OPCION INVALIDA \n\n");
		                 break;
		               default:
			             printf("OPCION INVALIDA INTENTE DE NUEVO");
			             break;    
		            }   
  printf ("GRACIAS POR ELEGIR Y/O PARTICIPAR");
	}
	return 0;
}
