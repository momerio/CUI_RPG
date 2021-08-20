# 操作方法画面
# メニュー画面

#ユーザ定義#
import DrawDisplay
import CommandManager


def run():
    DrawDisplay.clear()  # 画面削除

    # 描画

    DrawDisplay.initialDiplay([
        "######### 操作方法 #########",
        "asdw\t: コマンド移動",
        "Enter\t: 決定",
        "Esc\t: ゲーム終了",
        "",
        "Enterキーで戻る",
        ""
    ])

    command_number = 0
    command_line = [
    ]

    key = ""
    while True:
        key = CommandManager.CommandManager().pressKey()  # 入力キー取得
        DrawDisplay.clear()  # 画面を消す

        DrawDisplay.initialDiplay([
            "######### 操作方法 #########",
            "asdw\t: コマンド移動",
            "Enter\t: 決定",
            "Esc\t: ゲーム終了",
            "",
            "Enterキーで戻る",
            ""
        ])

        #コマンド操作#
        if key in CommandManager.ENTER:
            print("もどる")
            return 0
        elif key in CommandManager.ESC:
            print("Info: ESC終了!(MenuScene, run())")
            return 0

    return 1  # 異常終了


if __name__ == '__main__':
    run()
