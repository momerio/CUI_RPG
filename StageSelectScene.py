# ステージ選択画面

#ユーザ定義#
import DrawDisplay
import CommandManager
import PlayScene
import CreateMaze


def run():
    DrawDisplay.clear()  # 画面削除

    # 描画
    DrawDisplay.initialDiplay([
        "######### ステージ選択 #########",
        ""
    ])

    command_number = 0
    command_line = [
        """草原""",
        """洞窟""",

    ]+["""もどる"""]

    DrawDisplay.commandDisplay(command_line, command_number=command_number,
                               cursol="▶ ", line_end="\n", end="\n")

    key = ""
    while True:
        key = CommandManager.CommandManager().pressKey()  # 入力キー取得
        DrawDisplay.clear()  # 画面を消す

        #コマンド操作#
        if key in CommandManager.ENTER:
            print(command_number)
            if command_line[command_number] == "草原":
                maze = CreateMaze.CreateMaze(12, 12)  # 行列
                maze.make_maze()  # 迷路生成
                # maze.print_maze()  # 迷路出力
                maze.set_enemy(2, number=10, path_index=0)  # 敵番号2で10体配置
                maze.set_enemy(3, number=30, path_index=0)  # 草30配置
                maze.map_index = {0: "床", 1: "壁", 2: "敵", 3: "草"}  # MAPインデクス定義
                PlayScene.run(maze=maze)  # 迷路作成オブジェクトを引数に
            elif command_line[command_number] == "洞窟":
                maze = CreateMaze.CreateMaze(12, 40)  # 行列
                maze.make_maze()  # 迷路生成
                # maze.print_maze()  # 迷路出力
                maze.set_enemy(2, number=40, path_index=0)  # 敵番号2で10体配置
                maze.set_enemy(3, number=80, path_index=0)  #
                maze.map_index = {0: "床", 1: "壁", 2: "敵", 3: "石"}  # MAPインデクス定義
                PlayScene.run(maze=maze)  # 迷路作成オブジェクトを引数に
            # elif command_line[command_number] == "Hot Pepper 大海原":
            #     maze = CreateMaze.CreateMaze(60, 60)  # 行列
            #     maze.make_maze()  # 迷路生成
            #     maze.print_maze()  # 迷路出力
            #     maze.set_enemy(2, number=100, path_index=0)  # 敵番号2で10体配置
            #     maze.set_enemy(3, number=100, path_index=0)  #
            #     maze.map_index = {0: "海上", 1: "壁",
            #                       2: "敵", 3: "中ボス"}  # MAPインデクス定義
            #     PlayScene.run(maze=maze)  # 迷路作成オブジェクトを引数に
            elif command_line[command_number] == "もどる":
                return 0

        # 描画
        DrawDisplay.initialDiplay([
            "######### ステージ選択 #########",
            ""
        ])

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

    return 1  # 異常終了


if __name__ == '__main__':
    run()
