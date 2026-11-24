pipeline {
    agent { label 'ci-python-docker' }
    options {
        timeout(time: 15, unit: 'MINUTES')
        disableConcurrentBuilds()
    }
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Tests') {
            steps {
                // TODO: criar .venv, instalar requirements*.txt e executar pytest -q
                echo 'TODO: executar testes Python'
            }
        }
        stage('Docker Build') {
            steps {
                // TODO: docker build com tag natixis-support:ci-${BUILD_NUMBER}
                // TODO: confirmar imagem criada com docker image inspect
                echo 'TODO: construir e verificar imagem Docker'
            }
        }
    }
}
