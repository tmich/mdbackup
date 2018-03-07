#!/usr/bin/python

import Tkinter as tk
import gui
import database as db
from client import RpcClient
 
root = tk.Tk()

#print gui.ask_login(root)

#rpc_client = db.get_rpc_client()
	# login_dlg = LoginForm(master=root)
	# login_dlg.transient(root)    # only one window in the task bar
	# login_dlg.grab_set()         # modal
#else:

#mw = MainWindow(root, rpc_client)

must_login = not db.get_rpc_client()

rpc = RpcClient()
mw = gui.MainWindow(root, rpc, must_login=must_login)
# root.mainloop()

root.update()

d = gui.MyDialog(root)

root.wait_window(d.top)