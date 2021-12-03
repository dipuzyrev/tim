# ![Header](preview.png)

## Команда
- [Дмитрий Пузырев](https://t.me/dipuzyrev) - бэкенд
- [Платон Лапп](https://t.me/SeamMiner) - фронтенд
- [Александр Щеблыкин](https://t.me/greeneboy) - десигн

## О проекте

Витрина проектов для акселератора "Транспортные инновации Москвы".


## Технологический стэк

- [Django](https://www.djangoproject.com/) - свободный фреймворк для веб-приложений на языке Python
- [DRF](https://www.django-rest-framework.org/) -  библиотека, которая работает со стандартными моделями Django для создания гибкого API
- [Vue 3](https://v3.ru.vuejs.org/) - прогрессивный JavaScript-фреймворк для создания фронтенда веб-приложения
- [Vuex](https://vuex.vuejs.org/ru/) - официальный менеджер состояний для VueJS
- [Router](https://router.vuejs.org/ru/) - официальный маршрутизатор для VueJS



## Локальный запуск

```bash
git clone https://github.com/dipuzyrev/tim && cd tim

# Start API
cd backend
python3 -m venv env
source ./env/bin/activate  # WIN: "env\Scripts\activate"
pip install -r requirements.txt
python manage.py runserver

# Start frontend
cd ../frontend
yarn && yarn serve
```


### Локальные ссылки

- [Django админка](http://localhost:8000/admin/) (root@example.com / 111111)
