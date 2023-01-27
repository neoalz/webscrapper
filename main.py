from src.db import postgresql
from src.works.One23InkWorks import One23InkWorks
from src.works.PcCanadaworks import PcCanadaWorks
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
    work = PcCanadaWorks()
    work.go_to_ink_toner()
    work = One23InkWorks()
    work.go_to_hp()
    work.get_all_products("hp")
