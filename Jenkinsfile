pipeline {
    agent any
    // environment {
    // API_TOKEN = credentials('sysdig_api_token')
    // }
  parameters {
        // choice(name: 'UPDATE_CLUSTER', choices: ['pd-cp-dev-ll,pd-dp-dev-ll,pd-cp-dev-ll,pd-cp-dev-ll,pd-cp-dev-ll,pd-cp-dev-ll,pd-cp-dev-ll'], description: '')
      choice(name: 'UPDATE_CLUSTER', choices: ['scan', 'pdns-cp-dev-dal12', 'pdns-dp-dev-dal10', 'pdns-cp-stage-wdc-mzr', 'pdns-cp-stage-lon-mzr', 'pdns-dp-stage-wdc04', 'pdns-dp-stage-lon04', 'dev-dp', 'pdns-prod-bnpp-bastion', 'pdns-prod-cp-wdc', 'pdns-prod-cp-dal', 'pdns-prod-dal10', 'pdns-prod-dal12', 'pdns-prod-dal13', 'pdns-prod-wdc04', 'pdns-prod-wdc06', 'pdns-prod-wdc07', 'pdns-prod-lon04', 'pdns-prod-lon05', 'pdns-prod-lon06', 'pdns-prod-fra02', 'pdns-prod-fra04', 'pdns-prod-fra05', 'pdns-prod-tok02', 'pdns-prod-tok04', 'pdns-prod-tok05', 'pdns-prod-syd01', 'pdns-prod-syd04', 'pdns-prod-syd05', 'pdns-prod-osa21', 'pdns-prod-osa22', 'pdns-prod-osa23', 'pdns-prod-par04', 'pdns-prod-par05', 'pdns-prod-par06', 'pdns-prod-tor01', 'pdns-prod-tor04', 'pdns-prod-tor05', 'pdns-prod-sao01', 'pdns-prod-sao04', 'pdns-prod-sao05', 'pdns-prod-mad02', 'pdns-prod-mad04', 'pdns-prod-mad05'], description: '')

        string(name: 'TIMEOUT', defaultValue: '4h', description: '')
        string(name: 'API_TOKEN',defaultValue: "fddsfa",description: '')
    }
  
      stages {
        stage('Example Stage') {
            steps {
                script {
                    def sysdigGuid
                    def sysdigHost
                    def key
                    echo "sdfdsfsdf"

                    switch (params.UPDATE_CLUSTER) {
                        case ~/.*cp-dev.*/:
                        case ~/.*dp-dev.*/:
                        case ~/.*cp-stage.*/:
                        case ~/.*dp-stage.*/:
                            sysdigGuid = "dev and stage"
                            sysdigHost = "https://us-south.monitoud.ibm.com"
                            key =  "this is for the stage and dev"
                            break
                        case ~/.*prod-cp.*/:
                        case ~/.*dev-dp.*/:
                        case ~/.*pdns-prod-bnpp-bastion.*/:
                            sysdigGuid = "FIXME-PROD-CP"
                            sysdigHost = "https://us-south.monitoring.cloud.ibm.com"
                            key = "this is also for the prod"
                            break
                        case ~/.*pdns-prod.*/:
                            sysdigGuid = "FIXME--DP"
                            sysdigHost = "https://u.cloud.ibm.com"
                            key = "this is for the prod"
                            break
                        default:
                            echo "noop"
                            return
                    }
                    // Use the assigned values in subsequent steps or actions
                    echo "im echoing here"
                    echo "params.UPDATE_CLUSTER"
                    echo "SYSDIG_GUID: ${sysdigGuid}"
                    echo "SYSDIG_HOST: ${sysdigHost}"
                    echo "KEY: ${key}"
                    echo "Im ending the echoing here"
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


    

                                                 
