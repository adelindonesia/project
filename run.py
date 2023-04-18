from Expedia.Expedia import Expedia


with Expedia() as bot:
    bot.land_first_page()
    bot.close_pop_up()
    