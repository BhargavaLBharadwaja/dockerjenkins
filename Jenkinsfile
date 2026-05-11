pipeline{
    agent any
    
    environment{
        DOCKER_IMAGES="bhargavalb/my-python-appj"
        DOCKER_TAG="latest"
        }
    stages{
        
        stage('build'){
             
             steps{
                 sh 'docker build -t $DOCKER_IMAGE:$DOCKER_TAG'
                 }
                 }
         stage('login'){
              
               steps{
                    withCredentials([usernamePassword(
                                  credentialId:"credential",
                                  usernameVariable:'USER',
                                  passwordVariable:'PASS'
                                  
                    )]){
                        sh 'echo $PASS | docker login -u $USER --password -stdin'
                        }
                        }
                        }
           stage('push'){
                steps{
                     sh 'docker push $SOCKER_IMAGE:$DOCKER_TAG'
                     }
                     }
            stage('deploy'){
                  steps{
                       sh '''
                       docker stop my-python-appj || true
                       docker run my-python-appj  || true
                       docker run -d -p 5000:5000 --name myapp-container $DOCKER_IMAGES:$DOCKER_TAG
                       '''
                       }
                       }
                       }
                       }
