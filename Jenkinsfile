pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building...'
                // Add your build commands here
                sh 'mvn clean install' // Example for a Maven project
            }
        }

        stage('Test') {
            steps {
                echo 'Testing...'
                // Add your test commands here
                sh 'mvn test' // Example for a Maven project
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying...'
                // Add your deploy commands here
                sh 'scp target/myapp.jar user@server:/path/to/deploy/' // Example deployment step
            }
        }
    }
}
