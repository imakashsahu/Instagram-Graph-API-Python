# Instagram-Graph-API (Python)
This Repository Focus on the New ***Instagram Graph API*** and ***Fetches*** the Input from the ***CSV file*** and ***Writes*** the data in to ***CSV file*** as well.

## LIBRARYS NEEDED
```
1. subprocess
2. argparse
3. os
4. csv
5. requests
6. json
```
## STEPS TO FOLLOW
1. Create a *Facebook App* at developers.facebook.com 
2. Go to *Graph API Tools* to obtain the Access Token (https://developers.facebook.com/tools/explorer/)
3. Select User Token and Add the following permissions to access the Instagram Graph API
        *instagram_basic*
        *instagram_manage_comments*
        *instagram_manage_insights*
        *pages_read_engagement*
        *pages_show_list*
4. Generate the Access Token valid for 1 Hour
5. Now Copy the Access Token and Enter in  ***defines.py***
6. Copy you **Client ID** and **Client Secret Key** from the developers.facebook.com App
7. Now run the ***debug_access_token.py*** file to check the connection to the  ***Graph API***
8. Now run ***get_long_lived_access_token.py*** to get access token valid for 60 Days & Enter this in ***defines.py***
9. Now run ***get_uer_facebook_pages.py***  to get the **Facebook Page ID** & Enter this in ***defines.py***
10. Now run ***get_uer_instagram_account.py***  to get the **Instagram Account ID** & Enter this in ***defines.py***
11. Now Enter the Instagram Username you wish to fetch details of in the ***ig_username.csv*** file
12. Now run ***business_discovery.py*** to fetch the details of the usernames you entered in the ***ig_username.csv*** file
13. Now open the ***ig_business.csv*** newly created and verify for desired results
14. Now run ***media_discovery.py*** to fetch the details of the usernames you entered in the ***ig_username.csv*** file
15. Now open the ***ig_media.csv*** newly created and verify for desired results
16. Now Enter the Instagram Hashtag you wish to fetch Post of in the ***ig_hashtag_input.csv*** file
17. Now run ***hashtag_discovery_recent_media.py*** to fetch the details of the usernames you entered in the ***ig_hashtag_input.csv*** file
18. Now open the ***ig_hashtag_top_media.csv*** newly created and verify for desired results
19. Now run ***hashtag_discovery_top_media.py*** to fetch the details of the usernames you entered in the ***ig_hashtag_input.csv*** file
20. Now open the ***ig_hashtag_top_media.csv*** newly created and verify for desired results


