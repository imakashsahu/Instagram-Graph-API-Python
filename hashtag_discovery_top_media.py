import subprocess
import argparse, os, csv
import time
from defines import getCreds, makeApiCall
import sys

if __name__ == '__main__':
        filename = 'ig_hashtag_top_media.csv'
        open(filename, 'w').close()
        input = open('ig_hashtag_input.csv', 'r')
        content  = input.readlines()
        for line in content: 
                if line: 
                    ig_hashtag = line.strip()
                    #Function Declared
                    def getHashtagInfo( params ) :
                        endpointParams = dict() # parameter to send to the endpoint
                        endpointParams['user_id'] = params['instagram_account_id'] # user id making request
                        endpointParams['q'] = ig_hashtag # hashtag name
                        endpointParams['fields'] = 'id,name' # fields to get back
                        endpointParams['access_token'] = params['access_token'] # access token

                        url = params['endpoint_base'] + 'ig_hashtag_search' # endpoint url

                        return makeApiCall( url, endpointParams, params['debug'] )
            
                    
                    def getHashtagMedia( params ) :

                        endpointParams = dict() # parameter to send to the endpoint
                        endpointParams['user_id'] = params['instagram_account_id'] # user id making request
                        endpointParams['fields'] = 'id,permalink,comments_count,like_count,media_type,media_url,caption' # fields to get back
                        endpointParams['access_token'] = params['access_token'] # access token
                        
                        hashtagInfoResponse = getHashtagInfo( params ) # hit the api for some data!
                        params['hashtag_id'] = hashtagInfoResponse['json_data']['data'][0]['id']
                        
                        params['type'] = 'top_media' # set call to get top media for hashtag

                        url = params['endpoint_base'] + params['hashtag_id'] + '/' + params['type'] # endpoint url

                        return makeApiCall( url, endpointParams, params['debug'] ) # make the api call

                    params = getCreds() # get creds
                    params['debug'] = 'no' # set debug
                    response = getHashtagMedia( params ) # get users media from the api
                

                try:               
                    #Data From JSON
                    hashtag_post = response['json_data']['data']

                    #Data to CSV
                    with open(filename, 'a', encoding='utf-8') as csvfile:
                        employee_writer = csv.writer(csvfile, delimiter='\t', lineterminator='\r', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                        for pid in hashtag_post:
                            employee_writer.writerow([ig_hashtag,', ', pid.values()])

                    print(ig_hashtag + ' --- Done')
                except:
                    print(ig_hashtag + ' --- Failed')