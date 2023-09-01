import sys
import bcrypt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QTextEdit, QPushButton, QVBoxLayout
from PyQt5.QtGui import QIcon, QFont

class Klefki(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Klefki")
        self.setWindowIcon(QIcon("Klefki.ico"))
        self.setGeometry(100, 100, 350, 100)
        self.setStyleSheet("background-color: #E0E7E9;")

        layout = QVBoxLayout()

        title_label = QLabel("Klefki's Password Encrypter")
        title_label.setFont(QFont("Calibri", 12, QFont.Bold))
        layout.addWidget(title_label)

        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Enter Password")
        self.password_input.setStyleSheet("border: 3px groove #9DA0A4; background-color: white;")
        layout.addWidget(self.password_input)

        encrypt_button = QPushButton("Encrypt and Save")
        encrypt_button.clicked.connect(self.encrypt_and_save)
        layout.addWidget(encrypt_button)

        self.result_text = QTextEdit()
        self.result_text.setReadOnly(True)
        self.result_text.setStyleSheet("border: 3px groove #9DA0A4; background-color: white;")
        layout.addWidget(self.result_text)

        self.setLayout(layout)

    def encrypt_and_save(self):
        password = self.password_input.text().encode()
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(password, salt)

        self.result_text.setPlainText("Hashed:\n" + hashed.decode('utf-8'))

        with open("password.txt", "wb") as file:
            file.write(hashed)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Klefki()
    window.show()
    sys.exit(app.exec_())
