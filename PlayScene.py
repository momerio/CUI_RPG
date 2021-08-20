# 実際にプレイするダンジョンの画面
import CommandManager
import DrawDisplay
import BattleScene
import BattleInfo


class Walking(object):
    """
    >>Walking
    マップ作成と歩く関係のクラス

    >>メンバ変数
        x,y: 現在位置
        map_: マップ 2次元リストで表す
        up,down.left,right: 上下左右の移動を表す『コマンド』
        map_index: マップインデクスを表す辞書の定義
        next_up,next_down,next_left,next_right: 一歩先の上下左右の移動を表す『マップインデクス』(int)
        now_pos_index: 現在位置の状態
        command_draw: コマンド描画
    """

    def __init__(self, initial_x=1, initial_y=1, up="w", down="s", left="a", right="d", my_command_draw=None):

        ##初期位置##
        self.x = initial_x
        self.y = initial_y

        ##上下左右のコマンド定義##
        self.up = up
        self.down = down
        self.left = left
        self.right = right

        #禁止インデクス#
        self.forbidden = list()

        ##コマンドの描画##
        # self.command_draw = f"""
        #         {up}
        #         ↑
        #         w
        #         |
        # {left} ← a - YOU - d → {right}
        #         |
        #         s
        #         ↓
        #         {down}

        # """ if my_command_draw == None else my_command_draw

    def _mapping(self, x, y):

        ##自分のいる位置から上下左右のMAP情報を取得##
        self.next_up = self.map_[self.y-1][self.x]
        self.next_down = self.map_[self.y+1][self.x]
        self.next_left = self.map_[self.y][self.x-1]
        self.next_right = self.map_[self.y][self.x+1]

        result = []
        for pos in [self.next_up, self.next_down, self.next_left, self.next_right]:
            result.extend(self.map_index[pos])

        return result

    def draw_walking(self):

        up, down, left, right = self._mapping(self.x, self.y)

        self.command_draw = f"""
                  {up}
                  ↑
                  w
                  |
        {left} ← a - YOU - d → {right}
                  |
                  s
                  ↓
                  {down}

        """
        print(self.command_draw)

    def _waking_check_in_area(self, x, y):
        length_list = [len(idx) for idx in self.map_]  # マップの最大値を測るリスト
        max_x, max_y = length_list[0], len(length_list)  # マップの最大値

        """
        index外参照を防ぐため，必ずマップの全体1マスを見ないようにしている

        0 <= x <= max_x-1
        とする場合は，必ず移動不可のオブジェクトで周りを囲むこと
        """
        if 1 <= x <= max_x-2 and 1 <= y <= max_y-2:  # MAP内にいるか
            check = True
        else:
            check = False
        return check

    def _walking_forbidden(self, x, y):
        """
        移動禁止かどうか
        """
        if self.map_[y][x] in self.forbidden:
            return True  # 移動禁止

        return False  # 移動可能

    def walk(self, command):

        self.x_, self.y_ = self.x, self.y

        ##移動後代入##
        if command == self.up:
            self.y_ = self.y-1
        elif command == self.down:
            self.y_ = self.y+1
        elif command == self.left:
            self.x_ = self.x-1
        elif command == self.right:
            self.x_ = self.x+1

        if (not self._waking_check_in_area(self.x_, self.y_) or  # 移動後がMAP外だったら
                self._walking_forbidden(self.x_, self.y_)):  # 移動禁止ならば
            # self.x_, self.y_ = self.x, self.y  # 移動せず
            pass  # 移動せず
        else:
            ##移動##
            self.x = self.x_
            self.y = self.y_

        ##移動の表示##
        self.draw_walking()

        ##現在値の番号取得##
        self.now_pos_index = self.map_[self.y][self.x]

    def change_zero_on_myself(self):
        self.map_[self.y][self.x] = 0


