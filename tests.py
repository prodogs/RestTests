from pdb import run
from PyQt5.QtWidgets import QApplication, QWidget, QTabWidget
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QTextEdit, QProgressBar,QLabel,QFileDialog,QComboBox, QListWidget
import os
from PyQt5.QtWidgets import QAbstractItemView

def runTests():
    print("Running Tests")
    setStatusMessage("Running Tests")

def stopTests():
    print("Stopping Tests") 

def quitApplication():
    exit() 

def setStatusMessage(status):
    global statusLabel
    statusLabel.setText(f"Status : {status}")

def setProgress(progress):
    global progress_bar
    progress_bar.setValue(progress)

def setScenario(scenarioText):
    global scenario
    scenario.setText(scenarioText)

def setErrors(errors):
    global errorsLabel
    errorsLabel.setText(f"Errors : {errors}")

def setNumberOfTests(tests):
    global numberOfTests
    numberOfTests.setText(f"Number of Tests : {tests}")


def openTestFile():
    file_dialog = QFileDialog()
    file_name, _ = file_dialog.getOpenFileName()

    if file_name:
        print(f"Selected file: {file_name}")
    
    return file_name

def main():
    app = QApplication([])

    global statusLabel, errorsLabel,scenario, responseFile, test_file, window, progress_bar, numberOfTests, button2, layout, hlayout, tab_widget, tab1, tab2

    window = QWidget()
    window.setWindowTitle('API REST Test Runner')

    layout = QVBoxLayout()
    hlayout = QHBoxLayout()

    runButton = QPushButton("Run Tests")
    runButton.setFixedSize(100, 50)
    runButton.clicked.connect(runTests)

    stopButton = QPushButton("Stop Tests")
    stopButton.setFixedSize(100, 50)
    stopButton.clicked.connect(stopTests)
    
    openFileButton = QPushButton("OpenFile")
    openFileButton.setFixedSize(100, 50)
    openFileButton.clicked.connect(openTestFile)
    
    quitButton = QPushButton("Quit")
    quitButton.setFixedSize(100, 50)
    quitButton.clicked.connect(quitApplication)

    hlayout.addWidget(runButton)
    hlayout.addWidget(stopButton)
    hlayout.addWidget(openFileButton)
    hlayout.addWidget(quitButton)



    layout.addLayout(hlayout)

    progress_bar = QProgressBar()
    progress_bar.setRange(0, 100)
    progress_bar.setValue(50)
    progress_bar.setStyleSheet("""
    QProgressBar {
        border: 2px solid grey;
        border-radius: 5px;
        text-align: center;
    }

    QProgressBar::chunk {
        background-color: green;
    }
""")
    
    
    
    
    
    layout.addWidget(progress_bar)

    label = QLabel("API Test File Name : ") 
    layout.addWidget(label)

    baseUrlLabel = QLabel("Base URL : ") 
    layout.addWidget(baseUrlLabel)

    scenario = QLabel("Scenario : ") 
    layout.addWidget(scenario)
    
    numberOfTests = QLabel("Number Of Tests : ") 
    layout.addWidget(numberOfTests)

    errorsLabel = QLabel("Errors : ") 
    layout.addWidget(errorsLabel)

    skippedLabel = QLabel("Skipped : ") 
    layout.addWidget(skippedLabel)

    statusLabel = QLabel("Status : ") 
    statusLabel.setStyleSheet("background-color: yellow;color: black")

    filterLabel = QLabel("Filter : ")
    layout.addWidget(statusLabel)
    layout.addWidget(filterLabel)
    filterLayout = QHBoxLayout()    
    layout.addLayout(filterLayout)
    


    scenarioLayout = QVBoxLayout()
    title = QLabel("Select Scenario :")
    scenarioLayout.addWidget(title)
    combo_box = QComboBox()
    combo_box.addItem("Scenario 1")
    combo_box.addItem("Scenario 2")
    combo_box.addItem("Scenario 3")
    scenarioLayout.addWidget(combo_box)
    filterLayout.addLayout(scenarioLayout)


    typeChoiceLayout = QVBoxLayout()
    title = QLabel("Select Types :")
    typeChoiceLayout.addWidget(title)
    list_widget = QListWidget()
    list_widget.setSelectionMode(QAbstractItemView.MultiSelection)
    typeChoiceLayout.addWidget(list_widget)
    filterLayout.addLayout(typeChoiceLayout)
    
    for i in range(10):
        list_widget.addItem(f"Item {i+1}")

    filterLayout.addWidget(list_widget)


    tab_widget = QTabWidget()
    tab_widget.setFixedSize(800, 600) 

    current_directory = os.getcwd()
    print(current_directory)
    with open('tests.py', 'r') as file:
        text = file.read()

    test_file = QTextEdit()
    test_file.setPlainText(text)

    # Add the QTextEdit widget to the tab
    tab_widget.addTab(test_file, "Test File")
    layout.addWidget(tab_widget)

    responseFile = QTextEdit()
    responseFile.setPlainText(text)

    tab_widget.addTab(responseFile, "Results File")
    layout.addWidget(tab_widget)

    window.setLayout(layout)    
    window.show()

    app.exec_()

if __name__ == '__main__':
    main()


