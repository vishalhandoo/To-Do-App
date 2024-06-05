
import FreeSimpleGUI as sg

label = sg.Text("Enter Feet")
input_box1 = sg.InputText(tooltip="Enter Feet")

label1 = sg.Text("Enter Inches")
input_box2 = sg.InputText(tooltip="Enter inches")

Add_Button = sg.Button("Convert")

window = sg.Window("My app",[[label,input_box1],[label1,input_box2],[Add_Button]])
window.read()
window.close()
