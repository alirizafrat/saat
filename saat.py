import tkinter
from time import strftime
top = tkinter.Tk()
top.title('Saat')
top.resizable(0,0)
def zaman(): 
    string = strftime('%H:%M:%S %p') 
    clockTime.config(text = string) 
    clockTime.after(1000, zaman)
clockTime = tkinter.Label(top, font = ('Consolas', 40, 'bold'), background = 'black', foreground = 'white')
clockTime.pack(anchor = 'center')
zaman() 
top.mainloop()

###   Bu Proje Ali Rıza Fırat tarafından eğitim amaçlı olarak paylaşılmıştır.
###   https://alirizafirat.com/
###   alirizafirat@aol.com