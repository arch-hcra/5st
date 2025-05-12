pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/arch-hcra/5st.git'
            }
        }


        stage('Run Tests') {
            steps {
         
                sh 'pytest test_login.py'
            }
        }
    }

    post {
        always {
      
            echo 'Pipeline завершен.'
        }
        success {
            echo 'Тесты прошли успешно!'
        }
        failure {
            echo 'Тесты не прошли.'
        }
    }
}
