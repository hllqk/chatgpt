#写python一个小游戏

print("欢迎来到英雄联盟！")

name = input("请输入你的名字：")

print("欢迎%s加入英雄联盟！" % name)

hp = 100

print("%s的初始血量为：%d" % (name, hp))

while True:
    print("请选择你要进行的操作：")
    print("1. 吃药 2. 打怪 3. 逃跑")
    oper = input("输入你的选择：")

    if oper == "1":
        hp = hp + 50
        print("%s使用了药水，血量增加50，当前血量为：%d" % (name, hp))
    elif oper == "2":
        hp = hp - 20
        print("%s打怪，血量减少20，当前血量为：%d" % (name, hp))
    elif oper == "3":
        print("%s逃跑了！" % name)
        break
    else:
        print("输入有误，请重新输入！")

    if hp <= 0:
        print("%s血量不足，游戏结束！" % name)
        break

print("游戏结束，欢迎下次再来！")