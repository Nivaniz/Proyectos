#ifdef __MSDOS__
    #include <iostream.h>
    #include <stdlib.h>
#else
    using namespace std;
#endif

int main (void)
{
    int dia, mes;
    cout << "Ingrese el valor de dia: ";
    cin >> dia;
    cin.get();
    cout << "Ingrese el valor de mes: ";
    cin >> mes;
    cin.get();
    if((dia>=21&&mes==3)||(dia<=20&&mes==4))
    {
        cout << "Signo: Aries" << endl;
        cout << "Hor\242scopo: Escribe el hor\242scopo aqu\241." << endl;
    }
    if((dia>=24&&mes==9)||(dia<=23&&mes==10))
    {
        cout << "Signo: Libra" << endl;
        cout << "Hor\242scopo: Escribe el hor\242scopo aqu\241." << endl;
    }
    if((dia>=21&&mes==4)||(dia<=21&&mes==5))
    {
        cout << "Signo: Tauro" << endl;
        cout << "Hor\242scopo: Escribe el hor\242scopo aqu\241." << endl;
    }
    if((dia>=24&&mes==10)||(dia<=22&&mes==11))
    {
        cout << "Signo: Escorpio" << endl;
        cout << "Hor\242scopo: Escribe el hor\242scopo aqu\241." << endl;
    }
    if((dia>=22&&mes==5)||(dia<=21&&mes==6))
    {
        cout << "Signo: Geminis" << endl;
        cout << "Hor\242scopo: Escribe el hor\242scopo aqu\241." << endl;
    }
    if((dia>=23&&mes==11)||(dia<=21&&mes==12))
    {
        cout << "Signo: Sagitario" << endl;
        cout << "Hor\242scopo: Escribe el hor\242scopo aqu\241." << endl;
    }
    if((dia>=21&&mes==6)||(dia<=23&&mes==7))
    {
        cout << "Signo: Cancer" << endl;
        cout << "Hor\242scopo: Escribe el hor\242scopo aqu\241." << endl;
    }
    if((dia>=22&&mes==12)||(dia<=20&&mes==1))
    {
        cout << "Signo: Capricornio" << endl;
        cout << "Hor\242scopo: Escribe el hor\242scopo aqu\241." << endl;
    }
    if((dia>=24&&mes==7)||(dia<=23&&mes==8))
    {
        cout << "Signo: Leo" << endl;
        cout << "Hor\242scopo: Escribe el hor\242scopo aqu\241." << endl;
    }
    if((dia>=21&&mes==1)||(dia<=19&&mes==2))
    {
        cout << "Signo: Acuario" << endl;
        cout << "Hor\242scopo: Escribe el hor\242scopo aqu\241." << endl;
    }
    if((dia>=24&&mes==8)||(dia<=23&&mes==9))
    {
        cout << "Signo: Virgo" << endl;
        cout << "Hor\242scopo: Escribe el hor\242scopo aqu\241." << endl;
    }
    if((dia>=20&&mes==2)||(dia<=20&&mes==3))
    {
        cout << "Signo: Piscis" << endl;
        cout << "Hor\242scopo: Escribe el hor\242scopo aqu\241." << endl;
    }
    cout << endl;
    system ("pause");
    return EXIT_SUCCESS;
}
