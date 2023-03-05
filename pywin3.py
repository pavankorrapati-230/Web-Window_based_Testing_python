from pywinauto import application
import time

app=application.Application()
app.start('OperaBrowser.exe')
# app.Notepad.edit.TypeKeys("Make it now, if not happens...Break it now",
#                           with_spaces=True,
#                           with_newlines=True,
#                           with_tabs=True,
#                           pause=0.5)


# time.sleep(3)
# app.Notepad.Edit("SelectAll")
# # time.sleep(3)
# # app.SaveAs.edit.SetText("pyWinFile1.txt")
# # time.sleep(3)
# # app.SaveAs.Save.click()