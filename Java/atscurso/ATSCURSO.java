package atscurso;

import javax.swing.JOptionPane; //usada para cuadros de texto

public class ATSCURSO {

    public static void main(String[] args) {
        
        
        
        //CLASE 9 ENTRADA Y SALIDA CON CONVERSIONES USANDO JOPTIONPANE
        //Inicializamos variables que se mostraran
        String cadena;
        int entero;
        char letra;
        double decimal;
        
        //ENTRADA CON FORMATO STRING
        cadena = JOptionPane.showInputDialog("Digite una cadena: ");
        //SALIDA CON FORMATO STRING
        JOptionPane.showMessageDialog(null, "La cadena escrita es: "+cadena);    
     
        //ENTRADA CON FORMATO INT
        entero = Integer.parseInt(JOptionPane.showInputDialog("Digite un entero: "));
        //SALIDA CON FORMATO STRING
        JOptionPane.showMessageDialog(null, "El entero escrito es: "+entero);
        
        //ENTRADA CON FORMATO CHAR
        letra = JOptionPane.showInputDialog("Digite una letra: ").charAt(0);
        //SALIDA CON FORMATO STRING
        JOptionPane.showMessageDialog(null, "La letra escrita es: "+letra);
        
        //ENTRADA CON FORMATO DOUBLE O FLOAT
        decimal = Double.parseDouble (JOptionPane.showInputDialog("Digite un decimal: "));
        //SALIDA CON FORMATO STRING
        JOptionPane.showMessageDialog(null, "El decimal escrito es: "+decimal);
          
    }
    
}
