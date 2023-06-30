import requests
import json
from datetime import datetime
import argparse
def main():
    
    #to fetch the current date and time 
    now=datetime.now()
    curr_time_in_millisec = now.timestamp() * 1000

    parser = argparse.ArgumentParser()
    parser.add_argument('function', help='Name of function to call')
    parser.add_argument('--UPDATE_CLUSTER', help='cluster name', default='')
    parser.add_argument('--API_TOKEN', help='Sysdig api token', default='')
    parser.add_argument('--IBMInstanceID', help='IBMInstanceID', default='')
    parser.add_argument('--TIMEOUT', help='duration of the silence', default='')
    args = parser.parse_args()
    print("this is the output from the python script")
    print(args.function,"->",args.UPDATE_CLUSTER,"->",args.API_TOKEN,"->",args.IBMInstanceID,"->",args.TIMEOUT.lower())

    # if args.function.lower() == 'create':
    #     create_silencing_rule(curr_time_in_millisec,args.UPDATE_CLUSTER, args.API_TOKEN,args.IBMInstanceID,args.TIMEOUT.lower())
    # elif args.function.lower() == 'delete':
    #     delete_silencing_rule(args.UPDATE_CLUSTER,args.API_TOKEN,args.IBMInstanceID)
    # else:
    #     print('Invalid function name')
    
if __name__=='__main__':
    main()
