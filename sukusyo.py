import tkinter as tk
import win32clipboard as w32c
from PIL import ImageGrab
from PIL import Image
import io

# ボタンを押したときの処理
def grabimage():
    # クリップボードから画像を取得する
    im = ImageGrab.grabclipboard()
    # 画像を取得できなければ終了する
    if im is None:
        labelkanshi['text'] = 'None'
        return
    var = 0
    # 画像を縮小する
    if var == 0:
        small_image = im.resize((1920, 1080))
    elif var == 1:
        small_image = im.resize((1280, 720))

    output = io.BytesIO()
    small_image.convert("RGB").save(output,"BMP")
    data = output.getvalue()[14:]
    output.close()
    w32c.OpenClipboard()
    w32c.SetClipboardData(w32c.CF_DIB, data)
    w32c.CloseClipboard()
    labelkanshi['text']='Success!'

# 画面の表示
win = tk.Tk()
win.title("Clipboard Resize")
win.geometry("500x300")

# 部品を作成
labelsetsumei = tk.Label(win, text='クリップボードの画像を縮小します')
labelsetsumei.pack()
labelkanshi = tk.Label(win, text="---")
labelkanshi.pack()
# ラジオボタン
# ラジオボタンの初期値
var = tk.IntVar()
var.set(0)
rd1 = tk.Radiobutton(win, value=0, variable=var, text='FHD')
rd1.pack()
rd2 = tk.Radiobutton(win, value=1, variable=var, text='HD')
rd2.pack()
# ボタン
varnum = var.get()
button = tk.Button(win, text='縮小', command = grabimage)
button.pack()
# ウィンドウを動かす
win.mainloop()