def spisok_first():
    print("Добро пожаловать в игру!")
    print("Выберите действие:")
    print("1. Начать игру")
    print("2. Выйти из игры")
    print("3. Справка об игре")

def spisok2_one():
    print("Ты находишься в загадочном замке и тебе нужно выбрать\nправильные действия, чтобы выбраться оттуда живым. Вот твои варианты:")
    print("1. Войти в темную комнату")
    print("2. Открыть старую дверь или идти вниз по крутой лестнице?")
    print("3. Пойти через запертую железную дверь или пролезть через узкую трубу?")

def spisok3_one():
    print("Ты вошел в темную комнату. Перед тобой несколько дверей.\n На одной из них написано «Рай» на другой «Ад». Что выберешь?")
    print("1. Дверь Рай")
    print("2. Дверь Ад")

def spisok3_two():
    print("Открыв старую деревянную дверь и спустившись вниз\nпо крутой лестнице, перед тобой предстает выбор в виду двух дверей:")
    print("1. Спутиться в подземный мир")
    print("2. Новый китайский автомобиль OMODA C5 в нищенской комплектации")

def spisok3_three():
    print("После того, как ты прошел через железную дверь и пролез через узкую трубу, перед тобой:")
    print("1. Инновационный костюм железного человека")
    print("2. Стать Стивом Джобсом")
    print("Что выберешь?")

def spisok4_one_one():
    print("Открыв дверь, перед тобой оказалась большая лестница, \nведущая к большому величественному трону, на которой восседало что-то похожее на человека,\nно более больших размеров. «Оно» говорит тебе, ты обрел вечный покой")
    

def spisok4_one_two():
    print("Открыв дверь в \"АД\" из нее выливается раскаленная лава и ты сгораешь заживо..")

def spisok4_two_one():
    print("Ты выбрал спуститься в подземный мир. При входе в мир, стоит раскидистый дуб,\nа на нем написанно, что ты лягушка. шикарный конец АХХА")

def spisok4_two_two():
    print("Ты выбрал новое чудо китайского автомобилестроения,\nдо встречи в автосервисе через 5.000км со сгоревшей проводкой)")

def spisok4_three_one():
    what = "инновационный"
    who = "человека"
    message = f"Ты выбрал {what} костюм железного {who}. Теперь тебе не страшны *кхм* от твоей мамы, за то, что ты забыл купить гречку"
    print (message.upper())

def spisok4_three_two():
    print("Ты выбрал стать Стивом Джобсом. Какой жизненный путь ты выберешь")
    vibor = {"1. Создать компанию Apple", "2. Устроиться работать в мак"}
    print(vibor)

def one_one_two():
    print("Ты выбрал Вернуться в самое начало")

def three_two_one():
    print("Ты выбрал создать компанию Apple. Что ты хочешь выпускать под этим брендом?")
    stive = {"1": "1. Выпускать технику", "2":"2. Выпускать автомобили"}
    print(stive["1"])
    print(stive["2"])

def three_two_two():
    print("Ты выбрал устроиться Макдоналдс. Теперь ты сдохнешь в одиночестве,\nпотому что второй половинки, работая в маке ты не найдешь лол")

def three_two_one_one():
    print("Ты выбрал выпускать технику. В будущем твоя компания перерастет в\nцелую корпорацию, а ты станешь мультимиллиардером. У тебя будут:")
    chtobudet = ["деньги","тачки","админки"]
    print(chtobudet[1])

def three_two_one_two():
    print("Ты выбрал выпускать автомобили. А как мы все знаем,\nотчественный автопром - это кринж, поэтому твоя компания будет приносить\nтебе копейки и ты сдохнешь от бедности")


spisok_first()
first = input()

if first == "1":
    spisok2_one()
    two = input()
    if two == "1":
        spisok3_one()
        three = input()
        if three == "1":
            spisok4_one_one()
            six = input()
        elif three == "2":
            spisok4_one_two()
            seven = input()
    elif two == "2":
        spisok3_two()
        four = input()
        if four == "1":
            spisok4_two_one()
            eight = input()
        elif four == "2":
            spisok4_two_two()
            nine = input()
    elif two == "3":
        spisok3_three()
        five = input()
        if five == "1":
            spisok4_three_one()
            ten = input()
        elif five == "2":
            spisok4_three_two()
            eleven = input()
        if eleven == "1":
            three_two_one()
            twelv = input()
        elif eleven == "2":
            three_two_two()
            thirteen = input()
    elif thirteen == "1":
        three_two_one_one()
        fourteen = input()
    elif thirteen == "2":
        three_two_one_two()
        fifteen = input()
    elif six == "2":
        spisok_first()
    if twelv == "1":
        three_two_one_one()
    elif twelv == "2":
        three_two_one_two()
elif first == "2":
    print("Вы вышли из игры, до свидания")
elif first == "3":
    print("Игра была выполнена студентом группы П50-3-22. По содержанию не обеспокоены, кал получился АХХА")
