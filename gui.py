# import functions
import PySimpleGUI as Sg

label = Sg.Text("Hi enter the item to to do list")
input_value = Sg.InputText(tooltip="enter a value")
button_val = Sg.Button("ADD")

window_data = Sg.Window('this is my to-do app', layout=[[label], [input_value, button_val]])
window_data.read()
window_data.close()
