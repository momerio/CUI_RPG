def shop_battle_info(shop_info=None):
    """
    名前技名など取得
    """
    if shop_info == None:
        return {"名前": None, "技名": "", "攻撃力": 0, "HP": 0}
    shop_name = shop_info[1]  # 店名
    shop_waza = [shop_info[-2]]  # 技名(メニュー)

    # 攻撃力
    shop_attack = int(shop_info[-1])  # 攻撃力 (メニュー価格)
    if shop_attack <= 500:  # 最低攻撃力
        shop_attack = 500

    shop_hp = int(shop_info[3][:-1].split("～")[0])  # HP(価格帯)
    return {"店名": shop_name, "技名": shop_waza, "攻撃力": shop_attack, "HP": shop_hp}
