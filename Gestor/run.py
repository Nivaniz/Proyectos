import sys
import menu
import ui

if __name__ == "__main__":
    # Si pasamos un argumento -t lanzamos el modo terminal
    if len(sys.argv) > 1 and sys.argv[1] == "-t":
        menu.iniciar()
    # En cualquier otro caso lanzamos el modo gráfico
    else:
        app = ui.MainWindow()
        app.mainloop()

'''
    Para poder ejecutar desde la terminal 
    python3 run.py -t
    Para poder ejecutar desde la interfaz
    python3 run.py
'''
