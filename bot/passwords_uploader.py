from bot.config import file_location


async def save(clean_pass):
    with open(file_location, "a", encoding="utf-8") as f:
        f.write(f"{clean_pass}\n")