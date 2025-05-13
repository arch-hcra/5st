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
            script {
                if (currentBuild.result == 'SUCCESS') {
                    echo 'Yes complited'
                } else {
                    echo 'No complited'
                }
            }
        }
    }
}
