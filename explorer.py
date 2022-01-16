from win32gui import GetClassName, GetWindowText, GetForegroundWindow
from win32com.client import Dispatch 
from typing import Union


ShellWindowsCLSID = '{9BA05972-F6A8-11CF-A442-00A0C90A8F39}'


class Explorer:
    def __init__(self):
        self.ShellWindows = Dispatch ( ShellWindowsCLSID )


    @staticmethod
    def focused() -> Union[bool, int]:
        active_window_hwnd = GetForegroundWindow()
        if GetClassName(active_window_hwnd) == 'CabinetWClass':
            return active_window_hwnd

        return False


    def current_path(self):
        hwnd = self.focused()
        if not hwnd:
            print('This method is set to return only if Windows Explorer has focus')
            return 

        for sw in self.ShellWindows:
            if sw.HWND == hwnd:
                try:
                    path = sw.LocationURL.split('file:///')[1]
                    path = path.replace('/', '\\')
                    return path
                except IndexError:
                    print('Directory not accessible')


# EXEMPLO NO C#
#
# SHDocVw.ShellWindows shellWindows = new SHDocVw.ShellWindows();

# string filename;

# foreach (SHDocVw.InternetExplorer ie in shellWindows)
# {
#     filename = Path.GetFileNameWithoutExtension(ie.FullName).ToLower();

#     if (filename.Equals("explorer"))
#     {
#         // Save the location off to your application
#         Console.WriteLine("Explorer location : {0}", ie.LocationURL);

#         // Setup a trigger for when the user navigates
#         //ie.NavigateComplete2 += new SHDocVw.DWebBrowserEvents2_NavigateComplete2EventHandler(handlerMethod);
#     }
# }    