import PySimpleGUI as Sg

Label = Sg.Text("what are dolphins?")
option1 = Sg.Radio("Amphibians" , group_id="ques1")
option2 = Sg.Radio("Fish", group_id="ques1")
option3 = Sg.Radio("Mammals" , group_id="ques1")
options4 = Sg.Radio("Birds", group_id="ques1")

windows_data = Sg.Window("File Compressor", layout=[
    [Label],
    [option1],
    [option2],
    [option3],
    [options4]
])

windows_data.read()
windows_data.close()