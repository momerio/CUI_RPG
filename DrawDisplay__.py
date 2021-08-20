# ディスプレイする方法とかを記したファイル
# クラスVer


class DrawDisplay:
    def __init__(self):
        pass

    # 諦観
    # def depth(self, k):
    #     # print(k)
    #     if not k:
    #         print("not k", k)
    #         return 0
    #     else:
    #         if isinstance(k, list):
    #             # print(k,end="")
    #             print()
    #             # return 1 + max(self.depth(i) for i in k)
    #             # print([self.depth(i) for i in k])
    #             return max(self.depth(i) for i in k)
    #         else:
    #             print(k, end="")
    #             return k

    # def initialDiplay(self, disp_data, end="\n", line_end="\n"):
    #     """
    #     初期部分を表示

    #     @param
    #         dips_data,list          : 表示するデータ
    #         end,str,default='\n'    : 最後に出力する文字列
    #     """
    #     for line in disp_data:
    #         print(line, end=end)

    #     print(end=line_end)  # 最後に出力するもの

    # def commandDisplay(self, disp_data, end="\n", line_end="\n"):
    #     """
    #     画面描画のコマンド部分
    #     """
    #     self.cursol = "▶ "
    #     self.command_number = 0

    #     for command_num, line in enumerate(disp_data):
    #         if command_num == self.command_number:
    #             print("{}{}".format(self.cursol, line))
    #         else:
    #             print(line)

    #     print(end=line_end)  # 最後に出力するもの

    end = "\n"
    line_end = ""
    initials = [""]
    commands = [""]
    cursol = "▶ "
    command_number = 0

    def initialDiplay(self):
        """
        初期部分を表示
        """
        for line in self.initials:
            print(line, end=self.end)

        print(end=self.line_end)  # 最後に出力するもの

    def commandDisplay(self):
        """
        画面描画のコマンド部分
        """

        for command_num, line in enumerate(self.commands):
            if command_num == self.command_number:
                print("{}{}".format(self.cursol, line))
            else:
                print(line)

        print(end=self.line_end)  # 最後に出力するもの


if __name__ == '__main__':
    drawDisplay = DrawDisplay()

    drawDisplay.initials = ["========= START ==========", "DEMO RPG!"]
    drawDisplay.commands = ["command A", "command B", "command C"]

    drawDisplay.cursol = "▶ "
    drawDisplay.command_number = 1
    drawDisplay.line_end = "\n"

    drawDisplay.initialDiplay()
    drawDisplay.commandDisplay()
