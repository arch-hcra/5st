pipeline {
    agent any 
    
    stages {
        stage('Clone') {
            steps {
                git 'https://github.com/arch-hcra/5st.git'
            }
        }
        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
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
            junit '**/test-results/*.xml'
        }
        success {
            echo 'Tests passed!'
        }
        failure {
            echo 'Tests failed.'
        }
    }
}
