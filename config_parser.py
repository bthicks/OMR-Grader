class Parser:

    page_keys = ['page_width', 'page_height', 'bubble_width', 'bubble_height', 
        'qr_x', 'qr_y', 'x_error', 'y_error', 'boxes']

    box_keys = ['name', 'type', 'orientation', 'x', 'y', 'rows', 'columns', 
        'groups']

    group_keys = ['x_min', 'x_max', 'y_min', 'y_max']

    box_types = ['letter', 'number']

    box_orientations = ['left-to-right', 'top-to-bottom']

    def __init__(self, config, fname):
        self.config = config
        self.fname = fname
        self.status = 0
        self.error = ''

    def type_error(self, key, want, got):
        self.status = 1
        self.error = 'Key \'%s\' expected %s, found %s' % (key, want, got)

    def unknown_key_error(self, key):
        self.status = 1
        self.error = 'Unknown key \'%s\' in %s' % (key, self.fname)

    def missing_key_error(self, key, dict_name):
        self.status = 1
        self.error = 'Missing key \'%s\' in %s' % (key, dict_name)

    def unknown_value_error(self, key, value):
        self.status = 1
        self.error = 'Unknown value \'%s\' for key \'%s\'' % (value, key)

    def parse_int(self, key, value):
        if not (isinstance(value, int)):
            self.type_error(key, 'int', type(value))

    def parse_float(self, key, value):
        if not (isinstance(value, float)):
            self.type_error(key, 'float', type(value))

    def parse_box_orientation(self, orientation):
        if (orientation not in self.box_orientations):
            self.unknown_value_error('orientation', orientation)

    def parse_box_type(self, box_type):
        if (box_type not in self.box_types):
            self.unknown_value_error('type', box_type)

    def parse_string(self, key, value):
        if (isinstance(value, str)):
            if (key == 'type'):
                self.parse_box_type(value)
            elif (key == 'orientation'):
                self.parse_box_orientation(value)
        else:
            self.type_error(key, 'str', type(value))

    def parse_group_key(self, key, value):
        self.parse_float(key, value)

    def parse_group(self, group):
        if (isinstance(group, dict)):
            for key in self.group_keys:
                if key not in group:
                    self.missing_key_error(key, 'group')
                    break

            for (key, value) in group.items():
                if (key in self.group_keys):
                    self.parse_group_key(key, value)
                else:
                    self.unknown_key_error(key)
                    break
        else:
            self.type_error('group', 'dict', type(group))

    def parse_groups(self, groups):
        if (isinstance(groups, list)):
            for group in groups:
                self.parse_group(group)
        else:
            self.type_error('groups', 'list', type(groups))

    def parse_box_key(self, key, value):
        if (key == 'name' or key == 'type' or key == 'orientation'):
            self.parse_string(key, value)
        elif (key == 'x' or key == 'y'):
            self.parse_float(key, value)
        elif (key == 'rows' or key == 'columns'):
            self.parse_int(key, value)
        elif (key == 'groups'):
            self.parse_groups(value)

    def parse_box(self, box):
        if (isinstance(box, dict)):
            for key in self.box_keys:
                if key not in box:
                    self.missing_key_error(key, 'box')
                    break

            for (key, value) in box.items():
                if (key in self.box_keys):
                    self.parse_box_key(key, value)
                else:
                    self.unknown_key_error(key)
                    break
        else:
            self.type_error('box', 'dict', type(box))

    def parse_boxes(self, boxes):
        if (isinstance(boxes, list)):
            for box in boxes:
                self.parse_box(box)
        else:
            self.type_error('boxes', 'list', type(boxes))

    def parse_page_key(self, key, value):
        if (key == 'boxes'):
            self.parse_boxes(value)
        else:
            self.parse_float(key, value)

    def parse(self):
        if (isinstance(self.config, dict)):
            for key in self.page_keys:
                if key not in self.config:
                    self.missing_key_error(key, 'config')
                    break

            for (key, value) in self.config.items():
                if (key in self.page_keys): 
                    self.parse_page_key(key, value)
                else:
                    self.unknown_key_error(key)
                    break
        else:
            self.type_error('config', 'dict', type(self.config))

        return (self.status, self.error)


def duplicate_key_check(ordered_pairs):
    '''
    Raise value error if duplicate keys detected in config file.

    Args:
        ordered_pairs (list): A key/value pair in the config file.

    Returns:
        d (dict): A dictionary containing the key/value pair.

    '''
    d = {}

    for (key, value) in ordered_pairs:
        if (key in d):
            raise ValueError('duplicate key: %r' % key)
        else:
            d[key] = value

    return d
