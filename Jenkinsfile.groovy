pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/arch-hcra/5st.git'
            }
        }
        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt' // Убедитесь, что у вас есть файл requirements.txt
            }
        }
        stage('Run Tests') {
            steps {
                sh 'python -m pytest test_login.py'
            }
        }
    }

    post {
        always {
            junit '**/test-*.xml' // Если вы хотите собирать отчеты о тестах
        }
    }
}
