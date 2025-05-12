pipeline {
    agent any 
    
    stages {
        stage('Clone') {
            steps {
                git branch: 'main', url: 'https://github.com/arch-hcra/5st.git' 
            }
        }

        stage('Run Tests') {
            steps {
                bat 'pytest test_login.py'
            }
        }
    }
    
    // Уведомления о результате тестов
    post {
        always {
            script {
                if (currentBuild.result == 'SUCCESS') {
                    echo 'Тесты успешно пройдены!'
                } else {
                    echo 'Тесты не прошли.'
                }
            }
        }
    }
}
