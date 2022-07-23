#include <stdio.h>
#include <stdlib.h>
#include <conio.h>

int main (void)
{
    int dia, mes;
    char tecla_repetir;
    do {
        system ("cls");
        printf ("Ingrese el valor de dia: ");
        scanf ("%d", &dia);
        (void) getchar ();
        printf ("Ingrese el valor de mes: ");
        scanf ("%d", &mes);
        (void) getchar ();
        if((dia>=21&&mes==3)||(dia<=20&&mes==4))
            printf ("Aries\n");
        if((dia>=24&&mes==9)||(dia<=23&&mes==10))
            printf ("Libra\n");
        if((dia>=21&&mes==4)||(dia<=21&&mes==5))
            printf ("Tauro\n");
        if((dia>=24&&mes==10)||(dia<=22&&mes==11))
            printf ("Escorpio\n");
        if((dia>=22&&mes==5)||(dia<=21&&mes==6))
            printf ("G\202minis\n");
        if((dia>=23&&mes==11)||(dia<=21&&mes==12))
            printf ("Sagitario\n");
        if((dia>=21&&mes==6)||(dia<=23&&mes==7))
            printf ("C\240ncer\n");
        if((dia>=22&&mes==12)||(dia<=20&&mes==1))
            printf ("Capricornio\n");
        if((dia>=24&&mes==7)||(dia<=23&&mes==8))
            printf ("Leo\n");
        if((dia>=21&&mes==1)||(dia<=19&&mes==2))
            printf ("Acuario\n");
        if((dia>=24&&mes==8)||(dia<=23&&mes==9))
            printf ("Virgo\n");
        if((dia>=20&&mes==2)||(dia<=20&&mes==3))
            printf ("Piscis\n");
        putchar ('\n');
        printf ("\250Desea repetir el proceso? (S/N): ");
        do {
            tecla_repetir = (char) getch();
        } while (tecla_repetir!='s' && tecla_repetir!='n' && tecla_repetir!='S' && tecla_repetir!='N');
        putchar ('\n');
    } while (tecla_repetir=='s' || tecla_repetir=='S');
    return EXIT_SUCCESS;
}
