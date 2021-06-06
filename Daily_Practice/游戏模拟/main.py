# -*- coding: UTF-8 -*-
# 微信 : 咕咕咕呼哈
# 手机号 : 15339887672
# 说明 : 在本程序中并没有考虑 在最后输赢取决于单张牌的情况下，若有人最大的牌相同，理应比较第二大的牌，以此类推
#        在这种情况下，本程序只考虑了比较最大牌的大小


import random
import re

style = ['黑桃', '红桃', '梅花', '方块']  # 设置花色
data = ['3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A', '2']  # 设置数字

# 测试数值
# style = ['黑桃', '黑桃', '黑桃', '黑桃']
# data = ['3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A', '2', '0', '1']  # 设置数字

poker = []  # 初始化扑克

for style_mode in style:  # 进行造牌
    for num in data:
        poker.append(''.join([style_mode, num]))

random.shuffle(poker)  # 进行洗牌
# print(poker)

# 初始化五个玩家
player_A = []
player_B = []
player_C = []
player_D = []
player_E = []
players = [player_A, player_B, player_C, player_D, player_E]

# 发牌
prt_poker_count = 3  # 每个人的牌数, 也就是发牌的轮数
while prt_poker_count:
    player_num = 5  # 玩家个数
    i = 0  # 发牌时玩家的轮换
    while player_num:  # 开始发牌
        give_poker = random.choice(poker)  # 随机抽取一张
        if give_poker not in player_A and \
                give_poker not in player_B and \
                give_poker not in player_C and \
                give_poker not in player_D and \
                give_poker not in player_E:  # 牌发下去的前提是这张牌不属于任何人
            players[i].append(give_poker)  # 发牌
            i += 1  # 给下一位玩家发牌
            player_num -= 1
    prt_poker_count -= 1  # 轮数减一

print(players)  # 打印每个人牌的情况

# # 制定比赛规则
# for num, player in enumerate(players, 1):
#     append_num_data = ''
#     append_shape_data = ''
#     for shape in player:
#         append_num_data += shape[2:]  # 取牌号
#         append_shape_data += shape[:1]  # 取花色
#     player.append(append_num_data)
#     player.append(append_shape_data)
# print(players)

# 检查牌的情况
compare = [0, 0, 0, 0]  # 检查各种层次的牌各有几张

for per_player_shape in players:
    # 检验是否为豹子
    if (per_player_shape[0][2:] == per_player_shape[1][2:]) and \
            (per_player_shape[0][2:] == per_player_shape[2][2:]):
        per_player_shape.append(''.join([per_player_shape[0][2:], '豹子']))
        compare[0] += 1
    else:
        per_player_shape.append('')

    # 检查同花顺
    is_not_tong_hua_shun = 1  # 默认它不是顺子 , 采取这样的写法为了避免大量的 else 语句
    if per_player_shape[0][:2] == per_player_shape[1][:2] == per_player_shape[2][:2]:  # 同花
        num_index = [data.index(per_player_shape[i][2:]) for i in range(3)]
        num_index.sort()
        if num_index[0] <= 10:  # 如果牌的位置大于 10+1 = 11 就不可能组成顺子 , 同时也为了避免下方顺子检查造成越界
            if num_index[0] + 1 == num_index[1] and num_index[1] + 1 == num_index[2]:  # 检查是否为顺子
                per_player_shape.append(''.join([str(data[num_index[0]]), '同花顺']))
                is_not_tong_hua_shun = 0
                compare[1] += 1
    if is_not_tong_hua_shun:
        per_player_shape.append('')

    # 检查顺子
    is_not_shun_zi = 1
    num_index = [data.index(per_player_shape[i][2:]) for i in range(3)]
    num_index.sort()  # 将牌面的索引值进行排序
    if num_index[0] <= 10:  # 如果牌的位置大于 10+1 = 11 就不可能组成顺子 , 同时也为了避免下方顺子检查造成越界
        if num_index[0] + 1 == num_index[1] and num_index[1] + 1 == num_index[2]:  # 检查是否为顺子
            per_player_shape.append(''.join([str(data[num_index[0]]), '顺子']))
            compare[2] += 1
    if is_not_shun_zi:
        per_player_shape.append('')

    # 检查对子
    is_not_double = 1  # 假设没有对子
    only_one_double = 1  # 指定最多只能出现一个对子，防止遇到豹子导致后面的索引变乱
    if num_index[0] == num_index[1]:  # 第一张牌是否和第二张牌相同
        per_player_shape.append(''.join([str(data[num_index[0]]), '对子']))
        is_not_double = 0
        only_one_double = 0
        compare[3] += 1
    if is_not_double and only_one_double:  # 保证前面没有出现对子
        if num_index[0] == num_index[2]:  # 第一张牌是否和第三张牌相同
            per_player_shape.append(''.join([str(data[num_index[0]]), '对子']))
            is_not_double = 0
            only_one_double = 0
            compare[3] += 1
    if is_not_double and only_one_double:  # 保证前面没有出现对子
        if num_index[1] == num_index[2]:  # 第二张牌是否和第三张牌相同
            per_player_shape.append(''.join([str(data[num_index[1]]), '对子']))
            is_not_double = 0
            only_one_double = 0
            compare[3] += 1
    if is_not_double:
        per_player_shape.append('')

    # 添加单张
    per_player_shape.append(data[num_index[2]])  # 取出牌面的最大值

print(players)
print(compare)

# 统计情况
player = ["A", "B", "C", "D", "E"]
cmp_data = []
win_data = []
for num, i in enumerate(compare, 3):
    if i != 0:  # 就说明此层有特殊的牌
        cmp_data = [players[j][num] for j in range(5)]  # 就把此层的牌全部拿出来，进行比较
        break  # 既然已经有了特殊的牌，那么之后的再无必要取比较
    if num == 6:  # 走到了最后一步说明此轮比赛并没有特殊的牌出现，所以就只能比较最后牌面的大小了
        cmp_data = [players[j][7] for j in range(5)]  # 取出最后牌面的最大值

print(cmp_data)

# # 生成最后可用的判断结果
# for num, i in enumerate(cmp_data):
#     if i != '':
#         i = re.sub('[^\x00-\xff]', '', i)  # 利用re模块去除汉字
#         win_data.append([num, i])
#
# print(win_data)
#
# # 比较
# cmp_index = []
# for i in win_data:
#     cmp_index.append(data.index(i[1]))
# print(cmp_index)
# max_val_index = max(cmp_index)
# print(max_val_index)

for num, i in enumerate(cmp_data):
    if i != '':
        i = re.sub('[^\x00-\xff]', '', i)  # 利用re模块去除汉字
        val_index = data.index(i)
        win_data.append([num, val_index])  # 找出索引比大小
    else:
        win_data.append([num, -1])  # 将空值置为 -1 ，便于后面的排序
print(win_data)
win_data.sort(key=lambda x: x[1], reverse=True)  # 根据索引的值来比较大小，避免了 2 比 3 小的情况
print(win_data)

# 结果的输出
print("在本局中，最终获得胜利的玩家是 玩家{:}".format(player[win_data[0][0]]))
print("该玩家的牌为{}".format(players[win_data[0][0]][:3]))
