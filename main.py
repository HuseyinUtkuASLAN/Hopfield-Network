from Hopfield import *

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox, QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

def stability(stbTest,vOriginal,lstVector):

	string = ""

	if stbTest == None:
		string = "is not stable"
	elif np.array_equal(vOriginal,stbTest):
		string = "is stalbe. It is equal with original vector."
		string += str(np.transpose(stbTest))
	elif numpyVectorInList(vOriginal,lstVector):
		string = "is stable. It is same with another vector that is given."
		string += str(np.transpose(stbTest))
	else:
		string = "is stable. It is not same with vector or another vector. During the test there was another vector during the test"
		string += str(np.transpose(stbTest))

	return string

class App(QMainWindow):
 
    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 textbox - pythonspot.com'
        self.left = 10
        self.top = 10
        self.width = 450
        self.height = 250

        self.textboxSizeX = 30
        self.textboxSizeY = 20

        self.initUI()
 
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
 


        vectorGap = 50

        # Create textbox
        self.textbox000 = self.createTextBox(20,40)

        self.textbox001 = self.createTextBox(20,70)

        self.textbox002 = self.createTextBox(20,100)

        self.textbox010 = self.createTextBox(vectorGap+50,40)

        self.textbox011 = self.createTextBox(vectorGap+50,70)

        self.textbox012 = self.createTextBox(vectorGap+50,100)

        self.textbox020 = self.createTextBox(vectorGap *2 +80,40)

        self.textbox021 = self.createTextBox(vectorGap *2 +80,70)

        self.textbox022 = self.createTextBox(vectorGap *2 +80,100)



        secondMatrixPosition = 300

        self.textbox100 = self.createTextBox(secondMatrixPosition+20,40)

        self.textbox101 = self.createTextBox(secondMatrixPosition+60,40)

        self.textbox102 = self.createTextBox(secondMatrixPosition+100,40)

        self.textbox110 = self.createTextBox(secondMatrixPosition+20,70)

        self.textbox111 = self.createTextBox(secondMatrixPosition+60,70)

        self.textbox112 = self.createTextBox(secondMatrixPosition+100,70)

        self.textbox120 = self.createTextBox(secondMatrixPosition+20,100)

        self.textbox121 = self.createTextBox(secondMatrixPosition+60,100)

        self.textbox122 = self.createTextBox(secondMatrixPosition+100,100)

        self.textbox000.setText("1")
        self.textbox001.setText("1")
        self.textbox002.setText("1")

        self.textbox010.setText("1")
        self.textbox011.setText("1")
        self.textbox012.setText("1")

        self.textbox020.setText("1")
        self.textbox021.setText("1")
        self.textbox022.setText("1")


        self.labelV0 = QLabel("V0", self)
        self.labelV0.move(20,10)

        self.labelV1 = QLabel("V1", self)
        self.labelV1.move(100,10)

        self.labelV2 = QLabel("V2", self)
        self.labelV2.move(180,10)

        self.labelMatrix = QLabel("Weight Matrix", self)
        self.labelMatrix.move(318,10)

        self.labelV0Solution = QLabel("", self)
        self.labelV0Solution.move(20,120)
        self.labelV0Solution.resize(400,20)

        self.labelV1Solution = QLabel("", self)
        self.labelV1Solution.move(20,140)
        self.labelV1Solution.resize(400,20)

        self.labelV2Solution = QLabel("", self)
        self.labelV2Solution.move(20,160)
        self.labelV2Solution.resize(400,20)

        self.labelError = QLabel("", self)
        self.labelError.move(20,120)


		# Create a button in the window
        self.button = QPushButton('Run', self)
        self.button.resize(410,25)
        self.button.move(20,200)
 
        # connect button to function on_click
        self.button.clicked.connect(self.on_click)
        self.show()

    def createTextBox(self,x,y):
        textbox = QLineEdit(self)
        textbox.move(x, y)
        textbox.resize(self.textboxSizeX,self.textboxSizeY)
        return textbox


    @pyqtSlot()
    def on_click(self):
        #textboxValue = self.textbox.text()
        #QMessageBox.question(self, 'Message - pythonspot.com', "You typed: " + textboxValue, QMessageBox.Ok, QMessageBox.Ok)
        #self.textbox.setText("")

        maxIteration = 10

        v00 = int(self.textbox000.text())
        v01 = int(self.textbox001.text())
        v02 = int(self.textbox002.text())

        v10 = int(self.textbox010.text())
        v11 = int(self.textbox011.text())
        v12 = int(self.textbox012.text())

        v20 = int(self.textbox020.text())
        v21 = int(self.textbox021.text())
        v22 = int(self.textbox022.text())

        v0 = np.array([[v00], [v01], [v02]])
        v1 = np.array([[v10], [v11], [v12]])
        v2 = np.array([[v20], [v21], [v22]])

        lstVector = []

        lstVector.append(v0)
        lstVector.append(v1)
        lstVector.append(v2)

        weight = calculateWeight(lstVector)
        self.textbox100.setText(str(weight[0,0]))
        self.textbox101.setText(str(weight[0,1]))
        self.textbox102.setText(str(weight[0,2]))

        self.textbox110.setText(str(weight[1,0]))
        self.textbox111.setText(str(weight[1,1]))
        self.textbox112.setText(str(weight[1,2]))

        self.textbox120.setText(str(weight[2,0]))
        self.textbox121.setText(str(weight[2,1]))
        self.textbox122.setText(str(weight[2,2]))
        #print (weight)

        stbTest0 = stabilityCheck( weight,v0, "v0", maxIteration )
        stbTest1 = stabilityCheck( weight,v1, "v1", maxIteration )
        stbTest2 = stabilityCheck( weight,v2, "v2", maxIteration )

        stb0 = stability(stbTest0,v0,lstVector)
        stb1 = stability(stbTest1,v1,lstVector)
        stb2 = stability(stbTest2,v2,lstVector)

        self.labelV0Solution.setText("v0 " + stb0)
        self.labelV1Solution.setText("v1 " + stb1)
        self.labelV2Solution.setText("v2 " + stb2)
        #print ("")
        #print (stbTest0)
        #print (stbTest1)
        #print (stbTest2)


if __name__ == '__main__':
	Debug()
	app = QApplication(sys.argv)
	ex = App()
	sys.exit(app.exec_())
	