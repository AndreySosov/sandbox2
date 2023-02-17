# PSYNOTE

## Тестовая версия приложения PSYNOTE

Пирложение предназначено для ведения дневника эмоционального и психолгического состояни.
Поанируется реализация функционала: автоматический анализировать текст, составление графика отметок состояния и прочие аналитические инструменты

### Часто задаваемые вопросы

**Как я могу установить проект?**

Для установки проекта выполните следующие действия:

+ Клонируйте репозиторий с проектом на свой компьютер:

```bash
git clone https://github.com/your-project.git
```

+ Создайте виртуальное окружение и активируйте его:

```bash 
python3 -m venv myenv
source myenv/bin/activate
```


+ Установите зависимости проекта:

```bash
pip install -r requirements.txt
```

+ Настройте базу данных:

```bash
python manage.py migrate
```

+ Создайте суперпользователя:
```bash
python manage.py createsuperuser
```
+ Запустите локальный сервер:
```bash
python manage.py runserver
```


**Как можно добавить новые страницы в проект?**

Для добавления новых страниц в проект выполните следующие действия:

+ Создайте новый файл в директории templates с расширением .html.
+ Определите новый путь URL для новой страницы в файле urls.py.
+ Создайте новое представление для новой страницы в файле views.py.
+ Обновите базу данных, если новая страница содержит новую модель данных.

**Что делать, если вы забыл свой пароль?**

+ Если вы забыли свой пароль, выполните следующие действия:
+ На странице входа в приложение нажмите на ссылку "Забыли пароль?".
+ Введите свой адрес электронной почты, связанный с вашей учетной записью.
+ Нажмите на кнопку "Reset".
+ Проверьте свой почтовый ящик и следуйте инструкциям для сброса пароля.

**Где можно уточнить детали проекта?**

Вы можете написать на почту sosovandrey@mail.ru

