def teams(team1_num, team2_num):
    print('В команде Мастера кода участников: %s !' % (team1_num))
    print('Итого сегодня в командах участников: %s и %s !' % (team1_num, team2_num))
    print(teams(5, 6))

def format_(score_2, team1_time):
    print('Команда Волшебники данных решила задач: {}!'.format(score_2))
    print('Волшебники данных решили задачи за {} c. !'.format(team1_time))
    print(format_(42, 18015.2))

def challenge_result(score_1, score_2):
    print(f'Команды решили {score_1} и {score_2} задач.')
    if score_1 > score_2:
        print('Результат битвы: победа команды Мастера кода!')
    else:
        print('Результат битвы: победа команды Волшебники данных!')

    print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу')

tasks_total = 82
time_avg = 45.2
challenge_result(40, 42)
# team1_num = 5
# team2_num = 6
# score_1 = 40
# score_2 = 42
# team1_time = 1552.512
# team2_time = 2153.31451
# tasks_total = 82
# time_avg = 45.2
# challenge_result = 'Победа команды Волшебники данных!'

