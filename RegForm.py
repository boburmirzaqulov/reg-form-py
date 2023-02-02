from PyQt5.QtWidgets import *
from PyQt5 import QtCore
#comment


class RegForm(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.main_widget = QWidget()

        self.main_lyt = QVBoxLayout()

        self.lbl_V_lyt = QVBoxLayout()
        self.r_f_f_lbl = QLabel("Register for free!")
        self.r_f_f_lbl.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lbl_V_lyt.addWidget(self.r_f_f_lbl)

        self.create_lbl = QLabel("Create an account to save your stations and access")
        self.create_lbl.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lbl_V_lyt.addWidget(self.create_lbl)

        self.pandora_lbl = QLabel("Pandora anywhere")
        self.pandora_lbl.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lbl_V_lyt.addWidget(self.pandora_lbl)
        self.lbl_V_lyt.addStretch()
        self.main_lyt.addLayout(self.lbl_V_lyt)

        self.email_h_lyt = QHBoxLayout()
        self.email_lbl = QLabel("Your email")
        self.email_edit = QLineEdit()
        self.email_edit.setPlaceholderText("Enter your email...")
        self.email_edit.textEdited.connect(lambda: self.verification_edit_meth(self.email_edit))
        self.email_h_lyt.addWidget(self.email_lbl)
        self.email_h_lyt.addWidget(self.email_edit)
        self.email_h_lyt.addStretch()
        self.main_lyt.addLayout(self.email_h_lyt)

        self.password_h_lyt = QHBoxLayout()
        self.password_lbl = QLabel("Password")
        self.password_edit = QLineEdit()
        self.password_edit.textEdited.connect(lambda: self.verification_edit_meth(self.password_edit))
        self.password_edit.setPlaceholderText("Enter password...")
        self.password_h_lyt.addWidget(self.password_lbl)
        self.password_h_lyt.addWidget(self.password_edit)
        self.password_h_lyt.addStretch()
        self.main_lyt.addLayout(self.password_h_lyt)

        self.birthyear_h_lyt = QHBoxLayout()
        self.birthyear_lbl = QLabel("Birth year")
        self.birthyear_edit = QLineEdit()
        self.birthyear_edit.textEdited.connect(lambda: self.verification_edit_meth(self.birthyear_edit))
        self.birthyear_edit.setPlaceholderText("Ender your birth year")
        self.birthyear_h_lyt.addWidget(self.birthyear_lbl)
        self.birthyear_h_lyt.addWidget(self.birthyear_edit)
        self.birthyear_h_lyt.addStretch()
        self.main_lyt.addLayout(self.birthyear_h_lyt)

        self.zipcode_h_lyt = QHBoxLayout()
        self.zipcode_lbl = QLabel("US zip code")
        self.zipcode_edit = QLineEdit()
        self.zipcode_edit.textEdited.connect(lambda: self.verification_edit_meth(self.zipcode_edit))
        self.zipcode_edit.setPlaceholderText("Enter your zip code")
        self.zipcode_h_lyt.addWidget(self.zipcode_lbl)
        self.zipcode_h_lyt.addWidget(self.zipcode_edit)
        self.zipcode_h_lyt.addStretch()
        self.main_lyt.addLayout(self.zipcode_h_lyt)

        self.gender_h_lyt = QHBoxLayout()
        self.gender_lbl = QLabel("Gender")
        self.m_ch = QCheckBox("Male")
        self.f_ch = QCheckBox("Female")
        self.m_ch.setChecked(True)
        self.m_ch.stateChanged.connect(self.m_ch_meth)
        self.f_ch.stateChanged.connect(self.f_ch_meth)
        self.gender_h_lyt.addWidget(self.gender_lbl)
        self.gender_h_lyt.addWidget(self.m_ch)
        self.gender_h_lyt.addWidget(self.f_ch)
        self.gender_h_lyt.addStretch()
        self.main_lyt.addLayout(self.gender_h_lyt)

        self.recomend_chb = QCheckBox("Send me personalized recommendations and tips")
        self.agree_chb = QCheckBox("I have read, understood, and agreed to the Terms of Use and the Privacy Policy")
        self.agree_chb.stateChanged.connect(self.changeState)
        self.main_lyt.addWidget(self.recomend_chb)
        self.main_lyt.addWidget(self.agree_chb)

        self.btn_h_lyt = QHBoxLayout()
        self.reg_h_lyt = QHBoxLayout()
        self.reg_btn = QPushButton("Register")
        self.reg_btn.clicked.connect(self.reg_meth)
        self.reg_h_lyt.addWidget(self.reg_btn)
        self.reg_h_lyt.addStretch()
        self.reg_h_lyt.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight)

        self.back_h_lyt = QHBoxLayout()
        self.back_btn = QPushButton("Go Back")
        self.back_btn.clicked.connect(self.back_meth)
        self.back_h_lyt.addWidget(self.back_btn)
        self.back_h_lyt.addStretch()

        self.btn_h_lyt.addLayout(self.reg_h_lyt)
        self.btn_h_lyt.addLayout(self.back_h_lyt)
        self.main_lyt.addLayout(self.btn_h_lyt)

        self.main_lyt.addStretch()
        self.main_widget.setLayout(self.main_lyt)
        self.setCentralWidget(self.main_widget)

        self.show()

    def changeState(self, state):
        if state:
            self.agree_chb.setStyleSheet("background-color: white")

    def m_ch_meth(self, state):
        if state:
            self.f_ch.setChecked(False)

    def f_ch_meth(self, state):
        if state:
            self.m_ch.setChecked(False)

    def reg_meth(self):
        emailText = self.email_edit.text()
        if len(emailText) == 0:
            self.email_edit.setStyleSheet("background-color: red")
        passwordText = self.password_edit.text()
        if len(passwordText) == 0:
            self.password_edit.setStyleSheet("background-color: red")
        birthText = self.birthyear_edit.text()
        if len(birthText) == 0:
            self.birthyear_edit.setStyleSheet("background-color: red")
        zipCode = self.zipcode_edit.text()
        if len(zipCode) == 0:
            self.zipcode_edit.setStyleSheet("background-color: red")

        if not self.agree_chb.checkState():
            self.agree_chb.setStyleSheet("background-color: red")
        else:
            pass


    def back_meth(self):
        self.close()

    def verification_edit_meth(self, obj):
        obj.setStyleSheet("background-color: white")


app = QApplication([])
reg = RegForm()

app.exec_()
