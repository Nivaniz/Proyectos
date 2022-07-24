#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#define Max 15

int main(){

 char *nombres[Max];
 char nombre [25];
 char *letra;
  int i,j,n =sizeof(nombres)/sizeof (char*);

  for(i=0;i<n;i++)//Ciclo q va pidiendo los nombres
  {
      system("cls");
      printf("\n\nNombre %d:",i+1);
      fgets(nombre,sizeof(nombre),stdin);//guarda la  longitud de la palabra en la variable nombre
      letra=strchr(nombre,'\n');//localiza o ubica al apuntador letra en los caracteres empezando por el salto de linea
      if(letra!=NULL){//si temp no es un elemento nulo
         *letra='\0';
         nombres[i]=strdup(nombre);
      }
  }
  for(i=0;i<n;i++)//Ciclo q realiza el proceso de ordenamiento, recorre el apuntador la cadena para ordenar
    for(j=n-1;j>0;j--)
     if(strcmp(nombres[j],nombres[j-1])<0)
     {
      letra= nombres[j];
      nombres[j]=nombres[j-1];
      nombres[j-1]=letra;

     }
  for(i=0;i<n;i++)//ciclo q muestra los nombres ya ordenados q aparecera en pantalla
   {
       printf("%d: %s\n",i+1,nombres[i]);
   }
system("pause");
return EXIT_SUCCESS;
} 
