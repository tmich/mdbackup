import Tkinter as tk
#from tkinter import tk
from client import RpcClient
import tkMessageBox as tm
import tkSimpleDialog

class MyDialog(tkSimpleDialog.Dialog):

    def body(self, master):

        tk.Label(master, text="First:").grid(row=0)
        tk.Label(master, text="Second:").grid(row=1)

        self.e1 = tk.Entry(master)
        self.e2 = tk.Entry(master)

        self.e1.grid(row=0, column=1)
        self.e2.grid(row=1, column=1)
        return self.e1 # initial focus

    def apply(self):
        first = self.e1.get()
        second = self.e2.get()
        print first, second # or something

class LoginFrame(tk.Toplevel):
	def __init__(self, master, rpc):
		tk.Toplevel.__init__(self, master)
		self.grab_set()
		
		self.rpc = rpc

		self.label_username = tk.Label(self, text="Username")
		self.label_password = tk.Label(self, text="Password")

		self.entry_username = tk.Entry(self)
		self.entry_password = tk.Entry(self, show="*")

		self.label_username.grid(row=0, sticky=tk.E)
		self.label_password.grid(row=1, sticky=tk.E)
		self.entry_username.grid(row=0, column=1)
		self.entry_password.grid(row=1, column=1)

		self.checkbox = tk.Checkbutton(self, text="Keep me logged in")
		self.checkbox.grid(columnspan=2)

		self.logbtn = tk.Button(self, text="Login", command=self._login_btn_clicked)
		self.logbtn.grid(columnspan=2)
		

	def _login_btn_clicked(self):
		# print("Clicked")
		username = self.entry_username.get()
		password = self.entry_password.get()

		# print(username, password)

		if self.rpc.login(username, password):
			#tm.showinfo("Login info", "Welcome %s" % username)
			self.master.destroy()
		else:
			tm.showerror("Login error", "Incorrect username")
 
class MainWindow(tk.Frame):

	def __init__(self, master, rpc, must_login=False):
	
		tk.Frame.__init__(self, master)
	
		self.rpc = rpc
		
		# self.clone_btn = tk.Button(self.master, text='CLONE')
		# self.clone_btn.grid(row=1, column=5, sticky='NS')
		
		# self.pull_btn = tk.Button(self.master, text='PULL')
		# self.pull_btn.pack()
		
		# if must_login:
			# lf = LoginFrame(master, rpc)
		
		print('Prrrrrrr!')
		self.master = master
		
		# if rpc_client == None:
			# print('Primo accesso, serve login...')
			# Login(self.master)
			# #self.master.withdraw()
			
		
	
	def show(self):
		self.master.title('Main Window')
		self.master.geometry('800x600')
		self.pack()