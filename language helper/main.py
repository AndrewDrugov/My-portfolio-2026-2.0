import db

class Language_Assist:
    def start(self):
        while True:
            print('1. Добавит новое слово')
            print('2. Начать викторину')
            print("3. Выйти")
            anwser = input('Выберите дейвствие ').lower().strip()
            if anwser == '1':
                self.add_new_word()
            elif anwser == '2':
                self.quiz()
            elif anwser == '3':
                print('Давай досвидания')
                break
            else:
                print('Попробуй снова')

    def add_new_word(self):
        word= input('Введите иностраное слово: ')
        translation = input("Введите перевод слова: ").lower().strip()
        db.add_word(word= word, translation= translation)
        print('Ваше слово добавлено в базу данных')

    def quiz(self):
        score = 0
        total = 0
        print('Викторина начилась, чтобы выйти напишите "я спать"')
        while True:
            random_word = db.get_random_word()
            if not random_word:
                print("Словарь пуст, добавь слово")
                break
            print(f'Переведите данное слово {random_word.word}')
            anwser = input('Ваш перевод: ').lower().strip()
            if anwser == 'я спать':
                break
            if random_word.translation == anwser:
                score += 1
                print("Молодец")
            else:
                print(f"неверно слово переводится вот так: {random_word.translation}")
            total += 1
        if score>=1:
            pr = score / total * 100
            print(f'Количество ваших очков состовляет: {score}')
            print(f'Количество сыграных раундов состовляет: {total}')
            print(f'Ваш резултат состовляет: {pr}%')
if __name__ == "__main__":
    app = Language_Assist()
    app.start()