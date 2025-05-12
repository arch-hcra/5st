pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/arch-hcra/5st.git'
            }
        }
        stage('Run Tests') {
            steps {
                sh 'python -m pytest test_login.py'
            }
        }
    }
}
