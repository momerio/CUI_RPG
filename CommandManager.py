# コマンドを押したり引いたりすることを感知する
"""
参考:
ASCII CODE https://theasciicode.com.ar/ascii-control-characters/escape-ascii-code-27.html
"""

from msvcrt import getch


# キー設定
UP = ["w"]
DOWN = ["s"]
LEFT = ["a"]
RIGHT = ["d"]
ENTER = ["Enter"]
ESC = ["Esc"]


class CommandManager:
    def __init__(self):
        """
        ASCIIコードでKeyを指定
        {ASCII code : 押されたときの名前}
        """

        # コマンドを増やしたいとき増やしてください
        # key: ascii code, value: command name (user definition)
        self.setKey = {
            119: "w",
            115: "s",
            97: "a",
            98: "b",
            100: "d",
            13: "Enter",
            27: "Esc",
        }

    def pressKey(self):
        """
        キーボードを押したときに実行される関数
        @return:
            key name， e.g. [e]キーを押されたときは"e"と返る．
            変数: setKeyで登録されていない場合はNoneが返る．
        """
        key = ord(getch())  # 文字をUnicodeに変換

        if key in self.setKey:
            return self.setKey[key]
        else:
            print("Warning: setKeyで登録されていないキータイプです．(CommandManager.py, pressKey())")
            return None


if __name__ == "__main__":
    print(CommandManager().pressKey())  # pressKeyでinputと同じく止まる．一文字のみのキーを感知する．
