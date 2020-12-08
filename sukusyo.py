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
    # 画像を縮小する
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
win.title("スクショ圧縮")
win.geometry("500x300")

# 部品を作成
labelsetsumei = tk.Label(win, text='クリップボードの画像を縮小します')
labelsetsumei.pack()
labelkanshi = tk.Label(win, text="---")
labelkanshi.pack()

button = tk.Button(win, text='縮小', command = grabimage )
button.pack()
# ウィンドウを動かす
win.mainloop()