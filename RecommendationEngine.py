# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 16:20:06 2020

@author: ojaro
"""
from User import User


class RecommendationEngine:
    
    def __init__(self,user:User):
        self.user_ = user
        pass
    
    def WhatsHot(self):
        pass
    #TODO:  Send query to MMS to retrieve list of "hottest" movies.
    #       Criteria can be highest number of views and highest ratings
    
    def LoadRecommendations(self):
        pass
    #TODO:  Send query to MMS to retrieve list of "Recommended" movies for currently signed in user
    