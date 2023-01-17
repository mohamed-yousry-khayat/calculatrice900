from tkinter import *

champs_saisi = ""


def saisi(num):
    global champs_saisi
    champs_saisi = champs_saisi + str(num)
    entree.set(champs_saisi)


def egalsaisi():
    try:
        global champs_saisi

        resultat = str(eval(champs_saisi))
        entree.set(resultat)
        champs_saisi = resultat

    except:
        entree.set(" error ")
        champs_saisi = ""


def effacer():
    global champs_saisi
    champs_saisi = ""
    entree.set("")


if __name__ == "__main__":
    window = Tk()
    window.title("Calculatrice9000")
    window.geometry("375x375")
    window.resizable(width=False, height=False)
    window.iconbitmap("icone.ico")
    window.config(background='#dcdbd4')

    entree = StringVar()
    champs_saisi_entree = Entry(window, textvariable=entree)
    champs_saisi_entree.grid(columnspan=4, pady=30, padx=20, ipadx=100, ipady=10)

    btn_1 = Button(window, text=' 1 ', command=lambda: saisi(1), height=2, width=8, bg='#828788')
    btn_1.grid(row=2, column=0, pady=5)

    btn_2 = Button(window, text=' 2 ', command=lambda: saisi(2), height=2, width=8, bg='#828788')
    btn_2.grid(row=2, column=1, pady=5)

    btn_3 = Button(window, text=' 3 ', command=lambda: saisi(3), height=2, width=8, bg='#828788')
    btn_3.grid(row=2, column=2, pady=5)

    btn_4 = Button(window, text=' 4 ', command=lambda: saisi(4), height=2, width=8, bg='#828788')
    btn_4.grid(row=3, column=0, pady=5)

    btn_5 = Button(window, text=' 5 ', command=lambda: saisi(5), height=2, width=8, bg='#828788')
    btn_5.grid(row=3, column=1, pady=5)

    btn_6 = Button(window, text=' 6 ', command=lambda: saisi(6), height=2, width=8, bg='#828788')
    btn_6.grid(row=3, column=2, pady=5)

    btn_7 = Button(window, text=' 7 ', command=lambda: saisi(7), height=2, width=8, bg='#828788')
    btn_7.grid(row=4, column=0, pady=5)

    btn_8 = Button(window, text=' 8 ', command=lambda: saisi(8), height=2, width=8, bg='#828788')
    btn_8.grid(row=4, column=1, pady=5)

    btn_9 = Button(window, text=' 9 ', command=lambda: saisi(9), height=2, width=8, bg='#828788')
    btn_9.grid(row=4, column=2, pady=5)

    btn_0 = Button(window, text=' 0 ', command=lambda: saisi(0), height=2, width=8, bg='#828788')
    btn_0.grid(row=5, column=1, pady=5)

    plus = Button(window, text=' + ', command=lambda: saisi("+"), height=2, width=8, bg='#a5e3f6')
    plus.grid(row=2, column=3, pady=5)

    moins = Button(window, text=' - ', command=lambda: saisi("-"), height=2, width=8, bg='#a5e3f6')
    moins.grid(row=3, column=3, pady=5)

    multiplication = Button(window, text=' * ', command=lambda: saisi("*"), height=2, width=8, bg='#a5e3f6')
    multiplication.grid(row=4, column=3, pady=5)

    division = Button(window, text=' / ', command=lambda: saisi("/"), height=2, width=8, bg='#a5e3f6')
    division.grid(row=5, column=3, pady=5)

    egal = Button(window, text=' = ', command=egalsaisi, height=2, width=8, bg='green')
    egal.grid(row=6, column=3, pady=5)

    effacer = Button(window, text='effacer', command=effacer, height=2, width=8, bg='#a5e3f6')
    effacer.grid(row=5, column=0, pady=5)

    Decimal = Button(window, text='.', command=lambda: saisi('.'), height=2, width=8, bg='#d8dfe3')
    Decimal.grid(row=5, column=2, pady=5)

    pourcentage = Button(window, text='%', command=lambda: saisi('%'), height=2, width=8, bg='#a5e3f6')
    pourcentage.grid(row=6, column=1, pady=5)

    fermer = Button(window, text='Fermer', command=window.destroy, height=2, width=8, bg='#a5e3f6')
    fermer.grid(row=6, column=2, pady=5)

    racine = Button(window, text='√x', command=lambda: saisi('**0.5'), height=2, width=8, bg='#a5e3f6')
    racine.grid(row=6, column=0, pady=5)

window.mainloop()
