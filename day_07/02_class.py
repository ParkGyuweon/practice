# class는 자료형이고 그 자료형이 어떻게 동작하는지를 묘사하는 설계도이다. 
class Book:
    # 책은 무슨 정보를 가지고 있는가
    """
    제목, 작가, 내용
    """
    # 생성자
    # 이 객체가 존재하기 위해 필요한 정보를 받아 저장하는 메서드
    def __init__(self, title, author, content):
        self.title = title
        self.author = author
        self.content = content

    # 메서드
    # 어떤 객체가 가질 수 있는 기능을 묘사하는 메서드
    def get_info(self):
        return f'title: {self.title}, author: {self.author}'

"""
book_title = ''
booK_author = ''
print(book_title)
print(book_author)
"""

book = Book('파이썬 개론', '귀도 반 로섬', '')
print(book.title)
print(book.author)

class Movive:
    """
    제목, 감독, 런타임
    """
    def __init__(self, title, director, runtime):
        pass

class Account:
    """
    계좌번호, 계좌 종류, 잔액
    """
    def __init__(self, account_num, account_type, balance):
        pass