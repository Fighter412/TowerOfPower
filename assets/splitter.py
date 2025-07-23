# Import packages
import cv2
import numpy as np
 


status = ["IDLE_F", "IDLE_R", 0, "IDLE_L",
          0, "WALK_R", 0, "WALK_L",
          0, 0, 0, 0,
          0, "180_R_D", 0, "180_L_D",
          0, "180_R_U", 0, "180_L_U",
          0, "540_R", 0, "540_L",
          0, 0, 0, 0,
          0, "DAG_R", 0, "DAG_L",
          0, "A_IDLE_R", 0, "A_IDLE_L",
          0, "A_WALK_R", 0, "A_WALK_L"]
frames = [8, 8, 8, 8, 8, 6, 6, 6, 6, 10, 10, 2, 2, 8, 8, 8, 8]
colors = ["BLUE", "BROWN", "CREAM", "FOREST", "GREEN", "ORANGE", "RED", "TERRACOTTA"]
for color in colors:
    img = cv2.imread(r'Assets\avatars\Sprites\\'+color+'.PNG', cv2.IMREAD_UNCHANGED)
    PATH = r"Assets\avatars\\"+color
    # Cropping an image
    row = 0
    index=0
    for item in status:
        if item != 0:
            column = 0
            for i in range(frames[index]):
                cropped_image = img[row:row+64, column*64:(column+1)*64]
                Z= cv2.resize(cropped_image,(192 ,192),fx=0, fy=0, interpolation = cv2.INTER_NEAREST)
                cv2.imwrite(PATH+"\\"+item+"_"+str(column)+".PNG", Z)
                column += 1
            index += 1
        row += 64










































