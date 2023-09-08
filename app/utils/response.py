

class ResponseSuccess:
    def __init__(self, data, message):
        self.statusCode = 200
        self.message = message
        self.data = data

    def getResponse(self):
        return {
            "statusCode": self.statusCode,
            "message": self.message,
            "data": self.data
        }


class ResponseError:
    def __init__(self, data, message):

        self.message = message
        self.data = data

    def getResponse(self):

        name = self.data['name']
        print('yoyo', name)
        if (name == 'bad_request'):

            return {
                "statusCode": 400,
                "message": self.message,
                "data": self.data
            }

        if (name == 'forbidden'):

            return {
                "statusCode": 403,
                "message": self.message,
                "data": self.data
            }

        if (name == 'unauthorized'):

            return {
                "statusCode": 401,
                "message": self.message,
                "data": self.data
            }

        else:
            return {
                "statusCode": 500,
                "message": "Something Went wrong",
                "data": self.data
            }
