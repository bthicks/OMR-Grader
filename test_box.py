class TestBox:

    '''
    Constructor for a new test box.

    Args:
        page (numpy.ndarray): An ndarray representing the test image.
        config (dict): A dictionary containing the config file values for this
            test box.
        verbose_mode (bool): True to run program in verbose mode, False 
            otherwise.
        debug_mode (bool): True to run the program in debug mode, False 
            otherwise.

    Returns:
        TestBox: A newly created test box.

    '''
    def __init__(self, page, config, verbose_mode, debug_mode):
        self.page = page
        self.config = config
        self.verbose_mode = verbose_mode
        self.debug_mode = debug_mode

        self.name = config['name']
        self.type = config['type']
        self.orientation = config['orientation']
        self.x = config['x']
        self.y = config['y']
        self.rows = config['rows']
        self.columns = config['columns']
        self.groups = config['groups']

        self.bubbled = []
        self.unsure = []
        self.images = []
        self.status = 0

    '''
    Finds and grades a test box within a test image.

    Returns:
        data (dict): A dictionary containing info about the graded test box.

    '''
    def grade(self):
        # Initialize dictionary to be returned.
        data = {
            'status' : 0,
            'error' : ''
        }

        return data

