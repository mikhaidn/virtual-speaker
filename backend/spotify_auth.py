import base64, json, requests

class SpotifyAuthenticator:
    SPOTIFY_URL_AUTH = 'https://accounts.spotify.com/authorize/?'
    SPOTIFY_URL_TOKEN = 'https://accounts.spotify.com/api/token/'
    RESPONSE_TYPE = 'code'   
    HEADER = 'application/x-www-form-urlencoded'
    REFRESH_TOKEN = ''
    TOKEN_DATA = []

    def __init__(self,redirect_uri):
        
#       sensitive, refactor locally with spotify app client/secret
        self.CLIENT_ID = None
        self.CLIENT_SECRET = None

        #Add needed scope from spotify user
        self.SCOPE = "streaming%20user-read-email%20user-read-private"

        self.redirect_uri = redirect_uri
              

    def buildAuthCall(self):

        data = (self.SPOTIFY_URL_AUTH +
            "client_id=" + self.CLIENT_ID+
            "&response_type=" + self.RESPONSE_TYPE +
            "&redirect_uri=" + self.redirect_uri+
            "&scope="  + self.SCOPE )
        return data

    def getToken(self, code):
        body = {
            "grant_type": 'authorization_code',
            "code" : code,
            "redirect_uri": self.redirect_uri,
        }

        message = "{}:{}".format(self.CLIENT_ID, self.CLIENT_SECRET)
        message_bytes = message.encode('utf-8')
        base64_bytes = base64.b64encode(message_bytes)
        base64_message = base64_bytes.decode('utf-8')

        auth_string = "Basic " + base64_message

        headers = {"Content-Type" : 'application/x-www-form-urlencoded', "Authorization" : auth_string} 

        post = requests.post(self.SPOTIFY_URL_TOKEN, params=body, headers=headers)

        response = json.loads(post.text)

        auth_head = {"Authorization": "Basic {}".format(response["access_token"])}
        self.REFRESH_TOKEN = response["refresh_token"]

        token = [response["access_token"], auth_head, response["scope"], response["expires_in"]]
        return token

    def refreshToken(self):
        body = {
            "grant_type" : "refresh_token",
            "refresh_token" : REFRESH_TOKEN
        }

        post_refresh = requests.post(SPOTIFY_URL_TOKEN, data=body, headers=HEADER)
        p_back = json.dumps(post_refresh.text)
        
        return handleToken(p_back)
