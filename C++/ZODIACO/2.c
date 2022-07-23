#include <stdio.h>
#include <stdlib.h>

int main (void)
{
    int dia, mes;
    printf ("Ingrese el valor de dia: ");
    scanf ("%d", &dia);
    (void) getchar ();
    printf ("Ingrese el valor de mes: ");
    scanf ("%d", &mes);
    (void) getchar ();
    if((dia>=21&&mes==3)||(dia<=20&&mes==4))
    {
        printf ("Signo: Aries\n");
        printf ("Hor\242scopo: Escribe el hor\242scopo aqu\241.\n");
    }
    if((dia>=24&&mes==9)||(dia<=23&&mes==10))
    {
        printf ("Signo: Libra\n");
        printf ("Hor\242scopo: Escribe el hor\242scopo aqu\241.\n");
    }
    if((dia>=21&&mes==4)||(dia<=21&&mes==5))
    {
        printf ("Signo: Tauro\n");
        printf ("Hor\242scopo: Escribe el hor\242scopo aqu\241.\n");
    }
    if((dia>=24&&mes==10)||(dia<=22&&mes==11))
    {
        printf ("Signo: Escorpio\n");
        printf ("Hor\242scopo: Escribe el hor\242scopo aqu\241.\n");
    }
    if((dia>=22&&mes==5)||(dia<=21&&mes==6))
    {
        printf ("Signo: Geminis\n");
        printf ("Hor\242scopo: Escribe el hor\242scopo aqu\241.\n");
    }
    if((dia>=23&&mes==11)||(dia<=21&&mes==12))
    {
        printf ("Signo: Sagitario\n");
        printf ("Hor\242scopo: Escribe el hor\242scopo aqu\241.\n");
    }
    if((dia>=21&&mes==6)||(dia<=23&&mes==7))
    {
        printf ("Signo: Cancer\n");
        printf ("Hor\242scopo: Escribe el hor\242scopo aqu\241.\n");
    }
    if((dia>=22&&mes==12)||(dia<=20&&mes==1))
    {
        printf ("Signo: Capricornio\n");
        printf ("Hor\242scopo: Escribe el hor\242scopo aqu\241.\n");
    }
    if((dia>=24&&mes==7)||(dia<=23&&mes==8))
    {
        printf ("Signo: Leo\n");
        printf ("Hor\242scopo: Escribe el hor\242scopo aqu\241.\n");
    }
    if((dia>=21&&mes==1)||(dia<=19&&mes==2))
    {
        printf ("Signo: Acuario\n");
        printf ("Hor\242scopo: Escribe el hor\242scopo aqu\241.\n");
    }
    if((dia>=24&&mes==8)||(dia<=23&&mes==9))
    {
        printf ("Signo: Virgo\n");
        printf ("Hor\242scopo: Escribe el hor\242scopo aqu\241.\n");
    }
    if((dia>=20&&mes==2)||(dia<=20&&mes==3))
    {
        printf ("Signo: Piscis\n");
        printf ("Hor\242scopo: Escribe el hor\242scopo aqu\241.\n");
    }
    putchar ('\n');
    system ("pause");
    return EXIT_SUCCESS;
}
