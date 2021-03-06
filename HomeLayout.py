# -*- coding: utf-8 -*-


from PyQt5.QtWidgets import QGridLayout,QLabel,QWidget, QVBoxLayout, QStackedLayout
from User import User
from HomeController import HomeController
from PyQt5.QtCore import pyqtSignal
from ImageSlider import ImageSlider

#Home layout that shows recommended and hot movies
class HomeLayout(QWidget):
    _WatchMovie_ = pyqtSignal(str, int)
    def __init__(self,user:User):
        self.user = user
        super().__init__()
        self.controller = HomeController(user)        
        self.__home_grid = QGridLayout()
        self.recommended_for_you_label = QLabel("Recommended for you")
        self.recommended_for_you_label.setObjectName("recommended_for_you_label")
        self.recommended_for_you_label.setFixedWidth(200)
        self.whats_hot_label = QLabel("What's hot")
        self.whats_hot_label.setObjectName("whats_hot_label")
        self.whats_hot_label.setFixedWidth(105)


        
        self.recommended_display = ImageSlider()
        self.hot_display = ImageSlider()
        
        self.recommended_for_you = [] #list of recommended movies
        self.whats_hot = [] #list of popular movies
        

        self.stack = QStackedLayout()       
        self.movieLayout = None       
        self.vbox = QVBoxLayout()
        
        self.vboxRecommended = QVBoxLayout()
        self.vboxRecommended.addWidget(self.recommended_for_you_label)   
        self.vboxRecommended.addWidget(self.recommended_display)
        
        self.vboxhot = QVBoxLayout()
        self.vboxhot.addWidget(self.whats_hot_label)
        self.vboxhot.addWidget(self.hot_display)
        
       
        self.vbox.addLayout(self.__home_grid)
        self.vbox.addLayout(self.vboxRecommended)
        self.vbox.addLayout(self.vboxhot)
        self.vbox.addLayout(self.stack)
        
        print(self.stack)
    
        self.recommended_display.list_widget.itemPressed.connect(lambda: self.MovieIsClicked())
        self.hot_display.list_widget.itemPressed.connect(lambda: self.MovieIsClickedHot())
        
        
        self.generateRecommended()
        
        self.generateHot()
        self.setLayout(self.vbox)
    
    
    def MovieIsClicked(self):
        self._WatchMovie_.emit(self.recommended_display.list_widget.selectedItems()[0].url, self.recommended_display.list_widget.selectedItems()[0].movieID)
    
    def MovieIsClickedHot(self):
        self._WatchMovie_.emit(self.hot_display.list_widget.selectedItems()[0].url, self.hot_display.list_widget.selectedItems()[0].movieID)
    
    #generates recommended movies for user (user specific)
    def generateRecommended(self):
        self.images, self.url, self.moviesID, self.titles = self.controller.getRecommended()
        
        if(len(self.images) != 0):
            self.recommended_display.setImages(self.images, self.url, self.moviesID, self.titles)
    
    #generates "hot" movies for user (general)
    def generateHot(self):
        self.imageshot_hot, self.url_hot, self.moviesID_hot, self.titles_hot = self.controller.getHot()
        print("images", self.titles_hot)
        if(len(self.imageshot_hot) != 0):
            self.hot_display.setImages(self.imageshot_hot, self.url_hot, self.moviesID_hot, self.titles_hot)

        

        