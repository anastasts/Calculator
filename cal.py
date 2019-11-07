import telebot

def inside_br(inp):
    while '^' in inp:
        x = inp.index('^')
        inp[x] = inp[x-1]**inp[x+1]
        inp.pop(x+1)
        inp.pop(x-1)
    while '*' in inp:
        x = inp.index('*')
        inp[x] = inp[x - 1] * inp[x + 1]
        inp.pop(x + 1)
        inp.pop(x - 1)
    while '/' in inp:
        x = inp.index('/')
        inp[x] = inp[x-1]/inp[x+1]
        inp.pop(x+1)
        inp.pop(x-1)
    while '+' in inp:
        x = inp.index('+')
        inp[x] = inp[x-1]+inp[x+1]
        inp.pop(x+1)
        inp.pop(x-1)
    while '-' in inp:
        x = inp.index('-')
        inp[x] = inp[x-1]-inp[x+1]
        inp.pop(x+1)
        inp.pop(x-1)
    return inp[0]


def recur(a):
    while '(' in a:
        start=a.index('(')
        count=1
        index=start
        while count!=0:
            index += 1
            if a[index]=='(':
                count+=1
            if a[index]==')':
                count-=1
        res = recur(a[start + 1:index+1])
        del a[start:index + 1]
        a.insert(start, res)
    print('calculating', a)
    return inside_br(a)

def func(a):
    while len(a) > 1:
        a[0] = a[0]+a[1]
        a.pop(1)
    return float(a[0])

def program(a):
    a = list(a)
    print(a)
    k = {'0', '1', '2', '3', '4', '5','6','7','8','9', '+', '-','*','/', '^','(',')'}
    k1 = {'+', '-', '*', '/', '^','(',')'}
    i = 0
    while i < len(a):
        if a[i] not in k:
            a.pop(i)
        else:
            i += 1
    #print(a)
    if len(a)==0:
        return('Пожалуйста, введите выражение! Я готов считать.')
    x = -1
    i = x
    while x < len(a)-1:
        while a[i + 1] not in k1:
            i += 1
            if i >= len(a) - 1:
                break
        if (i-x) > 0: #если между двумя знаками что то есть то вызываем функцию
            res = func(a[x + 1:i + 1])
            del a[x + 1:i + 1]
            a.insert(x + 1, res) #что.куда (сразу после знака)
            x += 2 #перешагиваем через знак на котором были и через число
            i = x #идем от знака
        else:
            x += 1
            i = x
    #print(a)
    a=recur(a)
    return str(a)

bot = telebot.TeleBot('896427595:AAGzSD9zlj-Xd67eBg-qk2HiZHcOy3AsE1c')

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.send_message(chat_id=message.chat.id, text='Ваш результат: '+ program(message.text))

bot.polling()
