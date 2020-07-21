from defines import getCreds, makeApiCall

def getLongLivedAccessToken( params ) :

	endpointParams = dict() # parameter to send to the endpoint
	endpointParams['grant_type'] = 'fb_exchange_token' # tell facebook we want to exchange token
	endpointParams['client_id'] = params['client_id'] # client id from facebook app
	endpointParams['client_secret'] = params['client_secret'] # client secret from facebook app
	endpointParams['fb_exchange_token'] = params['access_token'] # access token to get exchange for a long lived token

	url = params['endpoint_base'] + 'oauth/access_token?' # endpoint url

	return makeApiCall( url, endpointParams, params['debug'] ) # make the api call

params = getCreds() # get creds
params['debug'] = 'yes' # set debug
response = getLongLivedAccessToken( params ) # hit the api for some data!

print ("\n ---- ACCESS TOKEN INFO ----\n") # section header
print ("Access Token:")  # label
print (response['json_data']['access_token']) # display access token