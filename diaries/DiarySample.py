from diaries.AbstractDiary import AbstractDiary

class DiarySample(AbstractDiary):
    
    def get_date(self):
        return "2022-12-8"

    def get_summary(self):
        return "何もない１日だった"

    def get_author(self):
        return "Sample"