from pywinauto import application
import time

app=application.Application()
app.start('Notepad.exe')
app.Notepad.edit.TypeKeys("Make it now, if not happens...Break it now",
                          with_spaces=True,
                          with_newlines=True,
                          with_tabs=True,
                          pause=0.5)
app.Notepad.MenuSelect("File->PageSetup")
app.Notepad.MenuSelect("File->Letter")


time.sleep(3)
# app.Notepad.MenuSelect("File->SaveAs")

# app.Notepad.MenuSelect("Edit->SelectAll")
# app.Notepad.MenuSelect("Edit->Copy")

# # app.Notepad.MenuSelect("Format->Font")
# app.Notepad.Font("Constantia")
# app.Click()
# app.Save()
time.sleep(3)

# app.SaveAs.edit.SetText("pyWinFile1.txt")
# time.sleep(3)
# app.SaveAs.Save.click()
# app.Yes.click()
# app.Notepad.MenuSelect("File->Exit")
# app.Exit("DontSave")
# app.click()