import tkinter as tk
def clicar(valor):
    visor.insert(tk.END, valor)
def limpar():
    visor.delete(0, tk.END)
def apagar():
    visor.delete(len(visor.get())-1, tk.END)
def calcular():
    try:
        resultado = eval(visor.get())
        visor.delete(0, tk.END)
        visor.insert(tk.END, resultado)
    except:
        visor.delete(0, tk.END)
        visor.insert(tk.END, "Erro")
janela = tk.Tk()
janela.title("Calculadora")
janela.config(bg="black")
visor = tk.Entry(janela, font=("Arial", 20), bg="black", fg="white", border=0, justify="right")
visor.grid(row=0, column=0, columnspan=4, pady=10, padx=10, ipady=10)
botoes = [
    ("C", limpar), ("⌫", apagar), ("/", lambda: clicar("/")), ("*", lambda: clicar("*")),
    ("7", lambda: clicar("7")), ("8", lambda: clicar("8")), ("9", lambda: clicar("9")), ("-", lambda: clicar("-")),
    ("4", lambda: clicar("4")), ("5", lambda: clicar("5")), ("6", lambda: clicar("6")), ("+", lambda: clicar("+")),
    ("1", lambda: clicar("1")), ("2", lambda: clicar("2")), ("3", lambda: clicar("3")), ("=", calcular),
    ("0", lambda: clicar("0")), (".", lambda: clicar(".")),
]
linha, coluna = 1, 0
for texto, comando in botoes:
    cor = "#b57edc" if texto == "=" else "#333333" if not texto.isdigit() else "#111111"
    tk.Button(
        janela, text=texto, width=5, height=2,
        font=("Arial", 18, "bold"),
        bg=cor, fg="white",
        command=comando
    ).grid(row=linha, column=coluna, padx=5, pady=5)
    coluna += 1
    if coluna > 3:
        coluna = 0
        linha += 1
janela.mainloop()
