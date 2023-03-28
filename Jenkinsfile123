// pipeline {
//   agent any
//   parameters {
//     choice(name: 'UPDATE_CLUSTER', choices: ['scan','webapCluster/cfvdf6ef0lb6gpb1puig', 'cis-dev-dal12', 'cis-int-mzr', 'cis-stage-wdc-mzr', 'cis-stage-lon-mzr', 'cis-prod-dal', 'cis-prod-wdc', 'cis-prod-fra', 'pdns-cp-dev-dal12', 'pdns-dp-dev-dal10', 'pdns-cp-stage-wdc-mzr', 'pdns-cp-stage-lon-mzr', 'pdns-dp-stage-wdc04', 'pdns-dp-stage-lon04', 'dev-dp', 'cis-prod-dal', 'cis-prod-wdc', 'pdns-prod-bnpp-bastion', 'pdns-prod-cp-wdc', 'pdns-prod-cp-dal', 'pdns-prod-dal10', 'pdns-prod-dal12', 'pdns-prod-dal13', 'pdns-prod-wdc04', 'pdns-prod-wdc06', 'pdns-prod-wdc07', 'pdns-prod-lon04', 'pdns-prod-lon05', 'pdns-prod-lon06', 'pdns-prod-fra02', 'pdns-prod-fra04', 'pdns-prod-fra05', 'pdns-prod-tok02', 'pdns-prod-tok04', 'pdns-prod-tok05', 'pdns-prod-syd01', 'pdns-prod-syd04', 'pdns-prod-syd05', 'pdns-prod-osa21', 'pdns-prod-osa22', 'pdns-prod-osa23', 'pdns-prod-par04', 'pdns-prod-par05', 'pdns-prod-par06', 'pdns-prod-tor01', 'pdns-prod-tor04', 'pdns-prod-tor05', 'pdns-prod-sao01', 'pdns-prod-sao04', 'pdns-prod-sao05'], description: '')
//     choice(name: 'UPDATE_TYPE', choices: ['patch', 'major/minor'], description: 'https://cloud.ibm.com/docs/containers?topic=containers-update')
//     booleanParam(name: 'SKIP_DISABLE_GLB', defaultValue: false, description: '')
//     booleanParam(name: 'SKIP_UPDATE', defaultValue: false, description: '')
//     booleanParam(name: 'SKIP_ACCEPTANCE_TEST', defaultValue: false, description: '')
//     booleanParam(name: 'SKIP_ENABLE_GLB', defaultValue: false, description: '')
//     string(name: 'TIMEOUT', defaultValue: '4h', description: '')
//     string(name: 'K8S_VERSION', defaultValue: '', description: 'https://cloud.ibm.com/docs/containers?topic=containers-cs_versions')
//     string(name: 'DEPLOY_TOOL_VERISON', defaultValue: 'v3.1.1', description: '')
//     string(name: 'SLACK_CHANNEL', defaultValue: 'pdns-slack-test-private', description: '')
// //     string(name: 'cluster_name', defaultValue: 'webapCluster/cfvdf6ef0lb6gpb1puig', description: 'Enter the cluster name')
// //     string(name: 'region', defaultValue: '"jp tok"', description: 'Enter the region name in this formate. ex:"jp tok" ')
//     choice(name: 'region', choices: ['jp_tok','jp_osa','eu_de','eu_gb','us_south','us_east','au_syd','ca_tor', 'br_sao'], description: 'Enter the region where the agent lies ')
//     string(name: 'api_token', defaultValue: '3e91771e-40d2-42cd-96ac-ebe08462c96c', description: 'Enter the api token of that region')
//     string(name: 'duration_in_hours', defaultValue: '1.5', description: 'Enter the duration for the silencing')
//   }
//   stages {
//     stage('silencing alert') {
//       steps {
//         sh """python3 creating_silencing_rule.py ${params.UPDATE_CLUSTER} ${params.region} ${params.api_token} ${params.duration_in_hours}"""
//       }
//     }
//      stage('sleep') {
//        steps {
//          sleep time: 30, unit: 'SECONDS' 
//        }
//      }
// //      stage('crash') {
// //        steps {
// //          sh 'python3 crash.py'
// //        }
// //        post {
// //          always {
// //                sh """python3 deleting_silencing_rule.py ${params.cluster_name} ${params.region} ${params.api_token} ${params.duration_in_hours}"""
// //                }
// //            }
// //     }
//      stage('deleting silencing rule') {
//        steps {
//          sh """python3 deleting_silencing_rule.py ${params.UPDATE_CLUSTER} ${params.region} ${params.api_token} ${params.duration_in_hours}"""
//        }
//      }
//   }
  
// }

