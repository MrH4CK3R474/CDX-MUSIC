from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from DAXXMUSIC import app
from config import BOT_USERNAME

start_txt = """**
✪ 𝚆𝙴𝙻𝙲𝙾𝙼𝙴 𝚃𝙾 𝙾𝚄𝚁 𝙶𝚁𝙾𝚄𝙿 ✪
 
 ➲ ⚡ 𝗝𝗢𝗜𝗡 𝗙𝗔𝗦𝗧 💖 
**"""




@app.on_message(filters.command("group","channel"))
async def start(_, msg):
    buttons = [
        [ 
          InlineKeyboardButton("💞 𝗞𝗜𝗗𝗡𝗔𝗣𝗘 💞", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
        ],
        [
          InlineKeyboardButton("🎃 𝗖𝗢𝗗𝗘𝗫 🎃", url="https://t.me/BWANDARLOK"),
          InlineKeyboardButton("🎃  𝗕𝗔𝗪𝗔𝗡𝗗𝗔𝗥𝗟𝗢𝗞 🎃", url="https://t.me/jarvis2O"),
          ],
               [
                InlineKeyboardButton("🎃 𝗨𝗣𝗗𝗔𝗧𝗘 🎃", url="https://t.me/BOT_WORLD"),

],
             [
              InlineKeyboardButton("🎃 𝗠𝗜𝗟𝗞𝗬 𝗪𝗔𝗬 🎃", url=f"https://MILKY_WAY_45"),
             ],
              [
               InlineKeyboardButton("🎃 𝗢𝗫𝗬 𝗦𝗧𝗢𝗥𝗘 🎃", url=f"https://t.me/OXY474_STORE"),
              ],
               [
                InlineKeyboardButton("🎃 𝗢𝗣 𝗖𝗗𝗫 🎃", url="https://t.me/OP_CODEX"),

        ]
    ]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://te.legra.ph/file/13bff2addf14807e934ee.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )
@app.on_message(filters.command("group", prefixes="#"))
@capture_err
async def repo(_, message):
    async with httpx.AsyncClient() as client:
        response = await client.get("https://t.me/TEAM_CDX")
    
    if response.status_code == 200:
        users = response.json()
        list_of_users = ""
        count = 1
        for user in users:
            list_of_users += f"{count}. [{user['login']}]({user['html_url']})\n"
            count += 1

        text = f"""[CHANNEL](https://t.me/OP_CODEX) | [𝖦𝖱𝖮𝖴𝖯](https://t.me/TEAM_CDX)
| 𝖢𝖮𝖭𝖳𝖱𝖨𝖡𝖴𝖳𝖮𝖱𝖲 |
----------------
{list_of_users}"""
        await app.send_message(message.chat.id, text=text, disable_web_page_preview=True)
    else:
        await app.send_message(message.chat.id, text="Failed to fetch contributors.")
