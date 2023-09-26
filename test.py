#音階を鳴らす
# Path: test.py

import winsound

winsound.Beep(262, 1000) # ド
winsound.Beep(294, 1000) # レ
winsound.Beep(330, 1000) # ミ
winsound.Beep(349, 1000) # ファ
winsound.Beep(392, 1000) # ソ
winsound.Beep(440, 1000) # ラ
winsound.Beep(494, 1000) # シ
winsound.Beep(523, 1000) # ド

#ディストーションをかける
winsound.PlaySound("test.wav", winsound.SND_FILENAME)
#音を選択する
#winsound.Beep以外の音を鳴らす


#Aマイナースケールを鳴らす
winsound.Beep(440, 1000) # ラ
winsound.Beep(494, 1000) # シ
winsound.Beep(523, 1000) # ド
winsound.Beep(587, 1000) # ミ
winsound.Beep(659, 1000) # ソ
winsound.Beep(698, 1000) # ラ
winsound.Beep(784, 1000) # ド
winsound.Beep(880, 1000) # ミ
winsound.Beep(988, 1000) # シ
winsound.Beep(1047, 1000) # ド

#ディミニッシュスケールを鳴らす
winsound.Beep(440, 1000) # ラ
winsound.Beep(494, 1000) # シ
winsound.Beep(523, 1000) # ド
winsound.Beep(587, 1000) # ミ
winsound.Beep(659, 1000) # ソ
winsound.Beep(698, 1000) # ラ
winsound.Beep(784, 1000) # ド
winsound.Beep(880, 1000) # ミ
winsound.Beep(988, 1000) # シ
winsound.Beep(1047, 1000) # ド

