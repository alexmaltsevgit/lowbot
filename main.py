from dotenv import load_dotenv

import bootstrap.instantiation

if __name__ == '__main__':
    load_dotenv()
    site = bootstrap.instantiation.instantiate_site()
    site.init()
