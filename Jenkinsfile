node {
    stage('Preparation') {
        deleteDir()
        checkout scm
        sh 'git submodule update --init --recursive'
        env.GIT_URL = sh(returnStdout: true, script: 'git config --get remote.origin.url').trim()
        env.GIT_BRANCH = sh(returnStdout: true, script: 'git rev-parse --abbrev-ref HEAD').trim()
        env.GIT_COMMIT = sh(returnStdout: true, script: 'git rev-parse HEAD').trim()
        def workspace = pwd()
        /*sh "cp /var/jenkins_home/deploy-app-vars.yml ${workspace}/ci/ansible/"
        sh "cp /var/jenkins_home/ansible-hosts ${workspace}/ci/ansible/hosts"
        sh '''if [ ! -d "venv" ]; then
            virtualenv venv
        fi'''
        sh ". venv/bin/activate"*/
       // sh "pip install django"
        sh "pip install -r requirement.txt"
        //sh "python3 manage.py makemigrations"
        //sh "python3 manage.py migrate"
    }
    stage('test')
    {
        sh "python3 manage.py test "
    }
    stage('docker-image'){
        dockerimage = sh "docker-compose build"
    }
    stage('deploy'){
        /*
        CONTAINER = test_web
        RUNNING = sh '(docker inspect --format= "{{  .state.Running}}" $CONTAINER  2> /dev/null)'
        script {
                    if ($RUNNING == 1){
                        echo "'$CONTAINER' does not exist"}
                    else{
                        sh "docker rm -f $CONTAINER"}
                }*/
        echo "......Deployment phase start......"

        sh "docker run --publish 8000:8000 -d demo_web"
        echo "...deployed here: 127.0.0.1.8000 " 
    }
}
