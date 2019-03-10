class TestBox:

    def __init__(self, page, config, verbose_mode):
        self.page = page
        self.config = config
        self.verbose_mode = verbose_mode

        self.bubbled = []
        self.unsure = []
        self.images = []
        self.status = 0