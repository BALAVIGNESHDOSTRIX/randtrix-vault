from typing import *

class RandtrixTools:
    """ Randtrix Tools """
    @staticmethod
    def index_manipulate(index:int=0) -> Dict:
        return {0: [index, index+1], 1: [index+1, index+2], 2: [index+2, index+3]}.get(index)