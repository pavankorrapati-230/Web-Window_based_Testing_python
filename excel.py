# import win32com.client as win32
from colorama import win32
from pywinauto import application
# from pywinauto import application
app=application.Application().start('mspaint.exe')
ms = win32.gencache.EnsureDispatch('mspaint.exe')
ms.DisplayAlerts = True

ms.Visible = True
pavan = input("Press ENTER to quit:")
ms.Workbooks.Open('assigned scenarios.xlsx')
ms.Application.Quit()