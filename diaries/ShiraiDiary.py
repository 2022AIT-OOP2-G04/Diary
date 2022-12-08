from diaries.AbstractDiary import AbstractDiary

class ShiraiDiary(AbstractDiary):
    
    def get_date(self):
        return "2022-12-9"

    def get_summary(self):
        return "課題が大変な1日だった。"

    def get_author(self):
        return "しらい"