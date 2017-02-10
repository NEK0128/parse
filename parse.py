import sys
import os

# 入力ディレクトリと出力ディレクトリを指定
readdir = sys.argv[1]
outdir = sys.argv[2]

print("readdir:\t", readdir)
print("outdir:\t", outdir)

# ディレクトリのファイル一覧を取得
txts = os.listdir(readdir)

for txt in txts:
    if not (txt.split(".")[-1] == "txt"):   # 拡張子がtxt以外を無視
        continue
    txt = os.path.join(readdir, txt)

    with open(txt, encoding='utf-8') as file:
        lines = file.readlines()

    for line in lines:
        # キャラ名を取得
        char_name = line[:line.find("「")]
        outfname = os.path.join(outdir, char_name + ".txt")

        # キャラ名のファイルがあるかどうか確認
        if os.path.exists(outfname):
            # ある場合は上書きモードで
            mode = "a"
        else:
            # ない場合は新規作成
            mode = "w"

        # セリフのみ抽出
        line_format = line[line.find("「") + 1:line.find("」")] + "\n"
        # セリフ書き込み
        with open(outfname, mode) as file:
            file.write(line_format)
