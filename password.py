import random
from tkinter import *
from tkinter import messagebox

# Classe para representar o Password Generator
class PasswordGenerator(): 
    def __init__(self) -> None:
        self.password= ''
    
    # Função que vai gerar uma senha
    def generate_password(self,lenght_password,option)->None:
         # Caracteres possiveis
        uppercaseLetters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        lowercaseLetters = uppercaseLetters.lower()
        numbers = '0123456789'
        symbols = '[]}{/*-~ç´;?'
        allCharacters = uppercaseLetters + lowercaseLetters + numbers + symbols
        lenght_password = int(lenght_password)
        if option == "single":
            password = ''.join(random.sample(allCharacters,lenght_password))
            self.password = password
            print(self.password)
    
    # Função da página  inicial
    def window(self):
        app = Tk()
        app.title("Password Generator")

        # Funções Get
        def get_lenght():
            return lenght_password.get()
        def get_option():
            return option.get()
        
        # Atualizar o valor ao gerar uma nova senha
        def return_password() -> StringVar:
            password_one.set(self.password) 

        # Definindo mensagens da situação da requisição
        def messageShow(type):
            if type == 'sucess':
                messagebox.showinfo(title="Success",message="Your password has been generated!")
            if type == 'warning':
                messagebox.showwarning(title="Warning",message="Max Leght is 50 characters! Minimum is 8 characters!")
            if type == 'error':
                messagebox.showerror(title="Error",message="Invalid Lenght, try again!")

        # Validação do tamanho e tipo da variavel lenght
        def validate(lenght):
            print(lenght)
            try:
                lenght = int(lenght)
                if lenght == 0 or lenght<0:
                    messageShow('error')
                elif lenght > 50:
                    messageShow('warning')
                elif lenght < 8:
                    messageShow('warning')
                else:
                    self.generate_password(get_lenght(),get_option())
                    return_password()
                    messageShow('sucess')

            except ValueError:
                messageShow('error')
                return -1
              
        password_one = StringVar()
        password_one.set(self.password)
        option = StringVar()
        option.set("single")
        
        # resolução da janela
        width = 1000
        height = 600

        # resolução do sistema 
        widht_screen = app.winfo_screenwidth()
        height_screen = app.winfo_screenheight()

        # posição da janela
        posx = widht_screen /2 - width / 2
        posy = height_screen /2 - height /2
        app.geometry("%dx%d+%d+%d" % (width,height,posx,posy))

        # container 
        container=Frame(app,bg="#1b1c1c")
        container.place(width=1000,height=600)
        
        tittle_app = Label(container,text="PASSWORD GENERATOR", font="Arial 20 bold", fg="#fff", bg="#1b1c1c")
        tittle_app.place(width=1000,height=50)

        # Body do app
        body=Frame(app,borderwidth=1,relief='solid')
        body.place(width=980,height=530,y=50,x=10)

        type_multiple= Radiobutton(body,text="Multiple passwords",font="Arial 12 bold",value="multiple",variable=option)
        type_multiple.place(x=450,y=20)
        
        type_single= Radiobutton(body,text="One password",font="Arial 12 bold",value="single",variable=option)
        type_single.place(x=300,y=20)

        label_lenght = Label(body,text="LENGHT:",width=10,font='Arial 12 bold')
        label_lenght.place(x=235,y=58)

        lenght_password = Entry(body,font="Arial 12",width=30)
        lenght_password.place(x=330,y=60)

        bt_entrar = Button(body, bd=0,text="Generate",borderwidth=1,relief='solid', command=lambda:[validate(get_lenght())]) 
        bt_entrar.place(width=250, height=50, x=340, y=90)
        
        # Output das senhas geradas
        output=Frame(body,borderwidth=1,relief='solid')
        output.place(width=500,height=200,y=150,x=210)
        password = Entry(output,textvariable=password_one,font='Arial 10',state='readonly',width=51,bd=0,relief='groove')
        password.place(x=80,y=10)
        
        # Inicialização da página
        app.resizable(False,False)
        app.mainloop()
        
init=PasswordGenerator()
init.window()
