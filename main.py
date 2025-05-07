import logging
import random
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Bot token
TOKEN = "7229115781:AAH9oBXdVhx6FBOsKTX78mHLNz6mXLQNikY"
ADMIN_ID = 123456789  # O'zingizning Telegram ID raqamingizni kiriting

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)

# 200 ta savol ro‘yxati
top_questions = [
    {"savol": "O‘zbekiston poytaxti qaysi shahar?", "javob": "Toshkent", "variantlar": ["Samarqand", "Buxoro", "Toshkent", "Andijon"]},
    {"savol": "Yerning sun’iy yo‘ldoshi nima?", "javob": "Oy", "variantlar": ["Mars", "Oy", "Yupiter", "Venera"]},
    {"savol": "Eng katta okean qaysi?", "javob": "Tinch okeani", "variantlar": ["Atlantika okeani", "Hind okeani", "Tinch okeani", "Shimoliy muz okeani"]},
    {"savol": "Eng katta qit'a qaysi?", "javob": "Osiyo", "variantlar": ["Yevropa", "Afrika", "Osiyo", "Janubiy Amerika"]},
    {"savol": "Dunyodagi eng uzun daryo qaysi?", "javob": "Nil", "variantlar": ["Nil", "Amazonka", "Missisipi", "Volga"]},
    {"savol": "Eng katta cho‘l qaysi?", "javob": "Sahara", "variantlar": ["Sahara", "Gobi", "Kalahari", "Arabiston"]},
    {"savol": "Eng katta orol qaysi?", "javob": "Grenlandiya", "variantlar": ["Madagaskar", "Grenlandiya", "Borneo", "Sumatra"]},
    {"savol": "Dunyodagi eng baland tog‘ qaysi?", "javob": "Everest", "variantlar": ["Everest", "Kilimanjaro", "Elbrus", "K2"]},
    {"savol": "O‘zbekistonda nechta viloyat bor?", "javob": "14", "variantlar": ["12", "14", "16", "13"]},
    {"savol": "Yerning eng ichki qatlami nima deb ataladi?", "javob": "Yadro", "variantlar": ["Qobiq", "Mantiya", "Yadro", "Magma"]},
    {"savol": "O‘zbekiston poytaxti qaysi shahar?", "javob": "Toshkent", "variantlar": ["Samarqand", "Buxoro", "Toshkent", "Andijon"]},
    {"savol": "Yerning sun’iy yo‘ldoshi nima?", "javob": "Oy", "variantlar": ["Mars", "Oy", "Yupiter", "Venera"]},
    {"savol": "Eng katta okean qaysi?", "javob": "Tinch okeani", "variantlar": ["Atlantika okeani", "Hind okeani", "Tinch okeani", "Shimoliy muz okeani"]},
    {"savol": "Eng katta qit'a qaysi?", "javob": "Osiyo", "variantlar": ["Yevropa", "Afrika", "Osiyo", "Janubiy Amerika"]},
    {"savol": "Dunyodagi eng uzun daryo qaysi?", "javob": "Nil", "variantlar": ["Nil", "Amazonka", "Missisipi", "Volga"]},
    {"savol": "Eng katta cho‘l qaysi?", "javob": "Sahara", "variantlar": ["Sahara", "Gobi", "Kalahari", "Arabiston"]},
    {"savol": "Eng katta orol qaysi?", "javob": "Grenlandiya", "variantlar": ["Madagaskar", "Grenlandiya", "Borneo", "Sumatra"]},
    {"savol": "Dunyodagi eng baland tog‘ qaysi?", "javob": "Everest", "variantlar": ["Everest", "Kilimanjaro", "Elbrus", "K2"]},
    {"savol": "O‘zbekistonda nechta viloyat bor?", "javob": "14", "variantlar": ["12", "14", "16", "13"]},
    {"savol": "Yerning eng ichki qatlami nima deb ataladi?", "javob": "Yadro", "variantlar": ["Qobiq", "Mantiya", "Yadro", "Magma"]},
    {"savol": "Futbol to‘pi necha gram og‘irlikda bo‘lishi kerak?", "javob": "410-450", "variantlar": ["350-400", "410-450", "300-350", "500-550"]},
    {"savol": "Basketbol o‘yinida bir jamoada necha kishi bo‘ladi?", "javob": "5", "variantlar": ["4", "5", "6", "7"]},
    {"savol": "Tennis to‘pi qanday rangda bo‘ladi?", "javob": "Sariq", "variantlar": ["Oq", "Yashil", "Sariq", "Ko‘k"]},
    {"savol": "Dunyodagi eng katta stadion qaysi?", "javob": "Rungrado May Day Stadium", "variantlar": ["Maracana Stadium", "Rungrado May Day Stadium", "Camp Nou", "Wembley"]},
    {"savol": "Olimpiya o‘yinlari har nechchi yilda o‘tkaziladi?", "javob": "4", "variantlar": ["2", "3", "4", "5"]},
    {"savol": "Futbol darvozasi eni qancha?", "javob": "7.32 metr", "variantlar": ["6.50 metr", "7.32 metr", "8.00 metr", "7.00 metr"]},
    {"savol": "Shaxtyor sporti qanday sport turi?", "javob": "Shaxmat", "variantlar": ["Boks", "Shaxmat", "Regbi", "Futbol"]},
    {"savol": "Dunyodagi eng tez yuguruvchi hayvon qaysi?", "javob": "Gepard", "variantlar": ["Arslon", "Bo‘ri", "Gepard", "Tulki"]},
    # {"savol": "Qaysi sport turi "qirollar sporti" deb ataladi?", "javob": "Shaxmat", "variantlar": ["Golf", "Tennis", "Shaxmat", "Boks"]},
    # {"savol": "Tennisda "Grand Slam" deganda nimani tushunishadi?", "javob": "4 asosiy turnir yutish", "variantlar": ["3 asosiy turnir", "4 asosiy turnir yutish", "5 asosiy turnir", "6 asosiy turnir"]},
    {"savol": "FIFA Jahon chempionatlari necha yilda bir marta bo‘lib o‘tadi?", "javob": "4", "variantlar": ["2", "3", "4", "5"]},
    {"savol": "O‘zbekistonda futbolning eng mashhur klubi qaysi?", "javob": "Paxtakor", "variantlar": ["Paxtakor", "Bunyodkor", "Nasaf", "Neftchi"]},
    {"savol": "Eng ko‘p Olimpiya oltin medalini qo‘lga kiritgan sportchi kim?", "javob": "Maykl Felps", "variantlar": ["Usayn Bolt", "Maykl Felps", "Muhammad Ali", "Cristiano Ronaldo"]},
    {"savol": "Futbol maydonining uzunligi qancha bo‘lishi kerak?", "javob": "100-110 metr", "variantlar": ["80-90 metr", "100-110 metr", "120-130 metr", "90-100 metr"]},
    {"savol": "Eng katta sayyora qaysi?", "javob": "Yupiter", "variantlar": ["Mars", "Venera", "Yupiter", "Saturn"]},
    {"savol": "Dunyodagi eng uzun daryo qaysi?", "javob": "Nil", "variantlar": ["Nil", "Amazonka", "Missisipi", "Volga"]},
    {"savol": "Eng tez yuguradigan hayvon qaysi?", "javob": "Gepard", "variantlar": ["Arslon", "Gepard", "Tulki", "Burgut"]},
    {"savol": "Suvning qaynash harorati qancha?", "javob": "100°C", "variantlar": ["90°C", "100°C", "110°C", "120°C"]},
    {"savol": "Pifagor teoremasi qaysi shaklga tegishli?", "javob": "Uchburchak", "variantlar": ["Doira", "To‘rtburchak", "Uchburchak", "Trapez"]},
    {"savol": "Eng katta okean qaysi?", "javob": "Tinch okeani", "variantlar": ["Atlantika okeani", "Hind okeani", "Tinch okeani", "Shimoliy muz okeani"]},
    {"savol": "Odam tanasida nechta suyak bor?", "javob": "206", "variantlar": ["200", "206", "210", "250"]},
    {"savol": "Dunyodagi eng katta hayvon qaysi?", "javob": "Ko‘k kit", "variantlar": ["Fil", "Ko‘k kit", "Krokodil", "Jirafa"]},
    {"savol": "Elektr toki o‘lchov birligi qaysi?", "javob": "Amper", "variantlar": ["Volt", "Amper", "Vatt", "Om"]},
    {"savol": "Qaysi sayyora 'Qizil sayyora' deb ataladi?", "javob": "Mars", "variantlar": ["Venera", "Mars", "Merkuriy", "Yupiter"]},
    {"savol": "O‘zbekiston davlat madhiyasi muallifi kim?", "javob": "Abdulla Oripov", "variantlar": ["Erkin Vohidov", "Abdulla Oripov", "Hamid Olimjon", "Alisher Navoiy"]},
    {"savol": "Eng katta qit'a qaysi?", "javob": "Osiyo", "variantlar": ["Yevropa", "Afrika", "Osiyo", "Janubiy Amerika"]},
    {"savol": "O‘zbekistonda nechta viloyat bor?", "javob": "14", "variantlar": ["12", "14", "16", "13"]},
    {"savol": "Eng uzun hayvon qaysi?", "javob": "Ko‘k kit", "variantlar": ["Fil", "Ko‘k kit", "Jirafa", "Pitond"]},
    {"savol": "Dunyodagi eng baland tog‘ qaysi?", "javob": "Everest", "variantlar": ["Everest", "Kilimanjaro", "Elbrus", "K2"]},
    {"savol": "Inson yuragi kuniga necha marta uradi?", "javob": "100,000", "variantlar": ["50,000", "75,000", "100,000", "120,000"]},
    {"savol": "Bosh harfi 'A' bo‘lgan meva?", "javob": "Olma", "variantlar": ["Gilos", "Anor", "Olma", "Shaftoli"]},
    {"savol": "Dunyodagi eng katta cho‘l qaysi?", "javob": "Sahara", "variantlar": ["Gobi", "Sahara", "Kalahari", "Arabiston"]},
    {"savol": "Kunduzning eng qisqa kuni qaysi oyda bo‘ladi?", "javob": "Dekabr", "variantlar": ["Yanvar", "Fevral", "Dekabr", "Mart"]},
    {"savol": "Eng katta metall ishlab chiqaruvchi davlat qaysi?", "javob": "Xitoy", "variantlar": ["Rossiya", "AQSh", "Xitoy", "Germaniya"]},
    {"savol": "5 × 6 nechiga teng?", "javob": "30", "variantlar": ["25", "30", "35", "40"]},
    {"savol": "15 + 27 nechiga teng?", "javob": "42", "variantlar": ["35", "40", "42", "45"]},
    {"savol": "144 ning kvadrat ildizi nechiga teng?", "javob": "12", "variantlar": ["10", "12", "14", "16"]},
    {"savol": "8 × 9 nechiga teng?", "javob": "72", "variantlar": ["64", "72", "81", "90"]},
    {"savol": "81 ÷ 9 nechiga teng?", "javob": "9", "variantlar": ["7", "8", "9", "10"]},
    {"savol": "Bir soatda nechta daqiqa bor?", "javob": "60", "variantlar": ["50", "55", "60", "70"]},
    {"savol": "0 ga bo‘lish mumkinmi?", "javob": "Yo‘q", "variantlar": ["Ha", "Yo‘q", "Ba'zan", "Aniq emas"]},
    {"savol": "3² nechiga teng?", "javob": "9", "variantlar": ["6", "8", "9", "12"]},
    {"savol": "25% bu qaysi kasr shaklida?", "javob": "1/4", "variantlar": ["1/3", "1/4", "1/5", "1/6"]},
    {"savol": "π (Pi) ning taxminiy qiymati qancha?", "javob": "3.14", "variantlar": ["3.12", "3.14", "3.16", "3.18"]},
    {"savol": "To‘g‘ri burchakli uchburchakning ichki burchaklar yig‘indisi nechiga teng?", "javob": "180°", "variantlar": ["90°", "120°", "150°", "180°"]},
    {"savol": "Bir dyuym necha santimetr?", "javob": "2.54", "variantlar": ["2", "2.54", "3", "3.5"]},
    {"savol": "4! (4 faktorial) nechiga teng?", "javob": "24", "variantlar": ["16", "24", "32", "36"]},
    {"savol": "Kvadratning bitta tomoni 5 sm bo‘lsa, yuzasi nechiga teng?", "javob": "25 sm²", "variantlar": ["20 sm²", "25 sm²", "30 sm²", "35 sm²"]},
    {"savol": "Teng yonli uchburchakning necha tomoni teng?", "javob": "2", "variantlar": ["1", "2", "3", "4"]},
    {"savol": "9 × 7 nechiga teng?", "javob": "63", "variantlar": ["54", "56", "63", "70"]},
    {"savol": "Paralelogrammning qarama-qarshi burchaklari qanday?", "javob": "Teng", "variantlar": ["To‘g‘ri", "Teng", "Har xil", "Aniq emas"]},
    {"savol": "Sonni kvadrat qilish nima degani?", "javob": "O‘ziga ko‘paytirish", "variantlar": ["Ikki marta qo‘shish", "O‘ziga ko‘paytirish", "2 ga bo‘lish", "3 ga bo‘lish"]},
    {"savol": "10 ning kubi nechiga teng?", "javob": "1000", "variantlar": ["10", "100", "1000", "10,000"]},
    {"savol": "18 + 24 nechiga teng?", "javob": "42", "variantlar": ["38", "40", "42", "44"]},
    {"savol": "O‘zingiz uxlayotgan vaqtda soat 3:00 bo‘lsa, 1 soatdan keyin soat nechchi bo‘ladi?", "javob": "4:00", "variantlar": ["2:00", "3:00", "4:00", "5:00"]},
    {"savol": "Agar 5 ta tovuq 5 kunda 5 ta tuxum qo‘ysa, 10 ta tovuq 10 kunda nechta tuxum qo‘yadi?", "javob": "10", "variantlar": ["5", "10", "15", "20"]},
    {"savol": "Agar sariq uy yashil uyning yonida bo‘lsa, ko‘k uy qaysi uyning yonida?", "javob": "Yo‘q", "variantlar": ["Sariq", "Qizil", "Yashil", "Yo‘q"]},
    {"savol": "Qaysi oyda 28 kun bor?", "javob": "Hamma oyda", "variantlar": ["Fevral", "Yanvar", "Dekabr", "Hamma oyda"]},
    {"savol": "5 ta sham yoqilgan. 3 tasini o‘chirib qo‘ysak, nechta sham qoladi?", "javob": "3", "variantlar": ["2", "3", "5", "0"]},
    # {"savol": "Qaysi sport turida "ace" termini ishlatiladi?", "javob": "Tennis", "variantlar": ["Boks", "Basketbol", "Tennis", "Shaxmat"]}
    
]

