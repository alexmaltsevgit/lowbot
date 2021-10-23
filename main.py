from dotenv import load_dotenv

import bootstrap.instantiation

if __name__ == '__main__':
    load_dotenv()
    bot = bootstrap.instantiation.instantiate_site()
    bot.init()
    bot.proceed_horses()
