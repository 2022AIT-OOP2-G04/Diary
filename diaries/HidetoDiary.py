from diaries.AbstractDiary import AbstractDiary

class HidetoDiary(AbstractDiary):
    
    def get_date(self):
        return "2023-3-24"

    def get_summary(self):
        return "今日は、新作のゲームを買った。1日中やったので、寝不足になった。"

    def get_author(self):
        return "秀人"