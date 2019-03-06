#TO DO LIST
"""
3 - Student Homework
4 - Search subjects and classes
5 - Behaviour and achievement points
6 - Clean up homescreen
7 - Add save function for homework


"""






#These are all the libraries that are being used in my program.
from PyQt4 import QtCore, QtGui #PyQt4 is the library I use to create the entire GUI and interactions with it.
#import MySQLdb
import sqlite3 #SQLite is the SQL interface for python where this allows me to interact with my database.
import hashlib #Hashlib is the default python library for hashing. This is useful for me as 
import sys #Used to interact with the system. Examples where this is used is sys.exit which allows me to close the program.
#from adminmain import Ui_AdminWindow
from userclasses import * #This is my own library. This imports the user classes.
import random #
import string
from shutil import copyfile
import os
from difflib import SequenceMatcher
from zxcvbn import zxcvbn
import time
import datetime


path = os.getcwd()
##host = "localhost"
##username = "default"
##password = "tomrowbotham"

#select * from users inner join students on users.id = students.id


#conn = MySQLdb.connect(host,username,password,db = "users")
conn = sqlite3.connect("school.db")
c = conn.cursor()


try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

#Global Background for all windows
css = _fromUtf8("QMainWindow {\n"
"background-color: qlineargradient(spread:pad, x1:0.494364, y1:0.806, x2:0.471, y2:0.142045, stop:0 rgba(17, 255, 56, 255), stop:1 rgba(255, 255, 255, 255));}")

labelfont = QtGui.QFont()
labelfont.setPointSize(12)

labelfont2 = QtGui.QFont()
labelfont2.setFamily(_fromUtf8("Gadugi"))
labelfont2.setPointSize(16)
labelfont2.setBold(False)
labelfont2.setWeight(50)

labelfont3 = QtGui.QFont()
labelfont3.setFamily(_fromUtf8("Gadugi"))
labelfont3.setBold(False)
labelfont3.setWeight(50)
labelfont3.setPointSize(12)

labelfont4 = QtGui.QFont()
labelfont4.setFamily(_fromUtf8("Gadugi"))
labelfont4.setBold(False)
labelfont4.setWeight(50)
labelfont4.setPointSize(10)



titlefont = QtGui.QFont()
titlefont.setFamily(_fromUtf8("Microsoft New Tai Lue"))
titlefont.setPointSize(36)
titlefont.setBold(True)
titlefont.setWeight(75)

titlefont2 = QtGui.QFont()
titlefont2.setFamily(_fromUtf8("Arial Black"))
titlefont2.setPointSize(24)
titlefont2.setBold(True)
titlefont2.setWeight(75)

titlefont3 = QtGui.QFont()
titlefont3.setPointSize(36)

titlefont4 = QtGui.QFont()
titlefont4.setFamily(_fromUtf8("Quicksand Light"))
titlefont4.setPointSize(18)

headerfont = QtGui.QFont()
headerfont.setFamily(_fromUtf8("Gadugi"))
headerfont.setPointSize(12)
headerfont.setBold(True)
headerfont.setWeight(75)

normalfont = QtGui.QFont()
normalfont.setFamily(_fromUtf8("Gadugi"))
normalfont.setPointSize(12)
normalfont.setBold(False)
normalfont.setWeight(50)

smalltitlefont = QtGui.QFont()
smalltitlefont.setFamily(_fromUtf8("Gadugi"))
smalltitlefont.setPointSize(15)
smalltitlefont.setBold(True)
smalltitlefont.setWeight(75)

typefont = QtGui.QFont()
typefont.setFamily(_fromUtf8("MS Shell Dlg 2"))
typefont.setPointSize(12)

numberfont = QtGui.QFont()
numberfont.setFamily(_fromUtf8("OCR A Std"))
numberfont.setPointSize(26)

regex=QtCore.QRegExp("[a-z-A-Z]+")
lettersvalidator = QtGui.QRegExpValidator(regex)

regex=QtCore.QRegExp("[a-z-A-Z ]+")
lettersandspacevalidator = QtGui.QRegExpValidator(regex)

regex=QtCore.QRegExp("[a-z-A-Z-0-9]+")
lettersandnumbersvalidator = QtGui.QRegExpValidator(regex)

regex=QtCore.QRegExp(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
emailvalidator = QtGui.QRegExpValidator(regex)	


        
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        #Creating Main Window
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 550)
        MainWindow.setAutoFillBackground(False)
        
        #Style Sheet (CSS)
        MainWindow.setStyleSheet(css)
        
        #Central Widget - Contains all buttons and labels
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))

        #Username Label
        self.usernameLabel = QtGui.QLabel(self.centralwidget)
        self.usernameLabel.setGeometry(QtCore.QRect(190, 190, 131, 51))
        self.usernameLabel.setFont(labelfont)
        self.usernameLabel.setObjectName(_fromUtf8("usernamelabel"))

        #Username Line Edit(Where you enter the username)
        self.usernameEdit = QtGui.QLineEdit(self.centralwidget)
        self.usernameEdit.setGeometry(QtCore.QRect(300, 200, 351, 31))
        self.usernameEdit.setFont(labelfont)
        self.usernameEdit.setObjectName(_fromUtf8("usernameEdit"))
        self.usernameEdit.setValidator(lettersandnumbersvalidator)

        #Password Label
        self.passwordLabel = QtGui.QLabel(self.centralwidget)
        self.passwordLabel.setGeometry(QtCore.QRect(190, 260, 131, 51))
        self.passwordLabel.setFont(labelfont)
        self.passwordLabel.setObjectName(_fromUtf8("passwordlabel"))

        #Password Line Edit 
        self.passwordEdit = QtGui.QLineEdit(self.centralwidget)
        self.passwordEdit.setEchoMode(QtGui.QLineEdit.Password)
        self.passwordEdit.setGeometry(QtCore.QRect(300, 270, 351, 31))
        self.passwordEdit.setFont(labelfont)
        self.passwordEdit.setObjectName(_fromUtf8("passwordEdit"))

        #Incorrect Label
        self.incorrectLabel = QtGui.QLabel(self.centralwidget)
        self.incorrectLabel.setGeometry(QtCore.QRect(150, 150, 600, 51))
        self.incorrectLabel.setFont(labelfont)
        self.incorrectLabel.setObjectName(_fromUtf8("incorrectLabel"))
        self.incorrectLabel.setStyleSheet("color:red")
        self.incorrectLabel.hide()


    ##        #Table Label
    ##        self.tableLabel = QtGui.QLabel(self.centralwidget)
    ##        self.tableLabel.setGeometry(QtCore.QRect(175, 325, 131, 51))
    ##        self.tableLabel.setFont(labelfont)
    ##        self.tableLabel.setAlignment(QtCore.Qt.AlignCenter)
    ##        self.tableLabel.setObjectName(_fromUtf8("tableLabel"))


    ##        #Table choice
    ##        self.tableChoice = QtGui.QComboBox(self.centralwidget)
    ##        self.tableChoice.setGeometry(QtCore.QRect(300, 337, 176, 26))
    ##        self.tableChoice.setObjectName(_fromUtf8("tableChoice"))
    ##        self.tableChoice.addItem("Student")
    ##        self.tableChoice.addItem("Teacher")
    ##        self.tableChoice.addItem("Admin")
        

        #Login Button
        self.loginBtn = QtGui.QPushButton(self.centralwidget)
        self.loginBtn.setGeometry(QtCore.QRect(485, 337, 75, 27))
        self.loginBtn.setFont(labelfont)
        self.loginBtn.setObjectName(_fromUtf8("loginBtn"))
        self.loginBtn.setShortcut("Enter")
        ########################Login Event###########################   
        self.loginBtn.clicked.connect(self.login_)      
        ##############################################################

        #Close Button
        self.closeBtn = QtGui.QPushButton(self.centralwidget)
        self.closeBtn.setGeometry(QtCore.QRect(575, 337, 75, 27))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.closeBtn.setFont(font)
        self.closeBtn.setObjectName(_fromUtf8("closeBtn"))
        #######################Close Event###########################
        self.closeBtn.clicked.connect(self.close_app)
        ##############################################################


        #School Logo
        self.logo = QtGui.QLabel(self.centralwidget)
        self.logo.setGeometry(QtCore.QRect(239, 0, 321, 181))
        self.logo.setText(_fromUtf8(""))
        self.logo.setPixmap(QtGui.QPixmap(_fromUtf8("logo-609437332.png")))
        self.logo.setScaledContents(False)
        self.logo.setAlignment(QtCore.Qt.AlignCenter)
        self.logo.setObjectName(_fromUtf8("logo"))

        MainWindow.setCentralWidget(self.centralwidget)

        #Menu Bar
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        MainWindow.setMenuBar(self.menuBar)

        #Status Bar
        self.statusBar = QtGui.QStatusBar(MainWindow)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Robert Smyth Login Form", None))
        self.usernameLabel.setText(_translate("MainWindow", "USERNAME", None))
        self.incorrectLabel.setText(_translate("MainWindow", "Error: User not found. Please verify details are correct and CAPS LOCK is not on.", None))
        self.passwordLabel.setText(_translate("MainWindow", "PASSWORD", None))
        #self.tableLabel.setText(_translate("MainWindow", "TABLE:", None))
        self.loginBtn.setText(_translate("MainWindow", "Login", None))
        self.closeBtn.setText(_translate("MainWindow", "Close", None))
        MainWindow.setWindowIcon(QtGui.QIcon('robertsmyth.png'))
        QtGui.QApplication.setStyle(QtGui.QStyleFactory.create("Windows Vista"))
        

    
    def close_app(self):
        choice = QtGui.QMessageBox.question(MainWindow, "Close Application",
                "Are you sure you would like to quit?",QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        if choice == QtGui.QMessageBox.Yes:
            sys.exit()
        else:
            pass
        

    def login_(self):
        #self.table = self.tableChoice.currentText()
        self.username = self.usernameEdit.text().lower()
        self.password = self.passwordEdit.text()
        self.password = hashing(self.password)

        c.execute("SELECT * FROM users WHERE username=:username AND password=:password ORDER BY username ASC",
                  {"username":self.username,"password":self.password})
        
        data = c.fetchone()
            #print(data)
        if data == None:
            self.incorrectLabel.show()
        else:
            global currentUser

            if data[6] == "Student":
                c.execute("SELECT yeargroup FROM student WHERE username=:username",{"username":self.username})
                yeargroup = c.fetchone()
                currentUser = Student(data[0],data[1],data[2],data[3],data[4],data[5],data[6],yeargroup,data[7])
            else:   
                currentUser = User(data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7])
            self.open_user()
                
                    
                #MainWindow.hide()
                

    def open_user(self):
        MainWindow.hide()
        self.window = QtGui.QMainWindow()
        self.ui = Ui_WelcomeWindow()
        self.ui.setupUi(self.window)
        self.window.show()




class Ui_WelcomeWindow(object):
    def setupUi(self, MainWindow):
        self.window = MainWindow
        #Creating Main Window
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        if currentUser.type == "Admin":
            height = 185
        else:
            height = 593
        MainWindow.resize(640, height)
        MainWindow.setStyleSheet(_fromUtf8("QMainWindow {\n"
"background-color: qlineargradient(spread:pad, x1:0.494364, y1:0.806, x2:0.471, y2:0.142045, stop:0 rgba(17, 255, 56, 255), stop:1 rgba(255, 255, 255, 255));}\n"
"QPushButton{background: transparent;"
"border: 1px solid black;}"))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))

        #Profile Picture
        self.profilePic = QtGui.QLabel(self.centralwidget)
        self.profilePic.setGeometry(QtCore.QRect(80, 10, 126, 126))
        self.profilePic.setText(_fromUtf8(""))
        if os.path.isfile(path + currentUser.pic):
            self.profilePic.setPixmap(QtGui.QPixmap(_fromUtf8(path + currentUser.pic)))
        else:
            self.profilePic.setPixmap(QtGui.QPixmap(_fromUtf8("placeholder.png")))

        self.profilePic.setScaledContents(True)
        self.profilePic.setObjectName(_fromUtf8("profilePic"))


        #Welcome Label
        self.welcomeLabel = QtGui.QLabel(self.centralwidget)
        self.welcomeLabel.setGeometry(QtCore.QRect(220, 0, 341, 141))
        self.welcomeLabel.setFont(titlefont3)
        self.welcomeLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.welcomeLabel.setObjectName(_fromUtf8("welcomeLabel"))


        #Homework Title - For Teachers and Admins This Will Be Labelled As Notices
        self.homeworkTitle = QtGui.QLabel(self.centralwidget)
        self.homeworkTitle.setGeometry(QtCore.QRect(80, 132, 481, 41))
        self.homeworkTitle.setFont(titlefont4)
        self.homeworkTitle.setObjectName(_fromUtf8("homeworkTitle"))


        #View Homework/Notices Button
        self.viewButton = QtGui.QPushButton(self.centralwidget)
        self.viewButton.setGeometry(QtCore.QRect(460, 330, 111, 23))
        font = QtGui.QFont()
        font.setUnderline(True)
        self.viewButton.setFont(font)
        self.viewButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.viewButton.setStyleSheet(_fromUtf8("QPushButton{background: transparent;\n"
"color: rgb(0, 0, 255);\n"
"text-decoration: underline;\n"
"border: 0px;}"))
        self.viewButton.setObjectName(_fromUtf8("viewButton"))


        ##TOP RESULTS

        ## RESULT ONE
        
        #Top button
        self.topButton = QtGui.QPushButton(self.centralwidget)
        self.topButton.setGeometry(QtCore.QRect(80, 180, 481, 51))
        self.topButton.setText(_fromUtf8(""))
        self.topButton.setObjectName(_fromUtf8("topButton"))

        #Result 1 Title
        self.topTitle = QtGui.QLabel(self.centralwidget)
        self.topTitle.setGeometry(QtCore.QRect(90, 187, 461, 21))
        self.topTitle.setFont(labelfont3)
        self.topTitle.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.topTitle.setObjectName(_fromUtf8("topTitle"))

        #Result 1 Description
        self.topDesc = QtGui.QLabel(self.centralwidget)
        self.topDesc.setGeometry(QtCore.QRect(90, 207, 461, 21))
        self.topDesc.setFont(labelfont4)
        self.topDesc.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.topDesc.setObjectName(_fromUtf8("topDesc"))

        self.top1 = WindowButtons(self.topButton,self.topTitle,self.topDesc,"Homework")


        ## RESULT TWO
        
        self.topTitle_2 = QtGui.QLabel(self.centralwidget)
        self.topTitle_2.setGeometry(QtCore.QRect(90, 237, 461, 21))
        self.topTitle_2.setFont(labelfont3)
        self.topTitle_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.topTitle_2.setObjectName(_fromUtf8("topTitle_2"))
        
        self.topDesc_2 = QtGui.QLabel(self.centralwidget)
        self.topDesc_2.setGeometry(QtCore.QRect(90, 257, 461, 21))
        self.topDesc_2.setFont(labelfont4)
        self.topDesc_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.topDesc_2.setObjectName(_fromUtf8("topDesc_2"))

        self.topButton_2 = QtGui.QPushButton(self.centralwidget)
        self.topButton_2.setGeometry(QtCore.QRect(80, 230, 481, 51))
        self.topButton_2.setText(_fromUtf8(""))
        self.topButton_2.setObjectName(_fromUtf8("topButton_2"))

        self.top2 = WindowButtons(self.topButton_2,self.topTitle_2,self.topDesc_2,"Homework")

        ##RESULT THREE
        self.topTitle_3 = QtGui.QLabel(self.centralwidget)
        self.topTitle_3.setGeometry(QtCore.QRect(90, 287, 461, 21))
        self.topTitle_3.setFont(labelfont3)
        self.topTitle_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.topTitle_3.setObjectName(_fromUtf8("topTitle_3"))
        
        self.topDesc_3 = QtGui.QLabel(self.centralwidget)
        self.topDesc_3.setGeometry(QtCore.QRect(90, 307, 461, 21))
        self.topDesc_3.setFont(labelfont4)
        self.topDesc_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.topDesc_3.setObjectName(_fromUtf8("topDesc_3"))
        
        self.topButton_3 = QtGui.QPushButton(self.centralwidget)
        self.topButton_3.setGeometry(QtCore.QRect(80, 280, 481, 51))
        self.topButton_3.setText(_fromUtf8(""))
        self.topButton_3.setObjectName(_fromUtf8("topButton_3"))

        self.top3 = WindowButtons(self.topButton_3,self.topTitle_3,self.topDesc_3,"Homework")


        #Achievement Point Box

        #Number
        self.achievementNumber = QtGui.QLabel(self.centralwidget)
        self.achievementNumber.setGeometry(QtCore.QRect(160, 410, 101, 61))
        self.achievementNumber.setFont(numberfont)
        self.achievementNumber.setAutoFillBackground(False)
        self.achievementNumber.setStyleSheet(_fromUtf8("QLabel{border: 1px solid black;\n"
        "background-color: rgb(0, 255, 0);}\n"
        ""))    
        self.achievementNumber.setAlignment(QtCore.Qt.AlignCenter)
        self.achievementNumber.setObjectName(_fromUtf8("achievementNumber"))

        #Title
        self.achievementTitle = QtGui.QLabel(self.centralwidget)
        self.achievementTitle.setGeometry(QtCore.QRect(160, 370, 101, 41))
        self.achievementTitle.setFont(typefont)
        self.achievementTitle.setAutoFillBackground(False)
        self.achievementTitle.setStyleSheet(_fromUtf8("QLabel{border: 1px solid black;\n"
        "background-color: rgb(255, 255, 255);}\n"
        ""))
        self.achievementTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.achievementTitle.setObjectName(_fromUtf8("achievementTitle"))


        #Behaviour Point Box
        #Number
        self.behaviourNumber = QtGui.QLabel(self.centralwidget)
        self.behaviourNumber.setGeometry(QtCore.QRect(370, 410, 101, 61))
        self.behaviourNumber.setFont(numberfont)
        self.behaviourNumber.setAutoFillBackground(False)
        self.behaviourNumber.setStyleSheet(_fromUtf8("QLabel{border: 1px solid black;\n"
        "background-color: rgb(255, 0, 0);}"))
        self.behaviourNumber.setAlignment(QtCore.Qt.AlignCenter)
        self.behaviourNumber.setObjectName(_fromUtf8("behaviourNumber"))

        #Title
        self.behaviourTitle = QtGui.QLabel(self.centralwidget)
        self.behaviourTitle.setGeometry(QtCore.QRect(370, 370, 101, 41))
        self.behaviourTitle.setFont(typefont)
        self.behaviourTitle.setAutoFillBackground(False)
        self.behaviourTitle.setStyleSheet(_fromUtf8("QLabel{border: 1px solid black;\n"
        "background-color: rgb(255, 255, 255);}\n"
        ""))
        self.behaviourTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.behaviourTitle.setObjectName(_fromUtf8("behaviourTitle"))

        #Sorting out alignment
        self.profilePic.raise_()
        self.welcomeLabel.raise_()
        self.homeworkTitle.raise_()
        self.viewButton.raise_()
        self.topTitle.raise_()
        self.topDesc.raise_()
        self.topTitle_2.raise_()
        self.topDesc_2.raise_()
        self.topTitle_3.raise_()
        self.topDesc_3.raise_()
        self.topButton.raise_()
        self.topButton_2.raise_()
        self.topButton_3.raise_()


        
