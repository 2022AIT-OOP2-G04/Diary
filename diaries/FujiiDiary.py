from diaries.AbstractDiary import AbstractDiary

class FujiiDiary(AbstractDiary):
    
    def get_date(self):
        return "2022-12-6"

    def get_summary(self):
        return "レポートの作成を行なった。つらかった。"

    def get_author(self):
        return "藤井"