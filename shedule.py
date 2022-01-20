import docx

doc = docx.Document(r'c:\users\admin\Desktop\Telegram_bot\Plan.docx')

def get_shedule(dic):
    name = dic['name']
    if name.lower() == 'все':
        name = ''
    startdate = dic['startdate']
    enddate = dic['enddate']
    month = dic['month']

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
