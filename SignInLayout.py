# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QGridLayout,QPushButton,QLineEdit,QLabel
from PyQt5.QtCore import pyqtSignal
from SignInController import SignInController

#Layout for signing in, first visual interface the user passes by
class SignInLayout(QGridLayout):
    success_signal = pyqtSignal()

    def __init__(self):
        super().__init__()
        
        self.register_button = QPushButton("Register")
        self.sign_in_button = QPushButton("Sign In") 
        
        self.register_button.setGeometry(100, 100, 120, 40) 
        self.sign_in_button.setGeometry(100, 100, 120, 40) 
      
        self.username_entry = QLineEdit()
        self.username_entry.setPlaceholderText("username")
    
        self.password_entry = QLineEdit()
        self.password_entry.setPlaceholderText("password")
        self.password_entry.setEchoMode(QLineEdit.Password)
        
        self.error_message = QLabel("")
                 
        self.addWidget(self.username_entry)
        self.addWidget(self.password_entry)
        self.addWidget(self.sign_in_button)
        self.addWidget(self.register_button)
        self.addWidget(self.error_message)
    
        
        self.sign_in_button.clicked.connect(lambda: self.ClickSignInButton())
        self.register_button.clicked.connect(lambda: self.ClickRegisterButton())
        self.controller = SignInController()

    #Calls AttemptSignIn from this layouts controller to check if user exits
    #if it does then it emits a signal to close this widget and open mainwidget
    #else it shows an error message
    def ClickSignInButton(self):
        username = self.username_entry.text()
        password = self.password_entry.text()
        controller_result = self.controller.AttemptSignIn(username,password)
        if controller_result == "success":
            self.success_signal.emit()
        else:
            self.error_message.setText(controller_result)
    
    #Takes user to registration layout to be added to the database      
    def ClickRegisterButton(self):
        state = self.controller.ToRegister()
        if(state == "success"):
            self.success_signal.emit()
           
        
        
        
        