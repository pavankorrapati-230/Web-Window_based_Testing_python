# import wmi
import win32com
wmi = win32com.client.GetObject('winmgmts:')
pids = [p.ProcessId for p in wmi.InstancesOf('win32_process') if p.Name == 'firefox.exe']