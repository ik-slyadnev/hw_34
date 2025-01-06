pipeline {
    agent any
    
    tools {
        allure 'allure'
    }
    
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Build and Run Tests') {
            steps {
                script {
                    sh 'mkdir -p allure-results'
                    sh '''
                        docker build -t playwright-tests .
                        docker run -v ${WORKSPACE}/allure-results:/tests/allure-results playwright-tests
                    '''
                }
            }
        }
        stage('Generate Allure Report') {
            steps {
                allure([
                    reportBuildPolicy: 'ALWAYS',
                    results: [[path: 'allure-results']]
                ])
            }
        }
    }
}
