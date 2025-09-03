pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t my-telebot:latest .'
            }
        }

        stage('Test Run') {
            steps {
                bat '''
                REM Удаляем старый тестовый контейнер, если есть
                docker rm -f test-bot || exit 0
                REM Запускаем контейнер в фоне на короткое время
                docker run -d --name test-bot my-telebot:latest
                REM Ждем 5 секунд
                timeout /t 5
                REM Проверяем, что контейнер запустился
                docker ps | findstr test-bot
                REM Останавливаем и удаляем тестовый контейнер
                docker rm -f test-bot
                '''
            }
        }

        stage('Deploy Bot') {
            steps {
                bat '''
                REM Удаляем старый контейнер продакшена, если есть
                docker rm -f my-telebot || exit 0
                REM Запускаем контейнер бота в фоне
                docker run -d --name my-telebot my-telebot:latest
                '''
            }
        }
    }
}
