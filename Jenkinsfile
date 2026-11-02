pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps { checkout scm }
        }
        stage('Install Dependencies') {
            steps {
                sh 'python3 -m venv venv'
                sh '. venv/bin/activate && pip install -r requirements.txt'
            }
        }
        stage('Unit Tests') {
            steps {
                sh '. venv/bin/activate && pytest'
            }
            post {
                always { junit 'test-results.xml' }
            }
        }
    }

    post {
        success { echo 'Build passed: all unit tests green.' }
        failure { echo 'Build failed: check the test report.' }
    }
}
