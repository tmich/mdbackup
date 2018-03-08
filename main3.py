# Python 2.7.14

import Tkinter as tk
import ttk
from client import RpcClient
import socket
import threading

rpc = RpcClient()


class LoginResult:

    def __init__(self):
        self.username = None
        self.password = None
        self.loggedin = False


class LoginDialog(tk.Toplevel):
    def __init__(self, parent, result, client=None):
        self.top = tk.Toplevel.__init__(self, parent)
        self.style = ttk.Style()
        self.style.configure("error.Label",
                             foreground="white", background="red")
        self.username = tk.StringVar()
        self.password = tk.StringVar()
        self.message = tk.StringVar()
        # self.client = client
        self.geometry("250x150")
        self.title("Login")
        self.result = result
        self.parent = parent
        # self.client = RpcClient()

        self.l_u = ttk.Label(self, text='Utente')
        self.e_username = ttk.Entry(self, textvariable=self.username)
        self.l_p = ttk.Label(self, text='Password')
        self.e_password = ttk.Entry(self, show="*", textvariable=self.password)
        self.b_login = ttk.Button(self, text='Login',
                                  command=self._login_btn_clicked)
        self.l_msg = ttk.Label(self, textvariable=self.message)
        self.l_u.pack()
        self.e_username.pack()
        self.l_p.pack()
        self.e_password.pack()
        self.b_login.pack()
        self.l_msg.pack()
        self.grab_set()

    def _error(self, msg):
        self.l_msg.configure(style="error.Label")
        self.message.set(msg)

    def _login_btn_clicked(self):
        usr = self.username.get()
        pwd = self.password.get()

        try:
            rpc.connect()
            if rpc.login(usr, pwd):
                self.result.loggedin = True
                self.result.username = self.username.get()
                self.result.password = self.password.get()
                self.destroy()
            else:
                self._error('access denied')
                print self.message.get()
        except socket.error as serr:
            self._error(str(serr))
        except Exception as exc:
            self._error(str(exc))


class Window(ttk.Frame):

    def __init__(self, parent):
        ttk.Frame.__init__(self, parent)
        self.parent = parent
        self.parent.withdraw()
        self.parent.geometry("400x300")
        self.parent.title("Main Window")
        self.parent.after(100,  self.login)

        self.items = []
        self.n_items = tk.IntVar()

        self.b1 = ttk.Button(self.parent,
                             text='Aggiorna', command=self._b1_clicked)
        self.b1.pack()

        self.l_items = ttk.Label(self.parent, textvariable=self.n_items)
        self.l_items.pack()
        self.parent.update()

    def _b1_clicked(self):
        self.b1.configure(state="disabled")
        self.b1.configure(text="in corso...")
        rpc.connect()
        self.async_result = rpc.aggiorna_async()
        t = threading.Thread(target=self.check_is_ready)
        t.start()

    def check_is_ready(self):
        while not self.async_result.ready:
            pass

        # risposta arrivata
        self.items = self.async_result.value
        self.is_ready()

    def is_ready(self):
        self.n_items.set(len(self.items))
        print 'PRONTO. Ricevuti %d oggetti' % self.n_items.get()
        self.b1.configure(state="normal")
        self.b1.configure(text="Aggiorna")

    def login(self):
        result = LoginResult()
        dialog = LoginDialog(self, result)
        self.parent.wait_window(dialog)

        if result.loggedin:
            print 'logged in as %s' % (result.username,)
            self.parent.deiconify()
        else:
            print 'closing app...'
            self.parent.destroy()


if __name__ == '__main__':
    app = tk.Tk()
    app.style = ttk.Style()
    app.style.theme_use('clam')
    w = Window(app)

    app.mainloop()
