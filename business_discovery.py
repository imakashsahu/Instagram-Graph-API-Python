import subprocess
import argparse, os, csv
import time
from defines import getCreds, makeApiCall

if __name__ == '__main__':
        filename = 'ig_business.csv'
        open(filename, 'w').close()
        input = open('ig_username.csv', 'r')
        content  = input.readlines()
        for line in content: 
                if line: 
                    ig_username = line.strip()
                    #Function Declared
                    def getAccountInfo( params ) :
                        
                        endpointParams = dict() # parameter to send to the endpoint
                        endpointParams['fields'] = 'business_discovery.username(' + ig_username + '){id,name,follows_count,followers_count,media_count,website,profile_picture_url,biography}' # string of fields to get back with the request for the account
                        endpointParams['access_token'] = params['access_token'] # access token

                        url = params['endpoint_base'] + params['instagram_account_id'] # endpoint url

                        return makeApiCall( url, endpointParams, params['debug'] ) # make the api call

                params = getCreds() # get creds
                params['debug'] = 'no' # set debug
                response = getAccountInfo( params ) # hit the api for some data!

                try:               
                    #Data From JSON
                    user_id = response['json_data']['business_discovery']['id']
                    name = response['json_data']['business_discovery']['name']
                    follows_count = response['json_data']['business_discovery']['follows_count']
                    follower_count = response['json_data']['business_discovery']['followers_count']
                    media_count = response['json_data']['business_discovery']['media_count']
                    website = response['json_data']['business_discovery']['website']
                    profile_pic = response['json_data']['business_discovery']['profile_picture_url']
                    biography = response['json_data']['business_discovery']['biography']
                    bio = str(biography.encode("utf-8"))
                    #Data to CSV
                    with open(filename, 'a', encoding='utf-8') as csvfile:
                        employee_writer = csv.writer(csvfile, delimiter='\t', lineterminator='\r', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                        employee_writer.writerow([ig_username,', ', name,', ', follows_count,', ', follower_count,', ', media_count,', ', user_id,', ', website,', ', profile_pic,', ', bio])

                    print(ig_username + ' --- Done')
                except:
                    print(ig_username + ' --- Failed')
                # time.sleep(10)  #Delay between every API CALL  