# 迷路作成ファイル

"""
迷路自動生成

↓引用元
https://yottagin.com/?p=1579
"""


import random
# import colorama
# import termcolor


class CreateMaze():
    """ 壁伸ばし方で迷路を作る。"""
    map_index=dict()

    def __init__(self, width, height):
        """ 迷路全体を構成する2次元配列、迷路の外周を壁とし、それ以外を通路とする。"""

        self.PATH = 0
        self.WALL = 1

        self.width = width
        self.height = height
        self.maze = []
        # 壁を作り始める開始ポイントを保持しておくリスト。
        self.lst_cell_start_make_wall = []
        # 迷路は、幅高さ5以上の奇数で生成する。
        if(self.height < 5 or self.width < 5):
            print('at least 5')
            exit()
        if (self.width % 2) == 0:
            self.width += 1
        if (self.height % 2) == 0:
            self.height += 1
        for x in range(0, self.width):
            row = []
            for y in range(0, self.height):
                if (x == 0 or y == 0 or x == self.width-1 or y == self.height - 1):
                    cell = self.WALL
                else:
                    cell = self.PATH
                    # xyとも偶数の場合は、壁を作り始める開始ポイントとして保持。
                    if (x % 2 == 0 and y % 2 == 0):
                        self.lst_cell_start_make_wall.append([x, y])
                row.append(cell)
            self.maze.append(row)
            # スタートとゴールを入れる。
        self.maze[1][1] = 0
        self.maze[width-2][height-2] = 9

    def make_maze(self):
        """ 迷路の配列を作り戻す """
        # 壁の拡張を開始できるセルがなくなるまでループする。
        while self.lst_cell_start_make_wall != []:
            # 開始セルをランダムに取得してリストからは削除。
            x_start, y_start = self.lst_cell_start_make_wall.pop(
                random.randrange(0, len(self.lst_cell_start_make_wall)))
            # 選択候補が通路の場合は壁の拡張を開始する。
            if self.maze[x_start][y_start] == self.PATH:
                # 拡張中の壁情報を保存しておくリスト。
                self.lst_current_wall = []
                self.extend_wall(x_start, y_start)
        return self.maze

    def extend_wall(self, x, y):
        """ 開始位置から壁を2つずつ伸ばす """
        # 壁を伸ばすことのできる方向を決める。通路かつ、その2つ先が現在拡張中の壁ではない。
        lst_direction = []
        if self.maze[x][y-1] == self.PATH and [x, y-2] not in self.lst_current_wall:
            lst_direction.append('up')
        if self.maze[x+1][y] == self.PATH and [x+2, y] not in self.lst_current_wall:
            lst_direction.append('right')
        if self.maze[x][y+1] == self.PATH and [x, y+2] not in self.lst_current_wall:
            lst_direction.append('down')
        if self.maze[x-1][y] == self.PATH and [x-2, y] not in self.lst_current_wall:
            lst_direction.append('left')
        # 壁を伸ばせる方向がある場合
        if lst_direction != []:
            # まずはこの地点を壁にして、拡張中の壁のリストに入れる。
            self.maze[x][y] = self.WALL
            self.lst_current_wall.append([x, y])
            # 伸ばす方向をランダムに決める
            direction = random.choice(lst_direction)
            # 伸ばす2つ先の方向が通路の場合は、既存の壁に到達できていないので、拡張を続ける判断のフラグ。
            contineu_make_wall = False
            # 伸ばした方向を壁にする
            if direction == 'up':
                contineu_make_wall = (self.maze[x][y-2] == self.PATH)
                self.maze[x][y-1] = self.WALL
                self.maze[x][y-2] = self.WALL
                self.lst_current_wall.append([x, y-2])
                if contineu_make_wall:
                    self.extend_wall(x, y-2)
            if direction == 'right':
                contineu_make_wall = (self.maze[x+2][y] == self.PATH)
                self.maze[x+1][y] = self.WALL
                self.maze[x+2][y] = self.WALL
                self.lst_current_wall.append([x+2, y])
                if contineu_make_wall:
                    self.extend_wall(x+2, y)
            if direction == 'down':
                contineu_make_wall = (self.maze[x][y+2] == self.PATH)
                self.maze[x][y+1] = self.WALL
                self.maze[x][y+2] = self.WALL
                self.lst_current_wall.append([x, y+2])
                if contineu_make_wall:
                    self.extend_wall(x, y+2)
            if direction == 'left':
                contineu_make_wall = (self.maze[x-2][y] == self.PATH)
                self.maze[x-1][y] = self.WALL
                self.maze[x-2][y] = self.WALL
                self.lst_current_wall.append([x-2, y])
                if contineu_make_wall:
                    self.extend_wall(x-2, y)
        else:
            previous_point_x, previous_point_y = self.lst_current_wall.pop()
            self.extend_wall(previous_point_x, previous_point_y)

    def print_maze(self):
        """ 迷路を出力"""
        for row in self.maze:
            for cell in row:
                if cell == self.PATH:
                    print(' ', end='')
                elif cell == self.WALL:
                    print('#', end='')
                elif cell == 'S':
                    print('S', end='')
                elif cell == 'G':
                    print('G', end='')
            print()

    def set_enemy(self, enemy_index, number, path_index=0):
        """
        敵をランダム配置する
        @param:
            enemy_index,int : 敵のインデクス番号
            number,int : 敵の数
        """
        number_ = 0
        while True:
            if number < number_:
                break

            random_width = random.randint(0, self.width-1)
            random_height = random.randint(0, self.height-1)

            if self.maze[random_width][random_height] == path_index:  # 通れる場合
                self.maze[random_width][random_height] = enemy_index
                number_ += 1
            else:  # 壁や敵などの場合
                continue


if __name__ == "__main__":
    maze = CreateMaze(21, 21)  # 行列21マス
    maze.make_maze()  # 迷路生成
    maze.print_maze()  # 迷路出力
    maze.set_enemy(2, 10, path_index=0)  # 敵番号2で10体配置
    maze.set_enemy(3, 15, path_index=0)  # 敵番号3で15体配置

    print(maze.maze)  # 迷路番号リスト
