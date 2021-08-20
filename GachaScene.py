# ガチャ画面

#ユーザ定義#
import time
import random
import DrawDisplay
import CommandManager
import MenuScene


def gacha_cheering():
    """
    ガチャが増えたら関数ごと増やしていく
    """
    description = [
        """
        ∧＿∧             　　∧＿∧
    　 (´･ω･)　               (･ω･｀)
    　 /ヽ)ヽ)　              ( っ日ｏ
    　(￣￣￣￣)　           (￣￣￣￣)
    日 []￣￣[]　             []￣￣[]

        """
    ]
    return description


def select_description(gacha_name: str):
    """
    ※ガチャを増やしたら変更する必要のある部分
    """
    if gacha_name == "基本ガチャ":
        return gacha_cheering()


def draw_gacha():
    temp = []
    for _ in range(100):  # 列
        time.sleep(0.01)
        for __ in range(100):  # 行
            # line+=str(random.randint(0, 1))

            print(str(random.randint(0, 1)), end="")
        print("")

    print("\n")
    return 0


def getting_shop(choice_number=1):
    """
    ガチャを引いている画面
    """

    # データ読み込み
    shops = []
    with open("./data/shopinfo.csv", "r", encoding="utf-8") as f:
        for line in f:
            shops.append(line.strip("\n").replace("\u3000", " ").split(","))

    # ガチャった飲食店
    shop = random.sample(shops, choice_number)

    # 飲食店情報をセーブ
    with open("./data/save_shop.csv", "a", encoding="utf-8") as f:
        for s in shop:
            f.write(",".join(s)+"\n")

    # ガチャ演出
    draw_gacha()

    # ガチャ確定
    shop_name = [idx[1] for idx in shop]  # ガチャった飲食店の名前
    for sp in shop_name:
        DrawDisplay.initialDiplay(
            [f"☆ {sp} をゲットしました!"])
    DrawDisplay.initialDiplay(["Enter キーを押してください"])

    while True:
        key = CommandManager.CommandManager().pressKey()  # 入力キー取得
        DrawDisplay.clear()  # 画面を消す

        # DrawDisplay.initialDiplay(
        #     [f"{shop_name} をゲットしました!", "Enter キーを押してください"])

        #コマンド操作#
        if key in CommandManager.ENTER:
            return 0
        elif key in CommandManager.ESC:
            print("Info: ESC終了!(MenuScene, run())")
            exit(0)  # 終了

    return -1  # 異常終了


def gacha_description_run(gacha_name: str):
    """
    ガチャの詳細画面
    @param
        gacha_name,str: 詳細ガチャ名 e.g.)春に行きたいお店ガチャ とか
    """
    DrawDisplay.clear()  # 画面削除

    # 描画
    DrawDisplay.initialDiplay([
        f"######### {gacha_name} #########",
        ""
    ])

    DrawDisplay.initialDiplay(select_description(gacha_name))  # 詳細情報を表示

    ticket_number = 10  # お食事券の枚数
    DrawDisplay.initialDiplay([f"■□ チケット: {ticket_number}枚"])  # お食事券

    command_number = 0
    command_line = [
        "1回引く (チケットを1枚消費します)",
        "10+1回引く(チケットを10枚消費します)",
        "もどる",
    ]

    DrawDisplay.commandDisplay(command_line, command_number=command_number,
                               cursol="▶ ", line_end="\n", end="\n")

    key = ""
    none_ticket_flag = False
    while True:
        key = CommandManager.CommandManager().pressKey()  # 入力キー取得
        DrawDisplay.clear()  # 画面を消す

        #コマンド操作#
        if key in CommandManager.ENTER:
            if command_line[command_number] == "1回引く (チケットを1枚消費します)":
                if ticket_number-1 < 0:  # お食事券がないとき
                    none_ticket_flag = True
                else:  # お食事券があるとき
                    ticket_number -= 1
                    getting_shop(choice_number=1)
            elif command_line[command_number] == "10+1回引く(チケットを10枚消費します)":
                if ticket_number-10 < 0:  # お食事券がないとき
                    none_ticket_flag = True
                else:  # お食事券があるとき
                    ticket_number -= 10
                    getting_shop(choice_number=11)
            elif command_line[command_number] == "もどる":
                return 0
            else:
                print("ERR: コマンドがありません")
                exit(-1)

        # 描画
        DrawDisplay.initialDiplay([
            f"######### {gacha_name} #########",
            ""
        ])

        DrawDisplay.initialDiplay(select_description(gacha_name))  # 詳細情報を表示

        DrawDisplay.initialDiplay([f"■□ チケット: {ticket_number}枚"])  # お食事券
        if none_ticket_flag:  # チケットがたりないとき
            DrawDisplay.initialDiplay(["チケットが足りません!!"])
            none_ticket_flag = False  # フラグリセット

        if key in CommandManager.UP:  # 上キー
            command_number -= 1
        if key in CommandManager.DOWN:  # 下キー
            command_number += 1
        elif key in CommandManager.ESC:
            print("Info: ESC終了!(MenuScene, run())")
            exit(0)  # 終了

        #コマンド#
        if command_number < 0:  # 一番上ならば一番下に
            command_number = len(command_line)-1
        elif len(command_line)-1 < command_number:  # 一番下ならば一番上に
            command_number = 0

        DrawDisplay.commandDisplay(command_line, command_number=command_number,
                                   cursol="▶ ", line_end="\n", end="\n")

    return -1  # 異常終了


def run():
    DrawDisplay.clear()  # 画面削除

    # 描画
    DrawDisplay.initialDiplay([
        "######### ガチャ #########",
        ""
    ])

    command_number = 0
    command_line = [
        "基本ガチャ",
        "もどる",
    ]

    DrawDisplay.commandDisplay(command_line, command_number=command_number,
                               cursol="▶ ", line_end="\n", end="\n")

    key = ""
    while True:
        key = CommandManager.CommandManager().pressKey()  # 入力キー取得
        DrawDisplay.clear()  # 画面を消す

        #コマンド操作#
        if key in CommandManager.ENTER:
            if command_line[command_number] == "もどる":
                MenuScene.run()
            else:  # ガチャ
                gacha_description_run(command_line[command_number])  # ガチャの詳細画面

        # 描画
        DrawDisplay.initialDiplay([
            "######### ガチャ #########",
            ""
        ])

        if key in CommandManager.UP:  # 上キー
            command_number -= 1
        if key in CommandManager.DOWN:  # 下キー
            command_number += 1
        elif key in CommandManager.ESC:
            print("Info: ESC終了!(MenuScene, run())")
            exit(0)  # 終了

        #コマンド#
        if command_number < 0:  # 一番上ならば一番下に
            command_number = len(command_line)-1
        elif len(command_line)-1 < command_number:  # 一番下ならば一番上に
            command_number = 0

        DrawDisplay.commandDisplay(command_line, command_number=command_number,
                                   cursol="▶ ", line_end="\n", end="\n")

    return -1  # 異常終了


if __name__ == '__main__':
    run()
