#!/usr/bin/python
import pywikibot
from pywikibot import pagegenerators, User, Site
from pywikibot.bot import ExistingPageBot
import typing
import time
from datetime import datetime
MAX_WINDOW_MIN = 10
MILLISEC_PER_SEC= 100
SEC_PER_MIN = 60

class OnlineBot(ExistingPageBot):

    update_options = {
        'text': 'away',
        'summary': '(minor) changing status'
    }

    def treat_page(self) -> None:
        # Get timestamp of user's last edit
        timestamp:float = 0
        user = User(Site(), "Orcanami")
        for page, oldid, ts, comment in user.contributions():
            timestamp = ts.timestamp()
            break
        text:str = self.current_page.text
        time_diff:float = time.mktime(time.gmtime()) - timestamp
        print("TIME DIFF:", time_diff)
        if text.lower() == "online" and time_diff > SEC_PER_MIN * MILLISEC_PER_SEC * MAX_WINDOW_MIN:
            new_text:str = "away"
            self.put_current(new_text, summary=self.opt.summary)
        elif text.lower() != "online" and time_diff < SEC_PER_MIN * MILLISEC_PER_SEC * MAX_WINDOW_MIN:
            new_text:str = "online"
            self.put_current(new_text, summary=self.opt.summary)


def main():
    """Parse command line arguments and invoke bot."""
    options = {}
    gen_factory = pagegenerators.GeneratorFactory()
    # Option parsing
    local_args = pywikibot.handle_args()  # global options
    local_args = gen_factory.handle_args(local_args)  # generators options
    for arg in local_args:
        opt, sep, value = arg.partition(':')
        if opt in ('-summary', '-text'):
            options[opt[1:]] = value
    OnlineBot(generator=gen_factory.getCombinedGenerator(), **options).run()

if __name__ == '__main__':
    main()

