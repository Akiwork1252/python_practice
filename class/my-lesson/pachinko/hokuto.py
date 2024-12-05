import random

# CR北斗の拳:
# (通常時の大当り確率): 1/349, (初当たり出玉): +300(80%) or +1500(20%),
# (確率変動突入率): 100%, (確率変動時の大当り確率): 当たり:1/40, 転落:1/150,
# (確率変動時の出玉振り分け): +300(25%) or +1500(75%),

# 抽選（通常時）
def lottery():
    probability_of_winning = 349  # 大当り確率
    n = random.randint(1, probability_of_winning)  # パチンコ台の乱数
    user = random.randint(1, probability_of_winning)  # ユーザーの乱数
    # ユーザー乱数＝パチンコ台乱数 >> 大当り
    if user == n:
        # 20%でビッグボーナス (+1500玉）
        if user <= (probability_of_winning * 0.2):
            big_bonus = 1500
            print('***BIG BONUS(+1500玉)ゲット*** >>> 確率変動突入!')
            return big_bonus
        else:
            bonus = 300
            print('***BONUS(+300玉)ゲット*** >>> 確率変動突入!')
            return bonus
    else:
        print('-', end='')
        return None

# 抽選（確率変動時） 大当り(1/40)転落(1/150)どちらか引くまで確率変動ループ
def lottery_bonus():
    winning = 40  # 大当り確率
    losing = 150  # 転落確率
    n_winning = random.randint(1, winning)  # パチンコ台の大当り乱数
    n_losing = random.randint(1, losing)  # パチンコ台の転落乱数
    user = random.randint(1, winning)  # ユーザーの乱数
    # ユーザー乱数＝パチンコ台当たり乱数 >> 大当り
    if user == n_winning:
        # 75%がビッグボーナス
        if user <= (winning * 0.75):
            big_bonus = 1500
            input('*BIG BONUS(+1500玉)* を引きました。>>> 確率変動継続! Enterキーを押してください。')
            return big_bonus
        else:
            bonus = 300
            input('*BONUS(+300玉)* を引きました。>>> 確率変動継続! Enterキーを押してください。')
            return bonus
    # ユーザー乱数＝パチンコ台転落乱数 >> 通常に転落
    elif user == n_losing:
        print(f'ハズレを引きました。確率変動を終了します。')
        end = 'end'
        return end
    else:
        print('-', end='')
        return None
