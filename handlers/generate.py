from aiogram import Router, types
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, BufferedInputFile
from aiogram.utils.keyboard import InlineKeyboardBuilder
from config import STYLE
from utils.generate_image import generate_picture
from utils.translate import translate


def style_button():
    builder = InlineKeyboardBuilder()
    for keys in STYLE.keys():
        print(keys)
        builder.button(text=keys, callback_data=keys)

    builder.adjust()
    return builder.as_markup()

class generate_fsm(StatesGroup):
    style = State()
    prompt = State()

generate_router = Router()

@generate_router.message(Command("generate"))
async def start_process_generate(message: types.Message, state: FSMContext):
    await state.set_state(state=generate_fsm.style)
    await message.answer("Выбери стиль", reply_markup=style_button())


@generate_router.callback_query(generate_fsm.style)
async def style_callback(callback: types.callback_query, state: FSMContext):
    await state.update_data(style=callback.data)
    
    await callback.message.edit_text("Напиши промпт")
    await state.set_state(generate_fsm.prompt)

    await callback.answer(f"Выбран стиль: {callback.data}")

@generate_router.message(generate_fsm.prompt)
async def prompt_process(message: types.Message, state: FSMContext):
    prompt = await translate(message.text)
    print(prompt, message.text)
    data = await state.get_data()
    await state.clear()
    
    await message.answer("генерируется")
    try:
        #Типо функция обработки описания
        buffered_photo = BufferedInputFile(await generate_picture(data.get("style"), prompt), filename="photo.png")
        #-------------------------------
        await message.answer_photo(photo = buffered_photo)
    except Exception as e:
        await message.answer(str(e))





