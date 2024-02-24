import PySimpleGUI as Sg

label = Sg.Text("choose the file")
input = Sg.Input()
button_data = Sg.FilesBrowse("choose")

label1 = Sg.Text("choose the file")
input1 = Sg.Input()
button_data1 = Sg.FolderBrowse("choose")

windows_data = Sg.Window("My To-do second app ", layout=[[label , input , button_data] ,[label1 , input1 , button_data1]])
windows_data.read()
windows_data.close()