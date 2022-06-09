import random
from tkinter import *
from tkinter import messagebox
from random import randint

# Classe para representar o Password Generator
class PasswordGenerator(): 
    def __init__(self) -> None:
        self.password= ''
        self.password_multiple= []
    
    # Função que vai gerar uma senha
    def generate_password(self,length_password,option)->None:
        # Caracteres possiveis
        uppercaseLetters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        lowercaseLetters = uppercaseLetters.lower()
        numbers = '0123456789'
        symbols = '[]}{/*-~ç´;?'
        allCharacters = uppercaseLetters + lowercaseLetters + numbers + symbols
        length_password = int(length_password)
        if option == "single":
            password = ''.join(random.sample(allCharacters,length_password))
            self.password = password
        else:
            self.password_multiple = []
            for password in range (10):
                password = ''.join(random.sample(allCharacters,length_password))
                self.password_multiple.append(password)
    
    def save_txt(self):
        name_archive = 'Password - ' + str(randint(0,1000)) 
        if len(self.password_multiple) != 0:
            name_archive = name_archive + ".txt"
            archive = open(name_archive, "x")
            archive.close()
            archive = open(name_archive, "w")
            for password in self.password_multiple:
                archive.write("- "+password+"\n")
            archive.close()
        else:
            self.messageShow('save_error')


            # Definindo mensagens da situação da requisição
    def messageShow(self,type):
        if type == 'sucess':
            messagebox.showinfo(title="Success",message="Your password has been generated!")
        if type == 'warning':
            messagebox.showwarning(title="Warning",message="Max Leght is 50 characters! Minimum is 8 characters!")
        if type == 'error':
            messagebox.showerror(title="Error",message="Invalid Lenght, try again!")
        if type == 'save_error':
            messagebox.showerror(title="Error",message="Save error, Try again")

    # Função da página  inicial
    def window(self):
        app = Tk()
        app.title("Password Generator")

        # Funções Get
        def get_length()-> StringVar:
            return length_password.get()
                 
        def get_option()-> StringVar:
            return option.get()
        
        # Atualizar o valor ao gerar uma nova senha
        def return_password() -> StringVar:
            password_one.set(self.password) 
        
        def return_multiple_password() -> StringVar:
            x = ''
            for i in self.password_multiple:
                x += i + '\n'
                password_m.set(x) 

        # Função que deixa a senha gerada na area de transferencia
        def copy_single():
            app.clipboard_clear()
            app.clipboard_append(self.password)
 


        # Validação do tamanho e tipo da variavel length
        def validate(length):
            try:
                length = int(length)
                if length == 0 or length<0:
                    self.messageShow('error')
                elif length > 50:
                    self.messageShow('warning')
                elif length < 8:
                    self.messageShow('warning')
                else:
                    self.generate_password(get_length(),get_option())
                    return_multiple_password()
                    return_password()
                    self.messageShow('sucess')


            except ValueError:
                self.messageShow('error')
                return -1
        
        password_one = StringVar()
        password_one.set(self.password)
        password_m = StringVar()

        option = StringVar()
        option.set("single")
        
        # resolução da janela
        width = 600
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
        container.place(width=600,height=600)
        tittle_app = Label(container,text="PASSWORD GENERATOR", font="Arial 20 bold", fg="#fff", bg="#1b1c1c")
        tittle_app.place(width=600,height=50)

        # Body do app
        body=Frame(app,borderwidth=1,relief='solid')
        body.place(width=580,height=530,y=50,x=10)

        container_main=Frame(body,borderwidth=1,relief='solid')
        container_main.place(width=440,height=350,x=75)

        type_multiple= Radiobutton(container_main,text="Multiple passwords",font="Arial 12 bold",value="multiple",variable=option)
        type_multiple.place(x=200,y=20)
        type_single= Radiobutton(container_main,text="One password",font="Arial 12 bold",value="single",variable=option)
        type_single.place(x=50,y=20)

        label_length = Label(container_main,text="LENGTH:",width=10,font='Arial 12 bold')
        label_length.place(x=40,y=58)
        length_password = Entry(container_main,font="Arial 12",width=22)
        length_password.place(x=135,y=60)

        bt_generate = Button(container_main, bd=0,text="Generate",borderwidth=1,relief='solid', command=lambda:[validate(get_length())]) 
        bt_generate.place(width=202, height=25, x=135, y=115)
        
        # Output das senhas geradas
        output=Frame(body,borderwidth=1,relief='solid')
        output.place(width=440,height=350,y=150,x=75)
        
        label_password = Label(output,text='PASSWORD',font='Arial 12 bold',width=10)
        label_password.place(x=2,y=6)
        password = Entry(output,textvariable=password_one,font='Arial 10',state='readonly',width=51,bd=0,relief='groove',justify=CENTER)
        password.place(x=40,y=33)

        line=Frame(body,bg="#1b1c1c")
        line.place(width=440,height=2,y=230,x=75)

        label_mpassword = Label(output,text='MULTIPLE PASSWORD',font='Arial 12 bold',width=18)
        label_mpassword.place(x=3,y=86)
        password_multiple = Label(output,textvariable=password_m,font='Arial 10',width=51,justify=CENTER)
        password_multiple.place(x=20,y=120)

        # Botões para manipulações das senhas geradas
        bt_copy = Button(body, bd=0,text="copy",borderwidth=1,relief='solid', command=copy_single) 
        bt_copy.place(width=50, height=20, x=450, y=205)

        bt_save = Button(body, bd=0,text="save text file",borderwidth=1,relief='solid', command=self.save_txt) 
        bt_save.place(width=100, height=20, x=400, y=470)
        
        # Inicialização da página
        app.resizable(False,False)
        app.mainloop()
        
init=PasswordGenerator()
init.window()
