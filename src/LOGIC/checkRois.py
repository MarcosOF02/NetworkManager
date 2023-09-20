import os


roiDir = os.listdir("./Rois/")

xsizeDesired = input("Size of axis x: ")
ysizeDesired = input("Size of axis y: ")

xsizeGot = None
ysizeGot = None

for r in roiDir:
    with open("./Rois/" + r,"r") as f:
        lines = f.readlines()
        c = 0
        for line in lines:
            c +=1
            xmin,ymin,xmax,ymax = map(int,line.split(" "))

            xsizeGot = xmax - xmin

            ysizeGot = ymax - ymin

            if xsizeDesired != xsizeGot:
                print("Tamanho del eje X erroneo ({}) en linea {} de: {}".format(xsizeGot, c, r))

            
            if ysizeDesired != ysizeGot:
                print("Tamanho del eje Y erroneo ({}) en linea {} de: {}".format(ysizeGot, c, r))



            



