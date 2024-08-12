import os

cmndlist = ["wgi", "wgun", "wgup", "wg", "wgsh", "wgsr"] #Список команд
cmnddescr = {"wgi": "install programm", "wgun": "uninstall programm", "wgup": "upgrade programm", "wg": "extra commands", "wgsh": "shows info about a programm", "wgsr": "find and show basic info of programms"} #Словарь содержащий описание команд
extrcmndlist = ["-e", "-faq", "-v", "-l"]
extrcmnddesc = {"-e": "exit the programm", "-faq": "introduction", "-v": "version of the original tool", "-l": "display installed programms"}

#Извлекает запрашиваемую утилиту
def get_prompt() -> str:
    global action
    try:
        prompt = action.split()[1]
    except IndexError:
        prompt = ""
    finally:
        return str(prompt)

#Получает запрос на установку
def install() -> None:
    os.system(f'cmd /c "winget install {get_prompt()}"') #Ввод в командную строку

#Получает запрос на удаление
def uninstall() -> None:
    os.system(f'cmd /c "winget uninstall {get_prompt()}"') #Ввод в командную строку

#Получает запрос на обновление
def upgrade() -> None:
    os.system(f'cmd /c "winget upgrade {get_prompt()}"') #Ввод в командную строку

#Получает запрос на показ версии утилиты
def extracommandversion() -> None:
    os.system(f'cmd /c "winget -v"') #Ввод в командную строку

#Получает запрос на показ списка установленных программ
def list() -> None:
    os.system(f'cmd /c "winget list"') #Ввод в командную строку

#Получает запрос на показ информации о программе
def show() -> None:
    os.system(f'cmd /c "winget show {get_prompt()}"') #Ввод в командную строку

#Получает запрос на поиск программы
def search() -> None:
    os.system(f'cmd /c "winget search {get_prompt()}"') #Ввод в командную строку

print('Welcome to winget helper utility! "wg -faq" for introduction!')

#Главный цикл выполнения утилиты
while True:

    action = input("> ") #Ввод действия пользователем

    #Проверка на наличие аргументов
    if get_prompt() == "":
        print("Error: no prompt found!")
        continue

    #Проверка на правильность команды
    if cmndlist[0] in action:
        install()
        continue
    elif cmndlist[1] in action:
        uninstall()
        continue
    elif cmndlist[2] in action:
        upgrade()
        continue
    elif cmndlist[4] in action:
        show()
        continue
    elif cmndlist[5] in action:
        search()
        continue
    elif cmndlist[3] in action:
        pass
    else:
        print("Error: incorrect action!")
        continue

    if get_prompt() == extrcmndlist[0]:
        input("To stop the programm press ENTER... ")
        quit()
    if get_prompt() == extrcmndlist[1]: #Вступление
        print("===================================================================================================================")
        print("This utility was made for command winget to make it more easier and faster to use!")
        print("")
        print("Example: [command] [programm]")
        print("")
        print("Here is command list for you:")
        for command in cmndlist:
            print(f"    {command} - {cmnddescr.get(command)}")
        print("")
        print("And some extra commands:")
        for extra in extrcmndlist:
            print(f"    {extra} - {extrcmnddesc.get(extra)}")
        print("===================================================================================================================")
        continue
    if get_prompt() == extrcmndlist[2]:
        extracommandversion()
    if get_prompt() == extrcmndlist[3]:
        list()
    else:
        print("Error: incorrect prompt!")
        continue
