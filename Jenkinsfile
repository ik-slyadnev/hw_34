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
        
        stage('Prepare') {
            steps {
                sh '''
                    mkdir -p allure-results
                    chmod -R 777 allure-results
                '''
            }
        }
        
        stage('Build and Run Tests') {
            steps {
                script {
                    sh '''
                        docker build -t playwright-tests .
                        docker run --rm \
                            -v "${WORKSPACE}/allure-results:/tests/allure-results" \
                            playwright-tests
                    '''
                }
            }
        }
        
        stage('Debug Allure Results') {
            steps {
                sh '''
                    echo "Содержимое папки allure-results:"
                    ls -la allure-results/
                    echo "Количество файлов в allure-results:"
                    find allure-results -type f | wc -l
                '''
            }
        }
        
        stage('Generate Allure Report') {
            steps {
                script {
                    // Добавим права доступа перед генерацией
                    sh 'chmod -R 777 allure-results'
                    
                    allure([
                        reportBuildPolicy: 'ALWAYS',
                        results: [[path: 'allure-results']],
                        report: 'allure-report',
                        enableProperties: true,
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
