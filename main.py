from src.db import postgresql
from src.works.StaplesWorks import StaplesWorks

if __name__ == '__main__':
    work = StaplesWorks()
    work.get_samsung_products()
    work.get_hp_products()
    work.get_staples_products()
    work.get_brother_products()
    work.get_canon_products()
    work.get_epson_products()
    work.get_fuzion_products()
    work.get_lexmark_products()


