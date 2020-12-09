from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField
from wtforms.validators import DataRequired

__all__ = ['PollForm']


def set_poll_questions(cls) -> None:
    questions = {
        'Читаешь книги?': [str(x) for x in range(7)],
        'Как хорошо вы знаете английский?': ['Оригатоё гайзаймас',
                                             'Чуть лучше, чем ничего',
                                             'Нормально',
                                             'Хорошо',
                                             'Отлично',
                                             'НЭЙТИВ ИНГЛИШ СПИКЕР'],
        'Что такое два.ч?': ['Не знаю',
                             'Паблик в ВК',
                             'Лучшая борда рунета!',
                             'Ненавижу Абу!'],
        'Как часто играешь в игры?'
        '(0 - не играю совсем, 7 - больше 6 часов в неделю)': [str(x) for x in range(8)],
        'Оцените ваш уровень вегетарианца по 5-ти бальной шкале': [str(x) for x in range(1, 6)]
    }

    questions = {x: [(str(i), a) for i, a in enumerate(y)] for x, y in questions.items()}

    for i, (question, answers) in enumerate(questions.items()):
        setattr(cls,
                'question_%i' % i,
                SelectField(question,
                            [DataRequired(message='Обязательный вопрос')],
                            choices=answers))
    return cls


@set_poll_questions
class PollForm(FlaskForm):
    submit = SubmitField('Узнать результат!')
