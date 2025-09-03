pipeline {
    agent any //указываем на каком агенте запускать
    
    stages { //список шагов пайплайна
        stage('checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    docker.build("my-telebot:latest")
                }
            }
        }

        stage('Test Run') {
            steps {
                script {
                    docker.image("my-telebot:latest").withRun('-d --name test-bot') { c ->
                        sleep 5
                        sh "docker ps | findstr test-bot"
                        sh "docker rm -f ${c.id}"
                    }
                }
            }
        }

        stage('Deploy Bot') {
            steps {
                script {
                    // Проверяем, есть ли старый контейнер
                    sh 'docker rm -f my-telebot || true'
                    // Запускаем контейнер в фоне
                    sh 'docker run -d --name my-telebot my-telebot:latest'
                }
            }
        }
    }
}