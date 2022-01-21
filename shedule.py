import docx
from datetime import datetime



monthdict = {'январь': '1_январь.docx',
             'февраль': '2_февраль.docx',
             'март': '',
             'апрель': '',
             'май':'',
             'июнь':'',
             'июль':'',
             'август':'',
             'сентябрь':'',
             'октябрь':'',
             'ноябрь':'',
             'декабрь':''
             }

def get_shedule(dic):

#обработка введенной группы
    name = dic['name']
    if name.lower() == 'все':
        name = ''

#обработка периода дат выборки
    startdate = dic['startdate']
    if startdate == 'Весь месяц':
        startdate = '01'
        enddate = '31'
    elif startdate == 'Сегодня':
        startdate = str(datetime.now().day)
        enddate = startdate
    else:
        enddate = dic['enddate']
    if not startdate.isdigit() or not enddate.isdigit():
        return 'Введите дату числами с клавиатуры!'
    if int(startdate) > int(enddate):
        return 'конечная дата периода раньше начальной'

#обработка месяца = выбор нужного файла
    month = dic['month'].lower()
    if month in monthdict.keys():
        docpath = 'c:\\users\\admin\\Desktop\\Telegram_bot\\'
        doc = docx.Document(docpath + monthdict[month])
    else:
        return 'Введите месяц с клавиатуры'
#основной поиск
    table = doc.tables[0]

    arr = []
    for j in range(1,len(table.rows)):
        string = ''
        currentdate = table.rows[j].cells[0].text.split()[0]
        currentdate = '0'+ currentdate if len(currentdate) == 1 else currentdate
        if startdate <= currentdate <= enddate:
            for i in range(6):
                string += table.rows[j].cells[i].text +'\n'
            if name.lower() in string.lower():
                arr.append(string)
    c = '\n\n'.join(arr)

    if c == '':
        c = 'Ничего не найдено'


    return c
