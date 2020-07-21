import requests
import json

def getCreds() :

	creds = dict() # dictionary to hold everything
	creds['access_token'] = 'EAAKeNEINqmwBAJts9o23ZCXAl66YBCLFQxTuHlTXsA6U5oVa3Fm7vch3AkoxURk8e427V9MbX0sHSwaiQ8CtZBojopZABbxZBTc4j0JNxYaI88NcgiZCxdU3jDLIKedmPK0DXITLZBJUhDY4d6ZCBDDrejaZBYAFZB65ybCILSHyYagZDZD' # access token for use with all api calls
	creds['client_id'] = '736897237101164' # client id from facebook app IG Graph API Test
	creds['client_secret'] = '0d08cbbb40c805926931849a95fc5d25' # client secret from facebook app
	creds['graph_domain'] = 'https://graph.facebook.com/' # base domain for api calls
	creds['graph_version'] = 'v7.0' # version of the api we are hitting
	creds['endpoint_base'] = creds['graph_domain'] + creds['graph_version'] + '/' # base endpoint with domain and version
	creds['debug'] = 'no' # debug mode for api call
	creds['page_id'] = '100760741699255' # users page id after running the "get_user_facebook_page.py"
	creds['instagram_account_id'] = '17841406228315535' # users instagram account id after running the "get_user_instagram_page.py"
	creds['ig_username'] = 'imakashsahu' # ig username to get details

	return creds

def makeApiCall( url, endpointParams, debug = 'no' ) :

	data = requests.get( url, endpointParams ) # make get request

	response = dict() # hold response info
	response['url'] = url # url we are hitting
	response['endpoint_params'] = endpointParams #parameters for the endpoint
	response['endpoint_params_pretty'] = json.dumps( endpointParams, indent = 4 ) # pretty print for cli
	response['json_data'] = json.loads( data.content ) # response data from the api
	response['json_data_pretty'] = json.dumps( response['json_data'], indent = 4 ) # pretty print for cli

	if ( 'yes' == debug ) : # display out response info
		displayApiCallData( response ) # display response

	return response # get and return content

def displayApiCallData( response ) :
	""" Print out to cli response from api call """

	print ("\nURL: ") # title
	print (response['url']) # display url hit
	print ("\nEndpoint Params: ") # title
	print (response['endpoint_params_pretty']) # display params passed to the endpoint
	print ("\nResponse: ") # title
	print (response['json_data_pretty']) # make look pretty for cli