questions = random.sample(top_questions, len(top_questions))

players = {}

@dp.message_handler(commands=['start'])
async def start_game(message: types.Message):
    chat_id = message.chat.id
    players[chat_id] = {"score": 0, "wrong": 0, "current_question": 0}
    await message.answer("🎮 <b>Aqilni Sinov o‘yini boshlandi!</b>\n\n❗ Istalgan vaqtda /stop buyrug‘ini bosib o‘yinni to‘xtatishingiz mumkin.", parse_mode="HTML")
    await ask_question(message)

async def ask_question(message):
    chat_id = message.chat.id
    player = players.get(chat_id)
    
    if player and player["current_question"] < len(questions):
        question_data = questions[player["current_question"]]
        savol = question_data["savol"]
        variantlar = question_data["variantlar"]
        
        keyboard = InlineKeyboardMarkup()
        for variant in variantlar:
            keyboard.add(InlineKeyboardButton(variant, callback_data=variant))
        
        await message.answer(f"❓ <b>{savol}</b>", parse_mode="HTML", reply_markup=keyboard)
    else:
        await show_results(message)

@dp.callback_query_handler(lambda call: True)
async def check_answer(call: types.CallbackQuery):
    chat_id = call.message.chat.id
    player = players.get(chat_id)
    
    if player:
        current_question = player["current_question"]
        correct_answer = questions[current_question]["javob"]
        
        if call.data == correct_answer:
            player["score"] += 1
            response_text = "✅ <b>To‘g‘ri javob!</b> 🎉"
        else:
            player["wrong"] += 1
            response_text = f"❌ <b>Noto‘g‘ri!</b> ✅ To‘g‘ri javob: <b>{correct_answer}</b>"
        
        player["current_question"] += 1
        await call.message.edit_text(response_text, parse_mode="HTML")
        await ask_question(call.message)

@dp.message_handler(commands=['stop'])
async def stop_game(message: types.Message):
    await message.answer("🛑 O‘yin to‘xtatildi!", parse_mode="HTML")
    await show_results(message)

async def show_results(message):
    chat_id = message.chat.id
    player = players.pop(chat_id, None)
    if player:
        total_correct = player["score"]
        total_wrong = player["wrong"]
        result_text = f"🏆 <b>O‘yin tugadi!</b>\n✅ To‘g‘ri javoblar: {total_correct}\n❌ Noto‘g‘ri javoblar: {total_wrong}"
        await message.answer(result_text, parse_mode="HTML")
    
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton("🔄 Qayta o‘ynash", callback_data="restart"))
    keyboard.add(InlineKeyboardButton("🌐 Telegram kanalimiz", url="https://t.me/webstormers"))
    await message.answer("🔄 O‘yinni qayta boshlash uchun tugmani bosing!", reply_markup=keyboard)

@dp.callback_query_handler(lambda call: call.data == "restart")
async def restart_game(call: types.CallbackQuery):
    chat_id = call.message.chat.id
    players.pop(chat_id, None)
    await start_game(call.message)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
