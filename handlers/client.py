from aiogram import types, Dispatcher
from create_bot import bot
from shedule import get_shedule
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from keyboards import kb_client_start, kb_client_days, kb_client_month, kb_client_group

async def command_start(message : types.Message):
    await bot.send_message(message.from_user.id, 'Привет, что хочешь узнать?', reply_markup=kb_client_start)

info_text = 'Для получения информации из плана мероприятий \
нажмите кнопку Расписание. Далее пишем свою \
фамилию(если её указывают в плане) либо выбираем \
свою группу: звук\свет\экран\видео или все(остальные). \
Выбираем месяц, потом начальную дату периода и конечную дату \
периода. Либо выбираем весь месяц или сегодняшнюю дату - \
в этом случае конечную дату выбирать нельзя'

async def command_info(message : types.Message):
    await bot.send_message(message.from_user.id, info_text, reply_markup=kb_client_start)


class FSMClient(StatesGroup):
    name = State()
    month = State()
    startdate = State()
    enddate = State()

#Начало диалога по выборке расписания
async def on_start(message : types.Message):
    await FSMClient.name.set()
    await message.reply('Выбери группу или введи свою Фамилию', reply_markup=kb_client_group)

#Первый ответ - группа или фамилия
async def set_group(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await FSMClient.next()
    await message.reply('Введи месяц', reply_markup=kb_client_month)

#Второй ответ - месяц
async def set_month(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['month'] = message.text
    await FSMClient.next()
    await message.reply('Введи начальную дату', reply_markup=kb_client_days)

#Третий - начальная дата или сегодня
async def set_startdate(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['startdate'] = message.text
    if message.text == "Сегодня" or message.text == 'Весь месяц':
        await bot.send_message(message.from_user.id, get_shedule(data), reply_markup = kb_client_start)
        await state.finish()
    else:
        await FSMClient.next()
        await message.reply('Введи конечную дату', reply_markup=kb_client_days)


#Четвертый ответ - конечная дата
async def set_enddate(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        if data['startdate'] == "Сегодня" or data['startdate'] == 'Весь месяц':
            return
        data['enddate'] = message.text
    await bot.send_message(message.from_user.id, get_shedule(data), reply_markup = kb_client_start)
    await state.finish()




#Блок регистрации хендлеров
def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands = ['start'])
    dp.register_message_handler(command_info, commands = ['Информация', 'help'])
    dp.register_message_handler(on_start, commands = ['Расписание'], state = None)
    dp.register_message_handler(set_group, state = FSMClient.name)
    dp.register_message_handler(set_month, state = FSMClient.month)
    dp.register_message_handler(set_startdate, state = FSMClient.startdate)
    dp.register_message_handler(set_enddate, state = FSMClient.enddate)
