import tkinter as tk
# import win32clipboard as winc
from PIL import ImageGrab
from PIL import Image

# ボタンを押したときの処理
def grabimage():
    # クリップボードから画像を取得する
    im = ImageGrab.grabclipboard()
    small_image = im.resize((1280, 720))
    im.save('somefile.png', 'PNG')
    small_image.save('somefile2.png', 'PNG')

# 画面の表示
win = tk.Tk()
win.title("スクショ圧縮")
win.geometry("500x300")

# 部品を作成
labelkanshi = tk.Label(win, text="NONE")
labelkanshi.pack()

button = tk.Button(win, text='PNG生成', command = grabimage )
button.pack()
# ウィンドウを動かす
win.mainloop()