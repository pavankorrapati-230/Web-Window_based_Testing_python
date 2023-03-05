from pywinauto.application import Application

# app=Application(backend='uia').start('notepad.exe').connect(title='Browser_QualiTek.txt - Notepad')
app=Application(backend='win32').start('Notepad++.exe').connect(title='MobileApplication.txt - Notepad++')
# app=Application(backend='uia').connect(title='MobileApplication.txt')
app.Properties.print_control_identifiers()