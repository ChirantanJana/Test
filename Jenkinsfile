node {
    stage('Checkout') {
        deleteDir()
        checkout scm
        sh 'git submodule update --init --recursive'
        env.GIT_URL = sh(returnStdout: true, script: 'git config --get remote.origin.url').trim()
        env.GIT_BRANCH = sh(returnStdout: true, script: 'git rev-parse --abbrev-ref HEAD').trim()
        env.GIT_COMMIT = sh(returnStdout: true, script: 'git rev-parse HEAD').trim()
        def workspace = pwd()
    }
        
    stage('Preparation'){
    sh "pip install -r requirement.txt"
    }
    stage('test')
    {
        sh "python3 manage.py test "
    }
    stage('docker-image'){
        dockerimage = sh "docker-compose build"
    }
    stage('deploy'){
        echo "......Deployment phase start......"

        sh "docker run --publish 8000:8000 -d demo_web"
        echo "...deployed here: 127.0.0.1.8000 " 
    }
}
