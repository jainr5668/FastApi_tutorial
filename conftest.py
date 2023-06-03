import multiprocessing
import pytest, time
import os

PORT = 8000


class UvicornTestServer():
    """ Test the app class. """
    def start_server(self):
        os.system('uvicorn app.main:app')
        
    def setUp(self):
        """ Bring server up. """
        self.proc = multiprocessing.Process(target=self.start_server)
        self.proc.start()
        print("waiting for server to start")
        time.sleep(8)

    def tearDown(self):
        """ Shutdown the app. """
        self.proc.terminate()
        self.proc.kill()
        


@pytest.fixture
def startup_and_shutdown_server():
    print("inconftest.py")
    """Start server as test fixture and tear down after test"""
    server = UvicornTestServer()
    server.setUp()
    yield
    print('test completed')
    server.tearDown()