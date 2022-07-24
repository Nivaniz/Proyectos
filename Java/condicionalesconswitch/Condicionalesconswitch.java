package condicionalesconswitch;

import javax.swing.JOptionPane;

public class Condicionalesconswitch {

    public static void main(String[] args) {
       
        /* INICIO
        //HACER UN PROGRAMA CON CALCULADORA ARITMÉTICA USANDO SWITCH PARA PONER S o s PARA SUMA ETC...
        int numero1,numero2,suma,resta,multiplicacion,division;
        char operacion;
        
        numero1 = Integer.parseInt(JOptionPane.showInputDialog("Digite un número: "));
         numero2 = Integer.parseInt(JOptionPane.showInputDialog("Digite un número: "));
        
        operacion = JOptionPane.showInputDialog("Digite la operación que desea realizar: ").charAt(0);
        
        switch (operacion){
            case 's':
            case 'S':
                suma = numero1+numero2;
            JOptionPane.showMessageDialog(null, "La suma es: "+suma);
                break;
                
            case 'r':
            case 'R':
                resta = numero1-numero2;
            JOptionPane.showMessageDialog(null, "La resta es: "+resta);
                break;
                
            case 'm':
            case 'M':
                multiplicacion = numero1*numero2;
            JOptionPane.showMessageDialog(null, "La multiplicacion es: "+multiplicacion);
                break;
             
            case 'd':
            case 'D':
                division = numero1/numero2;
            JOptionPane.showMessageDialog(null, "La división es: "+division);
                break;
                
            default: 
            JOptionPane.showMessageDialog(null, "ERROR ESOS NUMEROS NO VAN ");
                break;
        }
         FINAL */
        
        
        /* INICIO
        //PROGRAMA QUE TOME UNA NOTA DEL 1 AL 10 Y DIGA SI ES INEFICIENTE O SOBRESALIENTE
        int nota;
        
        nota = Integer.parseInt(JOptionPane.showInputDialog("Digite la nota del alumno: "));
        
        switch (nota){
            case 1:  JOptionPane.showMessageDialog(null, "La calificación: "+nota+" Es INEFICIENTE");
            break;
                case 2:  JOptionPane.showMessageDialog(null, "La calificación: "+nota+" Es INEFICIENTE");
                break;
                    case 3:  JOptionPane.showMessageDialog(null, "La calificación: "+nota+" Es INEFICIENTE");
                    break;
                        case 4:  JOptionPane.showMessageDialog(null, "La calificación: "+nota+" Es INEFICIENTE");
                        break;
                            case 5:  JOptionPane.showMessageDialog(null, "La calificación: "+nota+" Es INEFICIENTE");
                            break;
                                case 6: JOptionPane.showMessageDialog(null, "La calificación: "+nota+" Es INSATISFACTORIA");
                                break;
                                    case 7: JOptionPane.showMessageDialog(null, "La calificación: "+nota+" Es APROBATORIA"); 
                                    break;
                                        case 8: JOptionPane.showMessageDialog(null, "La calificación: "+nota+" Es SATISFACTORIA"); 
                                        break;
                                            case 9: JOptionPane.showMessageDialog(null, "La calificación: "+nota+" Es EXCELENTE"); 
                                            break;
                                                case 10: JOptionPane.showMessageDialog(null, "La calificación: "+nota+" Es SOBRESALIENTE");
                                                break;
                                                   default: 
                                                       JOptionPane.showMessageDialog(null, "ERROR, CALIFICACIÓN NO POSIBLE");
        }
        FINAL */
        
        
        /* INICIO
        //PROGRAMA QUE SIMULE UN CAJERO CON SALDO INCIAL DE 1000 PESOS Y QUE PERMITA INGRESAR DINERO,RETIRAR Y SALIR
        final int saldo_inicial = 1000; //establecer constante
        int opcion;
        float ingreso, saldoActual,retiro;
        
        opcion = Integer.parseInt(JOptionPane.showInputDialog("Bienvenido a su Cajero Automático\n"+
                "1. Ingresar dinero a la cuenta\n"+
                "2. Retirar dinero de la cuenta\n"+
                "3. Salir"));
        
        switch (opcion){
            case 1:
                ingreso = Float.parseFloat(JOptionPane.showInputDialog("Digite la cantidad que desea ingresar en cuenta: "));
                saldoActual = saldo_inicial + ingreso;
                JOptionPane.showMessageDialog(null, "Dinero en cuenta: "+saldoActual);
                break;
            case 2:
                retiro = Float.parseFloat(JOptionPane.showInputDialog("Digite la cantidad que desea retirar en cuenta: "));
                if (retiro > saldo_inicial){
                    JOptionPane.showMessageDialog(null, "RETIRO INCORRECTO\n"+
                            "CANTIDAD MAXIMA SOBREPASADA");
                }
                else{
                saldoActual = saldo_inicial - retiro;
                JOptionPane.showMessageDialog(null, "Dinero en cuenta: "+saldoActual);
                }
                break;
            case 3:                
                break; //PARA SALIR DEL PROGRAMA
            default:              
                JOptionPane.showMessageDialog(null,"OPCION INCORRECTA"); break;           
        }
        FINAL */
        
        
        /* INICIO
        //PROGRAMA QUE PASE DE KG A OTRAS UNIDADES DE MASA CON MENÚ
        float kg,hg,dag,g,dg,cg,mg;
        int opcion;
        
        kg = Float.parseFloat(JOptionPane.showInputDialog("Digite la cantidad de kilos a convertir: "));
        
        opcion = Integer.parseInt(JOptionPane.showInputDialog("Bienvenido a el convertidor de Kilogramos \n"+
                "1. Convertir kg a hg\n"+
                "2. Convertir kg a dag\n"+
                "3. Convertir kg a g\n"+
                "4. Convertir kg a dg\n"+
                "5. Convertir kg a cg\n"+
                "6. Convertir kg a mg\n"+
                "7. Salir"));
        
        switch (opcion){
            case 1:
                hg = kg * 10;
                JOptionPane.showMessageDialog(null, "La conversión a hg da: "+hg);
                break;
            case 2:
                dag = kg * 100;
                JOptionPane.showMessageDialog(null, "La conversión a dag da: "+dag);
                 break;
            case 3:
                g = kg * 1000;
                JOptionPane.showMessageDialog(null, "La conversión a g da: "+g);
                 break;
            case 4:
                dg = kg * 10000;
                JOptionPane.showMessageDialog(null, "La conversión a dg da: "+dg);
                 break;
            case 5:
                cg = kg * 100000;
                JOptionPane.showMessageDialog(null, "La conversión a cg da: "+cg);
                 break;
            case 6:
                mg = kg * 1000000;
                JOptionPane.showMessageDialog(null, "La conversión a mg da: "+mg);
                 break;
            case 7:
                break; //PARA SALIR DEL PROGRAMA
            default:              
                JOptionPane.showMessageDialog(null,"OPCION INVÁLIDA"); break;      
        }
       FINAL */
       
      
        
    }
    
}
