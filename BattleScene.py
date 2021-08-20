"""
自分のステータスや敵ステータスを
引数で指定できるように変更
"""

# バトル画面
# メニュー画面

#ユーザ定義#
import DrawDisplay
import CommandManager
import random


def run(my_name, my_hp, waza: list, enemy_name, enemy_hp):
    while enemy_hp > 0:
        DrawDisplay.clear()  # 画面削除

        # 描画
        display_info = [
            "== 情報 ==",
            "{}".format(enemy_name),
            "HP: {}".format(enemy_hp),
            "",
            "-----------------",
            "{}".format(my_name),
            "HP : {}".format(my_hp),
            "-----------------",
        ]

        # 描画
        DrawDisplay.initialDiplay(display_info)

        command_number = 0
        command_line = [
            """たたかう""",
            """にげる""",
        ]

        DrawDisplay.commandDisplay(command_line, command_number=command_number,
                                   cursol="▶ ", line_end="\n", end="\n")

        key = ""
        while True:
            key = CommandManager.CommandManager().pressKey()  # 入力キー取得
            DrawDisplay.clear()  # 画面を消す

            # 描画
            DrawDisplay.initialDiplay(display_info)

            #コマンド操作#
            if key in CommandManager.ENTER:
                print("OK")
                break
            if key in CommandManager.UP:  # 上キー
                command_number -= 1
            if key in CommandManager.DOWN:  # 下キー
                command_number += 1
            elif key in CommandManager.ESC:
                print("Info: ESC終了!(MenuScene, run())")
                exit()

            #コマンド#
            if command_number < 0:  # 一番上ならば一番下に
                command_number = len(command_line)-1
            elif len(command_line)-1 < command_number:  # 一番下ならば一番上に
                command_number = 0

            DrawDisplay.commandDisplay(command_line, command_number=command_number,
                                       cursol="▶ ", line_end="\n", end="\n")

        DrawDisplay.clear()  # 画面削除

        if command_number == 1:  # 逃げる処理
            print("{}は逃げ出した...".format(my_name))
            a = input()
            break

        if command_number == 0:  # 戦う処理
            DrawDisplay.clear()
            DrawDisplay.initialDiplay(display_info)

            # 技選択(一番上に技の変数、HPなど置いてある)
            command_line = [*waza]

            DrawDisplay.commandDisplay(command_line, command_number=command_number,
                                       cursol="▶ ", line_end="\n", end="\n")

            key = ""
            while True:
                key = CommandManager.CommandManager().pressKey()  # 入力キー取得
                DrawDisplay.clear()  # 画面を消す

                DrawDisplay.initialDiplay(display_info)

                #コマンド操作#
                if key in CommandManager.ENTER:
                    break
                if key in CommandManager.UP:  # 上キー
                    command_number -= 1
                if key in CommandManager.DOWN:  # 下キー
                    command_number += 1
                elif key in CommandManager.ESC:
                    print("Info: ESC終了!(MenuScene, run())")
                    return 0

                #コマンド#
                if command_number < 0:  # 一番上ならば一番下に
                    command_number = len(command_line)-1
                elif len(command_line)-1 < command_number:  # 一番下ならば一番上に
                    command_number = 0

                DrawDisplay.commandDisplay(command_line, command_number=command_number,
                                           cursol="▶ ", line_end="\n", end="\n")

            DrawDisplay.clear()  # 画面削除

            if command_number == 0:  # ハイドロポンプの処理
                print("{}は{}をはなった！".format(my_name, waza[0]))
                a = input()
                damage = random.randint(100, 120)  # ダメージの下限、上限
                enemy_hp = enemy_hp - damage
                print("{}は{}のダメージ！".format(enemy_name, damage))
                print("現在の敵のHP : {}".format(enemy_hp))
                a = input()

            if command_number == 1:  # たいあたりの処理
                print("{}は{}をはなった！".format(my_name, waza[1]))
                a = input()
                damage = random.randint(80, 120)  # ダメージの下限、上限
                enemy_hp = enemy_hp - damage
                print("{}は{}のダメージ！".format(enemy_name, damage))
                print("現在の敵のHP : {}".format(enemy_hp))
                a = input()

    return 1  # 異常終了


if __name__ == '__main__':
    my_hp = 89
    my_name = "ﾊﾊｯ"
    waza = ["ハイドロポンプ", "たいあたり"]
    enemy_hp = 600
    enemy_name = "ゆめのくに"
    run(my_name, my_hp, waza, enemy_name, enemy_hp)