def run(maze):
    """
    MAPでの数字の定義は辞書型で表す
        {マップインデクス:表示名}
    """
    walking = Walking()  # マップ関係オブジェクト
    walking.map_ = maze.maze  # マップをオブジェクトに入れる
    walking.map_index = maze.map_index  # MAPインデクス定義をオブジェクトに入れる
    walking.forbidden = [1]  # 移動不可インデクス定義

    command = ""
    DrawDisplay.clear()

    walking.walk(command)
    # DrawDisplay.initialDiplay([f"x:{walking.x} , y:{walking.y}"])
    DrawDisplay.initialDiplay(
        [f"現在は {maze.map_index[walking.now_pos_index]} にいます"])

    while(True):
        command = CommandManager.CommandManager().pressKey()

        DrawDisplay.clear()

        if command in CommandManager.LEFT:
            walking.walk("a")
        elif command in CommandManager.RIGHT:
            walking.walk("d")
        elif command in CommandManager.UP:
            walking.walk("w")
        elif command in CommandManager.DOWN:
            walking.walk("s")
        elif command in CommandManager.ESC:
            exit()
        else:
            DrawDisplay.initialDiplay(["無効なキーです"])
            continue

        # 敵
        if walking.now_pos_index in [2]:
            # 装備情報取得
            personal_data = []
            with open("./data/save_personal.csv", "r", encoding="utf-8") as f:
                for line in f:
                    personal_data.append(line.strip(
                        "\n").replace("\u3000", " ").split(","))
            player_info = BattleInfo.shop_battle_info(
                personal_data[1])  # バトル情報取得

            # 敵情報取得
            enemy_data = []
            with open("./data/shopinfo.csv", "r", encoding="utf-8") as f:
                for line in f:
                    enemy_data.append(line.strip(
                        "\n").replace("\u3000", " ").split(","))
            enemy_info = BattleInfo.shop_battle_info(
                enemy_data[1])

            # バトルシーンへ移動
            BattleScene.run(player_info["店名"],
                            player_info["HP"], player_info["技名"], enemy_info["店名"], enemy_info["HP"])

            command = ""
            DrawDisplay.clear()

            walking.walk(command)

        if (walking._walking_forbidden(walking.x_, walking.y_)):  # 移動できなければ
            DrawDisplay.initialDiplay(["移動できません！"])

        # DrawDisplay.initialDiplay([f"x:{walking.x} , y:{walking.y}"]) #デバッグ:現在位置を表示
        DrawDisplay.initialDiplay(
            [f"現在は {maze.map_index[walking.now_pos_index]} にいます"])


if __name__ == '__main__':
    """迷路生成と定義"""
    import CreateMaze
    maze = CreateMaze.CreateMaze(12, 12)  # 行列
    maze.make_maze()  # 迷路生成
    maze.print_maze()  # 迷路出力
    maze.set_enemy(2, 10, path_index=0)  # 敵番号2で10体配置
    # maze.set_enemy(3, 15, path_index=0)  # 敵番号3で15体配置
    maze.map_index = {0: "床", 1: "壁", 2: "草"}  # MAPインデクス定義

    run(maze=maze)  # 迷路作成オブジェクトを引数に


# if __name__ == '__main__':
#     """
#     MAPは行列で表す

#     正方行列でなくても可
#     3x4，5x5など

#     MAP作成の際の注意
#         必ず移動不可のオブジェクトで周りを囲むこと
#     """
#     # map_ = [
#     #     [1, 1, 1, 1, 1, 1],
#     #     [1, 0, 0, 1, 2, 1],
#     #     [1, 0, 2, 1, 0, 1],
#     #     [1, 0, 0, 0, 2, 1],
#     #     [1, 1, 1, 1, 1, 1],
#     # ]
#     maze = CreateMaze.CreateMaze(12, 12)  # 行列
#     maze.make_maze()  # 迷路生成
#     maze.print_maze()  # 迷路出力
#     maze.set_enemy(2, 10, path_index=0)  # 敵番号2で10体配置
#     # maze.set_enemy(3, 15, path_index=0)  # 敵番号3で15体配置

#     map_=maze.maze

#     """
#     MAPでの数字の定義は辞書型で表す
#         {マップインデクス:表示名}
#     """
#     map_index = {0: "床", 1: "壁", 2: "草"}  # MAPインデクス定義

#     walking = Walking()  # マップ関係オブジェクト
#     walking.map_ = map_  # マップをオブジェクトに入れる
#     walking.map_index = map_index  # MAPインデクス定義をオブジェクトに入れる
#     walking.forbidden = [1]  # 移動不可インデクス定義

#     command = ""

#     walking.walk(command)
#     print(f"x:{walking.x} , y:{walking.y}")
#     print(f"現在は {map_index[walking.now_pos_index]} にいます")

#     while(True):

#         command = CommandManager.CommandManager().pressKey()
#         if command in CommandManager.LEFT:
#             walking.walk("a")
#         elif command in CommandManager.RIGHT:
#             walking.walk("d")
#         elif command in CommandManager.UP:
#             walking.walk("w")
#         elif command in CommandManager.DOWN:
#             walking.walk("s")
#         elif command in CommandManager.ESC:
#             exit()

#         print(f"x:{walking.x} , y:{walking.y}")
#         print(f"現在は {map_index[walking.now_pos_index]} にいます")
