# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QFrame,QGridLayout,QWidget,QLabel, QPushButton, QSpacerItem, QFileDialog, QHBoxLayout, QVBoxLayout
from PyQt5.QtGui import QPixmap
from User import User
from ProfileController import ProfileController
import base64
from PyQt5.QtCore import pyqtSignal 
#Layout for the profile interface
#TODO: show relevant details for the user
class ProfileLayout(QWidget):
    changePass_request = pyqtSignal()
    changeImage_request = pyqtSignal(bytes)
    
    def __init__(self,user:User):
        super().__init__()
        self.title = 'User Profile'
        
        self.__profile_grid = QGridLayout()
        self.user = user
        self.controller = ProfileController(self.user)
        
        self.HBox1 = QHBoxLayout()
        self.HBox2 = QHBoxLayout()
        self.frame1 = QFrame()
        self.frame2 = QFrame()
        self.frame1.setLayout(self.HBox1)
        self.frame2.setLayout(self.HBox2)

        self.edit_button = QPushButton("Edit")
        self.edit_button.setObjectName("edit_button")
        self.edit_button.setFixedWidth(100)
        self.edit_button.clicked.connect(lambda:self.getFile())
        self.HBox1.addWidget(self.edit_button)

        self.change_password = QPushButton("Change Password")
        self.change_password.setObjectName("change_password")
        self.change_password.setFixedWidth(200)
        self.change_password.clicked.connect(lambda:self.changePassword())
        self.HBox2.addWidget(self.change_password)

        
        self.username = QLabel("Username:")
        self.username.setObjectName("username")
        self.firstName = QLabel("First Name:")
        self.firstName.setObjectName("firstName")
        self.lastName = QLabel("Last Name:")     
        self.lastName.setObjectName("lastName")
        self.user_username = QLabel(self.user.username)   
        self.user_firstName = QLabel(self.user.first_name)     
        self.user_lastName = QLabel(self.user.last_name)
       
        self.image = self.user.image
        self.image_label = QLabel()
       
        if(len(self.image) != 0):
            pm = QPixmap()
            pm.loadFromData(base64.b64decode(self.user.image))
            self.image_label.setPixmap(pm)
            self.image_label.setScaledContents(True)
        
        self.spacer= QSpacerItem(20,5)
        
        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.image_label)
        
        self.__profile_grid.addWidget(self.username,2,0)
        self.__profile_grid.addWidget(self.user_username,2,1)
        self.__profile_grid.addWidget(self.firstName,3,0)
        self.__profile_grid.addWidget(self.user_firstName,3,1)
        self.__profile_grid.addWidget(self.lastName,4,0)
        self.__profile_grid.addWidget(self.user_lastName,4,1)
      
        self.vbox.addWidget(self.frame1)
        self.vbox.addLayout(self.__profile_grid)
        self.vbox.addWidget(self.frame2)
        
        
        self.errorMessage = QLabel()
        self.vbox.addWidget(self.errorMessage)
        
        self.setLayout(self.vbox)
        

        
    def getFile(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', 'c:\\',"Image files (*.png *.jpg *.gif )")
        if(fname[0] != ""):
            self.image_label.setPixmap(QPixmap(fname[0]))
            self.image_label.setScaledContents(True)
            result, image = self.controller.editProfilePic(fname[0])
            if(isinstance(image, bytes)== True):
                self.changeImage_request.emit(image)
        
    def changePassword(self):
        self.changePass_request.emit()
#        self.controller.changePassword()
        
        
