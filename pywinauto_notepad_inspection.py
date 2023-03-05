from pywinauto.application import Application

app=Application(backend='uia').start('Notepad.exe')
app=Application(backend='uia').connect(title='Untitled - Notepad',timeout=10)
#app.connect(title='Untitled - Notepad')
app.UntitledNotepad.print_contol_identifiers()