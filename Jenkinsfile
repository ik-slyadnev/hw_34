pipeline {
    agent any

    environment {
        ALLURE_RESULTS = "${WORKSPACE}/allure-results"
        ALLURE_REPORT = "${WORKSPACE}/allure-report"
    }

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
                    echo "Cleaning up previous results..."
                    rm -rf ${ALLURE_RESULTS}
                    rm -rf ${ALLURE_REPORT}
                    
                    echo "Creating allure-results directory..."
                    mkdir -p ${ALLURE_RESULTS}
                    chmod -R 777 ${ALLURE_RESULTS}
                    
                    echo "Created allure-results directory:"
                    ls -la ${ALLURE_RESULTS}
                '''
            }
        }

        stage('Build and Run Tests') {
            steps {
                script {
                    // Убедимся что директория существует и имеет правильные права
                    sh '''
                        mkdir -p ${WORKSPACE}/allure-results
                        chmod -R 777 ${WORKSPACE}/allure-results
                    '''
                    
                    // Запуск тестов в Docker с правильным монтированием volume
                    sh '''
                        echo "Building Docker image..."
                        docker build -t playwright-tests .
                        
                        echo "Running tests..."
                        docker run --rm \
                            -v "${WORKSPACE}/allure-results:/tests/allure-results" \
                            --user "$(id -u):$(id -g)" \
                            playwright-tests \
                            pytest --alluredir=/tests/allure-results
                        
                        echo "Test results:"
                        ls -la ${WORKSPACE}/allure-results/
                    '''
                }
            }
        }

        stage('Generate Allure Report') {
            steps {
                script {
                    // Проверка наличия результатов
                    sh '''
                        echo "Allure results files:"
                        ls -la ${WORKSPACE}/allure-results/
                    '''
                    
                    // Генерация отчета
                    allure([
                        includeProperties: false,
                        jdk: '',
                        properties: [],
                        reportBuildPolicy: 'ALWAYS',
                        results: [[path: "${WORKSPACE}/allure-results"]],
                        report: "${WORKSPACE}/allure-report"
                    ])
                }
            }
        }
    }

    post {
        always {
            // Архивация артефактов
            archiveArtifacts(
                artifacts: 'allure-results/**/*,allure-report/**/*',
                allowEmptyArchive: true
            )
            
            // Публикация отчета Allure
            allure([
                includeProperties: false,
                jdk: '',
                properties: [],
                reportBuildPolicy: 'ALWAYS',
                results: [[path: "${WORKSPACE}/allure-results"]],
                report: "${WORKSPACE}/allure-report"
            ])
        }
        
        success {
            echo 'Pipeline completed successfully!'
        }
        
        failure {
            echo 'Pipeline failed!'
        }
    }
}
