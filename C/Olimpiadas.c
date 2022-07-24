#include <stdio.h>
#include <stdlib.h>

int main (void)
{
    int americanos, asiaticos, europeos, i, n;
    int pais;
    float dias, pago_total, total_del_pago_realizado;
    americanos = 0;
    asiaticos = 0;
    europeos = 0;
    total_del_pago_realizado = 0;
    printf ("Ingrese el valor de n: ");
    scanf ("%d", &n);
    (void) getchar ();
    for (i=1; i<=n; i++)
    {
        printf ("PROCESO %d\n", i);
        printf ("Ingrese el valor de dias: ");
        scanf ("%f", &dias);
        (void) getchar ();
        printf ("Seleccione el valor de pais.\n");
        printf ("\t1.- Espa\244a\n");
        printf ("\t2.- Estados Unidos\n");
        printf ("\t3.- Alemania\n");
        printf ("\t4.- China\n");
        printf ("\t5.- Brasil\n");
        printf ("\t6.- Argentina\n");
        printf ("\t7.- Per\243\n");
        printf ("\t8.- Chile\n");
        printf ("\t9.- Francia\n");
        printf ("\t: ");
        do {
            scanf ("%d", &pais);
            (void) getchar ();
            if (pais<1||pais>9)
                printf ("Valor incorrecto. Ingr\202selo nuevamente.: ");
        } while (pais<1||pais>9);
        pago_total=0;
        printf ("Olimpiadas Tokio 2020\n");
        if(pais==1)
        {
            pago_total=dias*20.1;
            printf ("Pa\241s origen: Espa\244a\n");
            europeos=europeos+1;
        }
        if(pais==2)
        {
            pago_total=dias*22.3;
            printf ("Pa\241s origen: Estados Unidos\n");
            americanos=americanos+1;
        }
        if(pais==3)
        {
            pago_total=dias*24.7;
            printf ("Pa\241s origen: Alemania\n");
            europeos=europeos+1;
        }
        if(pais==4)
        {
            pago_total=dias*15.1;
            printf ("Pa\241s origen: China\n");
            asiaticos=asiaticos+1;
        }
        if(pais==5)
        {
            pago_total=dias*17.4;
            printf ("Pa\241s origen: Brasil\n");
            americanos=americanos+1;
        }
        if(pais==6)
        {
            pago_total=dias*15.1;
            printf ("Pa\241s origen: Argentina\n");
            americanos=americanos+1;
        }
        if(pais==7)
        {
            pago_total=dias*16.1;
            printf ("Pa\241s origen: Per\243\n");
            americanos=americanos+1;
        }
        if(pais==8)
        {
            pago_total=dias*17.4;
            printf ("Pa\241s origen: Chile\n");
            americanos=americanos+1;
        }
        if(pais==9)
        {
            pago_total=dias*10.0;
            printf ("Pa\241s origen: Francia\n");
            europeos=europeos+1;
        }
        total_del_pago_realizado=total_del_pago_realizado+pago_total;
        printf ("Valor de pago total: %g\n", pago_total);
        putchar ('\n');
    }
    printf ("Valor de americanos: %d\n", americanos);
    printf ("Valor de asiaticos: %d\n", asiaticos);
    printf ("Valor de europeos: %d\n", europeos);
    printf ("Valor de total del pago realizado: %f\n", total_del_pago_realizado);
    system ("pause");
    return EXIT_SUCCESS;
}6
