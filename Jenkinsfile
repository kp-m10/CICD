node{
   stage('Build Docker Image'){
     sh 'docker build -t kunal007/dockerwebapp-2:0.1 .'
   }
   stage('Push Docker Image'){
     withCredentials([string(variable: 'dockerhub')]) {
        sh "docker login -u kunal007 -p ${dockerhub}"
     }
     sh 'docker push kunal007/dockerwebapp-2:0.1'
   }
   stage('Run Container on Dev Server'){
     def dockerRun ='docker run -p 8080:8080 -d --name my-app kammana/my-app:2.0.0'
     sshagent(['dev-server']) {
       sh "ssh -o StrictHostKeyChecking=no ec2-user@172.31.18.198 ${dockerRun}"
     }
   }
}
