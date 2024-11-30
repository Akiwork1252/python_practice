from IPython.display import clear_output
#==========================================
# 飲料ドリンククラス
class Drink:
    def __init__(self, name, price, stock_count):
        self.name = name
        self.price = price
        self.stock_count = stock_count

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

    def is_zero_stock_count(self):
        return self.stock_count <= 0

    def add_stock_count(self, count):
        self.stock_count += count


#==========================================
# 例外クラス
class NotFoundDrinkException(Exception):
    pass

class NotEnoughMoneyException(Exception):
    pass

class NotEnoughHaveMoneyException(Exception):
    pass

class NotEnoughStockException(Exception):
    pass


#==========================================
# 自販機クラス
# 自販機の中の処理
class VendingMachine:
    # 自販機内の釣銭の初期値
    INIT_CHANCE_MONEY = 1000

    # コンストラクタ
    def __init__(self):
        # 自販機内所持金
        self.total_money = self.INIT_CHANCE_MONEY
        # 投入金額
        self.insert_money = 0
        # 商品リスト
        self.drinks = [
            Drink('Cola', 120, 10),
            Drink('Fanta', 130, 10),
            Drink('Pocari', 140, 10),
        ]

    # 投入金の取得
    def get_insert_money(self):
        return self.insert_money

    # 投入金の設定（publicにしないでaddInsertMoney()メソッドから行うようにする
    # param insert_money 投入金
    def _set_insert_money(self, money):
        self.insert_money = money

    # お金を投入
    # param money 投入金額
    def add_insert_money(self, money):
        if money > 0:
            self._set_insert_money(self.get_insert_money() + money)

    # 購入をキャンセル
    # return 投入金を返す
    def cancel_buy(self):
        ret = self.get_insert_money()
        self._set_insert_money(0)
        return ret

    # 飲料の名前を取得
    # return メニューリスト
    def get_drink_name_list(self):
        return [drink.get_name() for drink in self.drinks]

    # 飲料の名前を取得する(list) 使いやすいようにいくつか同じメソッドを用意する
    # return 飲料の名前リスト
    def get_price_list(self):
        return [drink.get_price() for drink in self.drinks]

    # 値段一蘭の取得
    # return 値段リスト
    def get_price(self, name):
        for drink in self.drinks:
            if drink.get_name() == name:
                return drink.get_price()
        raise NotFoundDrinkException('エラー：指定の飲料が見つかりません')

    # 飲料の種類数を取得
    # return 種類数
    def get_menu_count(self):
        return len(self.drinks)

    # Drinkデータを取得する
    # param name Drinkの名前
    # return Drinkデータ
    def get_drink(self, name):
        for drink in self.drinks:
            if drink.get_name() == name:
                return drink
        raise NotFoundDrinkException('エラー：指定の飲料が見つかりません')

    # 現在の投入金額で購入可能な飲料リスト
    # return 購入可能な飲料リスト
    def get_sale_able_drink_list(self):
            return [drink for drink in self.drinks if not drink.is_zero_stock_count() and drink.get_price() <= self.get_insert_money()]

    # 自販機内の所持金があるか
    # param money 判定金額
    # return true 判定金額分ある
    def is_have_money(self, money):
        return self.total_money >= money

    # 自販機内残高が０か
    # return true=残高ゼロ
    def is_zero_total_money(self):
        return self.total_money == 0

    # 自販機内所持金の増減
    # param money 加算・減算する金額
    # return true=増減成功、false=マイナス　不足で処理しない
    def _add_total_money(self, money):
        if money >= 0:
            self.total_money += money
        elif self.total_money + money >= 0:
            self.total_money += money
            return True
        return False

    # 現在の投入金額で購入できるものはあるか
    # return True =購入可能
    def can_sale_drink(self):
        ret = False
        for drink in self.drinks:
            if drink.get_price() <= self.get_insert_money():
                ret = True
        return ret

    # 現在の投入金額で購入できるか
    # param name 商品名
    # return true 購入可能
    def can_sale_drink_name(self, name):
        try:
            drink = self.get_drink(name)
            return drink.get_price() <= self.get_insert_money()
        except NotFoundDrinkException:
            return False

    # 商品を購入
    # param name 商品名
    # return 釣銭
    def sale_drink(self, name):
        try:
            drink = self.get_drink(name)
            if drink.is_zero_stock_count():
                raise NotEnoughStockException('エラー：商品在庫がありません')
            if self.get_insert_money() < drink.get_price():
                raise NotEnoughMoneyException('エラー：投入金額が不足しています')

            change = self.get_insert_money() - drink.get_price()
            if not self.is_have_money(change):
                raise NotEnoughHaveMoneyException('エラー：お釣りが不足しています')

            self._add_total_money(-change)
            self._add_total_money(drink.get_price())
            drink.add_stock_count(-1)
            self._set_insert_money(0)

            return change
        except NotFoundDrinkException as e:
            print(e)
            return 0

