# Tkinterのライブラリを取り込む
import tkinter as tk
# from tkinter import messagebox as mbox

# ウィンドウを作成
win = tk.Tk()
win.title("Hello, World!")  #タイトル
win.geometry("500x250")  #サイズ

# 部品を作成
# ラベルを作成
label = tk.Label(win, text='名前は？')
label.pack()

# テキストボックスを作成
text = tk.Entry(win)
text.pack()
text.insert(tk.END, 'クジラ')  #初期値を指定

# OKボタンを押したとき
def ok_click():
    # テキストボックスの内容を得る
    s = text.get()
    # ダイアログを表示
    # mboxvs.showinfo('挨拶', s + 'さん，こんにちは!')
    tk.messagebox.showinfo('挨拶', s + 'さん，こんにちは!')

# ボタンを作成
okButton = tk.Button(win, text='OK', command=ok_click)
okButton.pack()

# ウィンドウを動かす
win.mainloop()