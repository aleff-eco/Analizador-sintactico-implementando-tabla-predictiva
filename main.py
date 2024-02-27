from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi

from analizer import Parser

class MiVentana(QMainWindow):
    def __init__(self):
        super(MiVentana, self).__init__()
        loadUi('ventana.ui', self)
        
        self.pushButton.clicked.connect(self.analizador)

    def analizador(self):
        self.textBrowser.clear()
        self.status.clear()
        self.value_input.clear()
        texto = self.textEdit.toPlainText()
        
        parser = Parser(texto)
        resultado = parser.parse()
        recorrido_pila = resultado['stack_trace']

        self.value_input.append(texto)
        self.textBrowser.append("Recorrido:")
        self.textBrowser.append("Pila inicial: ['$', 'FUNCION']")

        for paso in range(len(recorrido_pila) - 1):
            estado_anterior = recorrido_pila[paso]
            estado_actual = recorrido_pila[paso + 1]

            pila_anterior = estado_anterior[0]
            pila_actual = estado_actual[0]

            cambio = [simbolo for simbolo in pila_actual if simbolo not in pila_anterior]
            proceso = ' '.join(cambio)

            pila_mantener = [simbolo for simbolo in pila_actual if simbolo in pila_anterior]
            pila_final = pila_mantener + cambio

            if cambio:
                processed_symbol = estado_actual[1] if len(estado_actual) == 2 else ''
                
                self.textBrowser.append(f"Estado de la pila= {pila_final}")
                self.textBrowser.append(f"Token ' {processed_symbol} '")
                self.textBrowser.append(f"proceso ' {proceso} '")
            else:
                self.textBrowser.append(f"Continuar con la pila: {pila_final}")

        if resultado['success']:
            self.textBrowser.append("\nPila final: ['$']")
            self.textBrowser.append('Sentencia aceptada ✔')
            self.status.append("✔")
        else:
            self.textBrowser.append('✘')
            self.status.append("✘")

if __name__ == '__main__':
    app = QApplication([])
    ventana = MiVentana()
    ventana.show()
    app.exec_()
