from diaries.AbstractDiary import AbstractDiary

class SasakiDiary(AbstractDiary):
    
    def get_date(self):
        return "2022-12-15"

    def get_summary(self):
        return "課題が終わった"

    def get_author(self):
        return "ささき"