pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/arch-hcra/5st.git'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'pytest test_login.py'
            }
        }
    }
}
