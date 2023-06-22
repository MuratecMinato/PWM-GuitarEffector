# PWM-GuitarEffector
ラズパイPicoを使用して開発

音をADコンバータで取得し、ディストーション、オーバードライブなど音色の加工を行う

Pythonで開発

エレキギターでは、ギターの弦振動をピックアップで電圧に変換する
その際に弦振動の周波数も電圧に含まれる

ピックアップが出力する電圧をADコンバータで検出し、検出した電圧をPWMでスピーカへ出力すれば音として
再生できる

ブロック図

！[画像] (https://github.com/MuratecMinato/PWM-GuitarEffector/assets/71358603/465e4d10-94c8-4d7f-a8fa-cc5c2e4bcc13)
