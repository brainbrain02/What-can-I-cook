
import random

class Restaurant:
    def __init__(self, name, foodList):
        self.name = name
        self.foodList = foodList
    
    def randomFoodFromShop(self):
        print(self.name)
        selectedFood = random.choice(self.foodList)
        print(selectedFood)

restList = []

m_shop = Restaurant('麥記', ['麥樂雞', '安格斯牛堡'])
restList.append(m_shop)
mos_shop = Restaurant('Mos Burger', ['照燒牛肉漢堡'])
restList.append(mos_shop)
# new_forest = Restaurant('新森林', ['白汁雞皇飯 皇帝蟹柳沙律 一口蝦多士'])
# restList.append(new_forest)
eight_square = Restaurant('八方雲集', ['10隻 + 豆漿'])
restList.append(eight_square)
itamama = Restaurant('Itamama', ['MaMa Pizza', '三文魚炒飯'])
restList.append(itamama)
subway = Restaurant('Subway', ['Subway Melt'])
restList.append(subway)
eastTai = Restaurant('東泰', ['乾炒牛河'])
restList.append(eastTai)
southJi = Restaurant('南記', ['肥牛肉清湯米綫 + 招牌春捲'])
restList.append(southJi)
gutYeGa = Restaurant('吉野家', ['溫泉蛋牛肉飯'])
restList.append(gutYeGa)
donDonHouse = Restaurant('井井屋', ['大份南蠻雞便當'])
restList.append(donDonHouse)
taiHing = Restaurant('太興', ['叉燒飯'])
restList.append(taiHing)
kfc = Restaurant('KFC', ['家鄉雞'])
restList.append(kfc)
fairwood = Restaurant('大快活', ['粟米肉粒飯', '咖喱牛腩飯', '叉燒飯'])
restList.append(fairwood)
pizzaHut = Restaurant('Pizza Hut', ['Pizza'])
restList.append(pizzaHut)
breadPlace = Restaurant('麵包鋪', ['菠蘿包', '雞尾包', '腸仔包', '辣肉鬆包', '吞拿魚三文治'])
restList.append(breadPlace)


def randomFood():
    selectedShop = random.choice(restList)
    selectedShop.randomFoodFromShop()

def displayRest():
    print('Number of restaurants: ', len(restList))
    for restaurant in restList:
        if restaurant != restList[-1]:
            print(restaurant.name, end=', ')
        else:
            print(restaurant.name)

def main():
    while True:
        randomFood()
        again = input('Do you want to roll again? (y/n)')
        if again == 'n':
            break

if __name__ == '__main__':
    main()
