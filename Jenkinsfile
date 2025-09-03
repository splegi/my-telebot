pipeline {
    agent any

    environment {
        // Опционально: задаём имя образа Docker
        IMAGE_NAME = "my-telebot"
        IMAGE_TAG = "latest"
    }

    stages {
        stage('Проверка среды') {
            steps {
                echo 'Шаг 1: Проверяем Python и Docker'
                bat 'python --version'
                bat 'docker --version'
            }
        }

        stage('Запуск Python скрипта') {
            steps {
                echo 'Шаг 2: Запускаем import_telebot.py'
                bat 'python import_telebot.py'
            }
        }

        stage('Сборка Docker образа') {
            steps {
                echo 'Шаг 3: Сборка Docker образа'
                bat 'docker build -t %IMAGE_NAME%:%IMAGE_TAG% .'
            }
        }

        stage('Тестовый запуск Docker контейнера') {
            steps {
                echo 'Шаг 4: Тестовый запуск контейнера'
                // Запускаем контейнер на 5 секунд и убиваем его
                bat 'docker run --name test_%IMAGE_NAME% %IMAGE_NAME%:%IMAGE_TAG%'
                bat 'docker rm -f test_%IMAGE_NAME%'
            }
        }

        stage('Завершение') {
            steps {
                echo 'Шаг 5: Мини-пайплайн успешно выполнен!'
            }
        }
    }

    post {
        always {
            echo 'Сборка завершена!'
        }
        success {
            echo 'Статус: SUCCESS'
        }
        failure {
            echo 'Статус: FAILURE'
        }
    }
}
