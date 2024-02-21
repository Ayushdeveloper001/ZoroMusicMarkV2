from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID", "25981659"))
API_HASH = getenv("API_HASH", "3ba34b5488b1286c99bebdcae6daf75d")

BOT_TOKEN = getenv("BOT_TOKEN", "7101578630:AAEieG64jTu8_ZCShuuJvdThseuGnM9-m5c")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID"))

PING_IMG = getenv("PING_IMG", "https://te.legra.ph/file/6f99c49bdb4679acad717.jpg")
START_IMG = getenv("START_IMG", "https://te.legra.ph/file/f8ba75bdbb9931cbc8229.jpg")

SESSION = getenv("SESSION", "BAGMctsAi12RNp_-feb-bUop3xlNBfVaEzgK9FFNtZBfOaUW51dSBa35WKXHsvVrO5pG-TvsLpYs8WZDZ2rIrIL1UjE_zFrgJlonWWxWlzJes0HKhF3OdPQapB8vqMQVyXPMlvn3Q6dKr7wSWeY0CbTKjRmvRbZJMsNGkgBAKPc6mgbsHpLR2k-YdBxqKr6CTtbgkvEKNfHA-_QyvJzKCeL0Gk1U8Dq95atzhBEmodM46DwSg4196_9XuGZxdp_aC61m4jp139gZd_DX0U10VYRww-9enodkig9BdLMuROByKNiN4CVFTzl75re9V6i4Pdx30f19EdOg0Agyfcos6DLsQleINQAAAAFFZleeAA")

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/KawaiiAnimeChat")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/kawaiipos")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6993238295").split()))


FAILED = "https://te.legra.ph/file/4c896584b592593c00aa8.jpg"
