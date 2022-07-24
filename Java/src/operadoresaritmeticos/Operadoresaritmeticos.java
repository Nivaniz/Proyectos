package operadoresaritmeticos;

import java.util.Scanner;

public class Operadoresaritmeticos {

    
    public static void main(String[] args) {
       
        
        //Programa que tome 3 calificaciones y las imprima en una suma
        Scanner entrada = new Scanner(System.in);
        float uno,dos,tres,suma;
        
        System.out.println("Digite las tres calificaciones: ");
        uno = entrada.nextFloat();
         dos = entrada.nextFloat();
          tres = entrada.nextFloat();
          
          suma = uno + dos + tres;
          
          System.out.println("La suma es: "+suma);
         
        
          /*INICIO
        //Programa que saca N dinero de Gui, la mitad de Juan y Luis la mitad de Gui y Juan
        Scanner dinero = new Scanner(System.in);
        double money,gui,juan,luis,suma1,suma2;
        
        
        System.out.println("Cuánto dinero tiene Gui: ");
        gui = dinero.nextDouble();
        
        juan = gui / 2;
        suma1 = juan + gui;
        luis = suma1 / 2;
        
       suma2 = gui+juan+luis;
        
        System.out.println("Gui tiene: "+gui);
        System.out.println("Juan tiene tiene: "+juan);
        System.out.println("Luis tiene: "+luis);
        System.out.println("Los tres tienen "+suma2);
         FINAL */
          
          
          /*INICIO
       //PROGRAMA QUE CALCULA EL CUADRADO DE UNA SUMA (A+B)^2 = A^2 + B^2 + 2AB 
       Scanner numero = new Scanner(System.in);
       double a,b,c,resultado3,resultado4,exponente = 2;
       
        System.out.println("Digite el número A: ");
        a = numero.nextDouble();
        System.out.println("Digite el número B: ");
        b = numero.nextDouble();
      
        double resultado1 = Math.pow(a,exponente);
        double resultado2 = Math.pow(b,exponente);
        
        resultado3 = exponente*a*b;
        resultado4 = resultado3 + resultado1 + resultado2;
        
        System.out.println("El resultado es: "+resultado4);
        FINAL */
          
          
           /*INICIO
          //PROGRAMA QUE CALCULE DE HORAS A SEMANAS, DÍAS Y HORAS RESTANTES
          Scanner entrada = new Scanner(System.in);
          int horasTotales, semanas,dias,horas;
          
          System.out.println("Dígite el número de horas: ");
          horasTotales = entrada.nextInt();
          
          semanas = horasTotales/168;
          dias = horasTotales%168 / 24; //mod de lo que ya tenemos cargado como la resta
          horas = horasTotales%24;
          
          System.out.println("\n El equivalente es: ");
          System.out.println("Las semanas son: "+semanas);   
           System.out.println("Los días son: "+dias);   
            System.out.println("Las horas son: "+horas);  
            System.out.println("");
            FINAL */    
           
           
              /*INICIO
           //PROGRAMA QUE SAQUE LA FORMULA CUADRÁTICA
           Scanner entrada = new Scanner(System.in);
           double a,b,c,x1,x2;
           
        System.out.print("Digite el valor de a: ");
        a=entrada.nextDouble();
        
        System.out.print("Digite el valor de b: ");
        b=entrada.nextDouble();
        
        System.out.print("Digite el valor de c: ");
        c=entrada.nextDouble();
        
        x1 = (((-b)-Math.sqrt(Math.abs(Math.pow(b, 2)-4*a*c)))/2*a); //Abs por el valor de negativo que puede salir
        x2 = (((-b)+Math.sqrt(Math.abs(Math.pow(b, 2)-4*a*c)))/2*a);
        
        System.out.println(x1);
        System.out.println(x2);
           FINAL */ 
    }
}
