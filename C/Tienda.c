#include <stdio.h>
#include <stdlib.h>

//repetir (diseño del menú)
//borrar pantalla
int main(void){
 int op=0;
 
printf("\t\t Menu de recomendaciones:\n\n");
printf( "\t\t1. LITERATURA\n\n");
printf("\t\t2. CINE\n\n");
printf("\t\t3. MUSICA\n\n");
printf("\t\t4.VIDEOJUEGOS\n\n");
printf("\t\t5. SALIR\n\n");
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
		printf("+Ain´t no sunshine\n\n");
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
	default:
		printf("\t\t NUMERO NO VALIDO/OPCION INVALIDA VUELVA A COMENZAR\n\n");
		break;		
}
   printf("\t\t GRACIAS POR ELEGIR\n\n");
   return 0;
}
