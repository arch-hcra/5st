pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Получение кода из репозитория
                checkout scm
            }
        }
        stage('Install Dependencies') {
            steps {
                // Установка зависимостей
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Run Tests') {
            steps {
                // Запуск тестов с помощью pytest
                sh 'pytest'
            }
        }
    }

    post {
        always {
            // Действия, выполняемые всегда, например, публикация отчетов
            junit '**/test-results/*.xml' // Если у вас есть XML отчеты
        }
        success {
            echo 'Tests passed!'
        }
        failure {
            echo 'Tests failed!'
        }
    }
}
