node{
   stage('SCM Checkout'){
       git branch: 'main', credentialsId: 'github-password', url: 'https://github.com/kp-m10/CICD.git'
   }
   stage('Build Docker Image'){
     sh 'docker build -t kunal007/dockerwebapp-2:0.1 .'
   }
   stage('Push Docker Image'){
     withCredentials([string(credentialsId: 'docker-hub', variable: 'docker-hub')]) {
        sh "docker login -u kunal007 -p ${docker-hub}"
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
