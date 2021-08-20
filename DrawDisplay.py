# 表示関連ファイル
# 関数Ver

import os


def initialDiplay(disp_data, line_end="\n", end="\n"):
    """
    初期部分を表示

    @param
        dips_data,list              : 表示するデータ
        line_end,str,default='\n'   : 1行ごとの終わり文字列
        end,str,default='\n'        : 最後に出力する文字列
    """
    for line in disp_data:
        print(line, end=line_end)

    print(end=end)  # 最後に出力するもの


def commandDisplay(disp_data, command_number=0, cursol="▶ ", line_end="\n", end="\n"):
    """
    画面描画のコマンド部分
    @param
        dips_data,list              : 表示するデータ
        command_number,int,default=0: コマンド番号
        cursol,str,default="▶ "     : カーソル
        line_end,str,default='\n'   : 1行ごとの終わり文字列
        end,str,default='\n'        : 最後に出力する文字列
    """

    for command_num, line in enumerate(disp_data):
        if command_num == command_number:
            print("{}{}".format(cursol, line), end="")
        else:
            print(line, end="")
        print(end=line_end)

    print(end=end)  # 最後に出力するもの


def clear():
    """コンソール上の出力をすべて削除する"""
    os.system("cls")


if __name__ == "__main__":
    initials = ["========= START ==========",
                "DEMO RPG!", ""]
    commands = ["command A", "command B", "command C"]

    initialDiplay(initials, line_end="\n", end="------- command -------\n")
    commandDisplay(commands, command_number=0,
                   cursol="▶ ", line_end="\n", end="\n")
