from PySide6.QtGui import QIcon, QCursor, QTextDocument
from PySide6.QtCore import Qt, QStringListModel
from PySide6.QtWidgets import QApplication, QMainWindow, QLineEdit, QListView, QMenu, QMessageBox


import sys
import random
import string
import pyperclip
from ui_form import Ui_MainWindow  # Asegúrate de que este archivo esté correctamente generado

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Gestor de Contraseñas")
        self.setWindowIcon(QIcon("icono.png"))
        self.DBpassword = {}
        self.model = QStringListModel()

        self.ui.listView.setModel(self.model)
        self.ui.listView.clicked.connect(self.mostrar_datos_seleccionados)
        self.ui.listView.setEditTriggers(QListView.NoEditTriggers)

        self.ui.AddButton.clicked.connect(self.add_elemento_vacio)

        # Configurar el generador de contraseñas
        self.ui.letras_checkbox.setFocusPolicy(Qt.NoFocus)
        self.ui.contrasena.setTextFormat(Qt.RichText)
        self.ui.slider.setMinimum(8)
        self.ui.slider.setMaximum(64)
        self.ui.slider.setValue(15)
        self.ui.slider.setTickInterval(1)
        self.ui.sliderL.setText(f"{self.ui.slider.value()}")
        self.ui.slider.valueChanged.connect(self.actualizar_sliderL)
        self.ui.generarB.clicked.connect(self.mostrar_contrasena)
        self.ui.contrasena.setTextInteractionFlags(Qt.TextSelectableByMouse)
        self.ui.copiar.clicked.connect(self.copiar_texto)

        # Conectar el checkbox de mostrar/ocultar contraseña
        self.ui.mostrar_contrasena.stateChanged.connect(self.ocultar_contrasena)

        # Configurar los botones de crear, modificar y eliminar
        self.ui.crear.clicked.connect(self.crear_elemento)
        self.ui.modificar.clicked.connect(self.modificar_elemento)
        self.ui.eliminar.clicked.connect(self.eliminar_elemento)
        self.ui.password.setEchoMode(QLineEdit.Password)

    def contextMenuEvent(self, event):
        # Crear un menú de clic derecho
        menu = QMenu(self)
        eliminar_action = menu.addAction("Eliminar")

        # Obtener la posición global del ratón
        position = QCursor.pos()  # Usamos QCursor para obtener la posición global del ratón

        # Mostrar el menú en la posición exacta del ratón
        action = menu.exec(position)

        if action == eliminar_action:
            self.eliminar_elemento()

    """METODOS"""
    def add_elemento_vacio(self):
        # Agregar un elemento vacío al diccionario y actualizar el modelo
        nuevo_nombre = "Nuevo elemento"
        contador = 1

        # Asegurarse de que el nombre sea único
        while nuevo_nombre in self.DBpassword:
            nuevo_nombre = f"Nuevo elemento {contador}"
            contador += 1

        # Agregar al diccionario y actualizar el modelo
        self.DBpassword[nuevo_nombre] = {
            "url": "",
            "notas": "",
            "password": ""
        }
        self.model.setStringList(list(self.DBpassword.keys()))

    # Métodos del generador de contraseñas
    def actualizar_sliderL(self, valor):
        self.ui.sliderL.setText(f"{valor}")

    def generar_contrasena(self, longitud):
        psw = ""
        if self.ui.letras_checkbox.isChecked():
            psw += string.ascii_letters
        if self.ui.numeros_checkbox.isChecked():
            psw += string.digits
        if self.ui.caracteres_checkbox.isChecked():
            psw += "@-!$_"
        if not psw:
            psw = string.ascii_letters  # Usamos por defecto solo letras si no se seleccionan otros
        return ''.join(random.choice(psw) for _ in range(longitud))

    def mostrar_contrasena(self):
        longitud = self.ui.slider.value()
        contrasena = self.generar_contrasena(longitud)
        contrasena_html = "".join(
            f'<span style="color: {"red" if char.isdigit() else "blue" if char in "@-!$_" else "black"};">{char}</span>'
            for char in contrasena
        )
        self.ui.contrasena.setText(f'<html><head/><body>{contrasena_html}</body></html>')

    def copiar_texto(self):
       # Obtener el texto HTML de la etiqueta
       html_text = self.ui.contrasena.text()

       # Crear un QTextDocument para convertir el HTML a texto plano
       doc = QTextDocument()
       doc.setHtml(html_text)

       # Copiar el texto plano al portapapeles
       pyperclip.copy(doc.toPlainText())


    # Métodos del gestor de contraseñas
    def crear_elemento(self):
        nombre = self.ui.nombre.text()
        if nombre in self.DBpassword:
            self.mostrar_error("Este nombre ya existe. Usa 'Modificar' para cambiar los datos.")
            return

        password = self.ui.password.text()
        if not nombre or not password:
            self.mostrar_error("Por favor, completa los campos 'Nombre' y 'Contraseña' antes de crear.")
            return

        url = self.ui.url.text()
        notas = self.ui.notas.text()

        self.DBpassword[nombre] = {
            "url": url,
            "notas": notas,
            "password": password
        }

        self.model.setStringList(list(self.DBpassword.keys()))
        print(f"Elemento '{nombre}' creado.")

    def modificar_elemento(self):
        selected_index = self.ui.listView.selectedIndexes()
        if not selected_index:
            self.mostrar_error("Por favor, selecciona un elemento para modificar.")
            return

        nombre_original = self.model.data(selected_index[0], Qt.DisplayRole)

        if nombre_original not in self.DBpassword:
            self.mostrar_error("Este nombre no existe en la base de datos.")
            return

        nombre_modificado = self.ui.nombre.text()
        if nombre_modificado != nombre_original:
            if nombre_modificado in self.DBpassword:
                self.mostrar_error("Este nombre ya existe. Usa otro nombre.")
                return
            self.DBpassword[nombre_modificado] = self.DBpassword.pop(nombre_original)

        password = self.ui.password.text()
        if not password:
            self.mostrar_error("Por favor, completa el campo 'Contraseña' antes de modificar.")
            return

        url = self.ui.url.text()
        notas = self.ui.notas.text()

        self.DBpassword[nombre_modificado] = {
            "url": url,
            "notas": notas,
            "password": password
        }

        self.model.setStringList(list(self.DBpassword.keys()))
        print(f"Elemento '{nombre_modificado}' modificado.")

    def eliminar_elemento(self):
        nombre = self.ui.nombre.text()
        if nombre not in self.DBpassword:
            self.mostrar_error("Este nombre no existe.")
            return

        del self.DBpassword[nombre]
        self.model.setStringList(list(self.DBpassword.keys()))
        print(f"Elemento '{nombre}' eliminado.")

    def mostrar_datos_seleccionados(self, index):
        nombre = self.model.data(index, Qt.DisplayRole)

        if nombre in self.DBpassword:
            datos = self.DBpassword[nombre]
            self.ui.nombre.setText(nombre)
            self.ui.url.setText(datos["url"])
            self.ui.notas.setText(datos["notas"])
            self.ui.password.setText(datos["password"])

    def ocultar_contrasena(self):
        if self.ui.mostrar_contrasena.isChecked():
            self.ui.password.setEchoMode(QLineEdit.Normal)
        else:
            self.ui.password.setEchoMode(QLineEdit.Password)

    def mostrar_error(self, mensaje):
        msg = QMessageBox(self)
        msg.setIcon(QMessageBox.Warning)
        msg.setText(mensaje)
        msg.setWindowTitle("Error")
        msg.exec()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
