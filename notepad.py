from pywinauto.application import Application
app=Application().start("notepad.exe",timeout=10)
main_dlg=app.UntitledNotepad
main_dlg.Edit.type_keys("Hello Hai Corona, come again to do Work from Home",
                        with_spaces=True,
                        with_newlines=True,
                        pause=0.2,
                        with_tabs=True)
# font_menu=main_dlg.menu_select("Format->Font...")
# font_dlg=app.Font
# font_type=font_dlg.ComboBox
# font_type.select("Corbel")
# app.font_type.OK.click()





