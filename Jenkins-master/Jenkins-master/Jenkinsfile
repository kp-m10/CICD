node {

    checkout scm

    docker.withRegistry('https://registry.hub.docker.com','dockerhub') {
        def customImage = docker.build("kunal007/dockerwebapp-1")
        customImage.push()
    }
}