#==========================================
# メインクラス
# ユーザーの行動や表示などを処理
class Main:
    # 自販機インスタンス
    vending_machine = VendingMachine()

    # メインメソッド
    @staticmethod
    def main():
        # 購入がキャンセルされるまでループする
        while True:
            if not Main.insert_money(): # お金の投入（購入キャンセルの場合は以下の処理をしない）
                Main.display_menu() # 商品一蘭
                if Main.buy_drink(): # 購入処理
                    # 購入不可なので自動キャンセル
                    break
            else:
                # 購入キャンセル
                break
            # clear_output(wait=False)



    # お金の投入処理
    @staticmethod
    def insert_money():
        cancel = False

        # 購入金額を入れるまでループ
        while not Main.vending_machine.can_sale_drink():
            num = 0
            loop = True

            while loop:
                try:
                    num = int(input('投入する金額を入力してください。（０でキャンセル）：'))
                    if num > 0:
                        Main.vending_machine.add_insert_money(num)
                        loop = False
                    elif num == 0:
                        ret_money = Main.vending_machine.cancel_buy()
                        print('キャンセルされました。')
                        print(f'返金：{ret_money}円')
                        loop = False
                        cancel = True
                    else:
                        raise ValueError('不正な金額です。')
                except ValueError:
                    print('整数を入力してください。')

            # 購入キャンセルの場合はループを抜ける
            if cancel:
                break

            print(f'現在の投入金額：{Main.vending_machine.get_insert_money()}円')

        return cancel
     # メニュー表示
    @staticmethod
    def display_menu():
        print('='*20)
        print('現在購入できるメニュー')
        print('='*20)

        # 飲料データの取得
        menu = Main.vending_machine.get_sale_able_drink_list()
        if menu:
            for drink in menu:
                print(f'飲料名：{drink.get_name()} 価格：{drink.get_price()} 在庫数：{drink.stock_count}')
        else:
            print('購入できる商品がありません')
        print('='*20)

    # 飲料購入処理
    @staticmethod
    def buy_drink():
        error = True
        buy_name = None
        cancel = False

        while error:
            try:
                buy_name = input('商品名を入力してください')
                if Main.vending_machine.can_sale_drink_name(buy_name):
                    error = False
                else:
                    ret_money = Main.vending_machine.cancel_buy()
                    error = False
                    cancel = True
                    print(f'エラー：『{buy_name}』を購入できませんでいた。')
                    print(f'購入をキャンセルしました。返金：{ret_money}円')
            except NotFoundDrinkException:
                print(f'エラー：『{buy_name}』という商品が見つかりませんでした。')

        if not cancel:
            try:
                ret_money = Main.vending_machine.sale_drink(buy_name) # 商品購入
                print(f'『{buy_name}』を購入しました。')
                print(f'お釣り：{ret_money}円')
            except (NotEnoughMoneyException, NotEnoughHaveMoneyException, NotEnoughStockException) as e:
                print(e)

        return cancel


# エントリーポイント
if __name__ == '__main__':
    Main.main()