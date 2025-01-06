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
                        report: 'allure-report',
                        enableProperties: true,
                        jdk: '',
                        properties: [
                            [key: 'BUILD_NUMBER', value: "${BUILD_NUMBER}"],
                            [key: 'JOB_NAME', value: "${JOB_NAME}"],
                            [key: 'BUILD_URL', value: "${BUILD_URL}"]
                        ],
                        saveReportHistory: true
                    ])
                }
            }
        }
    }
    
    post {
        always {
            cleanWs()
        }
    }
}
