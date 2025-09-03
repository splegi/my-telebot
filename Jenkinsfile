pipeline {
    agent { label 'windows' } // агент Windows, как у тебя

    stages {
        stage('Build Docker Image') {
            steps {
                echo 'Шаг 1: Сборка Docker-образа...'
                bat 'docker build -t my-telebot .'
            }
        }

        stage('Run Docker Container') {
            steps {
                echo 'Шаг 2: Запуск контейнера...'
                bat 'docker run --rm my-telebot'
            }
        }

        stage('Finish') {
            steps {
                echo 'Шаг 3: Пайплайн завершён успешно!'
            }
        }
    }
}
