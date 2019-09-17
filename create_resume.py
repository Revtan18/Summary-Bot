# -*- coding: utf-8 -*-
import pdfkit

options = {
    'page-size': 'A4',
    'margin-top': '0.75in',
    'margin-right': '0.75in',
    'margin-bottom': '0.75in',
    'margin-left': '0.75in',
}

str = """
<!doctype html>
<html>
<head>
	<meta charset=utf-8>
	<title>Resume</title>
</head>
<body>
    <h2>{name}</h2>
    <ul>
        <li>Возраст: {age}</li>
        <li>Место проживания: {location}</li>
        <li>Образование: {education}</li>
        <li>Отношение к математике: {math}</li>
        <li>Уровень английского: {english}</li>
    </ul>
    <h3>Чем хочешь заниматься?</h3>
    <p>{desire}</p>
    <h3>Навыки</h3>
    <p>{skills}</p>
    <h3>Опыт работы</h3>
    <p>{expirience}</p>
    <h3>Цели</h3>
    <p>{goals}</p>
    <h3>Хобби</h3>
    <p>{hobbi}</p>
    <h3>Самая большая проблема</h3>
    <p>{problem}</p>
    <h3>Самый сложный проект</h3>
    <p>{project}</p>
    <h3>Что делаешь при выгорании?</h3>
    <p>{fire}</p>
    <h3>Деньги, знания, свобода?</h3>
    <p>{mkl}</p>
    <h3>Желаемая должность</h3>
    <p>{position}</p>
</body>
</html>
"""

def create_pdf(dict, title = 'resume'):
    pdfkit.from_string(str.format(**dict), '{}.pdf'.format(title), options=options)



if __name__ == '__main__':
    answers = { 'name': 'Иван Иванович',
                'age': '20',
                'location': 'Россия, Екатеринбург',
                'education': 'ИТМО, 1 курс',
                'math': 'нормальное',
                'english': 'B1',
                'desire': 'делать резюме',
                'skills': 'js, html, css',
                'expirience': 'не работал',
                'goals': 'web, mobile',
                'hobbi': 'музыка, велопутешествия',
                'problem': 'не смог найти решение на stackoverflow',
                'project': 'чат-бот',
                'fire': 'сижу в пледе и пью чай',
                'mkl': 'свобода',
                'position': 'веб-дизайнер'}
    create_pdf(answers, 'Ivanov')
