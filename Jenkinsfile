node{
   stage('SCM Checkout'){
       git branch: 'main',credentialsId: 'github-password', url: 'https://github.com/kp-m10/CICD.git'
   }
   stage('Build Docker Image'){
     sh 'docker build -t kunal007/dockerwebapp-2:0.1 .'
   }
   stage('Push Docker Image'){
     withCredentials([string(credentialsId: 'docker-pass', variable: 'dockerpass')]) {
        sh "docker login -u kunal007 -p ${dockerpass}"
     }
     sh 'docker push kunal007/dockerwebapp-2:0.1'
   }
   stage('Run Container on Dev Server'){
      def dockerRun ="docker run -p 3008:5000 -d kunal007/dockerwebapp-2:0.1"
     sshagent(['remote-dev']) {
       sh "ssh -o StrictHostKeyChecking=no kunal@jfrog.westus2.cloudapp.azure.com ${dockerRun}"
     }
   }
}
