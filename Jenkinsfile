pipeline {
    agent any
    
    tools {
        allure 'allure'
    }
    
    environment {
        ALLURE_RESULTS = "${WORKSPACE}/allure-results"
        ALLURE_REPORT = "${WORKSPACE}/allure-report"
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
                    # Очистка с выводом информации
                    echo "Cleaning up previous results..."
                    rm -rf ${ALLURE_RESULTS} || true
                    rm -rf ${ALLURE_REPORT} || true
                    
                    # Создание директории
                    echo "Creating allure-results directory..."
                    mkdir -p ${ALLURE_RESULTS}
                    chmod -R 777 ${ALLURE_RESULTS}
                    
                    # Проверка создания директории
                    echo "Created allure-results directory:"
                    ls -la ${ALLURE_RESULTS}
                '''
            }
        }
        
        stage('Build and Run Tests') {
            steps {
                script {
                    try {
                        sh '''
                            # Сборка образа
                            echo "Building Docker image..."
                            docker build -t playwright-tests .
                            
                            # Запуск тестов
                            echo "Running tests..."
                            docker run --rm \
                                -v "${ALLURE_RESULTS}:/tests/allure-results:rw" \
                                --user root \
                                playwright-tests
                            
                            # Проверка результатов
                            echo "Contents of allure-results after tests:"
                            ls -la ${ALLURE_RESULTS}/
                            
                            # Подсчет количества JSON файлов
                            echo "Number of JSON files in results:"
                            find ${ALLURE_RESULTS} -name "*.json" | wc -l
                            
                            # Исправление прав
                            echo "Fixing permissions..."
                            chmod -R 777 ${ALLURE_RESULTS}
                        '''
                    } catch (Exception e) {
                        echo "Error during test execution: ${e.message}"
                        currentBuild.result = 'FAILURE'
                        throw e
                    }
                }
            }
        }
        
        stage('Generate Allure Report') {
            steps {
                script {
                    try {
                        // Проверка наличия результатов
                        sh '''
                            echo "Contents before generating report:"
                            ls -la ${ALLURE_RESULTS}/
                            
                            echo "Sample of JSON files (first 3):"
                            find ${ALLURE_RESULTS} -name "*.json" -exec head -n 20 {} \\; | head -n 60 || true
                        '''
                        
                        // Генерация отчета
                        allure([
                            includeProperties: false,
                            jdk: '',
                            properties: [],
                            reportBuildPolicy: 'ALWAYS',
                            results: [[path: "${ALLURE_RESULTS}"]],
                            report: "${ALLURE_REPORT}"
                        ])
                        
                        // Проверка генерации отчета
                        sh '''
                            echo "Generated report contents:"
                            ls -la ${ALLURE_REPORT}/
                        '''
                    } catch (Exception e) {
                        echo "Error generating Allure report: ${e.message}"
                        currentBuild.result = 'UNSTABLE'
                        throw e
                    }
                }
            }
        }
    }
    
    post {
        always {
            script {
                // Архивация с проверкой
                echo "Archiving artifacts..."
                archiveArtifacts(
                    artifacts: 'allure-results/**/*', 
                    allowEmptyArchive: true,
                    fingerprint: true
                )
                archiveArtifacts(
                    artifacts: 'allure-report/**/*', 
                    allowEmptyArchive: true,
                    fingerprint: true
                )
            }
            
            // Очистка рабочего пространства
            cleanWs(
                cleanWhenNotBuilt: false,
                deleteDirs: true,
                disableDeferredWipeout: true,
                notFailBuild: true
            )
        }
        
        failure {
            echo "Build failed! Check the logs for details."
        }
        
        unstable {
            echo "Build is unstable! Check the Allure report generation."
        }
        
        success {
            echo "Build succeeded! Allure report should be available."
        }
    }
}
