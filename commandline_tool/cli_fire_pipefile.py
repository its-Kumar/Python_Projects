from getpass import getpass

import fire


def login(username=None):
    if username is None:
        username = input("what is your username?\n")
    if username is None:
        print("username is required!")
        return
    pw = getpass("what is your password?\n")
    return username, pw


def scrape_tag(tag="python", query_filter="Votes", max_pages=50, page_size=25):
    base_url = "https://stackoverflow.com/questions/tagged/"
    datas = []
    for p in range(max_pages):
        page_num = p + 1
        url = (
            f"{base_url}{tag}?tab={query_filter}&page={page_num}&page_size={page_size}"
        )
        # datas += extract_data_from_url(url)
        # time.sleep(1.2)
        datas.append(url)
    return datas


class PipeLine(object):
    def __init__(
        self,
    ):
        self.scrape = scrape_tag
        self.login = login


if __name__ == "__main__":
    fire.Fire(PipeLine())
