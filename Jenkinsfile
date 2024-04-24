pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh("sudo docker build -t sicei-${GIT_BRANCH}:1.0.0-${BUILD_NUMBER} .")
                sh("sudo docker image ls")
            }
        }
    }
}