class Status(object):
    def __init__(self) -> None:
        self.status = 1
        self.message = ""
        self.changeStatus(self.status) # Use the changeStatus method to generate the message
    def changeStatus(self, status: int, message:str | None = None):
        """Change Status of Server

        Args:
            status (int): Status Code 0-4
            message (str | None, optional): Message; Defaults Provided for Code. Defaults to None.
        """
        statuses = {
            0:"Everything working just fine.",
            1:"Minor Bugs.",
            2:"Bugs; Development needed.",
            3:"Development underway; check back later.",
            4:"Deprecated. Find a new serivce. :)",
        }
        # Change Status and then Message based from status
        self.status = status
        if message is not None:
            # If message is provided 
            self.message = message
        elif status <= 4 and status >= 0: 
            # Defaults for Status
            self.message = statuses[status]

        def __call__(self, status:int, message: str | None = None):
            """Change Status of Server
    
            Args:
                status (int): Status Code 0-4
                message (str | None, optional): Message; Defaults Provided for Code. Defaults to None.
            """
            self.changeStatus(status=status, message=message)