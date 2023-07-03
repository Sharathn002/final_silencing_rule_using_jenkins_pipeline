pipeline {
    agent any
    // environment {
    // API_TOKEN = credentials('sysdig_api_token')
    // }
  parameters {
        // choice(name: 'UPDATE_CLUSTER', choices: ['pd-cp-dev-ll,pd-dp-dev-ll,pd-cp-dev-ll,pd-cp-dev-ll,pd-cp-dev-ll,pd-cp-dev-ll,pd-cp-dev-ll'], description: '')
        string(name: 'TIMEOUT', defaultValue: '4h', description: '')
        string(name: 'API_TOKEN',defaultValue: "fddsfa",description: '')
    }
  
      stages {
        stage('create Stage') {
            steps {
                script {
                    def sysdigGuid
                    def sysdigHost
                    def key

                    switch (params.UPDATE_CLUSTER) {
                        case ~/.*cp-dev.*/:
                        case ~/.*dp-dev.*/:
                        case ~/.*cp-stage.*/:
                        case ~/.*dp-stage.*/:
                            sysdigGuid = ""
                            key =  ""
                            break
                        case ~/.*prod-cp.*/:
                        case ~/.*dev-dp.*/:
                        case ~/.*pdns-prod-bnpp-bastion.*/:
                            sysdigGuid = ""
                            key = ""
                            break
                        case ~/.*pdns-prod.*/:
                            sysdigGuid = ""
                            key = ""
                            break
                        default:
                            echo "default case"
                            return
                    }
                    echo "SYSDIG_GUID: ${sysdigGuid}"
                    echo "KEY: ${key}"
                    sh """python3 silencing_rule.py create --UPDATE_CLUSTER ${params.UPDATE_CLUSTER} --API_TOKEN  ${key} --IBMInstanceID ${sysdigGuid} --TIMEOUT ${params.TIMEOUT}"""
                }
            }
        }
      }
//   post {
//    always {
//        sh """python3 silencing_rule.py delete --UPDATE_CLUSTER ${params.UPDATE_CLUSTER} --API_TOKEN ${API_TOKEN} """
//    }
// }

}


    

                                                 
