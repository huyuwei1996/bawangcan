pipeline {
    agent any
    options {
        timestamps()
    }
    stages {
        stage("拉取代码") {
            steps {
                dingTalk accessToken: "https://oapi.dingtalk.com/robot/send?access_token=205e133a36dda2e3e1589d591606f777d0d92f5359f4890d9c5c59f01f47e724",
                imageUrl: "图片地址",
                jenkinsUrl: "http://jenkins.huyuwei.com.cn:8080/",
                message: "项目-霸王餐开始构建",
                notifyPeople: ""
                
//                 git credentialsId: "jenkins", url: "git@github.com:huyuwei1996/bawangcan.git"
            }
        }
        stage("使用环境变量") {
            steps {
                sh label: "", script: "export PATH=$PATH"
            }
        }
        stage("运行脚本") {
            steps {
                sh label: "", script: "./run.sh"
            }
        }
    }
    post {
        success {
            dingTalk accessToken: "https://oapi.dingtalk.com/robot/send?access_token=205e133a36dda2e3e1589d591606f777d0d92f5359f4890d9c5c59f01f47e724",
                imageUrl: "图片地址",
                jenkinsUrl: "http://jenkins.huyuwei.com.cn:8080/",
                message: "项目-霸王餐构建成功",
                notifyPeople: ""
        }
        failure {
            dingTalk accessToken: "https://oapi.dingtalk.com/robot/send?access_token=205e133a36dda2e3e1589d591606f777d0d92f5359f4890d9c5c59f01f47e724",
                imageUrl: "图片地址",
                jenkinsUrl: "http://jenkins.huyuwei.com.cn:8080/",
                message: "项目-霸王餐构建失败",
                notifyPeople: ""
        }
    }
}