pipeline {
    agent any
//     environment {
//         GHE_SSH_KEY = credentials('GITHUB_IBM_SSH_KEY')
//         GHE_API_KEY = credentials('GITHUB_IBM_API_KEY')
//         CIS_PROD_API_KEY = credentials('IC_CIS_API_KEY')
//         PDNS_STAGE_API_KEY = credentials('IC_STAGE_TEST_KEY')
//         PDNS_PROD_API_KEY = credentials('IC_TEST_KEY')
//         JENKINS_ENDPOINT="https://wcp-network-edge-svcs-team-jenkins.swg-devops.com"
//         JENKINS_USER = credentials('JENKINS_USER')
//         JENKINS_API = credentials('JENKINS_API')
//         AKAMAI_CLIENT_TOKEN = credentials('AKAMAI_CLIENT_TOKEN')
//         AKAMAI_CLIENT_SECRET = credentials('AKAMAI_CLIENT_SECRET')
//         AKAMAI_ACCESS_TOKEN = credentials('AKAMAI_ACCESS_TOKEN')
//         CF_EMAIL = credentials('CF_EMAIL')
//         CF_API = credentials('CF_API')
//         CF_ACCOUNT = credentials('CF_ACCOUNT')
//         SLACK_KEY = credentials('SLACK_KEY')
//         PDNS_CIS_STAGE_CRN="crn:v1:bluemix:public:internet-svcs:global:a/a4081b067ad64da4954399ba5409be7c:dfaa3571-f5a3-4233-8f22-4c2acf409f54::"
//         PDNS_CIS_PROD_CRN="crn:v1:bluemix:public:internet-svcs:global:a/fff1cdf3dc1e4ec692a5f78bbb2584bc:3d46b9c6-cf9f-4536-b8f4-dc1106c8ad41::"
//     }
    parameters {
        choice(name: 'UPDATE_CLUSTER', choices: ['scan', 'webapCluster/cfvdf6ef0lb6gpb1puig','cis-dev-dal12', 'cis-int-mzr', 'cis-stage-wdc-mzr', 'cis-stage-lon-mzr', 'cis-prod-dal', 'cis-prod-wdc', 'cis-prod-fra', 'pdns-cp-dev-dal12', 'pdns-dp-dev-dal10', 'pdns-cp-stage-wdc-mzr', 'pdns-cp-stage-lon-mzr', 'pdns-dp-stage-wdc04', 'pdns-dp-stage-lon04', 'dev-dp', 'cis-prod-dal', 'cis-prod-wdc', 'pdns-prod-bnpp-bastion', 'pdns-prod-cp-wdc', 'pdns-prod-cp-dal', 'pdns-prod-dal10', 'pdns-prod-dal12', 'pdns-prod-dal13', 'pdns-prod-wdc04', 'pdns-prod-wdc06', 'pdns-prod-wdc07', 'pdns-prod-lon04', 'pdns-prod-lon05', 'pdns-prod-lon06', 'pdns-prod-fra02', 'pdns-prod-fra04', 'pdns-prod-fra05', 'pdns-prod-tok02', 'pdns-prod-tok04', 'pdns-prod-tok05', 'pdns-prod-syd01', 'pdns-prod-syd04', 'pdns-prod-syd05', 'pdns-prod-osa21', 'pdns-prod-osa22', 'pdns-prod-osa23', 'pdns-prod-par04', 'pdns-prod-par05', 'pdns-prod-par06', 'pdns-prod-tor01', 'pdns-prod-tor04', 'pdns-prod-tor05', 'pdns-prod-sao01', 'pdns-prod-sao04', 'pdns-prod-sao05'], description: '')
        choice(name: 'UPDATE_TYPE', choices: ['patch', 'major/minor'], description: 'https://cloud.ibm.com/docs/containers?topic=containers-update')
        booleanParam(name: 'SKIP_DISABLE_GLB', defaultValue: false, description: '')
        booleanParam(name: 'SKIP_UPDATE', defaultValue: false, description: '')
        booleanParam(name: 'SKIP_ACCEPTANCE_TEST', defaultValue: false, description: '')
        booleanParam(name: 'SKIP_ENABLE_GLB', defaultValue: false, description: '')
        string(name: 'TIMEOUT', defaultValue: '4h', description: '')
        string(name: 'K8S_VERSION', defaultValue: '', description: 'https://cloud.ibm.com/docs/containers?topic=containers-cs_versions')
        string(name: 'DEPLOY_TOOL_VERISON', defaultValue: 'v3.1.1', description: '')
        string(name: 'SLACK_CHANNEL', defaultValue: 'pdns-slack-test-private', description: '')
        choice(name: 'region', choices: ['jp_tok','jp_osa','eu_de','eu_gb','us_south','us_east','au_syd','ca_tor', 'br_sao'], description: 'Enter the region where the agent lies ')
        string(name: 'api_token', defaultValue: '3e91771e-40d2-42cd-96ac-ebe08462c96c', description: 'Enter the api token of that region')
        string(name: 'duration_in_hours', defaultValue: '1.5', description: 'Enter the duration for the silencing')
    }
//     triggers {
//         parameterizedCron('''
//             H 9 * * 1 %UPDATE_CLUSTER=scan;UPDATE_TYPE=major/minor
//             H 8 * * 1-5 %UPDATE_CLUSTER=scan;UPDATE_TYPE=patch
//         ''')
//     }
    stages {
//         stage('Setup') {
//             steps {
//                 sh '''#!/bin/bash
//                       chmod +x ./scripts/jenkins/kubernetes-upgrade/setup.sh
//                       ./scripts/jenkins/kubernetes-upgrade/setup.sh
//                 '''
//             }
//         }
        stage('Check for Patch Updates') {
            when {
                expression {
                    params.UPDATE_CLUSTER == "scan" &&
                    params.UPDATE_TYPE == "patch"
                }
            }
            steps {
                sh '''#!/bin/bash
                   # run daily
                   source ./scripts/utils/error.sh
                   source ./scripts/utils/ic.sh
                   source ./scripts/utils/slack.sh

                   for key in "$CIS_PROD_API_KEY" "$PDNS_STAGE_API_KEY" "$PDNS_PROD_API_KEY"; do
                     ibmcloud_login "us-south" "$key" > /dev/null
                     CLUSTERS=($(ibmcloud ks clusters -s | awk '{print $1}' | paste -sd " " -))
                     for CLUSTER in "${CLUSTERS[@]}"; do
                       if ibmcloud ks workers -c $CLUSTER | tail -n 1 | grep -q "update"; then
                         echo "$CLUSTER" >> patches_available.txt
                       fi
                     done
                   done
                   if [[ -s patches_available.txt ]]; then
                     cat patches_available.txt
                     slack_upload "$SLACK_KEY" "$SLACK_CHANNEL" "Clusters with Patches Available" "patches_available" "@patches_available.txt"
                   else
                     echo "[INFO] No patches available at this time"
                   fi
                   '''
            }
        }
        stage('Check for Major/Minor Updates') {
            when {
                expression {
                    params.UPDATE_CLUSTER == "scan" &&
                    params.UPDATE_TYPE == "major/minor"
                }
            }
            steps {
                sh '''#!/bin/bash
                   # run weekly
                   source ./scripts/utils/error.sh
                   source ./scripts/utils/ic.sh
                   source ./scripts/utils/slack.sh

                   ic_login "CIS" > /dev/null
                   ibmcloud_login "us-south" "$PDNS_PROD_API_KEY"
                   DEFAULT_K8S_VERSION=$(ibmcloud ks versions -s --show-version kubernetes | grep default | awk '{print $1}' | cut -d "." -f -2)
                   touch updates_available.yaml
                   for key in "$CIS_PROD_API_KEY" "$PDNS_STAGE_API_KEY" "$PDNS_PROD_API_KEY"; do
                     ibmcloud_login "us-south" "$key"
                     CLUSTERS=($(ibmcloud ks clusters -s | awk '{print $1}' | paste -sd " " -))
                     for CLUSTER in "${CLUSTERS[@]}"; do
                       MASTER_VERSION=$(ibmcloud ks cluster get -c "$CLUSTER" | grep "Version:" | awk '{print $2}' | cut -d "." -f -2)
                       if [[ "$DEFAULT_K8S_VERSION" != "${MASTER_VERSION}" ]]; then
                         ./yq w -i updates_available.yaml "clusters.$CLUSTER.master" "true"
                       fi
                       WORKERS=($(ibmcloud ks workers -s -c "$CLUSTER" | awk 'NF > 0' | awk '{print $1}' | paste -sd " " -))
                       for WORKER in "${WORKERS[@]}"; do
                         WORKER_VERSION=$(ibmcloud ks worker get -s -c "$CLUSTER" -w "$WORKER" | grep "Version:" | awk '{print $2}' | cut -d "." -f -2)
                         if [[ "$DEFAULT_K8S_VERSION" != "$WORKER_VERSION" ]]; then
                           ./yq w -i updates_available.yaml "clusters.$CLUSTER.workers" true
                           break
                         fi
                       done
                     done
                   done

                   if [[ -s updates_available.yaml ]]; then
                     cat updates_available.yaml
                     slack_upload "$SLACK_KEY" "$SLACK_CHANNEL" "Clusters with Updates Available" "updates_available" "@updates_available.yaml"
                   else
                     echo "[INFO] No updates available at this time"
                   fi
                   '''
            }
        }
         stage('silencing alert') {
            steps {
              sh """python3 creating_silencing_rule.py ${params.UPDATE_CLUSTER} ${params.region} ${params.api_token} ${params.duration_in_hours}"""
            }
          }
        stage('Disable GLB') {
            when {
                expression {
                    params.UPDATE_CLUSTER != "scan"
                }
            }
            steps {
                sh '''#!/bin/bash
                      if [[ "$SKIP_DISABLE_GLB" == "true" ]]; then
                        exit 0
                      fi

                      # load functions
                      source ./scripts/utils/error.sh
                      source ./scripts/utils/glb.sh

                      _is_glb_needed "$UPDATE_CLUSTER"
                      if [[ "$GLB_TYPE" != "none" ]]; then
                        case $IC_ACCOUNT in
                          cis)
                            key="$CIS_PROD_API_KEY"
                            ;;
                          prod)
                            key="$PDNS_PROD_API_KEY"
                            cis_crn="$PDNS_CIS_PROD_CRN"
                            ;;
                          stage)
                            key="$PDNS_STAGE_API_KEY"
                            cis_crn="$PDNS_CIS_STAGE_CRN"
                            ;;
                          *)
                            echo "noop"
                            ;;
                        esac
                        ibmcloud_login "us-south" "$key"
                        # cis check
                        disable_glb "$UPDATE_CLUSTER" "$cis_crn"
                      fi
                   '''
            }
        }
        stage('Update') {
            when {
                expression {
                    params.UPDATE_CLUSTER != "scan"
                }
            }
            steps {
                sh '''#!/bin/bash
                       if [[ "$SKIP_UPDATE" == "true" ]]; then
                        exit 0
                      fi
                      chmod +x ./scripts/jenkins/kubernetes-upgrade/upgrade.sh
                      ./scripts/jenkins/kubernetes-upgrade/upgrade.sh
                   '''
            }
        }
        stage('Acceptance Test') {
            when {
                expression {
                    params.UPDATE_CLUSTER != "scan"
                }
            }
            steps {
                sh '''#!/bin/bash
                      if [[ "$SKIP_ACCEPTANCE_TEST" == "true" ]]; then
                        exit 0
                      fi

                      # load functions
                      source ./scripts/utils/error.sh
                      source ./scripts/utils/slack.sh

                      echo "[INFO] $(date "+%Y/%m/%d %T") Running acceptance test for $UPDATE_CLUSTER"
                      JENKINS_TEST=$(./yq r scripts/configs/acceptance_test.yaml "$UPDATE_CLUSTER")
                      JENKINS_RESULT=$(./jenkinsctl -j "$JENKINS_TEST")
                      echo "$JENKINS_RESULT"
                      if [[ "$JENKINS_RESULT" == *"succeeded"* ]]; then
                      # slack message as passed
                      slack_msg "$SLACK_KEY" "$SLACK_CHANNEL" "Acceptance test passed for $UPDATE_CLUSTER"
                      else
                      # slack message as failed
                      slack_msg "$SLACK_KEY" "$SLACK_CHANNEL" "Acceptance test failed for $UPDATE_CLUSTER"
                      exit 1
                      fi
                   '''
            }
        }
        stage('Enable GLB') {
            when {
                expression {
                    params.UPDATE_CLUSTER != "scan"
                }
            }
            steps {
                sh '''#!/bin/bash
                      if [[ "$SKIP_ENABLE_GLB" == "true" ]]; then
                        exit 0
                      fi

                      # load functions
                      source ./scripts/utils/error.sh
                      source ./scripts/utils/glb.sh

                      _is_glb_needed "$UPDATE_CLUSTER"
                      if [[ "$GLB_TYPE" != "none" ]]; then
                        case $IC_ACCOUNT in
                          cis)
                            key="$CIS_PROD_API_KEY"
                            ;;
                          prod)
                            key="$PDNS_PROD_API_KEY"
                            cis_crn="$PDNS_CIS_PROD_CRN"
                            ;;
                          stage)
                            key="$PDNS_STAGE_API_KEY"
                            cis_crn="$PDNS_CIS_STAGE_CRN"
                            ;;
                          *)
                            echo "noop"
                            ;;
                        esac
                        ibmcloud_login "us-south" "$key"
                        enable_glb "$UPDATE_CLUSTER" "$cis_crn"
                      fi
                   '''
            }
        }
    }
  post {
       always {
           sh """python3 deleting_silencing_rule.py ${params.UPDATE_CLUSTER} ${params.region} ${params.api_token} ${params.duration_in_hours}"""
       }
  }
}

