from diaries.AbstractDiary import AbstractDiary

class MasudaDiary(AbstractDiary):

    def get_date(self):
        return "2022-12-02"

    def get_summary(self):
        return """簡単だった"""

    def get_author(self):
        return "Masuda"