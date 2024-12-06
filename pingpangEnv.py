import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import pygame
import random

class PingPongEnv:
    def __init__(self):
        self.state = np.zeros((10, 10))  # 初始化一个10x10的网格
        self.ball_position = (1, 5)  # 球的初始位置\
        self.moveRow = -1;
        self.moveCol = -1;
        self.paddle_row = 5 #拍子位置
        self.paddle_size = 3  # Paddle size
        self.movepaddle = -1;

    def step(self,move):

        #new_row = self.
        
        # 更新球的位置
        if (self.ball_position[0] !=0 and self.ball_position[1]!=0 and self.ball_position[0] !=9 and self.ball_position[1]!=9):
            self.moveCol = self.moveCol;
            self.moveRow = self.moveRow;
        elif (self.ball_position[0] ==0  and (self.ball_position[1]!=0 or self.ball_position[1]!=9)):
            self.moveRow = -self.moveRow;
        elif (self.ball_position[0] ==9):
            if  self.ball_position[1]<(self.paddle_row + (self.paddle_size/2)) and self.ball_position[1]> (self.paddle_row - (self.paddle_size/2)):
                self.moveRow = -self.moveRow
            else:
                return 0 
        elif ((self.ball_position[0] !=0  or self.ball_position[0] !=9) and (self.ball_position[1]==0 or self.ball_position[1]==9)):
            self.moveCol = -self.moveCol;
        else:
            self.moveCol = -self.moveCol;
            self.moveRow = -self.moveRow;
            
        self.ball_position =  (self.ball_position[0] + self.moveRow, #np.random.choice([-1, 0, 1]),
                              self.ball_position[1] + self.moveCol)#np.random.choice([-1, 0, 1]))

        # 确保球在网格内
        self.ball_position = (int(max(0, min(9, self.ball_position[0]))),
                              int(max(0, min(9, self.ball_position[1]))))
        self.state[self.ball_position] = 1  # 标记球的位置
        self.movepaddle = move #拍子位置
        self.paddle_row = self.paddle_row + self.movepaddle #拍子位置
        if self.paddle_row < 0 or self.paddle_row>9:
            return 0
        #print(self.paddle_row)
        return 1

    def reset(self):
        random_number = np.random.uniform(1, 8)
        #self.satate = np.zeros((10, 10))
        print(self.ball_position)
        self.ball_position = (1,random_number)
        self.paddle_row = 5 #拍子位置
        self.moveRow = -1;
        self.moveCol = -1;

    def checkEnd(self,n):
        if  not n :
            self.reset()
        