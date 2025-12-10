import requests
from decouple import config

#test

class CallMeBot:
    
    def __init__(self):
        self.__base_url = config('BASE_URL')
        self.__phone_number = config('PHONE_NUMBER')
        self.__api_key = config('API_KEY')

    def send_message(self, message):
        URL = f'{self.__base_url}phone={self.__phone_number}&text={message}&apikey={self.__api_key}'
        __response = requests.get(url=URL)

        # data = __response.text
        # print(__response.text)
        
        return __response

if __name__ == '__main__':
    c = CallMeBot()
    c.send_message('Testando')
    print('foi')