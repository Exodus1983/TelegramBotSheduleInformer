from aiogram import types, Dispatcher
from create_bot import bot
from shedule import get_shedule
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup


class FSMClient(StatesGroup):
    name = State()
    month = State()
    startdate = State()
    enddate = State()

#Начало диалога по выборке расписания

async def on_start(message : types.Message):
    await FSMClient.name.set()
    await message.reply('Выбери группу или введи свою Фамилию')

#Первый ответ - группа или фамилия

async def set_group(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await FSMClient.next()
    await message.reply('Введи месяц')

#Второй ответ - месяц

async def set_month(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['month'] = message.text
    await FSMClient.next()
    await message.reply('Введи начальную дату')

#Третий - начальная дата

async def set_startdate(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['startdate'] = message.text
    await FSMClient.next()
    await message.reply('Введи конечную дату')

#Четвертый ответ - конечная дата

async def set_enddate(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['enddate'] = message.text
    await bot.send_message(message.from_user.id, get_shedule(data))
    await state.finish()



async def command_start(message : types.Message):
    await bot.send_message(message.from_user.id, 'Привет, что хочешь узнать?')



def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands = ['start', 'help'])
    dp.register_message_handler(on_start, commands = ['Расписание'], state = None)
    dp.register_message_handler(set_group, state = FSMClient.name)
    dp.register_message_handler(set_month, state = FSMClient.month)
    dp.register_message_handler(set_startdate, state = FSMClient.startdate)
    dp.register_message_handler(set_enddate, state = FSMClient.enddate)
