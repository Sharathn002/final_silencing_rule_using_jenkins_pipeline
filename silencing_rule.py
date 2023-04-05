import requests
import json
from datetime import datetime
import argparse


#this is the function to return the list of the notification_channel_ids present
def notification_channel_id(api_token,url):
    headers = {"Authorization": f'Bearer {api_token}'}
    response = requests.get(url, headers=headers)
    # print(response.json()["alerts"][0]["notificationChannelIds"])
    return response.json()["alerts"][0]["notificationChannelIds"] 

#This is the function to create the silencing
def create_silencing_rule(curr_time_in_millisec,cluster_name,api_token,duration):
    duration=float(duration)

    json_data=[
       {
         "api_token": api_token,
         "cluster_name":cluster_name,
         "duration_in_hours": duration
       }
     ]

    for dict in json_data:
        api_token=dict["api_token"]

        #This is the endpoint for the silencing
        url='https://us-south.monitoring.cloud.ibm.com/api/v1/silencingRules'

        #this is the endpoint for all the alerts present
        alert_url='https://us-south.monitoring.cloud.ibm.com/api/alerts'
        silence_config = {
            "durationInSec": dict["duration_in_hours"]*60*60,
            "enabled":True,
            "name": f'Silencing the alert with Cluster name: {dict["cluster_name"]}',
            "notificationChannelIds": notification_channel_id(api_token,alert_url),
            "scope":f'kubernetes.cluster.name in (\"{dict["cluster_name"]}\")',
            "startTs": curr_time_in_millisec
        }
        headers = {'Authorization': f'Bearer {api_token}', 'Content-Type': 'application/json'}
        response = requests.post(url, headers=headers, data=json.dumps(silence_config))

        if response.status_code == 201:
            silence_id = response.json()['id']
            print(f'Silencing rule created successfully with ID:{silence_id}')
        else:
            error_message = response.json()['errors'][0]['message']
            print(f'Error creating alert: {error_message}')


def delete_silencing_rule(cluster_name,api_token):
    json_data=[
      {
        "cluster_name":cluster_name,
        "api_token": api_token
      }
    ]

    for dict in json_data:
        api_token=dict["api_token"]

        #This is the endpoint for the silencing
        silencing_url='https://us-south.monitoring.cloud.ibm.com/api/v1/silencingRules'

        #this is the endpoint for disabling the silencing rule
        disable_url=silencing_url+'/disable'
        headers = {'Authorization': f'Bearer {api_token}', 'Content-Type': 'application/json'}
        response = requests.get(silencing_url, headers=headers)

        if response.status_code == 200:
            silence_rules = response.json()
            for silence_rule in silence_rules:
                
                #current date and time
                now=datetime.now()
                curr_time_in_millisec = now.timestamp() * 1000
                silence_end_time=silence_rule['startTs']+(silence_rule['durationInSec']*1000)
                # if (dict["cluster_name"] in silence_rule['scope']): # this condition is used to  check all the silencing rule with the same cluster name 
                #this condition is used to  check all the silencing rule with the same cluster name and to check whether the curr_time_in_millisec is lesser than silence_end_time
                if (dict["cluster_name"] in silence_rule['scope']) and (curr_time_in_millisec < silence_end_time) and (silence_rule['enabled']==True):
                    # print(silence_rule['id'])
                    rule_id=silence_rule['id']
                    delete_silencing_url=silencing_url+f"/{rule_id}"
                    # print(delete_silencing_url)
                    response = requests.delete(delete_silencing_url, headers=headers)
                    if response.status_code == 200:
                        print(f'Silencing rule with ID:{rule_id} deleted successfully.')
                    else:
                        print('Failed to delete silencing rule. Status code:', response.status_code)
        else:
            print(f'Request failed with status code {response.status_code}')


def main():
    
    #to fetch the current date and time 
    now=datetime.now()
    curr_time_in_millisec = now.timestamp() * 1000

    parser = argparse.ArgumentParser()
    parser.add_argument('function', help='Name of function to call')
    parser.add_argument('--cluster_name', help='First argument', default='')
    parser.add_argument('--api_token', help='Second argument', default='')
    parser.add_argument('--duration_in_hours', help='third argument', default='')
    args = parser.parse_args()

    if args.function == 'create':
        create_silencing_rule(curr_time_in_millisec,args.cluster_name, args.api_token,args.duration_in_hours)
    elif args.function == 'delete':
        delete_silencing_rule(args.cluster_name,args.api_token)
    else:
        print('Invalid function name')
    
if __name__=='__main__':
    main()


