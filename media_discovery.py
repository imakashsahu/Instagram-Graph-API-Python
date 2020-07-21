import subprocess
import argparse, os, csv
import time
from defines import getCreds, makeApiCall

if __name__ == '__main__':
        filename = 'ig_media.csv'
        open(filename, 'w').close()
        input = open('ig_username.csv', 'r')
        content  = input.readlines()
        for line in content: 
                if line: 
                    ig_username = line.strip()
                    #Function Declared
                    def getUserMedia( params, pagingUrl = '' ) :
    
                        endpointParams = dict() # parameter to send to the endpoint
                        endpointParams['fields'] = 'business_discovery.username(' + ig_username + '){media{username,id,permalink,like_count,comments_count,media_type,media_url,timestamp,caption}}' # fields to get back
                        endpointParams['access_token'] = params['access_token'] # access token

                        if ( '' == pagingUrl ) : # get first page
                            url = params['endpoint_base'] + params['instagram_account_id'] # endpoint url
                        else : # get specific page
                            url = pagingUrl  # endpoint url

                        return makeApiCall( url, endpointParams, params['debug'] ) # make the api call

                    params = getCreds() # get creds
                    params['debug'] = 'no' # set debug
                    response = getUserMedia( params ) # get users media from the api

                try:               
                    #Data From JSON
                    user_post = response['json_data'] 
                    post = user_post['business_discovery']['media']['data']

                    #Data to CSV
                    with open(filename, 'a', encoding='utf-8') as csvfile:
                        employee_writer = csv.writer(csvfile, delimiter='\t', lineterminator='\r', quotechar='"', quoting=csv.QUOTE_MINIMAL)

                        count = 0
                        for pid in post:
                            if count == 0:                                
                                header = pid.keys()
                                count += 1
                            employee_writer.writerow([ig_username,', ', pid.values()])
                    print(ig_username + ' --- Done')
                except:
                    print(ig_username + ' --- Failed')