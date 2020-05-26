'''
Chain of Responsibility
	- Opens various of possibilities of processing for a given request
	- Decouples a request and its processing
	- Problem
		+ One Request that can have various types of processing
	- Useful When
		+ Web/threads
	- Resources
		+ https://www.geeksforgeeks.org/chain-of-responsibility-python-design-patterns/
		+ 
'''


class Handler:  # Abstract handler
    """Abstract Handler"""

    def __init__(self, successor):
        self._successor = successor  # Define who is the next handler

    def handle(self, request):
        handled = self._handle(request)  # If handled, stop here

        # Otherwise, keep going
        if not handled:
            self._successor.handle(request)

    def _handle(self, request):
        raise NotImplementedError('Must provide implementation in subclass!')


class ConcreteHandler(Handler):  # Inherits from the abstract handler
    """Concrete handler 1"""

    def _handle(self, request):
        if 0 < request <= 10:  # Provide a condition for handling
            print("Request {} handled in handler 1".format(request))
            return True  # Indicates that the request has been handled


class DefaultHandler(Handler):  # Inherits from the abstract handler
    """Default handler"""

    def _handle(self, request):
        """If there is no handler available"""

        # No condition checking since this is a default handler
        print("End of chain, no handler for {}".format(request))

        return True  # Indicates that the request has been handled


class Client:  # Using handlers
    def __init__(self):
        # Create handlers and use them in a sequence you want
        # Note that the default handler has no successor
        self.handler = ConcreteHandler(DefaultHandler(None))

    def delegate(self, requests):  # Send your requests one at a time for handlers to handle
        for request in requests:
            self.handler.handle(request)


# Create a client
c = Client()

# Create requests
requests = [2, 5, 30]

# Send the requests
c.delegate(requests)
