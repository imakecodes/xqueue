pipeline {
  agent {
    docker {
      image 'python:3.8-buster'
    }

  }
  stages {
    stage('Build') {
      agent {
        docker {
          image 'python:3.8-buster'
        }

      }
      steps {
        echo 'Building the image'
      }
    }

    stage('Lint') {
      agent {
        docker {
          image 'python:3.8-buster'
        }

      }
      steps {
        echo 'Linting'
      }
    }

    stage('Test') {
      agent {
        docker {
          image 'python:3.8-buster'
        }

      }
      steps {
        echo 'Testing'
      }
    }

  }
}