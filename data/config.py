from environs import Env

# environs kutubxonasidan foydalanish
env = Env()
env.read_env()

# .env fayl ichidan quyidagilarni o'qiymiz
BOT_TOKEN = env.str("BOT_TOKEN")  # Bot token
API_KEY = env.str("API_KEY")  # rapidapi.com dan api olish
EXTRA_API_KEY = env.str("EXTRA_API_KEY")  # rapidapi.com dan qo'shimcha api olish
GROUP_USERNAME = env.str("CHANNEL_USERNAME")  # kanal/guruh linki
GROUP_USERNAME2 = env.str("CHANNEL_USERNAME2")  # kanal/guruh linki
GROUP_USERNAME3 = env.str("CHANNEL_USERNAME3")  # kanal/guruh linki
GROUP_USERNAME4 = env.str("CHANNEL_USERNAME4")  # kanal/guruh linki
ADMINS = env.list("ADMINS")  # adminlar ro'yxati
IP = env.str("ip")  # Xosting ip manzili
