package condicionales;

import javax.swing.JOptionPane;

public class Condicionales { //con IF PURO

    public static void main(String[] args) {
       
        
        //HACER UN PROGRAMA QUE LEA UN NÚMERO ENTERO Y MUESTRE SI EL NÚMERO ES MÚLTIPLO DE 10
        int numero;
        
        numero = Integer.parseInt (JOptionPane.showInputDialog("Digite un número: "));
        
        //Para saber si ese número es múltiplo se necesita divir entre 10 y ver si su mod es 0 lo es
        
        if (numero%10 == 0 ){
            JOptionPane.showMessageDialog(null,"Tu número es múltiplo de 10");
        }
        else{
            JOptionPane.showMessageDialog(null,"Tu número no es múltiplo de 10");
        }
           
        
        /*INICIO
        //PEDIR DOS NÚMEROS Y DECIR CUAL ES MAYOR O SI SON IGUALES
        int A,B;
            
         A = Integer.parseInt (JOptionPane.showInputDialog("Digite número uno: "));
          B = Integer.parseInt (JOptionPane.showInputDialog("Digite número dos: "));
          
          if (A > B){
              JOptionPane.showMessageDialog(null,"Tu número mayor es: "+A);
          }
          if (A < B){
               JOptionPane.showMessageDialog(null,"Tu número mayor es: "+B);
          }
          if (A == B){
              JOptionPane.showMessageDialog(null,"Tus números son iguales");
          }   
           FINAL */
        
        
          /*INICIO
        //PROGRAMA QUE LEE UN CARCÁCTER Y COMPRUEBE SI ES MAYÚSCULA
        char letra;
        
        letra = JOptionPane.showInputDialog("Digite una letra: ").charAt(0);
        
        if (Character.isUpperCase(letra)){
            JOptionPane.showMessageDialog(null,"Tu letra es Mayúscula");
        }
        else{
            JOptionPane.showMessageDialog(null,"Es una letra minúscula");
        }
        FINAL */
                    
          
         /*INICIO
          //POGRAMA QUE SE HACE 20% DE DESCUENTO SI LA COMPRA SUPERA 300$ Y MUESTRA
          //CUANTO VA PAGAR LA PERSONA
          
          double costo, descuento, compra;
          
          costo = Double.parseDouble(JOptionPane.showInputDialog("¿Cuál es el costo de la compra?: "));
          
          if (costo >= 300){
              descuento = (costo*20)/100;
              compra = costo - descuento;
              
             JOptionPane.showMessageDialog(null,"El costo total de tu compra es de: "+compra+" Con un descuento de: "+descuento); 
          }
          else{
              JOptionPane.showMessageDialog(null,"No se aplica descuento el costo es: "+costo); 
          }
              FINAL */
            
          
         /*INICIO
         //PROGRAMA QUE CALCULE SI SE TRABAJA MENOS DE 40 HORAS SE PAGA 16 Y SI SON MÁS SON 20$ LA HORA EXTRA
         int horasTrabajadas;
         float salario;
         
         horasTrabajadas = Integer.parseInt (JOptionPane.showInputDialog("¿Cuántas horas trabajó?:  "));
         
         if (horasTrabajadas <= 40){
             salario = (horasTrabajadas*16);
         }
         else{
             salario = (40*16) + ((horasTrabajadas-40)*20);
       }
          JOptionPane.showMessageDialog(null,"La paga es de: "+salario);          
          FINAL */
         
         
          /*INICIO
         //PROGRAMA QUE TOME DOS NÚMEROS Y DIGA SI AMBOS SON IMPARES O PARES
         int A,B;
         
        A = Integer.parseInt (JOptionPane.showInputDialog("¿Cuál es el valor del primer número:  "));
         B = Integer.parseInt (JOptionPane.showInputDialog("¿Cuál es el valor del segundo número:  "));
         
         A = A%2;
         B = B%2;
         
         if(A+B == 0){
             JOptionPane.showMessageDialog(null,"AMBOS SON PARES");             
         }
         else{
             if(A != 0){ //SI A ES IMPAR PERO B ES IMPAR
           if (B == 0){
               JOptionPane.showMessageDialog(null,"Tu primer número es impar pero tu segundo es par"); 
                             }
                       }
             if (A+B !=0){
                 JOptionPane.showMessageDialog(null,"AMBOS SON IMPARES");
             }
             else{
                if(B != 0){ //SI B ES IMPAR PERO A ES PAR
                  if (A == 0){
             JOptionPane.showMessageDialog(null,"Tu primer número es par pero tu segundo es impar");  
             }
         }
                  }
         }            
         FINAL */
          
          
          /*INICIO
          //OTRA FORMA DE HACER EL DE ARRIBA
          int n1,n2;
        
        JOptionPane.showMessageDialog(null,"Este programa le dira si los numeros ingresados son Par o Impar");
        n1=Integer.parseInt(JOptionPane.showInputDialog("Ingrese el primer numero: "));
        n2=Integer.parseInt(JOptionPane.showInputDialog("Ingrese el segundo numero: "));
        
        if(n2%2==0&&n1%2==0){ //SI NUMERO 2 MOD 2 RESIDUO 0 Y SI NÚMERO 1 MOD 2 RESIDUO 0 SON PARES
            JOptionPane.showMessageDialog(null, "Ambos son numeros Par");
        }
        else if(n1%2==0){ // DE OTRA FORMA SI NUMERO 1 MOD 2 RESIDUO 0 PRIMERO ES PAR Y SEGUNDO ES IMPAR
            JOptionPane.showMessageDialog(null,"El numero "+n1+" es Par y el numero "+n2+" es Impar");
        }
        else if(n2%2==0){ // DE OTRA FORMA SI NUMERO 2 MOD 2 RESIDUO 0 SEGUNDO ES PAR Y PRIMERO ES IMPAR
            JOptionPane.showMessageDialog(null,"El numero "+n2+" es Par y el numero "+n1+" es Impar");
        }
        else{ // SI NO SON MOD 0 SON IMPARES
           JOptionPane.showMessageDialog(null,"Ambos numeros son Impar");
        
        }
          FINAL */
                 
          
           /*INICIO
          //PROGRAMA QUE TOME 3 NUMEROS Y LOS ESCRIBA DE MAYOR A MENOR
         int n1,n2,n3;
         
         n1=Integer.parseInt(JOptionPane.showInputDialog("Ingrese el primer numero: "));
         n2=Integer.parseInt(JOptionPane.showInputDialog("Ingrese el segundo numero: "));
         n3=Integer.parseInt(JOptionPane.showInputDialog("Ingrese el tercer numero: "));
        
         if ((n1>n2) && (n2>n3)){
         JOptionPane.showMessageDialog(null,"El número mayor es: "+n1+"--"+n2+"--"+n3);
        }
         else if ((n1>n3)&&(n3>n2)){
             JOptionPane.showMessageDialog(null,"El número mayor es: "+n1+"--"+n3+"--"+n2);
         }
         else if ((n3>n1)&&(n2>n1)){//n1>n2
            JOptionPane.showMessageDialog(null,"El número mayor es: "+n3+"--"+n2+"--"+n1);
         }
          else if ((n3>n1)&&(n1>n2)){
            JOptionPane.showMessageDialog(null,"El número mayor es: "+n3+"--"+n1+"--"+n2);
         }
          else if ((n2>n3)&&(n3>n1)){
            JOptionPane.showMessageDialog(null,"El número mayor es: "+n2+"--"+n3+"--"+n1);
         }
          else if ((n2>n1)&&(n1>n3)){
            JOptionPane.showMessageDialog(null,"El número mayor es: "+n2+"--"+n1+"--"+n3);
         }
          FINAL */
                
           
           /*INICIO
          //PROGRAMA QUE TE DIGA CUANTAS CIFRAS TIENE UN NÚMERO ENTRE 0 Y 99,999
         //PRIMERA FORMA USANDO cifras = String.valueOf(num1).length();
         int num1,cifras;
         
         num1 =Integer.parseInt(JOptionPane.showInputDialog("Digite un numero entre 0 y 99,999: "));
         
         cifras = String.valueOf(num1).length(); //funcion para contar el largo de num
         
         if(num1 >=0 && num1<=99999){ //rango establecido
             
             JOptionPane.showMessageDialog(null,"El número tiene: "+cifras+" cifras"); 
         }
         else{
             JOptionPane.showMessageDialog(null,"El número está fuera de rango");
         }
         FINAL */
         
           
           /*INICIO
         //PROGRAMA QUE TE DIGA CUANTAS CIFRAS TIENE UN NÚMERO ENTRE 0 Y 99,999
         //SEGUNDA FORMA USANDO MUCHOS ELSE IF
         int numero;
         
         numero =Integer.parseInt(JOptionPane.showInputDialog("Digite un numero entre 0 y 99,999: "));
         
         if(numero>=0 && numero<99999){ //otra forma de poner un ranggo
             if(numero<9){
                 JOptionPane.showMessageDialog(null, "El número de cifras es: 1");
             }//if de una cifra
             else if(numero<99){
                 JOptionPane.showMessageDialog(null, "El número de cifras es: 2");
             } //else if de dos cifras
             else if(numero<999){
                 JOptionPane.showMessageDialog(null, "El número de cifras es: 3");               
             }//else if de tres cifras
             else if(numero<9999){
                 JOptionPane.showMessageDialog(null, "El número de cifras es: 4");
             }//else if de cuatro cifras
             else if(numero<99999){
                 JOptionPane.showMessageDialog(null, "El número de cifras es: 5");
             }//else if de cinco cifras
             else{
                 JOptionPane.showMessageDialog(null, "Número fuera de rango");
             }//else fuera de rango
         }
         FINAL */
         
           
           /*INICIO
           //PROGRAMA QUE PIDA EL DIA MES Y AÑO DE UNA FECHA Y CONFIRME SI ES CORRECTA (SI LOS MESES TUVIERAN 30 DÍAS)
           int dia,mes,año;
           
           dia =Integer.parseInt(JOptionPane.showInputDialog("Dígita el día:  "));
           mes =Integer.parseInt(JOptionPane.showInputDialog("Digita el mes (1-12):  "));
           año =Integer.parseInt(JOptionPane.showInputDialog("Digita el año:  "));
                  
           if(dia>=1 && dia <=30){ //seleccionando y filtrando lo que nosotros queremos
               if(mes>=1 && mes<=12){
                   if(año != 0){
                       JOptionPane.showMessageDialog(null, "Esta es una fecha correcta");
                   }
                   else{
                       JOptionPane.showMessageDialog(null, "Fecha incorrecta, año incorrecto");
                   }
               }
               else{
                   JOptionPane.showMessageDialog(null, "Fecha incorrecta, mes incorrecto");
               }
           }
           else{
               JOptionPane.showMessageDialog(null, "Fecha incorrecta, día incorrecto");
           }
         FINAL */
           
           
            /*INICIO
           //PROGRAMA QUE PIDA EL DIA MES Y AÑO DE UNA FECHA Y CONFIRME SI ES CORRECTA (SI LOS MESES TUVIERAN 30 DÍAS)
            int dia,mes,año;
           
           dia =Integer.parseInt(JOptionPane.showInputDialog("Dígita el día:  "));
           mes =Integer.parseInt(JOptionPane.showInputDialog("Digita el mes (1-12):  "));
           año =Integer.parseInt(JOptionPane.showInputDialog("Digita el año:  "));
           
           if(mes == 1){//ENERO
               if(dia>=1 && dia <=31){
                 if(año != 0){
                       JOptionPane.showMessageDialog(null, "Esta es una fecha correcta");
                   }
                 else{ //año mal
                     JOptionPane.showMessageDialog(null, "Fecha incorrecta, año incorrecto");
                 }
               }
               else{//dia mal
                   JOptionPane.showMessageDialog(null, "Fecha incorrecta, día incorrecto");
               }         
           } //fin de enero
           if(mes == 2){//FEBRERO
               if(dia>=1 && dia <=28){
                 if(año != 0){
                       JOptionPane.showMessageDialog(null, "Esta es una fecha correcta");
                   }
                 else{ //año mal
                     JOptionPane.showMessageDialog(null, "Fecha incorrecta, año incorrecto");
                 }
               }
               else{//dia mal
                   JOptionPane.showMessageDialog(null, "Fecha incorrecta, día incorrecto");
               }         
           } //fin de febrero
           if(mes == 3){//MARZO
               if(dia>=1 && dia <=31){
                 if(año != 0){
                       JOptionPane.showMessageDialog(null, "Esta es una fecha correcta");
                   }
                 else{ //año mal
                     JOptionPane.showMessageDialog(null, "Fecha incorrecta, año incorrecto");
                 }
               }
               else{//dia mal
                   JOptionPane.showMessageDialog(null, "Fecha incorrecta, día incorrecto");
               }         
           } //fin de marzo
           if(mes == 4){//ABRIL
               if(dia>=1 && dia <=30){
                 if(año != 0){
                       JOptionPane.showMessageDialog(null, "Esta es una fecha correcta");
                   }
                 else{ //año mal
                     JOptionPane.showMessageDialog(null, "Fecha incorrecta, año incorrecto");
                 }
               }
               else{//dia mal
                   JOptionPane.showMessageDialog(null, "Fecha incorrecta, día incorrecto");
               }         
           } //fin de abril
           if(mes == 5){//MAYO
               if(dia>=1 && dia <=31){
                 if(año != 0){
                       JOptionPane.showMessageDialog(null, "Esta es una fecha correcta");
                   }
                 else{ //año mal
                     JOptionPane.showMessageDialog(null, "Fecha incorrecta, año incorrecto");
                 }
               }
               else{//dia mal
                   JOptionPane.showMessageDialog(null, "Fecha incorrecta, día incorrecto");
               }         
           } //fin de mayo
           if(mes == 6){//JUNIO
               if(dia>=1 && dia <=30){
                 if(año != 0){
                       JOptionPane.showMessageDialog(null, "Esta es una fecha correcta");
                   }
                 else{ //año mal
                     JOptionPane.showMessageDialog(null, "Fecha incorrecta, año incorrecto");
                 }
               }
               else{//dia mal
                   JOptionPane.showMessageDialog(null, "Fecha incorrecta, día incorrecto");
               }         
           } //fin de JUNIO
           if(mes == 7){//JULIO
               if(dia>=1 && dia <=31){
                 if(año != 0){
                       JOptionPane.showMessageDialog(null, "Esta es una fecha correcta");
                   }
                 else{ //año mal
                     JOptionPane.showMessageDialog(null, "Fecha incorrecta, año incorrecto");
                 }
               }
               else{//dia mal
                   JOptionPane.showMessageDialog(null, "Fecha incorrecta, día incorrecto");
               }         
           } //fin de junio
           if(mes == 8){//AGOSTO
               if(dia>=1 && dia <=31){
                 if(año != 0){
                       JOptionPane.showMessageDialog(null, "Esta es una fecha correcta");
                   }
                 else{ //año mal
                     JOptionPane.showMessageDialog(null, "Fecha incorrecta, año incorrecto");
                 }
               }
               else{//dia mal
                   JOptionPane.showMessageDialog(null, "Fecha incorrecta, día incorrecto");
               }         
           } //fin de agosto
           if(mes == 9){//SEPTIEMBRE
               if(dia>=1 && dia <=30){
                 if(año != 0){
                       JOptionPane.showMessageDialog(null, "Esta es una fecha correcta");
                   }
                 else{ //año mal
                     JOptionPane.showMessageDialog(null, "Fecha incorrecta, año incorrecto");
                 }
               }
               else{//dia mal
                   JOptionPane.showMessageDialog(null, "Fecha incorrecta, día incorrecto");
               }         
           } //fin de septiembre
           if(mes == 10){//OCTUBRE
               if(dia>=1 && dia <=31){
                 if(año != 0){
                       JOptionPane.showMessageDialog(null, "Esta es una fecha correcta");
                   }
                 else{ //año mal
                     JOptionPane.showMessageDialog(null, "Fecha incorrecta, año incorrecto");
                 }
               }
               else{//dia mal
                   JOptionPane.showMessageDialog(null, "Fecha incorrecta, día incorrecto");
               }         
           } //fin de OCTUBRE
           if(mes == 11){//NOVIEMBRE
               if(dia>=1 && dia <=30){
                 if(año != 0){
                       JOptionPane.showMessageDialog(null, "Esta es una fecha correcta");
                   }
                 else{ //año mal
                     JOptionPane.showMessageDialog(null, "Fecha incorrecta, año incorrecto");
                 }
               }
               else{//dia mal
                   JOptionPane.showMessageDialog(null, "Fecha incorrecta, día incorrecto");
               }         
           } //fin de noviembre
           if(mes == 12){//DICIEMBRE
               if(dia>=1 && dia <=31){
                 if(año != 0){
                       JOptionPane.showMessageDialog(null, "Esta es una fecha correcta");
                   }
                 else{ //año mal
                     JOptionPane.showMessageDialog(null, "Fecha incorrecta, año incorrecto");
                 }
               }
               else{//dia mal
                   JOptionPane.showMessageDialog(null, "Fecha incorrecta, día incorrecto");
               }         
           } //fin dediciembre
           
           /*
           PARA ACUMULAR MESES EN UN IF Y NO PONER UNO POR UNO USAR:
           else if((mes==4 || mes==6 || mes==9 ||mes==11) && dia<=30) {
              JOptionPane.showMessageDialog(null, "la fecha: "+dia+" - "+mes+" - "+año+" es correcta");
           }else if((mes == 1 || mes == 3 || mes == 5 || mes == 7 || mes == 8 || mes == 10 || mes == 12) && dia <= 31) {
              JOptionPane.showMessageDialog(null, "la fecha: "+dia+" - "+mes+" - "+año+" es correcta");         
            FINAL */
                
    }
    
}
