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
        script {
            allure([
                reportBuildPolicy: 'ALWAYS',
                results: [[path: 'allure-results']],
                report: [[path: 'allure-report']],
                includeProperties: false,
                jdk: '',
                properties: [],
                reportBuildPolicy: 'ALWAYS',
                saveReportHistory: true
            ])
        }
    }
}
