import os
import shutil


def create_course_pack_folders(name_cource:str, total_lesson:int, epic:str, start_jira:int):
    root_folder = os.path.abspath('{0}'.format(name_cource))
    if not os.path.exists(root_folder):
        os.mkdir(root_folder)
    with open('{0}\\Readme'.format(root_folder), 'w') as file:
            file.write('Папка для эпика: {0}\n'.format('{0}{1}'.format(JiraCalc.jira_path, epic)))
            file.write('hw#             - Домашние задания для номаера #\n')
            file.write('cource_project  - Курсовой проект\n')
    create_hw_folders(total_lesson, name_cource, start_jira)
    create_cource_project_folder(name_cource)

def create_cource_project_folder(name_cource):
    cource_path_folder = os.path.abspath('{0}\\cource_project'.format(name_cource))
    if not os.path.exists(cource_path_folder):
        os.mkdir(cource_path_folder)
    with open('{0}\\Readme'.format(cource_path_folder), 'w') as file:
            file.write('Курсовой проект\n')
            file.write('Папка для эпика: \n')

def create_hw_folders(total_lesson:int, name_cource:str, start_jira:int):
    jira_calc = JiraCalc(start_jira)
    for number_lesson in range(1, total_lesson+1):
        path_folder = os.path.abspath('{0}\\hw{1}'.format(name_cource, number_lesson))
        if not os.path.exists(path_folder):
            os.mkdir(path_folder)
        with open('{0}\\Readme'.format(path_folder), 'w') as file:
            file.write('Homework {0}\n'.format(number_lesson))
            file.write('Папка для задачи: {0}\n'.format(jira_calc.get_jira_path(number_lesson-1)))

class JiraCalc:
    jira_path = 'http://jira.local:8080/browse/'

    def __init__(self, start_jira:int):
        self.__start_jira = start_jira

    def get_jira_path(self, num_lesson:int):
        return '{0}LS-{1}'.format(self.jira_path, self.__start_jira + num_lesson)

if __name__ == '__main__':
    create_course_pack_folders(
        'Recommendation_systems',
        8,
        'LS-98',
        99 
        )