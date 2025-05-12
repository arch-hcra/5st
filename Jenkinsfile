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
