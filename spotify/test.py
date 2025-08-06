from tkinter import Tk, Button
from reproductor import Reproductor

lista = ["musicas/swansong.mp3"]
musica = Reproductor(lista[0])

def reproducirMusica():
    musica.reproducir()

winamp = Tk()
winamp.title("WINAMP")
winamp.geometry("200x100")

bPlay = Button(text="▶", command=reproducirMusica)
bPlay.place(x=60, y=60)

winamp.mainloop()
