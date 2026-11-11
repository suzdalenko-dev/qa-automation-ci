
pipeline {
    agent any

    options {
        timestamps()
        skipDefaultCheckout(true)
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install dependencies') {
            steps {
                echo 'Instalando dependencias Python...'
            }
        }

        stage('Functional tests') {
            steps {
                echo 'Ejecutando pruebas funcionales con pytest...'
            }
        }

        stage('Performance tests') {
            steps {
                echo 'Ejecutando pruebas de rendimiento con k6...'
            }
        }
    }
}
