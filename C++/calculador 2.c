#include <stdio.h>

 
//Prototipo de la funcion
void calcularEdad( int anioAct , int mesAct, int fechAct, int anioNac, int mesNac, int fechNac);
 
int main ()
{
    int anioAct;  //Año Actual
    int mesAct; //Mes actual
    int fechAct; //Fecha actual
 
    int anioNac; //Año nacimiento
    int mesNac; //Mes nacimiento
    int fechNac; //Fecha nacimiento
 
    prinf("\n\tPrograma que calcula la Edad, Mes y Dia\n\n");
    printf("Ingrese Año Actual: ",cin >> anioAct) ;
    printf("Ingrese Mes Actual: ";   cin >> mesAct);
    printf ("Ingrese Fecha Actual: ";  cin >> fechAct);
 
    cout << "\nIngrese Año Nacimiento: ";  cin >> anioNac;
    cout << "Ingrese Mes de Nacimiento: ";  cin >> mesNac;
    cout << "Ingrese Fecha de Nacimiento: ";  cin >> fechNac;
 
    calcularEdad( anioAct , mesAct, fechAct, anioNac, mesNac, fechNac);
 
    return 0;
}