##        #Setting Menu Bar
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))

       
        
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuClasses = QtGui.QMenu(self.menubar)
        self.menuClasses.setObjectName(_fromUtf8("menuClasses"))
        self.menuMessages = QtGui.QMenu(self.menubar)
        self.menuMessages.setObjectName(_fromUtf8("menuMessages"))
        self.menuHomework = QtGui.QMenu(self.menubar)
        self.menuHomework.setObjectName(_fromUtf8("menuHomework"))
        self.menubar.addAction(self.menuFile.menuAction())

        if currentUser.type != "Admin":
            self.menuHomework = QtGui.QMenu(self.menubar)
            self.menuHomework.setObjectName(_fromUtf8("menuHomework"))
            self.menubar.addAction(self.menuHomework.menuAction())

            self.viewHomework = QtGui.QAction(MainWindow)
            self.viewHomework.setObjectName(_fromUtf8("viewHomework"))
            self.viewHomework.setStatusTip("View my homework")
            self.menuHomework.addAction(self.viewHomework)
            self.viewHomework.triggered.connect(self.view_homework)                

        if currentUser.type != "Student":
            self.menuSubjects = QtGui.QMenu(self.menubar)
            self.menuSubjects.setObjectName(_fromUtf8("menuSubjects"))
            self.menuUsers = QtGui.QMenu(self.menubar)
            self.menuUsers.setObjectName(_fromUtf8("menuUsers"))
            self.menubar.addAction(self.menuUsers.menuAction())
            #View Users
            self.viewUsers = QtGui.QAction(MainWindow)
            self.viewUsers.setObjectName(_fromUtf8("viewUsers"))
            self.viewUsers.setStatusTip("View Users")
            self.viewUsers.triggered.connect(self.view_users)

        if currentUser.type == "Teacher":
            self.addHomework = QtGui.QAction(MainWindow)
            self.addHomework.setObjectName(_fromUtf8("addHomework"))
            self.addHomework.setStatusTip("Create a new homework")
            self.menuHomework.addAction(self.addHomework)
            self.addHomework.triggered.connect(self.create_homework)



            
            

        if currentUser.type == "Admin":
            #Add Class
            self.addClass = QtGui.QAction(MainWindow)
            self.addClass.setObjectName(_fromUtf8("addClass"))
            self.addClass.setStatusTip("Create a new class")
            self.addClass.triggered.connect(self.create_class)

            #Add Subject
            self.addSubject = QtGui.QAction(MainWindow)
            self.addSubject.setObjectName(_fromUtf8("addSubject"))
            self.addSubject.setStatusTip("Create a new subject")
            self.addSubject.triggered.connect(self.create_subject)

            #Add Admin
            self.addAdmin = QtGui.QAction(MainWindow)
            self.addAdmin.setObjectName(_fromUtf8("addAdmin"))
            self.addAdmin.setStatusTip("Create a new Admin account")
            self.addAdmin.triggered.connect(self.create_admin)

            #Add Teacher
            self.addTeacher = QtGui.QAction(MainWindow)
            self.addTeacher.setObjectName(_fromUtf8("addTeacher"))
            self.addTeacher.setStatusTip("Create a new Teacher account")
            self.addTeacher.triggered.connect(self.create_teacher)

            #Add Student
            self.addStudent = QtGui.QAction(MainWindow)
            self.addStudent.setObjectName(_fromUtf8("addStudent"))
            self.addStudent.setStatusTip("Create a new student account")
            self.addStudent.triggered.connect(self.create_student)
            
            self.menuSubjects.addAction(self.addSubject)
            self.menuUsers.addAction(self.addAdmin)
            self.menuUsers.addAction(self.addTeacher)
            self.menuUsers.addAction(self.addStudent)
            self.menuUsers.addAction(self.viewUsers)
            self.menuClasses.addAction(self.addClass)

            self.menubar.addAction(self.menuSubjects.menuAction())
            self.menubar.addAction(self.menuClasses.menuAction())
            
                


         #Adding to the bars

        #Log Out
        self.actionLogOut = QtGui.QAction(MainWindow)
        self.actionLogOut.setObjectName(_fromUtf8("actionLogOut"))
        self.actionLogOut.setShortcut("Ctrl+L")
        self.actionLogOut.setStatusTip("Sign Out Of Your Account")
        self.actionLogOut.triggered.connect(self.log_out)

        #Quit
        self.actionQuit = QtGui.QAction(MainWindow)
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
        self.actionQuit.setShortcut("Ctrl+Q")
        self.actionQuit.setStatusTip("Leave The App")
        self.actionQuit.triggered.connect(self.close_app)


        self.resetPassword = QtGui.QAction(MainWindow)
        self.resetPassword.setObjectName(_fromUtf8("resetPassword"))
        self.resetPassword.setStatusTip("Change your password.")
        self.resetPassword.triggered.connect(self.reset_password)

        
        #Add actions onto menu
        self.menuFile.addAction(self.actionLogOut)
        self.menuFile.addAction(self.actionQuit)
        self.menuFile.addAction(self.resetPassword)
        

        MainWindow.setMenuBar(self.menubar)
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuMessages.menuAction())


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Welcome Window", None))
        self.welcomeLabel.setText(_translate("MainWindow", "Welcome back,\n"
"Tom!", None))
        self.homeworkTitle.setText(_translate("MainWindow", "My Homework: (x Due Soon)", None))
        self.viewButton.setText(_translate("MainWindow", "Click to view more", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuClasses.setTitle(_translate("MainWindow", "Classes", None))
        self.menuMessages.setTitle(_translate("MainWindow", "Messages", None))
        self.behaviourTitle.setText(_translate("MainWindow","Behaviour\nPoints",None))
        self.achievementTitle.setText(_translate("MainWindow","Achievement\nPoints",None))
        
        if currentUser.type != "Admin":
            self.menuHomework.setTitle(_translate("MainWindow", "Homework", None))
        
        if currentUser.type != "Student":
            if currentUser.type == "Admin":
                self.addClass.setText(_translate("MainWindow","Add Class",None))
                self.addSubject.setText(_translate("MainWindow","Add Subject",None))
                self.addTeacher.setText(_translate("MainWindow","Add Teacher",None))
                self.addStudent.setText(_translate("MainWindow","Add Student",None))
                self.viewUsers.setText(_translate("MainWindow","View Users",None))
                self.addAdmin.setText(_translate("MainWindow","Add Admin",None))
            else:
                self.addHomework.setText(_translate("MainWindow","Add Homework",None))
                self.viewHomework.setText(_translate("MainWindow","View Homework",None))
            self.menuSubjects.setTitle(_translate("MainWindow", "Subjects", None))
            self.menuUsers.setTitle(_translate("MainWindow", "Users", None))
        self.actionQuit.setText(_translate("MainWindow", "Quit Application", None))
        self.actionLogOut.setText(_translate("MainWindow", "Log Out", None))
        self.resetPassword.setText(_translate("MainWindow","Reset Password",None))
        MainWindow.setWindowIcon(QtGui.QIcon('robertsmyth.png'))

    def view_users(self):
        self.viewUserPage = EditWindow()
        self.viewUserUi = Ui_SearchUsers()
        self.viewUserUi.setupUi(self.viewUserPage,"Search",None)
        self.viewUserPage.show()


    def create_admin(self):
        self.createAdminPage = EditWindow()
        self.createAdminUi = Ui_EditUserWindow()
        self.createAdminUi.setupUi(self.createAdminPage,"Admin",User("NULL","NULL","NULL","NULL","NULL","NULL","Admin","NULL"))
        self.createAdminPage.show()

    def create_teacher(self):
        self.createTeacherPage = EditWindow()
        self.createTeacherUi = Ui_EditUserWindow()
        self.createTeacherUi.setupUi(self.createTeacherPage,"Teacher",User("NULL","NULL","NULL","NULL","NULL","NULL","Teacher","NULL"))
        self.createTeacherPage.show()

    def create_student(self):
        self.createStudentPage = EditWindow()
        self.createStudentUi = Ui_EditUserWindow()
        self.createStudentUi.setupUi(self.createStudentPage,"Student",Student("NULL","NULL","NULL","NULL","NULL","NULL","Student","NULL","NULL"))
        self.createStudentPage.show()

    def create_subject(self):
        self.subjectPage = EditWindow()
        self.subjectui = Ui_EditSubjectWindow()
        self.subjectui.setupUi(self.subjectPage,Subject("NULL","NULL","NULL"))
        self.subjectPage.show()
        
    def create_class(self):
        self.classPage = EditWindow()
        self.classui = Ui_CreateClassWindow()
        self.classui.setupUi(self.classPage,Class("NULL","NULL","NULL","NULL"))
        self.classPage.show()


    def create_homework(self):
        self.homeworkPage = EditWindow()
        self.homeworkui = Ui_HomeWorkWindow()
        self.homeworkui.setupUi(self.homeworkPage,Homework("NULL","NULL","01/01/2001","NULL","NULL"))
        self.homeworkPage.show()

    def view_homework(self):
        self.viewHomeworkPage = EditWindow()
        self.viewhomeworkui = Ui_ViewHomeworkWindow()
        self.viewhomeworkui.setupUi(self.viewHomeworkPage,"Future")
        self.viewHomeworkPage.show()

    
    def close_app(self):
        choice = QtGui.QMessageBox.question(self.window,"Close Application","Are you sure you would like to quit?",QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        if choice == QtGui.QMessageBox.Yes:
            sys.exit()
        else:
            pass
    def log_out(self):
        self.window.close()
        self.open_login()
        


    def open_login(self):
        MainWindow.show()
        ui.usernameEdit.clear()
        ui.passwordEdit.clear()

    def reset_password(self):
        self.passwordPage = EditWindow()
        self.passwordUi = Ui_PasswordWindow()
        self.passwordUi.setupUi(self.passwordPage)
        self.passwordPage.show()


class WindowButtons():
    def __init__(self,button,title,desc,typeOfBox):
        self.button = button
        self.title = title
        self.desc = desc
        self.typeOfBox = typeOfBox

        self.button.clicked.connect(self.open_window)

    def retranslateUi(self,title,desc,id):
        self.title.setText(_translate("MainWindow",title,None))
        self.desc.setText(_translate("MainWindow",desc,None))
        self.id = id

    def hide_all(self):
        self.button.hide()
        self.title.hide()
        self.desc.hide()

    def show_all(self):
        self.button.show()
        self.title.show()
        self.desc.show()

    def open_window(self):
        if self.typeOfBox == "Homework":
            c.execute("SELECT * FROM homework WHERE homeworkid = :id",{"id":self.id})
            lesson = c.fetchone()
            self.homeworkPage = EditWindow()
            self.homeworkui = Ui_HomeWorkWindow()
            self.homeworkui.setupUi(self.homeworkPage,Homework(lesson[0],lesson[1],lesson[2],lesson[3],lesson[4]))
            self.homeworkPage.show()

class Ui_PasswordWindow(object):
    def setupUi(self, MainWindow):
        self.window = MainWindow
        #Creating Window
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(640, 480)
        MainWindow.setStyleSheet(css)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))

        #Title
        self.resetPasswordLabel = QtGui.QLabel(self.centralwidget)
        self.resetPasswordLabel.setGeometry(QtCore.QRect(110, 60, 421, 91))
        self.resetPasswordLabel.setFont(titlefont)
        self.resetPasswordLabel.setTextFormat(QtCore.Qt.PlainText)
        self.resetPasswordLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.resetPasswordLabel.setObjectName(_fromUtf8("resetPasswordLabel"))

        #Old Password Edit
        self.oldEdit = QtGui.QLineEdit(self.centralwidget)
        self.oldEdit.setGeometry(QtCore.QRect(210, 150, 351, 31))
        self.oldEdit.setObjectName(_fromUtf8("oldEdit"))
        self.oldEdit.setEchoMode(QtGui.QLineEdit.Password)

        #Old Password Label
        self.oldLabel = QtGui.QLabel(self.centralwidget)
        self.oldLabel.setGeometry(QtCore.QRect(60, 140, 141, 51))
        self.oldLabel.setFont(labelfont)
        self.oldLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.oldLabel.setObjectName(_fromUtf8("oldLabel"))

        #New Password Edit
        self.newEdit = QtGui.QLineEdit(self.centralwidget)
        self.newEdit.setGeometry(QtCore.QRect(210, 200, 351, 31))
        self.newEdit.setObjectName(_fromUtf8("newEdit"))
        self.newEdit.setEchoMode(QtGui.QLineEdit.Password)

        #New Password Label 
        self.newLabel = QtGui.QLabel(self.centralwidget)
        self.newLabel.setGeometry(QtCore.QRect(60, 190, 141, 51))
        self.newLabel.setFont(labelfont)
        self.newLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.newLabel.setObjectName(_fromUtf8("newLabel"))

        #Confirm Password Edit
        self.confirmEdit = QtGui.QLineEdit(self.centralwidget)
        self.confirmEdit.setGeometry(QtCore.QRect(210, 250, 351, 31))
        self.confirmEdit.setObjectName(_fromUtf8("confirmEdit"))
        self.confirmEdit.setEchoMode(QtGui.QLineEdit.Password)

        #Confirm Password Label
        self.confirmLabel = QtGui.QLabel(self.centralwidget)
        self.confirmLabel.setGeometry(QtCore.QRect(30, 240, 171, 51))
        self.confirmLabel.setFont(labelfont)
        self.confirmLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.confirmLabel.setObjectName(_fromUtf8("confirmLabel"))

        #Save Button
        self.saveBtn = QtGui.QPushButton(self.centralwidget)
        self.saveBtn.setGeometry(QtCore.QRect(486, 300, 75, 27))
        self.saveBtn.setFont(labelfont)
        self.saveBtn.setObjectName(_fromUtf8("saveBtn"))
        self.saveBtn.clicked.connect(self.change_pass)

        


        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Reset Password", None))
        MainWindow.setWindowIcon(QtGui.QIcon('robertsmyth.png'))
        self.resetPasswordLabel.setText(_translate("MainWindow", "RESET PASSWORD", None))
        self.oldLabel.setText(_translate("MainWindow", "OLD PASSWORD:", None))
        self.newLabel.setText(_translate("MainWindow", "NEW PASSWORD:", None))
        self.confirmLabel.setText(_translate("MainWindow", "CONFIRM PASSWORD:", None))
        self.saveBtn.setText(_translate("MainWindow", "Save", None))

    def change_pass(self):
        old = self.oldEdit.text()
        old = hashing(old)
        if currentUser.password == old:
            new = self.newEdit.text()
            if new == self.confirmEdit.text():
                strength = zxcvbn(new,[currentUser.first,currentUser.last,currentUser.dob])["score"]
                if strength > 2:
                    currentUser.password = hashing(new)
                    c.execute("UPDATE users SET password = :password WHERE username =:username",
                              {"password":currentUser.password,"username":currentUser.username})
                    conn.commit()
                    QtGui.QMessageBox.question(self.window,"Saved","Save Successful",
                                   QtGui.QMessageBox.Ok)
                    self.window.hide()
                    return
                QtGui.QMessageBox.question(self.window,"Error","Error: Your password is too weak and could be guessed easy. Please try use a more complex password.",
                                            QtGui.QMessageBox.Ok)
                return
            QtGui.QMessageBox.question(self.window,"Error","Error: Passwords did not match.",
                                        QtGui.QMessageBox.Ok)
            return
        QtGui.QMessageBox.question(self.window,"Error","Error: Incorrect password.",
                                    QtGui.QMessageBox.Ok)
            
            


class Ui_CreateClassWindow(object):
    def setupUi(self, CreateClassWindow,currentClass):
        
        #Creating Main Window
        CreateClassWindow.setObjectName(_fromUtf8("CreateClassWindow"))
        CreateClassWindow.resize(640, 480)
        
        #Style Sheet (CSS)
        CreateClassWindow.setStyleSheet(css)
        
        #Central Widget
        self.centralwidget = QtGui.QWidget(CreateClassWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.currentClass = currentClass
        self.window = CreateClassWindow

        #Label for subject name
        self.subjectLabel = QtGui.QLabel(self.centralwidget)
        self.subjectLabel.setGeometry(QtCore.QRect(100, 105, 71, 51))
        self.subjectLabel.setFont(labelfont)
        self.subjectLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.subjectLabel.setObjectName(_fromUtf8("subjectLabel"))

        #Label for teacher name
        self.teacherLabel = QtGui.QLabel(self.centralwidget)
        self.teacherLabel.setGeometry(QtCore.QRect(100, 145, 71, 51))
        self.teacherLabel.setFont(labelfont)
        self.teacherLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.teacherLabel.setObjectName(_fromUtf8("teacherLabel"))

        #Create Subject Label
        self.createSubjectLabel = QtGui.QLabel(self.centralwidget)
        self.createSubjectLabel.setGeometry(QtCore.QRect(130, 10, 371,91))
        self.createSubjectLabel.setFont(titlefont)
        self.createSubjectLabel.setTextFormat(QtCore.Qt.PlainText)
        self.createSubjectLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.createSubjectLabel.setObjectName(_fromUtf8("createSubjectLabel"))

        #Button to create
        self.createBtn = QtGui.QPushButton(self.centralwidget)
        self.createBtn.setGeometry(QtCore.QRect(530, 430, 75, 27))
        self.createBtn.setFont(labelfont)
        self.createBtn.setObjectName(_fromUtf8("createBtn"))
        if self.currentClass.id == "NULL":
            self.createBtn.clicked.connect(self.create_)
        else:
            self.createBtn.clicked.connect(self.save_changes)


        
        #Muli Choice Lesson 1 Timetable
        self.lesson1Box = QtGui.QComboBox(self.centralwidget)
        self.lesson1Box.setGeometry(QtCore.QRect(180, 200, 351, 22))
        self.lesson1Box.setObjectName(_fromUtf8("lesson1Box"))
        
        #Muli Choice Lesson 2 Timetable
        self.lesson2Box = QtGui.QComboBox(self.centralwidget)
        self.lesson2Box.setGeometry(QtCore.QRect(180, 240, 351, 22))
        self.lesson2Box.setObjectName(_fromUtf8("lesson2Box"))
        #Lesson 3
        self.lesson3Box = QtGui.QComboBox(self.centralwidget)
        self.lesson3Box.setGeometry(QtCore.QRect(180, 280, 351, 22))
        self.lesson3Box.setObjectName(_fromUtf8("lesson3Box"))
        #Lesson 4
        self.lesson4Box = QtGui.QComboBox(self.centralwidget)
        self.lesson4Box.setGeometry(QtCore.QRect(180, 320, 351, 22))
        self.lesson4Box.setObjectName(_fromUtf8("lesson4Box"))
        #Year Group
        self.yearCombo = QtGui.QComboBox(self.centralwidget)
        self.yearCombo.setGeometry(QtCore.QRect(180, 360, 351, 22))
        self.yearCombo.setObjectName(_fromUtf8("yearCombo"))
        self.yearCombo.addItem("Year 12")
        self.yearCombo.addItem("Year 13")
        if self.currentClass.yearGroup == "13":
            self.yearCombo.setCurrentIndex(1)
            

        #Adding Lessons to boxes
        self.lesson1Box.addItem("N/A")
        self.lesson2Box.addItem("N/A")
        self.lesson3Box.addItem("N/A")
        self.lesson4Box.addItem("N/A")
        week = ["MON","TUE","WED","THURS","FRI"]
        lessons = []
        for day in week:
            for lesson in range (1,6):
                self.lesson1Box.addItem(day + " " + str(lesson))
                self.lesson2Box.addItem(day + " " + str(lesson))
                self.lesson3Box.addItem(day + " " + str(lesson))
                self.lesson4Box.addItem(day + " " + str(lesson))



        #Lesson 1 Label
        self.lesson1Label = QtGui.QLabel(self.centralwidget)
        self.lesson1Label.setGeometry(QtCore.QRect(100, 185, 71, 51))
        self.lesson1Label.setFont(labelfont)
        self.lesson1Label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lesson1Label.setObjectName(_fromUtf8("lesson1Label"))

        #Lesson 2 Label
        self.lesson2Label = QtGui.QLabel(self.centralwidget)
        self.lesson2Label.setGeometry(QtCore.QRect(100, 225, 71, 51))
        self.lesson2Label.setFont(labelfont)
        self.lesson2Label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lesson2Label.setObjectName(_fromUtf8("lesson2Label"))

        #Lesson 3 Label
        self.lesson3Label = QtGui.QLabel(self.centralwidget)
        self.lesson3Label.setGeometry(QtCore.QRect(100, 265, 71, 51))
        self.lesson3Label.setFont(labelfont)
        self.lesson3Label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lesson3Label.setObjectName(_fromUtf8("lesson3Label"))

        #Lesson 4 Label
        self.lesson4Label = QtGui.QLabel(self.centralwidget)
        self.lesson4Label.setGeometry(QtCore.QRect(90, 305, 81, 51))
        self.lesson4Label.setFont(labelfont)
        self.lesson4Label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lesson4Label.setObjectName(_fromUtf8("lesson4Label"))

        #Year Group Label
        self.yearLabel = QtGui.QLabel(self.centralwidget)
        self.yearLabel.setGeometry(QtCore.QRect(50, 345, 121, 51))
        self.yearLabel.setFont(labelfont)
        self.yearLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.yearLabel.setObjectName(_fromUtf8("yearLabel"))

        #Teacher Combo Box
        self.teacherCombo = QtGui.QComboBox(self.centralwidget)
        self.teacherCombo.setGeometry(QtCore.QRect(180, 160, 351, 22))
        self.teacherCombo.setObjectName(_fromUtf8("teacherCombo"))
        c.execute("""SELECT first, last, username
                  FROM users
                  WHERE type = 'Teacher'
                  ORDER BY first ASC""")
        data = c.fetchall()
        for i in range(len(data)):
            self.teacherCombo.addItem("{} {} ({})".format(data[i][0],data[i][1],data[i][2] ))
            if data[i][2] == self.currentClass.teacher:
                self.teacherCombo.setCurrentIndex(i)

        #Subject Combo Box
        self.subjectCombo = QtGui.QComboBox(self.centralwidget)
        self.subjectCombo.setGeometry(QtCore.QRect(180, 120, 351, 22))
        self.subjectCombo.setObjectName(_fromUtf8("subjectCombo"))
        c.execute("""SELECT fullname
                  FROM subjects
                  ORDER BY fullname ASC""")
        data = c.fetchall()
        for i in range(len(data)):
            self.subjectCombo.addItem("{}".format(data[i][0]))
            if data[i][0] == self.currentClass.subject:
                self.subjectCombo.setCurrentIndex(i)


        #Class ID Line Edit
        self.idEdit = QtGui.QLineEdit(self.centralwidget)
        self.idEdit.setGeometry(QtCore.QRect(180, 400, 351, 21))
        self.idEdit.setObjectName(_fromUtf8("idEdit"))
        self.idEdit.setEnabled(False)

        #Class ID Label
        self.idLabel = QtGui.QLabel(self.centralwidget)
        self.idLabel.setGeometry(QtCore.QRect(90, 385, 81, 51))
        self.idLabel.setFont(labelfont)
        self.idLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.idLabel.setObjectName(_fromUtf8("idLabel"))
        self.idLabel.setEnabled(False)
        


        
        CreateClassWindow.setCentralWidget(self.centralwidget)

        #Creating Menu Bar
        self.menubar = QtGui.QMenuBar(CreateClassWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 21))

        CreateClassWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(CreateClassWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        CreateClassWindow.setStatusBar(self.statusbar)
        self.retranslateUi(CreateClassWindow)
        QtCore.QMetaObject.connectSlotsByName(CreateClassWindow)

    def retranslateUi(self, CreateClassWindow):
        if self.currentClass.id == "NULL":
            CreateClassWindow.setWindowTitle(_translate("CreateClassWindow", "Create Class Window", None))
            self.createSubjectLabel.setText(_translate("CreateClassWindow", "CREATE CLASS", None))
            self.createBtn.setText(_translate("CreateClassWindow", "Create", None))
        else:
            CreateClassWindow.setWindowTitle(_translate("CreateClassWindow", "Edit Class Window", None))
            self.createSubjectLabel.setText(_translate("CreateClassWindow", "EDIT CLASS", None))
            self.createBtn.setText(_translate("CreateClassWindow", "Save", None))
            self.idEdit.setText(_translate("EditUserWindow",self.currentClass.id,None))

        self.subjectLabel.setText(_translate("CreateClassWindow", "SUBJECT", None))
        self.teacherLabel.setText(_translate("CreateClassWindow", "TEACHER", None))
        self.lesson1Label.setText(_translate("CreateClassWindow", "LESSON 1", None))
        self.lesson2Label.setText(_translate("CreateClassWindow", "LESSON 2", None))
        self.lesson3Label.setText(_translate("CreateClassWindow", "LESSON 3", None))
        self.lesson4Label.setText(_translate("CreateClassWindow", "LESSON 4", None))
        self.yearLabel.setText(_translate("CreateClassWindow", "YEAR GROUP", None))
        self.idLabel.setText(_translate("CreateClassWindow", "CLASS ID", None))
        CreateClassWindow.setWindowIcon(QtGui.QIcon('robertsmyth.png'))
        

    def create_(self):
        #self.table = self.tableChoice.currentText()
        #self.username = self.usernameEdit.text()

        self.get_details()
        #TEST THIS LATER
        c.execute("SELECT shortname FROM subjects WHERE fullname = :fullname",
                  {"fullname":self.currentClass.subject})
        self.currentClass.id = c.fetchone()[0]
        c.execute("SELECT id FROM classes WHERE id LIKE :id",
                  {"id":self.currentClass.id + "%"})
        data = c.fetchall()
        classes = []
        self.currentClass.id += "1"
        for item in data:
            classes.append(item[0])
            chosen = False
            while not chosen:
                if self.currentClass.id in classes:
                    #print(self.username[:len(self.last)+1])
                    self.currentClass.id = self.currentClass.id[:-1] + str(int(self.currentClass.id[-1])+1)
                else:
                    chosen = True
        c.execute("INSERT INTO classes VALUES (:yeargroup,:teacher,:subject,:id)",
                  {"yeargroup":self.currentClass.yearGroup,"teacher":self.currentClass.teacher,"subject":self.currentClass.subject,"id":self.currentClass.id})
        c.execute("CREATE TABLE "+self.currentClass.id+
                  "(Student text)")

        conn.commit()

        self.window.hide()
        self.newWindow = EditWindow()
        self.newPage = Ui_CreateClassWindow()
        self.newPage.setupUi(self.newWindow,self.currentClass)
        self.newWindow.show()


    def get_details(self):
        self.currentClass.subject = self.subjectCombo.currentText()
        self.currentClass.teacher = self.teacherCombo.currentText()
        self.currentClass.teacher = self.currentClass.teacher[self.currentClass.teacher.find("(")+1:self.currentClass.teacher.find(")")]
        self.currentClass.yearGroup = self.yearCombo.currentText()[-2:]

        



    def save_changes(self):
        choice = QtGui.QMessageBox.question(self.window,"Save Changes","Are you sure you would like save the changes?\n"
                                            "Any previous data will be lost.",QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        if choice == QtGui.QMessageBox.Yes:
            self.save_()

    def save_(self):
        self.get_details()
        c.execute("UPDATE classes SET teacher = :teacher AND yeargroup = :yearGroup WHERE id = :id",
                  {"teacher":self.currentClass.teacher,"yearGroup":self.currentClass.yearGroup,"id":self.currentClass.id})
        conn.commit()
        self.saved_window()

    def saved_window(self):
        QtGui.QMessageBox.question(self.window,"Saved","Save Successful",
                                   QtGui.QMessageBox.Ok)




class Ui_EditSubjectWindow(object):
    def setupUi(self, EditSubjectWindow,subject):
        self.subject = subject
        #Creating Main Window
        EditSubjectWindow.setObjectName(_fromUtf8("EditSubjectWindow"))
        EditSubjectWindow.resize(640, 480)
        #Style Sheet 
        EditSubjectWindow.setStyleSheet(css)
        self.window = EditSubjectWindow
        #Central Widget
        self.centralwidget = QtGui.QWidget(EditSubjectWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))

        #Edit Subject Label
        self.editSubjectLabel = QtGui.QLabel(self.centralwidget)
        self.editSubjectLabel.setGeometry(QtCore.QRect(130, 40, 391, 91))
        self.editSubjectLabel.setFont(titlefont)
        self.editSubjectLabel.setTextFormat(QtCore.Qt.PlainText)
        self.editSubjectLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.editSubjectLabel.setObjectName(_fromUtf8("editSubjectLabel"))

        #Full name label
        self.fullNameLabel = QtGui.QLabel(self.centralwidget)
        self.fullNameLabel.setGeometry(QtCore.QRect(70, 150, 141, 51))
        self.fullNameLabel.setFont(labelfont)
        self.fullNameLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.fullNameLabel.setObjectName(_fromUtf8("fullNameLabel"))

        #Full name text
        self.fullNameEdit = QtGui.QLineEdit(self.centralwidget)
        self.fullNameEdit.setGeometry(QtCore.QRect(220, 160, 351, 31))
        self.fullNameEdit.setFont(labelfont)
        self.fullNameEdit.setObjectName(_fromUtf8("fullNameEdit"))
        self.fullNameEdit.setValidator(lettersandspacevalidator)

        #Short name edit
        self.shortNameEdit = QtGui.QLineEdit(self.centralwidget)
        self.shortNameEdit.setGeometry(QtCore.QRect(220, 210, 351, 31))
        self.shortNameEdit.setFont(labelfont)
        self.shortNameEdit.setObjectName(_fromUtf8("shortNameEdit"))
        self.shortNameEdit.setValidator(lettersvalidator)
        self.shortNameEdit.setMaxLength(8)

        #Short name label      
        self.shortNameLabel = QtGui.QLabel(self.centralwidget)
        self.shortNameLabel.setGeometry(QtCore.QRect(70, 200, 141, 51))
        self.shortNameLabel.setFont(labelfont)
        self.shortNameLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.shortNameLabel.setObjectName(_fromUtf8("shortNameLabel"))

        #Head Of Subject Label
        self.headOfSubjectLabel = QtGui.QLabel(self.centralwidget)
        self.headOfSubjectLabel.setGeometry(QtCore.QRect(70, 250, 141, 51))
        self.headOfSubjectLabel.setFont(labelfont)
        self.headOfSubjectLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.headOfSubjectLabel.setObjectName(_fromUtf8("headOfSubjectLabel"))

        #Save Button
        self.saveBtn = QtGui.QPushButton(self.centralwidget)
        self.saveBtn.setGeometry(QtCore.QRect(500, 300, 75, 27))
        self.saveBtn.setFont(labelfont)
        self.saveBtn.setObjectName(_fromUtf8("saveBtn"))
        #######################Button Event###########################
        if self.subject.fullname == "NULL":
            self.saveBtn.clicked.connect(self.create_)
        else:
            self.saveBtn.clicked.connect(self.save_changes)

        #Head Of Subject combo box
        self.headCombo = QtGui.QComboBox(self.centralwidget)
        self.headCombo.setGeometry(QtCore.QRect(220, 260, 351, 31))
        self.headCombo.setObjectName(_fromUtf8("headCombo"))
        c.execute("""SELECT first, last, username
                  FROM users
                  WHERE type = 'Teacher'
                  ORDER BY first ASC""")
        data = c.fetchall()
        for i in range(len(data)):
            self.headCombo.addItem("{} {} ({})".format(data[i][0],data[i][1],data[i][2] ))
            if data[i][2] == self.subject.head:
                self.headCombo.setCurrentIndex(i)
 

        #Menu and status bars
        EditSubjectWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(EditSubjectWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        EditSubjectWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(EditSubjectWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        EditSubjectWindow.setStatusBar(self.statusbar)

        self.retranslateUi(EditSubjectWindow)
        QtCore.QMetaObject.connectSlotsByName(EditSubjectWindow)
        self.statusbar = QtGui.QStatusBar(EditSubjectWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        EditSubjectWindow.setStatusBar(self.statusbar)
        self.retranslateUi(EditSubjectWindow)
        QtCore.QMetaObject.connectSlotsByName(EditSubjectWindow)


    def retranslateUi(self, EditSubjectWindow):
        EditSubjectWindow.setWindowTitle(_translate("EditSubjectWindow", "Edit Subject", None))
        if self.subject.fullname == "NULL":
            self.editSubjectLabel.setText(_translate("EditSubjectWindow", "CREATE SUBJECT", None))
            self.saveBtn.setText(_translate("EditSubjectWindow", "Create", None))
        else:
            self.fullNameEdit.setText(_translate("EditSubjectWindow", self.subject.fullname, None))
            self.fullNameEdit.setEnabled(False)
            self.shortNameEdit.setEnabled(False)
            self.shortNameEdit.setText(_translate("EditSubjectWindow", self.subject.shortname, None))
            #self.headCombo.setText(_translate("EditSubjectWindow", self.subject.head, None)) 
            self.saveBtn.setText(_translate("EditSubjectWindow", "Save", None))
            self.editSubjectLabel.setText(_translate("EditSubjectWindow", "EDIT SUBJECT", None))
        self.fullNameLabel.setText(_translate("EditSubjectWindow", "FULL NAME", None))
        self.shortNameLabel.setText(_translate("EditSubjectWindow", "SHORT NAME", None))
        self.headOfSubjectLabel.setText(_translate("EditSubjectWindow", "HEAD OF SUBJECT", None))
        EditSubjectWindow.setWindowIcon(QtGui.QIcon('robertsmyth.png'))



    def create_(self):
        #self.table = self.tableChoice.currentText()
        #self.username = self.usernameEdit.text()

        self.get_details()
        c.execute("INSERT INTO subjects VALUES (:full,:short,:head)",
                  {"full":self.subject.full,"short":self.subject.short,"head":self.subject.head})

        self.subject = Subject(self.subject.full,self.subject.short,self.subject.head)
        
        conn.commit()

        self.window.hide()
        self.newWindow = EditWindow()
        self.newPage = Ui_EditSubjectWindow()
        self.newPage.setupUi(self.newWindow,self.subject)
        self.newWindow.show()


    def get_details(self):
        self.subject.full = self.fullNameEdit.text()
        self.subject.short = self.shortNameEdit.text()
        self.subject.head = self.headCombo.currentText()
        self.subject.head = self.subject.head[self.subject.head.find("(")+1:self.subject.head.find(")")]
        return self.subject.full,self.subject.short,self.subject.head
    
    def save_changes(self):
        choice = QtGui.QMessageBox.question(self.window,"Save Changes","Are you sure you would like save the changes?\n"
                                            "Any previous data will be lost.",QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        if choice == QtGui.QMessageBox.Yes:
            self.save_()

    def save_(self):
        self.get_details()
        c.execute("UPDATE subjects SET head = :head WHERE fullname = :full",
                  {"head":self.subject.head,"full":self.subject.full})
        conn.commit()
        self.saved_window()

    def saved_window(self):
        QtGui.QMessageBox.question(self.window,"Saved","Save Successful",
                                   QtGui.QMessageBox.Ok)



class Ui_EditUserWindow(object):
    def setupUi(self, EditUserWindow,typeOfUser,user):
        self.user = user
        #print(self.user.first,self.user.last,self.user.username,self.user.password,self.user.dob,self.user.email,self.user.type,self.user.pic,self.user.yeargroup)
        #Creating Main Window
        EditUserWindow.setObjectName(_fromUtf8("EditUserWindow"))
        EditUserWindow.resize(640, 480)
        EditUserWindow.setAutoFillBackground(False)
        self.window = EditUserWindow
        self.type = typeOfUser
        moveY = 0
        self.centralwidget = QtGui.QWidget(EditUserWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))


            
        #CSS
        EditUserWindow.setStyleSheet(css)
        #Creating widget
        self.centralwidget = QtGui.QWidget(EditUserWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))

        if self.type == "Student":
            #Year Group chooser
            self.yearGroup = QtGui.QComboBox(self.centralwidget)
            self.yearGroup.setGeometry(QtCore.QRect(190, 340, 351, 31))
            self.yearGroup.setObjectName(_fromUtf8("yearGroup"))
            self.yearGroup.addItem("12")
            self.yearGroup.addItem("13")

            #Year group label
            self.yearGroupLabel = QtGui.QLabel(self.centralwidget)
            self.yearGroupLabel.setGeometry(QtCore.QRect(40, 330, 141, 51))
            self.yearGroupLabel.setFont(labelfont)
            self.yearGroupLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
            self.yearGroupLabel.setObjectName(_fromUtf8("yearGroupLabel"))

            #MoveY
            moveY += 30

        #Profile Picture
        self.profilePic = QtGui.QLabel(self.centralwidget)
        self.profilePic.setGeometry(QtCore.QRect(30, 10, 126, 126))
        self.profilePic.setText(_fromUtf8(""))
        if os.path.isfile(path + self.user.pic):
            self.profilePic.setPixmap(QtGui.QPixmap(_fromUtf8(path + self.user.pic)))
        else:
            self.profilePic.setPixmap(QtGui.QPixmap(_fromUtf8("placeholder.png")))
        self.profilePic.setScaledContents(True)
        self.profilePic.setObjectName(_fromUtf8("profilePic"))
        

        #Title label
        self.titleLabel = QtGui.QLabel(self.centralwidget)
        self.titleLabel.setGeometry(QtCore.QRect(140, 30, 411, 91))
        self.titleLabel.setFont(titlefont)
        self.titleLabel.setTextFormat(QtCore.Qt.PlainText)
        self.titleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.titleLabel.setObjectName(_fromUtf8("titleLabel"))

        #Date of birth editor
        self.dateEdit = QtGui.QDateEdit(self.centralwidget)
        self.dateEdit.setGeometry(QtCore.QRect(190, 300, 351, 31))
        self.dateEdit.setObjectName(_fromUtf8("dateEdit"))
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.calendarWidget().installEventFilter(EditUserWindow)
        self.dateEdit.setMaximumDate(QtCore.QDate.currentDate())

        #Date of birth label
        self.dateLabel = QtGui.QLabel(self.centralwidget)
        self.dateLabel.setGeometry(QtCore.QRect(40, 290, 141, 51))
        self.dateLabel.setFont(labelfont)
        self.dateLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.dateLabel.setObjectName(_fromUtf8("dateLabel"))

        #Last name label
        self.lastLabel = QtGui.QLabel(self.centralwidget)
        self.lastLabel.setGeometry(QtCore.QRect(40, 170, 141, 51))
        self.lastLabel.setFont(labelfont)
        self.lastLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lastLabel.setObjectName(_fromUtf8("lastLabel"))

        #Lastname editor
        self.lastEdit = QtGui.QLineEdit(self.centralwidget)
        self.lastEdit.setGeometry(QtCore.QRect(190, 180, 351, 31))
        self.lastEdit.setFont(labelfont)
        self.lastEdit.setObjectName(_fromUtf8("lastEdit"))
        self.lastEdit.setValidator(lettersvalidator)
        

        #Username editor
        self.usernameEdit = QtGui.QLineEdit(self.centralwidget)
        self.usernameEdit.setGeometry(QtCore.QRect(190, 220, 351, 31))
        self.usernameEdit.setFont(labelfont)
        self.usernameEdit.setObjectName(_fromUtf8("usernameEdit"))
        self.usernameEdit.setEnabled(False)

        #Username label
        self.usernameLabel = QtGui.QLabel(self.centralwidget)
        self.usernameLabel.setGeometry(QtCore.QRect(40, 210, 141, 51))
        self.usernameLabel.setFont(labelfont)
        self.usernameLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.usernameLabel.setObjectName(_fromUtf8("usernameLabel"))
        self.usernameLabel.setEnabled(False)

        #Email Label
        self.emailLabel = QtGui.QLabel(self.centralwidget)
        self.emailLabel.setGeometry(QtCore.QRect(40, 250, 141, 51))
        self.emailLabel.setFont(labelfont)
        self.emailLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.emailLabel.setObjectName(_fromUtf8("emailLabel"))

        #Email Editor
        self.emailEdit = QtGui.QLineEdit(self.centralwidget)
        self.emailEdit.setGeometry(QtCore.QRect(190, 260, 351, 31))
        self.emailEdit.setFont(labelfont)
        self.emailEdit.setText(_fromUtf8(""))
        self.emailEdit.setObjectName(_fromUtf8("emailEdit"))
        self.emailEdit.setValidator(emailvalidator)

        #First name editor
        self.firstEdit = QtGui.QLineEdit(self.centralwidget)
        self.firstEdit.setGeometry(QtCore.QRect(190, 140, 351, 31))
        self.firstEdit.setFont(labelfont)
        self.firstEdit.setObjectName(_fromUtf8("firstEdit"))
        self.firstEdit.setValidator(lettersvalidator)

        #Firstname label
        self.firstLabel = QtGui.QLabel(self.centralwidget)
        self.firstLabel.setGeometry(QtCore.QRect(40, 130, 141, 51))
        self.firstLabel.setFont(labelfont)
        self.firstLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.firstLabel.setObjectName(_fromUtf8("firstLabel"))



        #Edit button
        self.editBtn = QtGui.QPushButton(self.centralwidget)
        self.editBtn.setGeometry(QtCore.QRect(470, 350+moveY, 75, 27))
        self.editBtn.setFont(labelfont)
        self.editBtn.setObjectName(_fromUtf8("editBtn"))
        #######################Button Event###########################
        if self.user.first == "NULL":
            self.editBtn.clicked.connect(self.create_)
        else:
            self.editBtn.clicked.connect(self.save_changes)
                    #Upload pic button
            self.uploadPic = QtGui.QPushButton(self.centralwidget)
            self.uploadPic.setGeometry(QtCore.QRect(340, 380+moveY, 206, 27))
            self.uploadPic.setFont(labelfont)
            self.uploadPic.setObjectName(_fromUtf8("uploadPic"))
            self.uploadPic.clicked.connect(self.upload_picture)
                    #Reset password button
            self.resetPassword = QtGui.QPushButton(self.centralwidget)
            self.resetPassword.setGeometry(QtCore.QRect(340, 350+moveY, 121, 27))
            self.resetPassword.setFont(labelfont)
            self.resetPassword.setObjectName(_fromUtf8("resetPassword"))
            self.resetPassword.clicked.connect(self.generate_password)

            if self.user.type != "Admin":
                self.selectClasses = QtGui.QPushButton(self.centralwidget)
                self.selectClasses.setGeometry(QtCore.QRect(210, 350+moveY, 121, 57))
                self.selectClasses.setFont(labelfont)
                self.selectClasses.setObjectName(_fromUtf8("selectClasses"))
                self.selectClasses.clicked.connect(self.select_classes)
            
        ##############################################################


        #Menu and status bars
        EditUserWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(EditUserWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        EditUserWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(EditUserWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        EditUserWindow.setStatusBar(self.statusbar)

        self.retranslateUi(EditUserWindow)
        QtCore.QMetaObject.connectSlotsByName(EditUserWindow)
        self.statusbar = QtGui.QStatusBar(EditUserWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        EditUserWindow.setStatusBar(self.statusbar)
        self.retranslateUi(EditUserWindow)
        QtCore.QMetaObject.connectSlotsByName(EditUserWindow)


    def retranslateUi(self, EditUserWindow):
        if self.user.first == "NULL":
            self.editBtn.setText(_translate("EditUserWindow", "Create", None))
            if self.type == "Student":
                EditUserWindow.setWindowTitle(_translate("EditUserWindow", "Create Student Page", None))
                self.yearGroupLabel.setText(_translate("EditUserWindow", "YEAR GROUP", None))
                self.titleLabel.setText(_translate("EditUserWindow", "CREATE STUDENT", None))
            elif self.type == "Admin":
                self.titleLabel.setText(_translate("EditUserWindow", "CREATE ADMIN", None))
                EditUserWindow.setWindowTitle(_translate("EditUserWindow", "Create Admin Page", None))
            else:
                self.titleLabel.setText(_translate("EditUserWindow", "CREATE TEACHER", None))
                EditUserWindow.setWindowTitle(_translate("EditUserWindow", "Create Teacher Page", None))

        else:
            date = QtCore.QDate(int(self.user.dobyear),int(self.user.dobmonth),int(self.user.dobday))
            self.dateEdit.setDate(date)
            self.resetPassword.setText(_translate("EditUserWindow", "Reset Password", None))  
            self.uploadPic.setText(_translate("EditUserWindow", "Upload Profile Picture", None))    
            self.editBtn.setText(_translate("EditUserWindow", "Save", None))
            self.firstEdit.setText(_translate("EditUserWindow",self.user.first,None))
            self.lastEdit.setText(_translate("EditUserWindow",self.user.last,None))
            if self.user.email != "NULL":
                self.emailEdit.setText(_translate("EditUserWindow",self.user.email,None))
            self.usernameEdit.setText(_translate("EditUserWindow",self.user.username,None))
            if self.type == "Student":
                EditUserWindow.setWindowTitle(_translate("EditUserWindow", "Edit Student Page", None))
                self.yearGroupLabel.setText(_translate("EditUserWindow", "YEAR GROUP", None))
                self.titleLabel.setText(_translate("EditUserWindow", "EDIT STUDENT", None))
                if self.user.yeargroup == "13":
                    self.yearGroup.setCurrentIndex(1)

                self.selectClasses.setText(_translate("EditUserWindow", "Select\nClasses", None)) 
            elif self.type == "Admin":
                self.titleLabel.setText(_translate("EditUserWindow", "EDIT ADMIN", None))
                EditUserWindow.setWindowTitle(_translate("EditUserWindow", "Edit Admin Page", None))
            else:
                self.titleLabel.setText(_translate("EditUserWindow", "EDIT TEACHER", None))
                EditUserWindow.setWindowTitle(_translate("EditUserWindow", "Edit Teacher Page", None))
                self.selectClasses.setText(_translate("EditUserWindow", "Select\nClasses", None)) 

        
        self.dateLabel.setText(_translate("EditUserWindow", "DATE OF BIRTH", None))
        EditUserWindow.setWindowIcon(QtGui.QIcon('robertsmyth.png'))
        self.lastLabel.setText(_translate("EditUserWindow", "LAST NAME", None))
        self.usernameLabel.setText(_translate("EditUserWindow", "USERNAME", None))
        self.emailLabel.setText(_translate("EditUserWindow", "EMAIL", None))
        self.firstLabel.setText(_translate("EditUserWindow", "FIRST NAME", None))
    ##        self.menuFile.setTitle(_translate("EditUserWindow", "File", None))
    ##        self.menuSubjects.setTitle(_translate("EditUserWindow", "Subjects", None))
    ##        self.menuLessons.setTitle(_translate("EditUserWindow", "Lessons", None))
    ##        self.menuUsers.setTitle(_translate("EditUserWindow", "Users", None))
    ##        #self.actionQuit.setText(_translate("EditUserWindow", "Quit", None))

    def create_(self):
        #self.table = self.tableChoice.currentText()
        #self.username = self.usernameEdit.text()
        self.user.first = self.firstEdit.text()
        self.user.last = self.lastEdit.text()
        self.user.username = (self.user.first[0]+self.user.last).lower()
        length = len(self.user.username) 
        #TEST THIS LATER
        c.execute("SELECT username FROM users WHERE username LIKE :username ORDER BY username ASC",
                  {"username":str(self.user.username)+"%"})
        data = c.fetchall()
        usernames = []
        for item in data:
            usernames.append(item[0])
        if self.user.username in usernames:
            self.user.username += "1"
            chosen = False
            while not chosen:
                if self.user.username in usernames:
                    #print(self.username[:len(self.last)+1])
                    self.user.username = self.user.username[:length-1] + str(int(self.user.username[length-1:])+1)
                else:
                    chosen = True
        self.user.dob = str(self.dateEdit.date().toPyDate())
        self.user.dob = self.user.dob[8:]+"-"+self.user.dob[5:7]+"-"+self.user.dob[:4]
        self.user.email = self.emailEdit.text()
        self.user.password = "NULL"
        self.user.pic = "NULL"
        c.execute("INSERT INTO users VALUES (:first,:last,:username,:password, :dob,:email,:type,:pic)",
                  {"first":self.user.first,"last":self.user.last,"username":self.user.username,"password":self.user.password,"dob":self.user.dob,"email":self.user.email,"type":self.user.type,"pic":self.user.pic})
        if self.user.type == "Student":
            self.user.yeargroup = self.yearGroup.currentText()
            c.execute("INSERT INTO student VALUES (:username,:yeargroup,0,0)",{"username":self.user.username,"yeargroup":self.user.yeargroup})
        conn.commit()
        self.window.hide()
        self.newWindow = EditWindow()
        self.newPage = Ui_EditUserWindow()
        self.newPage.setupUi(self.newWindow,self.type,self.user)
        self.newWindow.show()
        self.saved_window()



    def save_(self):
        self.first = self.firstEdit.text()
        self.last = self.lastEdit.text()
        self.dob = str(self.dateEdit.date().toPyDate())
        self.dob = self.dob[8:]+"-"+self.dob[5:7]+"-"+self.dob[:4]
        self.email = self.emailEdit.text()
        try:
            copyfile(self.picture,path + self.user.pic)
        except:
            pass
        #c.execute("UPDATE users SET pic = :pictureLocation WHERE username = :username",{"pictureLocation":self.pictureLocation,"username":self.user.username})
        c.execute("UPDATE users SET first = :first, last = :last,dob = :dob, email = :email, pic = :pic WHERE username = :username",
                  {"first":self.first,"last":self.last,"dob":self.dob,"email":self.email,"pic": self.user.pic,"username":self.user.username})
        if self.user.type == "Student":
            self.user.yeargroup = self.yearGroup.currentText()
            c.execute("UPDATE student SET yeargroup = :yeargroup WHERE username = :username",{"yeargroup":self.year,"username":self.user.username})
        conn.commit()
        self.saved_window()


    def upload_picture(self):
        self.picture = QtGui.QFileDialog.getOpenFileName(None,"Select Profile Picture","","Images (*png)")
        self.user.pic = "\\userphotos\\"+self.user.username + ".png"
        try:
            self.profilePic.setPixmap(QtGui.QPixmap(_fromUtf8(path + self.user.pic)))
        except FileNotFoundError:
            QtGui.QMessageBox.question(self.window,"Error","Error: File not found",
                                       QtGui.QMessageBox.Ok)
            
        #c.execute("UPDATE users SET pic = :pictureLocation WHERE username = :username",{"pictureLocation":self.pictureLocation,"username":self.user.username})


           

    def generate_password(self):
        self.password = ""
        for i in range(9):
            self.password += random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits)
        choice = QtGui.QMessageBox.question(self.window,"Generate Password?","Are you sure you would like to create a new password?"
                                    "\nAny previous password will be lost.",QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        if choice == QtGui.QMessageBox.Yes:
            self.password_popup()

    def save_changes(self):
        choice = QtGui.QMessageBox.question(self.window,"Save Changes","Are you sure you would like save the changes?\n"
                                            "Any previous data will be lost.",QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        if choice == QtGui.QMessageBox.Yes:
            self.save_()


    def password_popup(self):
        QtGui.QMessageBox.question(self.window,"Password","The generated password is: "+ self.password +
                                    "\nMake a note of this password as you will not be able\nto access this again.",
                                   QtGui.QMessageBox.Ok)
        self.password = hashing(self.password)
        c.execute("UPDATE users SET password = :password WHERE username = :username",{"password":self.password,"username":self.user.username})
        conn.commit()

    def saved_window(self):
        QtGui.QMessageBox.question(self.window,"Saved","Save Successful",
                                   QtGui.QMessageBox.Ok)

    def select_classes(self):
        self.selectClass = EditWindow()
        self.selectClassUi = Ui_ClassListWindow()
        if self.type == "Student":
            self.selectClassUi.setupUi(self.selectClass,self.user.username,self.user.type,self.user.yeargroup,"List")
        else:
            self.selectClassUi.setupUi(self.selectClass,self.user.username,self.user.type,"N/A","List")
        self.selectClass.show()


class Ui_SearchUsers(object):
    def setupUi(self, SearchUsers,typeOfWindow,homework):

        self.typeOfWindow = typeOfWindow
        self.homework = homework
        self.data = []
        self.page = 1
        self.window = SearchUsers
        
        #Setting the window up
        SearchUsers.setObjectName(_fromUtf8("SearchUsers"))
        SearchUsers.resize(973, 860)
        SearchUsers.setStyleSheet(_fromUtf8("QMainWindow {\n"
"background-color: qlineargradient(spread:pad, x1:0.494364, y1:0.806, x2:0.471, y2:0.142045, stop:0 rgba(17, 255, 56, 255), stop:1 rgba(255, 255, 255, 255));}"))
        self.centralwidget = QtGui.QWidget(SearchUsers)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))

        #Title label
        self.titleLabel = QtGui.QLabel(self.centralwidget)
        self.titleLabel.setGeometry(QtCore.QRect(280, -10, 411, 91))
        self.titleLabel.setFont(titlefont)
        self.titleLabel.setTextFormat(QtCore.Qt.PlainText)
        self.titleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.titleLabel.setObjectName(_fromUtf8("titleLabel"))

        #########################################   FILTERS   #######################################################
        #Rectangle that stores all of the filter options
        self.filterRect = QtGui.QLabel(self.centralwidget)
        self.filterRect.setGeometry(QtCore.QRect(20, 65, 931, 191))
        self.filterRect.setAutoFillBackground(False)
        self.filterRect.setStyleSheet(_fromUtf8("border: 1px solid black;\n"
"background-color: rgb(255, 255, 255);"))
        self.filterRect.setText(_fromUtf8(""))
        self.filterRect.setObjectName(_fromUtf8("filterRect"))

        ## FULL NAME FILTER
        self.nameLabel = QtGui.QLabel(self.centralwidget)
        self.nameLabel.setGeometry(QtCore.QRect(20, 80, 141, 51))
        self.nameLabel.setFont(labelfont)
        self.nameLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.nameLabel.setObjectName(_fromUtf8("nameLabel"))


        self.nameEdit = QtGui.QLineEdit(self.centralwidget)
        self.nameEdit.setGeometry(QtCore.QRect(170, 90, 351, 31))
        self.nameEdit.setFont(labelfont)
        self.nameEdit.setText(_fromUtf8(""))
        self.nameEdit.setObjectName(_fromUtf8("nameEdit"))

        self.fullNameCheck = QtGui.QCheckBox(self.centralwidget)
        self.fullNameCheck.setGeometry(QtCore.QRect(170, 70, 131, 20))
        self.fullNameCheck.setObjectName(_fromUtf8("fullNameCheck"))


        ## DATE OF BIRTH FILTER
        self.dobCheck = QtGui.QCheckBox(self.centralwidget)
        self.dobCheck.setGeometry(QtCore.QRect(570, 70, 131, 20))
        self.dobCheck.setObjectName(_fromUtf8("dobCheck"))
                
        self.dateEdit = QtGui.QDateEdit(self.centralwidget)
        self.dateEdit.setGeometry(QtCore.QRect(570, 90, 121, 31))
        self.dateEdit.setObjectName(_fromUtf8("dateEdit"))
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.calendarWidget().installEventFilter(SearchUsers)
        self.dateEdit.setMaximumDate(QtCore.QDate.currentDate())



        ## USERNAME FILTER
        self.usernameLabel = QtGui.QLabel(self.centralwidget)
        self.usernameLabel.setGeometry(QtCore.QRect(20, 140, 141, 51))
        self.usernameLabel.setFont(labelfont)
        self.usernameLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.usernameLabel.setObjectName(_fromUtf8("usernameLabel"))
        
        self.usernameEdit = QtGui.QLineEdit(self.centralwidget)
        self.usernameEdit.setGeometry(QtCore.QRect(170, 150, 351, 31))
        self.usernameEdit.setFont(labelfont)
        self.usernameEdit.setText(_fromUtf8(""))
        self.usernameEdit.setObjectName(_fromUtf8("usernameEdit"))
        
        self.usernameCheck = QtGui.QCheckBox(self.centralwidget)
        self.usernameCheck.setGeometry(QtCore.QRect(170, 130, 131, 20))
        self.usernameCheck.setObjectName(_fromUtf8("usernameCheck"))


        ## TYPE OF USER FILTER
        self.typeCombo = QtGui.QComboBox(self.centralwidget)
        self.typeCombo.setGeometry(QtCore.QRect(570, 150, 121, 31))
        self.typeCombo.setObjectName(_fromUtf8("typeCombo"))
        self.typeCombo.addItem("Student")
        self.typeCombo.addItem("Teacher")
        self.typeCombo.addItem("Admin")
        
        self.typeCheck = QtGui.QCheckBox(self.centralwidget)
        self.typeCheck.setGeometry(QtCore.QRect(570, 130, 131, 20))
        self.typeCheck.setObjectName(_fromUtf8("typeCheck"))


        ## SUBJECT FILTER
        self.subjectCheck = QtGui.QCheckBox(self.centralwidget)
        self.subjectCheck.setGeometry(QtCore.QRect(740, 70, 131, 20))
        self.subjectCheck.setObjectName(_fromUtf8("subjectCheck"))
        
        self.subjectCombo = QtGui.QComboBox(self.centralwidget)
        self.subjectCombo.setGeometry(QtCore.QRect(740, 90, 121, 31))
        self.subjectCombo.setObjectName(_fromUtf8("subjectCombo"))

        if self.typeOfWindow == "Homework":
            self.subjectCombo.addItem("Not Completed")
            self.subjectCombo.addItem("Completed")
            self.subjectCombo.addItem("A*")
            self.subjectCombo.addItem("A")
            self.subjectCombo.addItem("B")
            self.subjectCombo.addItem("C")
            self.subjectCombo.addItem("D")
            self.subjectCombo.addItem("E")
            self.subjectCombo.addItem("F")
            self.subjectCombo.addItem("U")
        else:
            c.execute("SELECT fullname FROM subjects")
            data = c.fetchall()
            for i in range(len(data)):
                self.subjectCombo.addItem(data[i][0])



        ## CLASS FILTER
        self.classCheck = QtGui.QCheckBox(self.centralwidget)
        self.classCheck.setGeometry(QtCore.QRect(740, 130, 131, 20))
        self.classCheck.setObjectName(_fromUtf8("classCheck"))
        
        self.classCombo = QtGui.QComboBox(self.centralwidget)
        self.classCombo.setGeometry(QtCore.QRect(740, 150, 121, 31))
        self.classCombo.setObjectName(_fromUtf8("classCombo"))

        c.execute("SELECT id FROM classes")
        data = c.fetchall()
        for i in range(len(data)):
            self.classCombo.addItem(data[i][0])


        ## SORTING RESULTS
        self.sortCombo = QtGui.QComboBox(self.centralwidget)
        self.sortCombo.setGeometry(QtCore.QRect(170, 210, 121, 31))
        self.sortCombo.setObjectName(_fromUtf8("sortCombo"))
        self.sortCombo.addItem("Name (ASC)")
        self.sortCombo.addItem("Name (DESC)")
        self.sortCombo.addItem("Date Of Birth(ASC)")
        self.sortCombo.addItem("Date Of Birth(DESC)")
        
        self.sortLabel = QtGui.QLabel(self.centralwidget)
        self.sortLabel.setGeometry(QtCore.QRect(20, 200, 141, 51))
        self.sortLabel.setFont(labelfont)
        self.sortLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.sortLabel.setObjectName(_fromUtf8("sortLabel"))

        
        ## YEAR GROUP FILTER
        self.yearCheck = QtGui.QCheckBox(self.centralwidget)
        self.yearCheck.setGeometry(QtCore.QRect(570, 190, 131, 20))
        self.yearCheck.setObjectName(_fromUtf8("yearCheck"))
        
        self.yearCombo = QtGui.QComboBox(self.centralwidget)
        self.yearCombo.setGeometry(QtCore.QRect(570, 210, 121, 31))
        self.yearCombo.setObjectName(_fromUtf8("yearCombo"))
        self.yearCombo.addItem("12")
        self.yearCombo.addItem("13")

        ## SEARCH BUTTON
        self.searchButton = QtGui.QPushButton(self.centralwidget)
        self.searchButton.setGeometry(QtCore.QRect(310, 210, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.searchButton.setFont(font)
        self.searchButton.setObjectName(_fromUtf8("searchButton"))
        self.searchButton.clicked.connect(self.search)

        if self.typeOfWindow == "Homework":
            self.classCheck.hide()
            self.classCombo.hide()
            self.yearCombo.hide()
            self.yearCheck.hide()
            self.typeCheck.hide()
            self.typeCombo.hide()

        ##############################################################################################


        ## RESULT ONE

        #Pic
        self.profilePic = QtGui.QLabel(self.centralwidget)
        self.profilePic.setGeometry(QtCore.QRect(60, 270, 63, 63))
        self.profilePic.setText(_fromUtf8(""))
        self.profilePic.setPixmap(QtGui.QPixmap(_fromUtf8("E:/School Database PyQt/placeholder.png")))
        self.profilePic.setScaledContents(True)
        self.profilePic.setObjectName(_fromUtf8("profilePic"))

        #Name Label
        self.resultTitle = QtGui.QLabel(self.centralwidget)
        self.resultTitle.setGeometry(QtCore.QRect(140, 280, 551, 30))
        self.resultTitle.setFont(labelfont2)
        self.resultTitle.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.resultTitle.setObjectName(_fromUtf8("resultTitle"))

        #Button that links to user page
        self.resultButton = QtGui.QPushButton(self.centralwidget)
        self.resultButton.setGeometry(QtCore.QRect(20, 270, 931, 71))
        self.resultButton.setStyleSheet(_fromUtf8("QPushButton{background: transparent;}"))
        self.resultButton.setText(_fromUtf8(""))
        self.resultButton.setObjectName(_fromUtf8("resultButton"))

        #White Rectangle for the result
        self.resultRectangle = QtGui.QLabel(self.centralwidget)
        self.resultRectangle.setGeometry(QtCore.QRect(20, 267, 931, 71))
        self.resultRectangle.setAutoFillBackground(False)
        self.resultRectangle.setStyleSheet(_fromUtf8("border: 1px solid black;\n"
"background-color: rgb(255, 255, 255);"))
        self.resultRectangle.setText(_fromUtf8(""))
        self.resultRectangle.setObjectName(_fromUtf8("resultRectangle"))

        #Label describes the type of user.
        self.resultType = QtGui.QLabel(self.centralwidget)
        self.resultType.setGeometry(QtCore.QRect(140, 305, 91, 21))
        self.resultType.setFont(labelfont3)
        self.resultType.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.resultType.setObjectName(_fromUtf8("resultType"))

        self.result1 = SearchBox(self.resultRectangle,self.resultType,self.profilePic,self.resultButton,self.resultTitle,self.typeOfWindow,self.homework)
        
        ## RESULT 2

        self.resultTitle_2 = QtGui.QLabel(self.centralwidget)
        self.resultTitle_2.setGeometry(QtCore.QRect(140, 355, 551, 30))
        self.resultTitle_2.setFont(labelfont2)
        self.resultTitle_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.resultTitle_2.setObjectName(_fromUtf8("resultTitle_2"))

        self.profilePic_2 = QtGui.QLabel(self.centralwidget)
        self.profilePic_2.setGeometry(QtCore.QRect(60, 345, 63, 63))
        self.profilePic_2.setText(_fromUtf8(""))
        self.profilePic_2.setPixmap(QtGui.QPixmap(_fromUtf8("E:/School Database PyQt/placeholder.png")))
        self.profilePic_2.setScaledContents(True)
        self.profilePic_2.setObjectName(_fromUtf8("profilePic_2"))
        
        self.resultButton_2 = QtGui.QPushButton(self.centralwidget)
        self.resultButton_2.setGeometry(QtCore.QRect(20, 345, 931, 71))
        self.resultButton_2.setStyleSheet(_fromUtf8("QPushButton{background: transparent;}"))
        self.resultButton_2.setText(_fromUtf8(""))
        self.resultButton_2.setObjectName(_fromUtf8("resultButton_2"))

        self.resultType_2 = QtGui.QLabel(self.centralwidget)
        self.resultType_2.setGeometry(QtCore.QRect(140, 380, 91, 21))
        self.resultType_2.setFont(labelfont3)
        self.resultType_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.resultType_2.setObjectName(_fromUtf8("resultType_2"))
        
        self.resultRectangle_2 = QtGui.QLabel(self.centralwidget)
        self.resultRectangle_2.setGeometry(QtCore.QRect(20, 342, 931, 71))
        self.resultRectangle_2.setAutoFillBackground(False)
        self.resultRectangle_2.setStyleSheet(_fromUtf8("border: 1px solid black;\n"
"background-color: rgb(255, 255, 255);"))
        self.resultRectangle_2.setText(_fromUtf8(""))
        self.resultRectangle_2.setObjectName(_fromUtf8("resultRectangle_2"))

        self.result2 = SearchBox(self.resultRectangle_2,self.resultType_2,self.profilePic_2,self.resultButton_2,self.resultTitle_2,self.typeOfWindow,self.homework)


        ## RESULT 3
        
        self.resultTitle_3 = QtGui.QLabel(self.centralwidget)
        self.resultTitle_3.setGeometry(QtCore.QRect(140, 430, 551, 30))
        self.resultTitle_3.setFont(labelfont2)
        self.resultTitle_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.resultTitle_3.setObjectName(_fromUtf8("resultTitle_3"))
        
        self.resultType_3 = QtGui.QLabel(self.centralwidget)
        self.resultType_3.setGeometry(QtCore.QRect(140, 455, 91, 21))
        self.resultType_3.setFont(labelfont3)
        self.resultType_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.resultType_3.setObjectName(_fromUtf8("resultType_3"))

        self.resultRectangle_3 = QtGui.QLabel(self.centralwidget)
        self.resultRectangle_3.setGeometry(QtCore.QRect(20, 417, 931, 71))
        self.resultRectangle_3.setAutoFillBackground(False)
        self.resultRectangle_3.setStyleSheet(_fromUtf8("border: 1px solid black;\n"
"background-color: rgb(255, 255, 255);"))
        self.resultRectangle_3.setText(_fromUtf8(""))
        self.resultRectangle_3.setObjectName(_fromUtf8("resultRectangle_3"))
        
        self.resultButton_3 = QtGui.QPushButton(self.centralwidget)
        self.resultButton_3.setGeometry(QtCore.QRect(20, 420, 931, 71))
        self.resultButton_3.setStyleSheet(_fromUtf8("QPushButton{background: transparent;}"))
        self.resultButton_3.setText(_fromUtf8(""))
        self.resultButton_3.setObjectName(_fromUtf8("resultButton_3"))
        
        self.profilePic_3 = QtGui.QLabel(self.centralwidget)
        self.profilePic_3.setGeometry(QtCore.QRect(60, 420, 63, 63))
        self.profilePic_3.setText(_fromUtf8(""))
        self.profilePic_3.setPixmap(QtGui.QPixmap(_fromUtf8("E:/School Database PyQt/placeholder.png")))
        self.profilePic_3.setScaledContents(True)
        self.profilePic_3.setObjectName(_fromUtf8("profilePic_3"))

        self.result3 = SearchBox(self.resultRectangle_3,self.resultType_3,self.profilePic_3,self.resultButton_3,self.resultTitle_3,self.typeOfWindow,self.homework)

        ## RESULT 4
        self.resultTitle_4 = QtGui.QLabel(self.centralwidget)
        self.resultTitle_4.setGeometry(QtCore.QRect(140, 505, 551, 30))
        self.resultTitle_4.setFont(labelfont2)
        self.resultTitle_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.resultTitle_4.setObjectName(_fromUtf8("resultTitle_4"))
        
        self.resultRectangle_4 = QtGui.QLabel(self.centralwidget)
        self.resultRectangle_4.setGeometry(QtCore.QRect(20, 492, 931, 71))
        self.resultRectangle_4.setAutoFillBackground(False)
        self.resultRectangle_4.setStyleSheet(_fromUtf8("border: 1px solid black;\n"
"background-color: rgb(255, 255, 255);"))
        self.resultRectangle_4.setText(_fromUtf8(""))
        self.resultRectangle_4.setObjectName(_fromUtf8("resultRectangle_4"))
        
        self.profilePic_4 = QtGui.QLabel(self.centralwidget)
        self.profilePic_4.setGeometry(QtCore.QRect(60, 495, 63, 63))
        self.profilePic_4.setText(_fromUtf8(""))
        self.profilePic_4.setPixmap(QtGui.QPixmap(_fromUtf8("E:/School Database PyQt/placeholder.png")))
        self.profilePic_4.setScaledContents(True)
        self.profilePic_4.setObjectName(_fromUtf8("profilePic_4"))
        
        self.resultButton_4 = QtGui.QPushButton(self.centralwidget)
        self.resultButton_4.setGeometry(QtCore.QRect(20, 495, 931, 71))
        self.resultButton_4.setStyleSheet(_fromUtf8("QPushButton{background: transparent;}"))
        self.resultButton_4.setText(_fromUtf8(""))
        self.resultButton_4.setObjectName(_fromUtf8("resultButton_4"))
        
        self.resultType_4 = QtGui.QLabel(self.centralwidget)
        self.resultType_4.setGeometry(QtCore.QRect(140, 530, 91, 21))
        self.resultType_4.setFont(labelfont3)
        self.resultType_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.resultType_4.setObjectName(_fromUtf8("resultType_4"))

        self.result4 = SearchBox(self.resultRectangle_4,self.resultType_4,self.profilePic_4,self.resultButton_4,self.resultTitle_4,self.typeOfWindow,self.homework)

        ## RESULT 5
        self.resultRectangle_5 = QtGui.QLabel(self.centralwidget)
        self.resultRectangle_5.setGeometry(QtCore.QRect(20, 567, 931, 71))
        self.resultRectangle_5.setAutoFillBackground(False)
        self.resultRectangle_5.setStyleSheet(_fromUtf8("border: 1px solid black;\n"
"background-color: rgb(255, 255, 255);"))
        self.resultRectangle_5.setText(_fromUtf8(""))
        self.resultRectangle_5.setObjectName(_fromUtf8("resultRectangle_5"))
        
        self.resultTitle_5 = QtGui.QLabel(self.centralwidget)
        self.resultTitle_5.setGeometry(QtCore.QRect(140, 580, 551, 30))
        self.resultTitle_5.setFont(labelfont2)
        self.resultTitle_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.resultTitle_5.setObjectName(_fromUtf8("resultTitle_5"))
        
        self.profilePic_5 = QtGui.QLabel(self.centralwidget)
        self.profilePic_5.setGeometry(QtCore.QRect(60, 570, 63, 63))
        self.profilePic_5.setText(_fromUtf8(""))
        self.profilePic_5.setPixmap(QtGui.QPixmap(_fromUtf8("E:/School Database PyQt/placeholder.png")))
        self.profilePic_5.setScaledContents(True)
        self.profilePic_5.setObjectName(_fromUtf8("profilePic_5"))
        
        self.resultType_5 = QtGui.QLabel(self.centralwidget)
        self.resultType_5.setGeometry(QtCore.QRect(140, 605, 91, 21))
        self.resultType_5.setFont(labelfont3)
        self.resultType_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.resultType_5.setObjectName(_fromUtf8("resultType_5"))
        
        self.resultButton_5 = QtGui.QPushButton(self.centralwidget)
        self.resultButton_5.setGeometry(QtCore.QRect(20, 570, 931, 71))
        self.resultButton_5.setStyleSheet(_fromUtf8("QPushButton{background: transparent;}"))
        self.resultButton_5.setText(_fromUtf8(""))
        self.resultButton_5.setObjectName(_fromUtf8("resultButton_5"))

        self.result5 = SearchBox(self.resultRectangle_5,self.resultType_5,self.profilePic_5,self.resultButton_5,self.resultTitle_5,self.typeOfWindow,self.homework)

        ## RESULT 6
        self.resultButton_6 = QtGui.QPushButton(self.centralwidget)
        self.resultButton_6.setGeometry(QtCore.QRect(20, 645, 931, 71))
        self.resultButton_6.setStyleSheet(_fromUtf8("QPushButton{background: transparent;}"))
        self.resultButton_6.setText(_fromUtf8(""))
        self.resultButton_6.setObjectName(_fromUtf8("resultButton_6"))
        
        self.resultRectangle_6 = QtGui.QLabel(self.centralwidget)
        self.resultRectangle_6.setGeometry(QtCore.QRect(20, 642, 931, 71))
        self.resultRectangle_6.setAutoFillBackground(False)
        self.resultRectangle_6.setStyleSheet(_fromUtf8("border: 1px solid black;\n"
"background-color: rgb(255, 255, 255);"))
        self.resultRectangle_6.setText(_fromUtf8(""))
        self.resultRectangle_6.setObjectName(_fromUtf8("resultRectangle_6"))
        
        self.resultTitle_6 = QtGui.QLabel(self.centralwidget)
        self.resultTitle_6.setGeometry(QtCore.QRect(140, 655, 551, 30))
        self.resultTitle_6.setFont(labelfont2)
        self.resultTitle_6.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.resultTitle_6.setObjectName(_fromUtf8("resultTitle_6"))
        
        self.profilePic_6 = QtGui.QLabel(self.centralwidget)
        self.profilePic_6.setGeometry(QtCore.QRect(60, 645, 63, 63))
        self.profilePic_6.setText(_fromUtf8(""))
        self.profilePic_6.setPixmap(QtGui.QPixmap(_fromUtf8("E:/School Database PyQt/placeholder.png")))
        self.profilePic_6.setScaledContents(True)
        self.profilePic_6.setObjectName(_fromUtf8("profilePic_6"))
        
        self.resultType_6 = QtGui.QLabel(self.centralwidget)
        self.resultType_6.setGeometry(QtCore.QRect(140, 680, 91, 21))
        self.resultType_6.setFont(labelfont3)
        self.resultType_6.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.resultType_6.setObjectName(_fromUtf8("resultType_6"))

        self.result6 = SearchBox(self.resultRectangle_6,self.resultType_6,self.profilePic_6,self.resultButton_6,self.resultTitle_6,self.typeOfWindow,self.homework)

        ## RESULT 7
        self.resultRectangle_7 = QtGui.QLabel(self.centralwidget)
        self.resultRectangle_7.setGeometry(QtCore.QRect(20, 717, 931, 71))
        self.resultRectangle_7.setAutoFillBackground(False)
        self.resultRectangle_7.setStyleSheet(_fromUtf8("border: 1px solid black;\n"
"background-color: rgb(255, 255, 255);"))
        self.resultRectangle_7.setText(_fromUtf8(""))
        self.resultRectangle_7.setObjectName(_fromUtf8("resultRectangle_7"))

        self.resultType_7 = QtGui.QLabel(self.centralwidget)
        self.resultType_7.setGeometry(QtCore.QRect(140, 755, 91, 21))
        self.resultType_7.setFont(labelfont3)
        self.resultType_7.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.resultType_7.setObjectName(_fromUtf8("resultType_7"))
        
        self.profilePic_7 = QtGui.QLabel(self.centralwidget)
        self.profilePic_7.setGeometry(QtCore.QRect(60, 720, 63, 63))
        self.profilePic_7.setText(_fromUtf8(""))
        self.profilePic_7.setPixmap(QtGui.QPixmap(_fromUtf8("E:/School Database PyQt/placeholder.png")))
        self.profilePic_7.setScaledContents(True)
        self.profilePic_7.setObjectName(_fromUtf8("profilePic_7"))
        
        self.resultButton_7 = QtGui.QPushButton(self.centralwidget)
        self.resultButton_7.setGeometry(QtCore.QRect(20, 720, 931, 71))
        self.resultButton_7.setStyleSheet(_fromUtf8("QPushButton{background: transparent;}"))
        self.resultButton_7.setText(_fromUtf8(""))
        self.resultButton_7.setObjectName(_fromUtf8("resultButton_7"))
        
        self.resultTitle_7 = QtGui.QLabel(self.centralwidget)
        self.resultTitle_7.setGeometry(QtCore.QRect(140, 730, 551, 30))
        self.resultTitle_7.setFont(labelfont2)
        self.resultTitle_7.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.resultTitle_7.setObjectName(_fromUtf8("resultTitle_7"))

        self.result7 = SearchBox(self.resultRectangle_7,self.resultType_7,self.profilePic_7,self.resultButton_7,self.resultTitle_7,self.typeOfWindow,self.homework)

        ################## BOTTOM OF PAGE INFO ####################################

        #Label includes amount of results and how many pages worth of users there are.
        self.amountLabel = QtGui.QLabel(self.centralwidget)
        self.amountLabel.setGeometry(QtCore.QRect(30, 810, 151, 21))
        self.amountLabel.setFont(labelfont3)
        self.amountLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.amountLabel.setObjectName(_fromUtf8("amountLabel"))

        #Page number
        self.pageNumber = QtGui.QLabel(self.centralwidget)
        self.pageNumber.setGeometry(QtCore.QRect(460, 810, 51, 21))
        self.pageNumber.setFont(labelfont3)
        self.pageNumber.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.pageNumber.setObjectName(_fromUtf8("pageNumber"))

        #Previous button
        self.previousButton = QtGui.QPushButton(self.centralwidget)
        self.previousButton.setGeometry(QtCore.QRect(380, 810, 81, 21))
        self.previousButton.setStyleSheet(_fromUtf8("QPushButton{background: transparent;}"))
        self.previousButton.setText(_fromUtf8(""))
        self.previousButton.setObjectName(_fromUtf8("previousButton"))
        self.previousButton.clicked.connect(self.previous_page)

        #Next button        
        self.nextButton = QtGui.QPushButton(self.centralwidget)
        self.nextButton.setGeometry(QtCore.QRect(510, 810, 81, 21))
        self.nextButton.setStyleSheet(_fromUtf8("QPushButton{background: transparent;}"))
        self.nextButton.setText(_fromUtf8(""))
        self.nextButton.setObjectName(_fromUtf8("nextButton"))
        self.nextButton.clicked.connect(self.next_page)
         

        #################################################################################################


        #Arranging objects 
        self.resultRectangle.raise_()
        self.filterRect.raise_()
        self.titleLabel.raise_()
        self.nameLabel.raise_()
        self.nameEdit.raise_()
        self.dateEdit.raise_()
        self.dobCheck.raise_()
        self.fullNameCheck.raise_()
        self.usernameLabel.raise_()
        self.usernameEdit.raise_()
        self.usernameCheck.raise_()
        self.typeCombo.raise_()
        self.typeCheck.raise_()
        self.subjectCheck.raise_()
        self.subjectCombo.raise_()
        self.classCheck.raise_()
        self.classCombo.raise_()
        self.sortCombo.raise_()
        self.sortLabel.raise_()
        self.profilePic.raise_()
        self.resultTitle.raise_()
        self.resultType.raise_()
        self.searchButton.raise_()
        self.amountLabel.raise_()
        self.pageNumber.raise_()
        self.previousButton.raise_()
        self.nextButton.raise_()
        self.yearCheck.raise_()
        self.yearCombo.raise_()
        self.resultRectangle_2.raise_()
        self.profilePic_2.raise_()
        self.resultType_2.raise_()
        self.resultTitle_2.raise_()
        self.resultRectangle_3.raise_()
        self.profilePic_3.raise_()
        self.resultType_3.raise_()
        self.resultTitle_3.raise_()
        self.resultRectangle_4.raise_()
        self.profilePic_4.raise_()
        self.resultType_4.raise_()
        self.resultTitle_4.raise_()
        self.resultRectangle_5.raise_()
        self.resultTitle_5.raise_()
        self.profilePic_5.raise_()
        self.resultType_5.raise_()
        self.resultRectangle_6.raise_()
        self.resultTitle_6.raise_()
        self.profilePic_6.raise_()
        self.resultType_6.raise_()
        self.resultButton_6.raise_()
        self.resultButton.raise_()
        self.resultButton_2.raise_()
        self.resultButton_3.raise_()
        self.resultButton_4.raise_()
        self.resultButton_5.raise_()
        self.resultRectangle_7.raise_()
        self.resultType_7.raise_()
        self.profilePic_7.raise_()
        self.resultButton_7.raise_()
        self.resultTitle_7.raise_()


        
        SearchUsers.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(SearchUsers)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 973, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        SearchUsers.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(SearchUsers)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        SearchUsers.setStatusBar(self.statusbar)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(SearchUsers)




    def retranslateUi(self):

        if len(self.data) >= 1+((self.page-1)*7):
            self.result1.retranslateUi(self.data[0+(self.page-1)*7][0],self.data[0+(self.page-1)*7][1],self.data[0+(self.page-1)*7][2],self.data[0+(self.page-1)*7][6],self.data[0+(self.page-1)*7][7])            
            self.result1.show_all()

        else:
            self.result1.hide_all()

        if len(self.data) >= 2+((self.page-1)*7):
            self.result2.retranslateUi(self.data[1+(self.page-1)*7][0],self.data[1+(self.page-1)*7][1],self.data[1+(self.page-1)*7][2],self.data[1+(self.page-1)*7][6],self.data[1+(self.page-1)*7][7])            
            self.result2.show_all()
        else:
            self.result2.hide_all()

        if len(self.data) >= 3+(self.page-1)*7:
            self.result3.retranslateUi(self.data[2+(self.page-1)*7][0],self.data[2+(self.page-1)*7][1],self.data[2+(self.page-1)*7][2],self.data[2+(self.page-1)*7][6],self.data[2+(self.page-1)*7][7])            
            self.result3.show_all()
        else:
            self.result3.hide_all()

        if len(self.data) >= 4+(self.page-1)*7:
            self.result4.retranslateUi(self.data[3+(self.page-1)*7][0],self.data[3+(self.page-1)*7][1],self.data[3+(self.page-1)*7][2],self.data[3+(self.page-1)*7][6],self.data[3+(self.page-1)*7][7])            
            self.result4.show_all()
        else:
            self.result4.hide_all()

        if len(self.data) >= 5+(self.page-1)*7:
            self.result5.retranslateUi(self.data[4+(self.page-1)*7][0],self.data[4+(self.page-1)*7][1],self.data[4+(self.page-1)*7][2],self.data[4+(self.page-1)*7][6],self.data[4+(self.page-1)*7][7])            
            self.result5.show_all()
        else:
            self.result5.hide_all()

        if len(self.data) >= 6+(self.page-1)*7:
            self.result6.retranslateUi(self.data[5+(self.page-1)*7][0],self.data[5+(self.page-1)*7][1],self.data[5+(self.page-1)*7][2],self.data[5+(self.page-1)*7][6],self.data[5+(self.page-1)*7][7])            
            self.result6.show_all()
        else:
            self.result6.hide_all()

        if len(self.data) >= 7+(self.page-1)*7:
            self.result7.retranslateUi(self.data[6+(self.page-1)*7][0],self.data[6+(self.page-1)*7][1],self.data[6+(self.page-1)*7][2],self.data[6+(self.page-1)*7][6],self.data[6+(self.page-1)*7][7])            
            self.result7.show_all()
        else:
            self.result7.hide_all()




                    
        self.window.setWindowTitle(_translate("SearchUsers", "Search User Window", None))
        self.titleLabel.setText(_translate("SearchUsers", "SEARCH USERS", None))
        self.nameLabel.setText(_translate("SearchUsers", "FULL NAME", None))
        self.dobCheck.setText(_translate("SearchUsers", "Filter by date of birth?", None))
        self.fullNameCheck.setText(_translate("SearchUsers", "Filter by full name?", None))
        self.usernameLabel.setText(_translate("SearchUsers", "USERNAME", None))
        self.usernameCheck.setText(_translate("SearchUsers", "Filter by username?", None))
        self.typeCheck.setText(_translate("SearchUsers", "Filter by type of user?", None))
        if self.typeOfWindow == "Homework":
            self.subjectCheck.setText(_translate("SearchUsers", "Filter by grade?", None))
        else:
            self.subjectCheck.setText(_translate("SearchUsers", "Filter by subject?", None))
        self.classCheck.setText(_translate("SearchUsers", "Filter by class?", None))
        self.sortLabel.setText(_translate("SearchUsers", "Sort By:", None))
        self.searchButton.setText(_translate("SearchUsers", "SEARCH", None))
        self.amountLabel.setText(_translate("SearchUsers", str(len(self.data)) + " Results (" + str((len(self.data))//7+1 )+ " Pages)", None))
        self.pageNumber.setText(_translate("SearchUsers", str(self.page), None))
        self.previousButton.setText(_translate("SearchUsers", "Previous", None))
        self.window.setWindowIcon(QtGui.QIcon('robertsmyth.png'))
        if self.page == 1:
            self.previousButton.setEnabled(False)
        else:
            self.previousButton.setEnabled(True)
        self.nextButton.setText(_translate("SearchUsers", "Next", None))
        
        if self.page < (len(self.data)+1)//7+1:
            self.nextButton.setEnabled(True)
        else:
            self.nextButton.setEnabled(False)
        self.yearCheck.setText(_translate("SearchUsers", "Filter by year group?", None))

    def next_page(self):
        self.page += 1
        self.retranslateUi()

    def previous_page(self):
        self.page -= 1
        self.retranslateUi() 

    def search(self):

        if self.typeOfWindow == "Search":
            c.execute("SELECT * FROM USERS WHERE TYPE = 'Admin' OR TYPE = 'Teacher'")
            data1 = c.fetchall()
            c.execute("SELECT * FROM USERS,STUDENT WHERE USERS.USERNAME = STUDENT.USERNAME")
            data2 = c.fetchall()
            
            self.data = []
            for i in range(len(data1)):
                #Converting the tuples to a list
                self.data.append(list(data1[i]))

            for i in range(len(data2)):
                #Converting the tuples to a list
                self.data.append(list(data2[i]))


        elif self.typeOfWindow == "Homework":
            c.execute("SELECT * FROM USERS,"+self.homework.classId + " WHERE USERS.USERNAME = "+self.homework.classId+".Student")
            data = c.fetchall()
            self.data = []
            for i in range(len(data)):
                self.data.append(list(data[i]))


    

        #Filter by full name
        if self.fullNameCheck.isChecked():
            search = self.nameEdit.text()
            filtered = []
            for i in range(len(self.data)):
                if SequenceMatcher(None, self.data[i][0] + " " + self.data[i][1],search).ratio() > 0.75 or search.lower() in self.data[i][0].lower() + " " + self.data[i][1].lower():
                    filtered.append(self.data[i])
            self.data = filtered


        #Filter by username
        if self.usernameCheck.isChecked():
            search = self.usernameEdit.text()
            filtered = []
            for i in range(len(self.data)):
                if SequenceMatcher(None, self.data[i][2],search).ratio() > 0.75 or search.lower() in self.data[i][2].lower():
                    filtered.append(self.data[i])
            self.data = filtered

        #Filter by date of birth
        if self.dobCheck.isChecked():
            filtered = []
            dob = str(self.dateEdit.date().toPyDate())
            for i in range(len(self.data)):
                if self.data[i][4] == dob:
                    filtered.append(self.data[i])
            self.data = filtered

        if self.typeCheck.isChecked():
            filtered = []
            typeOfUser = self.typeCombo.currentText()
            for i in range(len(self.data)):
                if self.data[i][6] == typeOfUser:
                    filtered.append(self.data[i])
            self.data = filtered

        if self.yearCheck.isChecked():
            filtered = []
            yearGroup = self.yearCombo.currentText()
            if self.typeCheck.isChecked():
                if typeOfUser != "Student":
                    QtGui.QMessageBox.question(self.window,"Error has occurred","Search Unsuccessful: " + typeOfUser + "does not have attribute 'Year Group'",
                        QtGui.QMessageBox.Ok)
                    return

            for i in range(len(self.data)):
                if self.data[i][6] == "Student":
                    if self.data[i][9] == int(yearGroup):
                        filtered.append(self.data[i])
            self.data = filtered

        if self.subjectCheck.isChecked():
            filtered = []
            if self.typeOfWindow == "Search":
                if self.typeCheck.isChecked():
                    if typeOfUser == "Admin":
                        QtGui.QMessageBox.question(self.window,"Error has occurred","Search Unsuccessful: " + typeOfUser + "does not have attribute 'Subject'",
                            QtGui.QMessageBox.Ok)
                        return

                c.execute("SELECT id,teacher FROM classes WHERE subject = :subject",{"subject":self.subjectCombo.currentText()})
                classes = c.fetchall()
                users = []
                for i in range(len(classes)):
                    c.execute("SELECT student FROM "+classes[i][0])
                    temp = c.fetchall()
                    students = []
                    if temp != None:
                        for i in range(len(temp)):
                            students.append(temp[i][0])
                    users.extend(students)
                for i in range(len(self.data)):
                    if self.data[i][2] in users:
                        filtered.append(self.data[i][2])
                teachers = []
                for i in range(len(classes)):
                    teachers.append(classes[i][2])
                for i in range(len(self.data)):
                    if self.data[i][2] in teachers:
                        filtered.append(self.data)
            else:
                grade = self.subjectCombo.currentText()

                if grade == "Not Completed":
                    #c.execute("SELECT Student FROM "+self.homework.classId+" WHERE :homeworkId is Null",
                              #{"homeworkId":self.homework.homeworkId})
                    c.execute("SELECT Student,"+ self.homework.homeworkId+" FROM "+self.homework.classId)
                    data = c.fetchall()
                    notcompleted = []
                    for i in range(len(data)):
                        if data[i][1] == None:
                            notcompleted.append(data[i][0])
                    for i in range(len(self.data)):
                        if self.data[i][2] in notcompleted:
                            filtered.append(self.data[i])
                else:
                    c.execute("SELECT Student FROM "+self.homework.classId+" WHERE :homeworkId = :grade",
                          {"homeworkId":self.homework.homeworkId,"grade":grade})
                data = c.fetchall()
                students = []
                for i in range(len(data)):
                    students.append(data[i][0])
                for i in range(len(self.data)):
                    if self.data[i][2] in students:
                        filtered.append(self.data[i])

            self.data = filtered               
                    

        if self.classCheck.isChecked():
            filtered = []
            if self.typeCheck.isChecked():
                if typeOfUser == "Admin":
                    QtGui.QMessageBox.question(self.window,"Error has occurred","Search Unsuccessful: " + typeOfUser + "does not have attribute 'Class'",
                        QtGui.QMessageBox.Ok)
                    return
            c.execute("SELECT student FROM "+classes[i][0])
            temp = c.fetchall()
            students = []
            if temp != None:
                for i in range(len(temp)):
                    students.append(temp[i][0])
                for i in range(len(self.data)):
                    if self.data[i][2] in students:
                        filtered.append(self.data)
            c.execute("SELECT teacher FROM classes WHERE id = :id",{"id":self.classCombo.currentText()})
            data = c.fetchall()
            for i in range(len(self.data)):
                if self.data[i][2] == data[0][0]:
                    filtered.append(self.data[i])

            self.data = filtered

        if "Name" in self.sortCombo.currentText():
            self.data = sorted(self.data, key=lambda x : x[0])
            if "DESC" in self.sortCombo.currentText():
                self.data.reverse()
        elif self.sortCombo.currentText() == "Date Of Birth":
            self.data = sorted(self.data, key=lambda x : x[4])
            if "DESC" in self.sortCombo.currentText():
                self.data = self.data.reverse()

        self.retranslateUi()

class SearchBox():
    
    def __init__(self,rectangle,resultType,pic,button,name,typeOfSearch,homework):
        self.rectangle = rectangle
        self.type = resultType
        self.pic = pic
        self.button = button
        self.name = name
        self.typeOfSearch = typeOfSearch
        self.homework = homework

        self.button.clicked.connect(self.open_window)

        

    def retranslateUi(self,firstName,lastName,username,resultType,pic):
        self.username = username
        self.first = firstName
        self.last = lastName
        self.type.setText(_translate("SearchUsers", resultType, None))
        self.name.setText(_translate("SearchUsers", firstName + " " + lastName + "(" + username
                                              + ")", None))
        if os.path.isfile(path + pic):
            self.pic.setPixmap(QtGui.QPixmap(_fromUtf8(path + pic)))


    def hide_all(self):
        self.rectangle.hide()
        self.type.hide()
        self.pic.hide()
        self.button.hide()
        self.name.hide()

    def show_all(self):
        self.rectangle.show()
        self.type.show()
        self.pic.show()
        self.button.show()
        self.name.show()

    def open_window(self):

        if self.typeOfSearch == "Homework":
            self.edit_grade()
            return
        
        c.execute("SELECT * FROM users WHERE username=:username ORDER BY username ASC",
                  {"username":self.username})
        
        data = c.fetchone()

        if data[6] == "Student":
            c.execute("SELECT yeargroup FROM student WHERE username=:username",{"username":self.username})
            yeargroup = c.fetchone()
            
            self.user = Student(data[0],data[1],data[2],data[3],data[4],data[5],data[6],yeargroup[0],data[7])
            self.edit_student()
        else:   
            self.user = User(data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7])
            if self.user.type == "Admin":                   
                self.edit_admin()
            if self.user.type == "Teacher":                   
                self.edit_teacher()

    def edit_grade(self):
        self.editGradePage = EditWindow()
        self.editGradeUi = Ui_GradeWindow()
        self.editGradeUi.setupUi(self.editGradePage,self.homework,self.username,self.first,self.last)
        self.editGradePage.show()

                                    
    def edit_admin(self):
        self.createAdminPage = EditWindow()
        self.createAdminUi = Ui_EditUserWindow()
        self.createAdminUi.setupUi(self.createAdminPage,"Admin",self.user)
        self.createAdminPage.show()

    def edit_teacher(self):
        self.createTeacherPage = EditWindow()
        self.createTeacherUi = Ui_EditUserWindow()
        self.createTeacherUi.setupUi(self.createTeacherPage,"Teacher",self.user)
        self.createTeacherPage.show()

    def edit_student(self):
        self.createStudentPage = EditWindow()
        self.createStudentUi = Ui_EditUserWindow()
        self.createStudentUi.setupUi(self.createStudentPage,"Student",self.user)
        self.createStudentPage.show()

    def open_grade_window(self):
        pass


class Ui_ClassListWindow(object):
    def setupUi(self, ClassListWindow,username,typeOfUser,yearGroup,typeOfSearch):

        #Year Group can be left as NULL for instances not needed.
        #and TypeOfUser = Search to show classes window

        self.data = []
        self.page = 1
        self.username = username
        self.type = typeOfUser
        self.yearGroup = yearGroup
        self.typeOfUser = typeOfUser
        self.typeOfSearch = typeOfSearch
        self.window = ClassListWindow
        self.window.setStyleSheet(css)
        
        #Creating main window
        ClassListWindow.setObjectName(_fromUtf8("ClassListWindow"))
        ClassListWindow.resize(642, 571)
        self.centralwidget = QtGui.QWidget(ClassListWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))

        #Title Label
        self.titleLabel = QtGui.QLabel(self.centralwidget)
        self.titleLabel.setFont(titlefont)
        self.titleLabel.setTextFormat(QtCore.Qt.PlainText)
        self.titleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.titleLabel.setObjectName(_fromUtf8("titleLabel"))

        if self.typeOfUser == "Student":
            c.execute("SELECT classid FROM studentclass WHERE username = :username",{"username":self.username})
            self.allClasses = list(c.fetchall())
        else:
            c.execute("SELECT id FROM classes WHERE teacher = :username",{"username":self.username})
            self.allClasses = list(c.fetchall())

        if self.typeOfSearch == "Search":
            self.titleLabel.setGeometry(QtCore.QRect(0, 0, 641, 91))
            
            self.subjectLabel = QtGui.QLabel(self.centralwidget)
            self.subjectLabel.setFont(labelfont)
            self.subjectLabel.setTextFormat(QtCore.Qt.PlainText)
            self.subjectLabel.setGeometry(QtCore.QRect(20,90,141,51))
            self.subjectLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
            self.subjectLabel.setObjectName(_fromUtf8("subjectLabel"))

            self.subjectCombo = QtGui.QComboBox(self.centralwidget)
            self.subjectCombo.setGeometry(QtCore.QRect(170, 100, 421, 31))
            self.subjectCombo.setObjectName(_fromUtf8("subjectCombo"))


            c.execute("SELECT fullname FROM subjects ORDER BY fullname ASC")
            data = c.fetchall()
            for i in range(len(data)):
                self.subjectCombo.addItem(data[i][0])
            self.subject = self.subjectCombo.currentText()
            self.subjectCombo.activated[str].connect(self.show_classes)
            
        else:
            self.titleLabel.setGeometry(QtCore.QRect(140, 40, 411, 91))
                    #Profile Pic
            self.profilePic = QtGui.QLabel(self.centralwidget)
            self.profilePic.setGeometry(QtCore.QRect(30, 20, 126, 126))
            self.profilePic.setText(_fromUtf8(""))
            self.profilePic.setPixmap(QtGui.QPixmap(_fromUtf8("placeholder.png")))
            self.profilePic.setScaledContents(True)
            self.profilePic.setObjectName(_fromUtf8("profilePic"))

        self.refresh = QtGui.QPushButton(self.centralwidget)
        self.refresh.setGeometry(QtCore.QRect(561, 0, 81,31))
        self.refresh.setObjectName(_fromUtf8("refresh"))
        self.refresh.clicked.connect(self.refresh_page)

        ## Class 1

        #Class Button
        self.class_1 = QtGui.QPushButton(self.centralwidget)
        self.class_1.setGeometry(QtCore.QRect(90, 150, 411, 31))
        self.class_1.setObjectName(_fromUtf8("class_1"))

        #Remove Button
        self.remove_1 = QtGui.QPushButton(self.centralwidget)
        self.remove_1.setGeometry(QtCore.QRect(510, 150, 81, 31))
        self.remove_1.setObjectName(_fromUtf8("remove_1"))

        self.class1 = UsersClass(self.class_1,self.remove_1,self.typeOfSearch,self.allClasses,self.typeOfUser,self.username,self.window)


        ## Class 2
        
        self.remove_2 = QtGui.QPushButton(self.centralwidget)
        self.remove_2.setGeometry(QtCore.QRect(510, 190, 81, 31))
        self.remove_2.setObjectName(_fromUtf8("remove_2"))
        
        self.class_2 = QtGui.QPushButton(self.centralwidget)
        self.class_2.setGeometry(QtCore.QRect(90, 190, 411, 31))
        self.class_2.setObjectName(_fromUtf8("class_2"))

        self.class2 = UsersClass(self.class_2,self.remove_2,self.typeOfSearch,self.allClasses,self.typeOfUser,self.username,self.window)

        ## Class 3
        
        self.remove_3 = QtGui.QPushButton(self.centralwidget)
        self.remove_3.setGeometry(QtCore.QRect(510, 230, 81, 31))
        self.remove_3.setObjectName(_fromUtf8("remove_3"))
        
        self.class_3 = QtGui.QPushButton(self.centralwidget)
        self.class_3.setGeometry(QtCore.QRect(90, 230, 411, 31))
        self.class_3.setObjectName(_fromUtf8("class_3"))

        self.class3 = UsersClass(self.class_3,self.remove_3,self.typeOfSearch,self.allClasses,self.typeOfUser,self.username,self.window)

        ## Class 4

        self.remove_4 = QtGui.QPushButton(self.centralwidget)
        self.remove_4.setGeometry(QtCore.QRect(510, 270, 81, 31))
        self.remove_4.setObjectName(_fromUtf8("remove_4"))
        
        self.class_4 = QtGui.QPushButton(self.centralwidget)
        self.class_4.setGeometry(QtCore.QRect(90, 270, 411, 31))
        self.class_4.setObjectName(_fromUtf8("class_4"))

        self.class4 = UsersClass(self.class_4,self.remove_4,self.typeOfSearch,self.allClasses,self.typeOfUser,self.username,self.window)

        ##Class 5

        self.remove_5 = QtGui.QPushButton(self.centralwidget)
        self.remove_5.setGeometry(QtCore.QRect(510, 310, 81, 31))
        self.remove_5.setObjectName(_fromUtf8("remove_5"))
        
        self.class_5 = QtGui.QPushButton(self.centralwidget)
        self.class_5.setGeometry(QtCore.QRect(90, 310, 411, 31))
        self.class_5.setObjectName(_fromUtf8("class_5"))

        self.class5 = UsersClass(self.class_5,self.remove_5,self.typeOfSearch,self.allClasses,self.typeOfUser,self.username,self.window)

        ## Class 6

        self.remove_6 = QtGui.QPushButton(self.centralwidget)
        self.remove_6.setGeometry(QtCore.QRect(510, 350, 81, 31))
        self.remove_6.setObjectName(_fromUtf8("remove_6"))
        
        self.class_6 = QtGui.QPushButton(self.centralwidget)
        self.class_6.setGeometry(QtCore.QRect(90, 350, 411, 31))
        self.class_6.setObjectName(_fromUtf8("class_6"))

        self.class6 = UsersClass(self.class_6,self.remove_6,self.typeOfSearch,self.allClasses,self.typeOfUser,self.username,self.window)

        ## Class 7

        self.class_7 = QtGui.QPushButton(self.centralwidget)
        self.class_7.setGeometry(QtCore.QRect(90, 390, 411, 31))
        self.class_7.setObjectName(_fromUtf8("class_7"))
        
        self.remove_7 = QtGui.QPushButton(self.centralwidget)
        self.remove_7.setGeometry(QtCore.QRect(510, 390, 81, 31))
        self.remove_7.setObjectName(_fromUtf8("remove_7"))

        self.class7 = UsersClass(self.class_7,self.remove_7,self.typeOfSearch,self.allClasses,self.typeOfUser,self.username,self.window)

        ##Class 8

        self.remove_8 = QtGui.QPushButton(self.centralwidget)
        self.remove_8.setGeometry(QtCore.QRect(510, 430, 81, 31))
        self.remove_8.setObjectName(_fromUtf8("remove_8"))
        
        self.class_8 = QtGui.QPushButton(self.centralwidget)
        self.class_8.setGeometry(QtCore.QRect(90, 430, 411, 31))
        self.class_8.setObjectName(_fromUtf8("class_8"))

        self.class8 = UsersClass(self.class_8,self.remove_8,self.typeOfSearch,self.allClasses,self.typeOfUser,self.username,self.window)

        #Previous Button
        self.previousButton = QtGui.QPushButton(self.centralwidget)
        self.previousButton.setGeometry(QtCore.QRect(220, 510, 81, 21))
        self.previousButton.setStyleSheet(_fromUtf8("QPushButton{background: transparent;}"))
        self.previousButton.setText(_fromUtf8(""))
        self.previousButton.setObjectName(_fromUtf8("previousButton"))
        self.previousButton.clicked.connect(self.previous_page)
        
        #Next Button
        self.nextButton = QtGui.QPushButton(self.centralwidget)
        self.nextButton.setGeometry(QtCore.QRect(350, 510, 81, 21))
        self.nextButton.setStyleSheet(_fromUtf8("QPushButton{background: transparent;}"))
        self.nextButton.setText(_fromUtf8(""))
        self.nextButton.setObjectName(_fromUtf8("nextButton"))
        self.nextButton.clicked.connect(self.next_page)

        #Page Number
        self.pageNumber = QtGui.QLabel(self.centralwidget)
        self.pageNumber.setGeometry(QtCore.QRect(300, 510, 51, 21))
        self.pageNumber.setFont(labelfont3)
        self.pageNumber.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.pageNumber.setObjectName(_fromUtf8("pageNumber"))

        #Amount Of Results
        self.amountLabel = QtGui.QLabel(self.centralwidget)
        self.amountLabel.setGeometry(QtCore.QRect(20, 510, 151, 21))
        self.amountLabel.setFont(labelfont3)
        self.amountLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.amountLabel.setObjectName(_fromUtf8("amountLabel"))

        #New Class Button
        self.newClassButton = QtGui.QPushButton(self.centralwidget)
        self.newClassButton.setGeometry(QtCore.QRect(510, 510, 111, 21))
        self.newClassButton.setStyleSheet(_fromUtf8("QPushButton{background: transparent;}"))
        self.newClassButton.setText(_fromUtf8(""))
        self.newClassButton.setObjectName(_fromUtf8("newClassButton"))
        if self.typeOfSearch == "Search":
            self.newClassButton.clicked.connect(self.new_class)
        else:
            self.newClassButton.clicked.connect(self.class_button)

        
        #Menu and Status Bars
        ClassListWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(ClassListWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 642, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        ClassListWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(ClassListWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        ClassListWindow.setStatusBar(self.statusbar)

        self.retranslateUi(ClassListWindow)
        QtCore.QMetaObject.connectSlotsByName(ClassListWindow)

    def retranslateUi(self, ClassListWindow):
        self.search()
        ClassListWindow.setWindowIcon(QtGui.QIcon('robertsmyth.png'))
        if len(self.data) >= 1+((self.page-1)*8):
            self.class1.retranslateUi(self.data[0+(self.page-1)*8][3],self.data[0+(self.page-1)*8][2])
            self.class1.show_all()
        else:
            self.class1.hide_all()

        if len(self.data) >= 2+((self.page-1)*8):
            self.class2.retranslateUi(self.data[1+(self.page-1)*8][3],self.data[1+(self.page-1)*8][2])
            self.class2.show_all()
        else:
            self.class2.hide_all()

        if len(self.data) >= 3+((self.page-1)*8):
            self.class3.retranslateUi(self.data[2+(self.page-1)*8][3],self.data[2+(self.page-1)*8][2])
            self.class3.show_all()
        else:
            self.class3.hide_all()

        if len(self.data) >= 4+((self.page-1)*8):
            self.class4.retranslateUi(self.data[3+(self.page-1)*8][3],self.data[3+(self.page-1)*8][2])
            self.class4.show_all()
        else:
            self.class4.hide_all()

        if len(self.data) >= 5+((self.page-1)*8):
            self.class5.retranslateUi(self.data[4+(self.page-1)*8][3],self.data[4+(self.page-1)*8][2])
            self.class5.show_all()
        else:
            self.class5.hide_all()

        if len(self.data) >= 6+((self.page-1)*8):
            self.class6.retranslateUi(self.data[5+(self.page-1)*8][3],self.data[5+(self.page-1)*8][2])
            self.class6.show_all()
        else:
            self.class6.hide_all()

        if len(self.data) >= 7+((self.page-1)*8):
            self.class7.retranslateUi(self.data[6+(self.page-1)*8][3],self.data[6+(self.page-1)*8][2])
            self.class7.show_all()
        else:
            self.class7.hide_all()
            
        if len(self.data) >= 8+((self.page-1)*8):
            self.class8.retranslateUi(self.data[7+(self.page-1)*8][3],self.data[7+(self.page-1)*8][2])
            self.class8.show_all()
        else:
            self.class8.hide_all()
            
        ClassListWindow.setWindowTitle(_translate("ClassListWindow", "Classes Window", None))
        if self.typeOfSearch == "Search":            
            self.titleLabel.setText(_translate("ClassListWindow", "CLASSES", None))
            self.subjectLabel.setText(_translate("ClassListWindow", "Subject:", None))
        else:            
            self.titleLabel.setText(_translate("ClassListWindow", "USER CLASSES", None))
        self.previousButton.setText(_translate("ClassListWindow", "Previous", None))
        if self.page == 1:
            self.previousButton.setEnabled(False)
        else:
            self.previousButton.setEnabled(True)

        if self.page < (len(self.data)+1)//7:
            self.nextButton.setEnabled(True)
        else:
            self.nextButton.setEnabled(False)
            
        self.nextButton.setText(_translate("ClassListWindow", "Next", None))
        self.refresh.setText(_translate("ClassListWindow","Refresh",None))
        self.pageNumber.setText(_translate("ClassListWindow", str(self.page), None))
        self.amountLabel.setText(_translate("ClassListWindow", str(len(self.data))+ " Results ("+str(len(self.data)//7+1)+" Pages)", None))
        if self.typeOfSearch == "Search":
            self.newClassButton.setText(_translate("ClassListWindow", "Create New Class", None))
        else:
            self.newClassButton.setText(_translate("ClassListWindow", "Add New Class", None))


    def next_page(self):
        self.page += 1
        self.retranlsateUi()

    def previous_page(self):
        self.page += 1
        self.retranlsateUi(self.window)

    def search(self):
        self.data = []
        if self.typeOfSearch == "Search":
            c.execute("SELECT * FROM classes WHERE subject = :subject",{"subject":self.subject})
            data = list(c.fetchall())
            for i in range(len(data)):
                self.data.append(list(data[i]))
            print(self.data)
        elif self.type == "Student":
        
            c.execute("SELECT classid FROM studentclass WHERE username = :username",{"username":self.username})
            data = list(c.fetchall())
            for i in range(len(data)):
                c.execute("SELECT * FROM classes WHERE id = :id",{"id":data[i][0]})
                temp = c.fetchone()
                if temp != None:
                    self.data.append(list(temp))
    

        else:
            c.execute("SELECT * FROM classes WHERE teacher = :username",{"username":self.username})
            data = c.fetchall()





    def class_button(self):
        self.showClassesPage = EditWindow()
        self.showClassesUi = Ui_ClassListWindow()
        self.showClassesUi.setupUi(self.showClassesPage,self.username,self.typeOfUser,self.yearGroup,"Search")
        self.showClassesPage.show()        

    def show_classes(self,text):
        self.subject = text
        self.retranslateUi(self.window)
        
    def new_class(self):
        self.classPage = EditWindow()
        self.classui = Ui_CreateClassWindow()
        self.classui.setupUi(self.classPage,Class("NULL",self.username,"NULL","NULL"))
        self.classPage.show()

    def refresh_page(self):
        self.retranslateUi(self.window)

        

class UsersClass():

    def __init__(self,main,remove,typeOfWindow,allClasses,typeOfUser,username,window):
        self.typeOfUser = typeOfUser
        self.allClasses =allClasses
        self.main = main
        self.remove = remove
        self.type = typeOfWindow
        self.username = username
        self.window = window
        self.main.clicked.connect(self.open_window)
        self.remove.clicked.connect(self.remove_button)
        self.signal = ""

    def retranslateUi(self,id, subject):
        self.id = id
        self.subject = subject
        self.main.setText(_translate("ClassListWindow",id + " - " + subject,None))
        if self.type == "List":
            if self.typeOfUser == "Teacher":
                self.remove.setText(_translate("ClassListWindow","Edit",None))
                self.signal = "Edit"
            else:
                self.signal = "Remove"
                self.remove.setText(_translate("ClassListWindow","Remove",None))
             
        else:

            if self.typeOfUser == "Student":
                self.signal = "Add"
                self.remove.setText(_translate("ClassListWindow","Add",None))
                for i in range(len(self.allClasses)):
                    if self.id == self.allClasses[i]:
                        self.remove.setText(_translate("ClassListWindow","Remove",None))
                        self.signal = "Remove"
                        break
            else:
                self.signal = "Remove"
                self.remove.setText(_translate("ClassListWindow","Remove",None))


    def remove_button(self):
        if self.signal == "Edit":
            self.open_window()
        elif self.signal == "Remove":
            self.remove_student()
        elif self.signal == "Add":
            self.add_student()   
        

    def hide_all(self):
        self.main.hide()
        self.remove.hide()

    def show_all(self):
        self.main.show()
        self.remove.show()

    def open_window(self):
        self.classPage = EditWindow()
        self.classui = Ui_CreateClassWindow()
        c.execute("SELECT * FROM classes WHERE id = :id",{"id":self.id})
        data = c.fetchone()
        self.classui.setupUi(self.classPage,Class(data[0],data[1],data[2],data[3]))
        self.classPage.show()

    def add_student(self):
        choice = QtGui.QMessageBox.question(MainWindow, "Add Student?",
        "Are you sure you would add the student to this class?",QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        if choice == QtGui.QMessageBox.Yes:         
            c.execute("INSERT INTO studentclass VALUES (:username,:classid)",{"username":self.username,"classid":self.id})
            c.execute("INSERT INTO " + self.id + " (student) VALUES (:username)",{"username":self.username})
            conn.commit()
            self.allClasses.append(self.id)
            self.retranslateUi(self.id,self.subject)
            self.saved_window()
            


    def saved_window(self):
        QtGui.QMessageBox.question(self.window,"Saved","Save Successful",
                                   QtGui.QMessageBox.Ok)


    def remove_student(self):
        choice = QtGui.QMessageBox.question(MainWindow, "Remove Student?",
        "Are you sure you would remove the student from this class?",QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        if choice == QtGui.QMessageBox.Yes:          
            c.execute("DELETE FROM studentclass WHERE username = :username AND classid = :classid",{"username":self.username,"classid":self.id})
            c.execute("DELETE FROM "+self.id+ " WHERE student = :username",{"username":self.username})
            conn.commit()
            QtGui.QMessageBox.question(self.window,"Saved","Save Successful",
                                        QtGui.QMessageBox.Ok)
            try:
                self.allClasses.remove(self.id)
            except:
                pass
            self.retranslateUi(self.id,self.subject)
            if self.type == "List":
                self.hide_all()



class Ui_HomeWorkWindow(object):
    def setupUi(self, MainWindow,homework):


        self.window = MainWindow
        self.homework = homework

        #Creating Main Window
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(640, 480)
        MainWindow.setStyleSheet(css)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))

        #Save Button
        self.saveBtn = QtGui.QPushButton(self.centralwidget)
        self.saveBtn.setGeometry(QtCore.QRect(550, 390, 75, 27))
        self.saveBtn.setFont(labelfont)
        self.saveBtn.setObjectName(_fromUtf8("saveBtn"))
        if self.homework.homeworkId == "NULL":
            self.saveBtn.clicked.connect(self.create)
        else:
            self.saveBtn.clicked.connect(self.edit)
            #Grades Button
            self.gradesBtn = QtGui.QPushButton(self.centralwidget)
            self.gradesBtn.setGeometry(QtCore.QRect(550, 330, 75, 51))
            self.gradesBtn.setFont(labelfont)
            self.gradesBtn.setObjectName(_fromUtf8("gradesBtn"))
            self.gradesBtn.clicked.connect(self.grades_window)

        #Full Name Button
        self.classLabel = QtGui.QLabel(self.centralwidget)
        self.classLabel.setGeometry(QtCore.QRect(30, 80, 141, 51))
        self.classLabel.setFont(labelfont)
        self.classLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.classLabel.setObjectName(_fromUtf8("classLabel"))

        #Class Combo Box
        self.classCombo = QtGui.QComboBox(self.centralwidget)
        self.classCombo.setGeometry(QtCore.QRect(180, 90, 351, 31))
        self.classCombo.setObjectName(_fromUtf8("classCombo"))
        if currentUser.type == "Teacher":
            c.execute("SELECT id FROM classes WHERE teacher == :teacher",{"teacher":currentUser.username})
            data = list(c.fetchall())
            for classid in data:
                self.classCombo.addItem(classid[0])
        else:
            c.execute("SELECT classid FROM studentclass WHERE username == :username",{"username":currentUser.username})
            data = list(c.fetchall())
            for classid in data:
                self.classCombo.addItem(classid[0])
        if self.homework.homeworkId != "NULL":
            for i in range(len(data)):
                if self.homework.classId == data[i][0]:
                    self.classCombo.setCurrentIndex(i)

        #Edit Homework Label
        self.editHomeworkLabel = QtGui.QLabel(self.centralwidget)
        self.editHomeworkLabel.setGeometry(QtCore.QRect(65, 0, 511, 91))
        self.editHomeworkLabel.setFont(titlefont)
        self.editHomeworkLabel.setTextFormat(QtCore.Qt.PlainText)
        self.editHomeworkLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.editHomeworkLabel.setObjectName(_fromUtf8("editHomeworkLabel"))

        #Short Name Label
        self.dueLabel = QtGui.QLabel(self.centralwidget)
        self.dueLabel.setGeometry(QtCore.QRect(30, 130, 141, 51))
        self.dueLabel.setFont(labelfont)
        self.dueLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.dueLabel.setObjectName(_fromUtf8("dueLabel"))

        #Date Edit
        self.dateEdit = QtGui.QDateEdit(self.centralwidget)
        self.dateEdit.setGeometry(QtCore.QRect(180, 140, 351, 31))
        self.dateEdit.setObjectName(_fromUtf8("dateEdit"))
        self.dateEdit.setMinimumDate(QtCore.QDate.currentDate())
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.calendarWidget().installEventFilter(MainWindow)
        date = QtCore.QDate(int(self.homework.dueyear),int(self.homework.duemonth),int(self.homework.dueday))
        self.dateEdit.setDate(date)
        

        #Description Edit
        self.descriptionEdit = QtGui.QPlainTextEdit(self.centralwidget)
        self.descriptionEdit.setGeometry(QtCore.QRect(180, 240, 351, 181))
        self.descriptionEdit.setObjectName(_fromUtf8("descriptionEdit"))
        if self.homework.desc != "NULL":
            self.descriptionEdit.setPlainText(_translate("EditHomeWorkWindow",self.homework.desc,None))

        #Description Label
        self.descriptionLabel = QtGui.QLabel(self.centralwidget)
        self.descriptionLabel.setGeometry(QtCore.QRect(30, 230, 141, 51))
        self.descriptionLabel.setFont(labelfont)
        self.descriptionLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.descriptionLabel.setObjectName(_fromUtf8("descriptionLabel"))

        #Title Label
        self.titleLabel = QtGui.QLabel(self.centralwidget)
        self.titleLabel.setGeometry(QtCore.QRect(30, 180, 141, 51))
        self.titleLabel.setFont(labelfont)
        self.titleLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.titleLabel.setObjectName(_fromUtf8("titleLabel"))

        #Title Edit
        self.titleEdit = QtGui.QLineEdit(self.centralwidget)
        self.titleEdit.setGeometry(QtCore.QRect(180, 190, 351, 31))
        self.titleEdit.setObjectName(_fromUtf8("titleEdit"))
        if self.homework.title != "NULL":
            self.titleEdit.setText(_translate("EditHomeWorkWindow",self.homework.title,None))

        self.gradeTitle = QtGui.QLabel(self.centralwidget)

        if currentUser.type == "Student":
            self.gradeTitle = QtGui.QLabel(self.centralwidget)
            self.gradeTitle.setGeometry(QtCore.QRect(60, 280, 101, 41))
            self.gradeTitle.setFont(typefont)
            self.gradeTitle.setAutoFillBackground(False)
            self.gradeTitle.setStyleSheet(_fromUtf8("QLabel{border: 1px solid black;\n"
            "background-color: rgb(255, 255, 255);}\n"
            ""))
            self.gradeTitle.setAlignment(QtCore.Qt.AlignCenter)
            self.gradeTitle.setObjectName(_fromUtf8("gradeTitle"))

            self.grade = QtGui.QLabel(self.centralwidget)
            self.grade.setGeometry(QtCore.QRect(60, 320, 101, 61))
            self.grade.setFont(numberfont)
            self.grade.setAutoFillBackground(False)
            self.grade.setAlignment(QtCore.Qt.AlignCenter)
            self.grade.setObjectName(_fromUtf8("grade"))
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        if self.homework.homeworkId == "NULL":
            self.saveBtn.setText(_translate("MainWindow", "Create", None))
            MainWindow.setWindowTitle(_translate("MainWindow", "Create Homework Window", None))
            self.editHomeworkLabel.setText(_translate("MainWindow", "CREATE HOMEWORK", None))
        else:
            self.saveBtn.setText(_translate("MainWindow", "Save", None))
            MainWindow.setWindowTitle(_translate("MainWindow", "Edit Homework Window", None))
            self.editHomeworkLabel.setText(_translate("MainWindow", "EDIT HOMEWORK", None))
            self.gradesBtn.setText(_translate("MainWindow", "Update\nGrades", None))
        self.classLabel.setText(_translate("MainWindow", "CLASS:", None))
        
        
        self.dueLabel.setText(_translate("MainWindow", "DUE DATE:", None))
        self.descriptionLabel.setText(_translate("MainWindow", "DESCRIPTION:", None))
        self.titleLabel.setText(_translate("MainWindow", "TITLE:", None))
        MainWindow.setWindowIcon(QtGui.QIcon('robertsmyth.png'))

        if currentUser.type == "Student":
            self.classCombo.setEnabled(False)
            self.dateEdit.setEnabled(False)
            self.titleEdit.setEnabled(False)
            self.descriptionEdit.setEnabled(False)
            self.saveBtn.hide()
            self.gradesBtn.hide()
            self.gradeTitle.setText(_translate("MainWindow", "Homework\n Status", None))
            c.execute("SELECT "+self.homework.homeworkId+" FROM "+self.homework.classId+" WHERE Student = :username",
                      {"username":currentUser.username})
            data = c.fetchall()
            grade = data[0][0]
            print(grade)
            if grade != None and grade != "Completed":
                self.grade.setText(_translate("MainWindow", grade, None))
                if grade == "A*" or grade == "A":
                    self.grade.setStyleSheet(_fromUtf8("QLabel{border: 1px solid black;\n"
                    "background-color: rgb(0, 255, 0);}\n"
                    ""))
                if grade == "B" or grade == "C":
                    self.grade.setStyleSheet(_fromUtf8("QLabel{border: 1px solid black;\n"
                    "background-color: rgb(255, 165, 0);}\n"
                    ""))
                else:
                    self.grade.setStyleSheet(_fromUtf8("QLabel{border: 1px solid black;\n"
                    "background-color: rgb(255, 0, 0);}\n"
                    ""))
            else:
                self.grade.setText(_translate("MainWindow", "N/A", None))
                self.grade.setStyleSheet(_fromUtf8("QLabel{border: 1px solid black;\n"
                    "background-color: rgb(255, 255, 255);}\n"
                    ""))


    def create(self):
        classid = self.classCombo.currentText()
        duedate = str(self.dateEdit.date().toPyDate())
        duedate = duedate[8:]+ "-"+duedate[5:7]+"-"+duedate[:4]
        title = self.titleEdit.text()
        desc = self.descriptionEdit.toPlainText()
        homeworkId = classid + "_"
        length = len(homeworkId)-1

        c.execute("SELECT homeworkid FROM homework WHERE homeworkid LIKE :homeworkid ORDER BY homeworkid ASC",
                  {"homeworkid":homeworkId+ "%"})
        homeworkid += "1"
        data = list(c.fetchall())
        newdata = []
        for i in range(len(data)):
            newdata.append(data[i][0])
        if homeworkId in newdata:
            chosen = False
            while not chosen:
                if homeworkId in newdata:
                    homeworkId = homeworkId[:length]+str(int(homeworkId[length:])+1)
                else:
                    chosen = True
        c.execute("INSERT INTO homework VALUES (:homeworkid,:classid,:duedate,:title,:description)",
                  {"homeworkid":homeworkId,"classid":classid,"duedate":duedate,"title":title,"description":desc})
        c.execute("ALTER TABLE "+classid+" ADD "+ homeworkId+ " text;")
        conn.commit()
        self.window.hide()
        self.newWindow = EditWindow()
        self.newPage = Ui_HomeWorkWindow()
        self.newPage.setupUi(self.newWindow,Homework(homeworkId,classid,duedate,title,desc))
        self.newWindow.show()

            

    def edit(self):
        pass

    def grades_window(self):
        self.searchPage = EditWindow()
        self.SearchUi = Ui_SearchUsers()
        self.SearchUi.setupUi(self.searchPage,"Homework",self.homework)
        self.searchPage.show()


class Ui_ViewHomeworkWindow(object):
    def setupUi(self, ViewHomeworkWindow,typeOfWindow):
        self.window = ViewHomeworkWindow
        self.page = 1
        self.typeOfWindow = typeOfWindow

        
        #Setting Window Up
        ViewHomeworkWindow.setObjectName(_fromUtf8("ViewHomeworkWindow"))
        ViewHomeworkWindow.resize(640, 551)
        self.centralwidget = QtGui.QWidget(ViewHomeworkWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.window.setStyleSheet(_fromUtf8("QMainWindow {\n"
        "background-color: qlineargradient(spread:pad, x1:0.494364, y1:0.806, x2:0.471, y2:0.142045, stop:0 rgba(17, 255, 56, 255), stop:1 rgba(255, 255, 255, 255));}\n"
        "QPushButton{background: transparent;"
        "border: 1px solid black;}"))

        #Type Button
        self.typeBtn = QtGui.QPushButton(self.centralwidget)
        self.typeBtn.setGeometry(QtCore.QRect(0, 0, 75, 51))
        self.typeBtn.setFont(labelfont)
        self.typeBtn.setObjectName(_fromUtf8("typeBtn"))
        self.typeBtn.clicked.connect(self.change_type)


        #Homework Label
        self.myHomeworkLabel = QtGui.QLabel(self.centralwidget)
        self.myHomeworkLabel.setGeometry(QtCore.QRect(0, 0, 641, 91))
        self.myHomeworkLabel.setFont(titlefont)
        self.myHomeworkLabel.setTextFormat(QtCore.Qt.PlainText)
        self.myHomeworkLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.myHomeworkLabel.setObjectName(_fromUtf8("myHomeworkLabel"))

        #Class Label
        self.classLabel = QtGui.QLabel(self.centralwidget)
        self.classLabel.setGeometry(QtCore.QRect(-10, 70, 141, 51))
        self.classLabel.setFont(labelfont)
        self.classLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.classLabel.setObjectName(_fromUtf8("classLabel"))


        
        #Class Combo
        self.classCombo = QtGui.QComboBox(self.centralwidget)
        self.classCombo.setGeometry(QtCore.QRect(140, 80, 421, 31))
        self.classCombo.setObjectName(_fromUtf8("classCombo"))

        if currentUser.type == "Student":
            c.execute("SELECT classid FROM studentclass WHERE username = :username",
                      {"username":currentUser.username})
        else:
            c.execute("SELECT id FROM classes WHERE teacher = :username",
                      {"username":currentUser.username})

        self.data = list(c.fetchall())
        self.classCombo.addItem("All")
        for classid in self.data:
            self.classCombo.addItem(classid[0])

        self.classid = self.classCombo.currentText()
        self.classCombo.activated[str].connect(self.show_homework)

        ##################RESULTS##############################

        ##1st Result

        #Button
        self.topButton = QtGui.QPushButton(self.centralwidget)
        self.topButton.setGeometry(QtCore.QRect(80, 130, 481, 51))
        self.topButton.setStyleSheet(_fromUtf8("QPushButton{background: transparent;\n"
        "border: 1px solid black;}"))
        self.topButton.setText(_fromUtf8(""))
        self.topButton.setObjectName(_fromUtf8("topButton"))

        #Description
        self.topDesc = QtGui.QLabel(self.centralwidget)
        self.topDesc.setGeometry(QtCore.QRect(90, 157, 461, 21))
        self.topDesc.setFont(labelfont4)
        self.topDesc.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.topDesc.setObjectName(_fromUtf8("topDesc"))

        #Title
        self.topTitle = QtGui.QLabel(self.centralwidget)
        self.topTitle.setGeometry(QtCore.QRect(90, 137, 461, 21))
        self.topTitle.setFont(labelfont3)
        self.topTitle.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.topTitle.setObjectName(_fromUtf8("topTitle"))

        self.top1 =  WindowButtons(self.topButton,self.topTitle,self.topDesc,"Homework")

        ##2nd Result
        self.topTitle_2 = QtGui.QLabel(self.centralwidget)
        self.topTitle_2.setGeometry(QtCore.QRect(90, 187, 461, 21))
        self.topTitle_2.setFont(normalfont)
        self.topTitle_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.topTitle_2.setObjectName(_fromUtf8("topTitle_2"))

        self.topDesc_2 = QtGui.QLabel(self.centralwidget)
        self.topDesc_2.setGeometry(QtCore.QRect(90, 207, 461, 21))
        self.topDesc_2.setFont(labelfont4)
        self.topDesc_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.topDesc_2.setObjectName(_fromUtf8("topDesc_2"))

        self.topButton_2 = QtGui.QPushButton(self.centralwidget)
        self.topButton_2.setGeometry(QtCore.QRect(80, 180, 481, 51))
        self.topButton_2.setObjectName(_fromUtf8("topButton_2"))

        self.top2 = WindowButtons(self.topButton_2,self.topTitle_2,self.topDesc_2,"Homework")

        ##3rd Result
        self.topButton_3 = QtGui.QPushButton(self.centralwidget)
        self.topButton_3.setGeometry(QtCore.QRect(80, 230, 481, 51))
        self.topButton_3.setObjectName(_fromUtf8("topButton_3"))
        
        self.topDesc_3 = QtGui.QLabel(self.centralwidget)
        self.topDesc_3.setGeometry(QtCore.QRect(90, 257, 461, 21))
        self.topDesc_3.setFont(labelfont4)
        self.topDesc_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.topDesc_3.setObjectName(_fromUtf8("topDesc_3"))
        
        self.topTitle_3 = QtGui.QLabel(self.centralwidget)
        self.topTitle_3.setGeometry(QtCore.QRect(90, 237, 461, 21))
        self.topTitle_3.setFont(labelfont3)
        self.topTitle_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.topTitle_3.setObjectName(_fromUtf8("topTitle_3"))

        self.top3 = WindowButtons(self.topButton_3,self.topTitle_3,self.topDesc_3,"Homework")
    
        ##4th Result
        self.topDesc_4 = QtGui.QLabel(self.centralwidget)
        self.topDesc_4.setGeometry(QtCore.QRect(90, 307, 461, 21))
        self.topDesc_4.setFont(labelfont4)
        self.topDesc_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.topDesc_4.setObjectName(_fromUtf8("topDesc_4"))

        self.topTitle_4 = QtGui.QLabel(self.centralwidget)
        self.topTitle_4.setGeometry(QtCore.QRect(90, 287, 461, 21))
        self.topTitle_4.setFont(labelfont3)
        self.topTitle_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.topTitle_4.setObjectName(_fromUtf8("topTitle_4"))
        
        self.topButton_4 = QtGui.QPushButton(self.centralwidget)
        self.topButton_4.setGeometry(QtCore.QRect(80, 280, 481, 51))
        self.topButton_4.setObjectName(_fromUtf8("topButton_4"))

        self.top4 = WindowButtons(self.topButton_4,self.topTitle_4,self.topDesc_4,"Homework")

        ##5th Result
        self.topButton_5 = QtGui.QPushButton(self.centralwidget)
        self.topButton_5.setGeometry(QtCore.QRect(80, 330, 481, 51))
        self.topButton_5.setObjectName(_fromUtf8("topButton_5"))

        self.topTitle_5 = QtGui.QLabel(self.centralwidget)
        self.topTitle_5.setGeometry(QtCore.QRect(90, 337, 461, 21))
        self.topTitle_5.setFont(labelfont3)
        self.topTitle_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.topTitle_5.setObjectName(_fromUtf8("topTitle_5"))

        self.topDesc_5 = QtGui.QLabel(self.centralwidget)
        self.topDesc_5.setGeometry(QtCore.QRect(90, 357, 461, 21))
        self.topDesc_5.setFont(labelfont4)
        self.topDesc_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.topDesc_5.setObjectName(_fromUtf8("topDesc_5"))

        self.top5 = WindowButtons(self.topButton_5,self.topTitle_5,self.topDesc_5,"Homework")
        
        ##6th Result
        self.topDesc_6 = QtGui.QLabel(self.centralwidget)
        self.topDesc_6.setGeometry(QtCore.QRect(90, 407, 461, 21))
        self.topDesc_6.setFont(labelfont4)
        self.topDesc_6.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.topDesc_6.setObjectName(_fromUtf8("topDesc_6"))

        self.topButton_6 = QtGui.QPushButton(self.centralwidget)
        self.topButton_6.setGeometry(QtCore.QRect(80, 380, 481, 51))
        self.topButton_6.setObjectName(_fromUtf8("topButton_6"))

        self.topTitle_6 = QtGui.QLabel(self.centralwidget)
        self.topTitle_6.setGeometry(QtCore.QRect(90, 387, 461, 21))
        self.topTitle_6.setFont(labelfont3)
        self.topTitle_6.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.topTitle_6.setObjectName(_fromUtf8("topTitle_6"))
        
        self.top6 = WindowButtons(self.topButton_6,self.topTitle_6,self.topDesc_6,"Homework")
        
        ##7th Result
        self.topTitle_7 = QtGui.QLabel(self.centralwidget)
        self.topTitle_7.setGeometry(QtCore.QRect(90, 437, 461, 21))
        self.topTitle_7.setFont(labelfont3)
        self.topTitle_7.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.topTitle_7.setObjectName(_fromUtf8("topTitle_7"))
        
        self.topDesc_7 = QtGui.QLabel(self.centralwidget)
        self.topDesc_7.setGeometry(QtCore.QRect(90, 457, 461, 21))
        self.topDesc_7.setFont(labelfont4)
        self.topDesc_7.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.topDesc_7.setObjectName(_fromUtf8("topDesc_7"))
        
        self.topButton_7 = QtGui.QPushButton(self.centralwidget)
        self.topButton_7.setGeometry(QtCore.QRect(80, 430, 481, 51))
        self.topButton_7.setObjectName(_fromUtf8("topButton_7"))

        self.top7 = WindowButtons(self.topButton_7,self.topTitle_7,self.topDesc_7,"Homework")

        #######################################################################

        #New Homework Button
        if currentUser.type == "Teacher":
            self.newHomeworkButton = QtGui.QPushButton(self.centralwidget)
            self.newHomeworkButton.setGeometry(QtCore.QRect(470, 510, 151, 21))
            self.newHomeworkButton.setFont(labelfont3)
            self.newHomeworkButton.setObjectName(_fromUtf8("newHomeworkButton"))
            self.newHomeworkButton.clicked.connect(self.new_homework)
            self.newHomeworkButton.setStyleSheet(_fromUtf8("QPushButton{background: transparent;border: 0px transparent;}"))
            self.newHomeworkButton.clicked.connect(self.new_homework)


        #Previous Button
        self.previousButton = QtGui.QPushButton(self.centralwidget)
        self.previousButton.setGeometry(QtCore.QRect(220, 510, 81, 21))
        self.previousButton.setStyleSheet(_fromUtf8("QPushButton{background: transparent;border: 0px transparent;}"))
        self.previousButton.setObjectName(_fromUtf8("previousButton"))
        self.previousButton.clicked.connect(self.previous_page)
        
        #Next Button
        self.nextButton = QtGui.QPushButton(self.centralwidget)
        self.nextButton.setGeometry(QtCore.QRect(350, 510, 81, 21))
        self.nextButton.setStyleSheet(_fromUtf8("QPushButton{background: transparent;border: 0px transparent;}"))
        self.nextButton.setObjectName(_fromUtf8("nextButton"))
        self.nextButton.clicked.connect(self.next_page)

        #Page Number
        self.pageNumber = QtGui.QLabel(self.centralwidget)
        self.pageNumber.setGeometry(QtCore.QRect(300, 510, 51, 21))
        self.pageNumber.setFont(labelfont3)
        self.pageNumber.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.pageNumber.setObjectName(_fromUtf8("pageNumber"))

        #Amount Of Results
        self.amountLabel = QtGui.QLabel(self.centralwidget)
        self.amountLabel.setGeometry(QtCore.QRect(20, 510, 151, 21))
        self.amountLabel.setFont(labelfont3)
        self.amountLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.amountLabel.setObjectName(_fromUtf8("amountLabel"))

        
        self.topTitle_2.raise_()
        self.topDesc.raise_()
        self.topTitle.raise_()
        self.topDesc_3.raise_()
        self.topDesc_2.raise_()
        self.topTitle_3.raise_()
        self.myHomeworkLabel.raise_()
        self.classLabel.raise_()
        self.classCombo.raise_()
        self.topDesc_6.raise_()
        self.topTitle_5.raise_()
        self.topTitle_6.raise_()
        self.topDesc_4.raise_()
        self.topDesc_5.raise_()
        self.topTitle_4.raise_()
        self.topTitle_7.raise_()
        self.topDesc_7.raise_()
        self.amountLabel.raise_()
        self.previousButton.raise_()
        self.nextButton.raise_()
        self.pageNumber.raise_()
        self.topButton_3.raise_()
        self.topButton_2.raise_()
        self.topButton_5.raise_()
        self.topButton_7.raise_()
        self.topButton_4.raise_()
        self.topButton_6.raise_()
        self.topButton.raise_()
        ViewHomeworkWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(ViewHomeworkWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        ViewHomeworkWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(ViewHomeworkWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        ViewHomeworkWindow.setStatusBar(self.statusbar)
        self.search()
        self.retranslateUi(ViewHomeworkWindow)
        QtCore.QMetaObject.connectSlotsByName(ViewHomeworkWindow)
        

    def retranslateUi(self, ViewHomeworkWindow):

        if len(self.homeworks) >= 1+((self.page-1)*7):
            if len(self.homeworks[0+(self.page-1)*7][3]) > 45:
                   self.homeworks[0+(self.page-1)*7][3]= self.homeworks[0+(self.page-1)*7][3][:42]+"..."
            self.top1.retranslateUi(self.homeworks[0+(self.page-1)*7][3],
                                    self.homeworks[0+(self.page-1)*7][1] + " - Due "+self.homeworks[0+(self.page-1)*7][2],
                                    self.homeworks[0+(self.page-1)*7][0])
            self.top1.show_all() 
        else:
            self.top1.hide_all()


        if len(self.homeworks) >= 2+((self.page-1)*7):
            if len(self.homeworks[1+(self.page-1)*7][3]) > 45:
                   self.homeworks[1+(self.page-1)*7][3]= self.homeworks[1+(self.page-1)*7][3][:42]+"..."
            self.top2.retranslateUi(self.homeworks[1+(self.page-1)*7][3],
                                    self.homeworks[1+(self.page-1)*7][1] + " - Due "+self.homeworks[1+(self.page-1)*7][2],
                                    self.homeworks[1+(self.page-1)*7][0])
            self.top2.show_all() 
        else:
            self.top2.hide_all()

        if len(self.homeworks) >= 3+((self.page-1)*7):
            if len(self.homeworks[2+(self.page-1)*7][3]) > 45:
                   self.homeworks[2+(self.page-1)*7][3]= self.homeworks[2+(self.page-1)*7][3][:42]+"..."
            self.top3.retranslateUi(self.homeworks[2+(self.page-1)*7][3],
                                    self.homeworks[2+(self.page-1)*7][1] + " - Due "+self.homeworks[2+(self.page-1)*7][2],
                                    self.homeworks[2+(self.page-1)*7][0])
            self.top3.show_all() 
        else:
            self.top3.hide_all()


        if len(self.homeworks) >= 4+((self.page-1)*7):
            if len(self.homeworks[3+(self.page-1)*7][3]) > 45:
                   self.homeworks[3+(self.page-1)*7][3]= self.homeworks[3+(self.page-1)*7][3][:42]+"..."
            self.top4.retranslateUi(self.homeworks[3+(self.page-1)*7][3],
                                    self.homeworks[3+(self.page-1)*7][1] + " - Due "+self.homeworks[3+(self.page-1)*7][2],
                                    self.homeworks[3+(self.page-1)*7][0])
            self.top4.show_all() 
        else:
            self.top4.hide_all()


        if len(self.homeworks) >= 5+((self.page-1)*7):
            if len(self.homeworks[4+(self.page-1)*7][3]) > 45:
                   self.homeworks[4+(self.page-1)*7][3]= self.homeworks[4+(self.page-1)*7][3][:42]+"..."
            self.top5.retranslateUi(self.homeworks[4+(self.page-1)*7][3],
                                    self.homeworks[4+(self.page-1)*7][1] + " - Due "+self.homeworks[4+(self.page-1)*7][2],
                                    self.homeworks[4+(self.page-1)*7][0])
            self.top5.show_all() 
        else:
            self.top5.hide_all()


        if len(self.homeworks) >= 6+((self.page-1)*7):
            if len(self.homeworks[5+(self.page-1)*7][3]) > 45:
                   self.homeworks[5+(self.page-1)*7][3]= self.homeworks[5+(self.page-1)*7][3][:42]+"..."
            self.top6.retranslateUi(self.homeworks[5+(self.page-1)*7][3],
                                    self.homeworks[5+(self.page-1)*7][1] + " - Due "+self.homeworks[5+(self.page-1)*7][2],
                                    self.homeworks[5+(self.page-1)*7][0])
            self.top6.show_all() 
        else:
            self.top6.hide_all()


        if len(self.homeworks) >= 7+((self.page-1)*7):
            if len(self.homeworks[6+(self.page-1)*7][3]) > 45:
                   self.homeworks[6+(self.page-1)*7][3]= self.homeworks[6+(self.page-1)*7][3][:42]+"..."
            self.top7.retranslateUi(self.homeworks[6+(self.page-1)*7][3],
                                    self.homeworks[6+(self.page-1)*7][1] + " - Due "+self.homeworks[6+(self.page-1)*7][2],
                                    self.homeworks[6+(self.page-1)*7][0])
            self.top7.show_all() 
        else:
            self.top7.hide_all()        

        if self.page == 1:
            self.previousButton.setEnabled(False)
        else:
            self.previousButton.setEnabled(True)

        if self.page < (len(self.homeworks)//7+1):
            self.nextButton.setEnabled(True)
        else:
            self.nextButton.setEnabled(False)
                
        ViewHomeworkWindow.setWindowTitle(_translate("ViewHomeworkWindow", "View Homework", None))
        ViewHomeworkWindow.setWindowIcon(QtGui.QIcon('robertsmyth.png'))
        self.myHomeworkLabel.setText(_translate("ViewHomeworkWindow", "MY HOMEWORK", None))
        self.classLabel.setText(_translate("ViewHomeworkWindow", "CLASS:", None))
        if currentUser.type == "Teacher":
            self.newHomeworkButton.setText(_translate("ViewHomeworkWindow", "Add New Homework", None))
        self.amountLabel.setText(_translate("ViewHomeworkWindow",str(len(self.homeworks))+" Results ("+str((len(self.homeworks))//7+1) +" Pages)", None))
        self.previousButton.setText(_translate("ViewHomeworkWindow", "Previous", None))
        self.nextButton.setText(_translate("ViewHomeworkWindow", "Next", None))
        self.pageNumber.setText(_translate("ViewHomeworkWindow", str(self.page), None))

    def change_type(self):
        if self.typeOfWindow == "Future":
            self.typeOfWindow = "Past"
        else:
            self.typeOfWindow = "Future"
        self.search()


    def previous_page(self):
        self.page -= 1
        self.retranslateUi(self.window)
    def next_page(self):
        self.page += 1
        self.retranslateUi(self.window)
    def new_homework(self):
        self.homeworkPage = EditWindow()
        self.homeworkui = Ui_HomeWorkWindow()
        self.homeworkui.setupUi(self.homeworkPage,Homework("NULL","NULL","01/01/2001","NULL","NULL"))
        self.homeworkPage.show()

    def show_homework(self,text):
        self.classid = text
        self.search()
        self.retranslateUi(self.window)

    def search(self):
        if self.classid != "All":
            c.execute("SELECT * FROM homework WHERE classid = :classid",{"classid":self.classid})
            data = c.fetchall()
            new = []
            
            if self.typeOfWindow == "Future":
                for homework in data:
                    pass

            else:
                c.execute("SELECT * FROM homework WHERE classid = :classid AND duedate > :date",{"classid":self.classid,"date":date})
            temp = c.fetchall()
            if temp != None:
                data = list(temp)
            else:
                data = []
            
        else:
            data = []
            for classid in self.data:
                if self.typeOfWindow == "Future":
                    c.execute("SELECT * FROM homework WHERE classid = :classid",{"classid":classid[0]})
                    print(data)
                else:
                    c.execute("SELECT * FROM homework WHERE classid = :classid",{"classid":classid[0]})
                temp = c.fetchall()
                if temp != None:
                    data.extend(list(temp))

        data.sort(key=lambda x: time.mktime(time.strptime(x[2],"%d-%m-%Y")))
        self.homeworks = data

def is_future(date):
    today = datetime.datetime.today().strftime('%d-%m-%Y')
    temp = datetime.strptime(date, '%d-%m-%Y')
    if today <= temp:
        return True
    else:
        return False

def find_past(array):
    today = datetime.datetime.today().strftime('%d-%m-%Y')
    temp = datetime.strptime(date, '%d-%m-%Y')
    if today > temp:
        return True
    else:
        return False
    
    

class Ui_GradeWindow(object):
    def setupUi(self, GradeWindow,homework,username,first,last):
        self.window = GradeWindow
        self.username = username
        self.homework = homework
        self.first = first
        self.last = last
        c.execute("SELECT "+self.homework.homeworkId+" FROM "+self.homework.classId+" WHERE Student = '"+self.username+"'")
        data = c.fetchall()
        grade = data[0][0]
        if grade == None:
            grade = "Not Completed"
            
        
        #Setting window up
        GradeWindow.setObjectName(_fromUtf8("GradeWindow"))
        GradeWindow.resize(304, 228)
        self.centralwidget = QtGui.QWidget(GradeWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        GradeWindow.setStyleSheet(css)

        #Label of users name
        self.nameLabel = QtGui.QLabel(self.centralwidget)
        self.nameLabel.setGeometry(QtCore.QRect(0, 10, 301, 51))
        self.nameLabel.setFont(smalltitlefont)
        self.nameLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.nameLabel.setObjectName(_fromUtf8("nameLabel"))

        #Grade combo
        self.gradeCombo = QtGui.QComboBox(self.centralwidget)
        self.gradeCombo.setGeometry(QtCore.QRect(130, 80, 101, 31))
        self.gradeCombo.setObjectName(_fromUtf8("gradeCombo"))
        self.gradeCombo.addItem("Not Completed")
        self.gradeCombo.addItem("Completed")
        self.gradeCombo.addItem("A*")
        self.gradeCombo.addItem("A")
        self.gradeCombo.addItem("B")
        self.gradeCombo.addItem("C")
        self.gradeCombo.addItem("D")
        self.gradeCombo.addItem("E")
        self.gradeCombo.addItem("F")
        self.gradeCombo.addItem("U")
        index = self.gradeCombo.findText(grade, QtCore.Qt.MatchFixedString)
        if index >= 0:
            self.gradeCombo.setCurrentIndex(index)



        #Grade Label
        self.gradeLabel = QtGui.QLabel(self.centralwidget)
        self.gradeLabel.setGeometry(QtCore.QRect(-20, 70, 141, 51))
        self.gradeLabel.setFont(labelfont)
        self.gradeLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.gradeLabel.setObjectName(_fromUtf8("gradeLabel"))

        #Save Button
        self.saveBtn = QtGui.QPushButton(self.centralwidget)
        self.saveBtn.setGeometry(QtCore.QRect(210, 140, 75, 27))
        self.saveBtn.setFont(labelfont)
        self.saveBtn.setObjectName(_fromUtf8("saveBtn"))
        self.saveBtn.clicked.connect(self.save)
        
        
        GradeWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(GradeWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 304, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        GradeWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(GradeWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        GradeWindow.setStatusBar(self.statusbar)

        self.retranslateUi(GradeWindow)
        QtCore.QMetaObject.connectSlotsByName(GradeWindow)

    def retranslateUi(self, GradeWindow):
        GradeWindow.setWindowTitle(_translate("GradeWindow", "Grade Window", None))
        self.nameLabel.setText(_translate("GradeWindow", self.first + " " + self.last, None))
        self.gradeLabel.setText(_translate("GradeWindow", "GRADE:", None))
        self.saveBtn.setText(_translate("GradeWindow", "Update", None))

    def save(self):
        grade = self.gradeCombo.currentText()
        if grade != "Not Completed":
            c.execute("UPDATE "+self.homework.classId+" SET "+self.homework.homeworkId+" = :grade WHERE student = :student",
                  {"grade":grade,"student":self.username})
            conn.commit()
            QtGui.QMessageBox.question(self.window,"Saved","Save Successful",
                    QtGui.QMessageBox.Ok)

#Use this as MainWindow for the close event popup window
class EditWindow(QtGui.QMainWindow):
    def closeEvent(self,event):
        result = QtGui.QMessageBox.question(self,
                      "Close The Window",
                      "Are you sure you want to exit? \nAny unsaved data will be lost.",
                      QtGui.QMessageBox.Yes| QtGui.QMessageBox.No)
        event.ignore()

        if result == QtGui.QMessageBox.Yes:
            event.accept()


        
#Hashing
def hashing(password):
    """Using a sha-512 hashing algorithm to hash a string"""
    hashed = hashlib.sha512(password.encode('utf-8'))
    return hashed.hexdigest()          
        
            
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
