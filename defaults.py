# Paths
# Fill this according to own setup
BACKGROUND_DIR = '/content/drive/MyDrive/datasets/background/farm/'
BACKGROUND_GLOB_STRING = '*.jpg'
POISSON_BLENDING_DIR = '/content/pb'
SELECTED_LIST_FILE = '/content/drive/MyDrive/datasets/pig_data_scripts/selected.txt'
DISTRACTOR_LIST_FILE = '' 
DISTRACTOR_DIR = ''
DISTRACTOR_GLOB_STRING = '*.jpg'
INVERTED_MASK = True # Set to true if white pixels represent background

# Parameters for generator
NUMBER_OF_WORKERS = 4
BLENDING_LIST = ['gaussian', 'none', 'box', 'motion']

# Parameters for images
MIN_NO_OF_OBJECTS = 1
MAX_NO_OF_OBJECTS = 4
MIN_NO_OF_DISTRACTOR_OBJECTS = 2
MAX_NO_OF_DISTRACTOR_OBJECTS = 4
WIDTH = 224
HEIGHT = 224
MAX_ATTEMPTS_TO_SYNTHESIZE = 20

# Parameters for objects in images
MIN_SCALE = 0.4 # min scale for scale augmentation
MAX_SCALE = 1.0 # max scale for scale augmentation
MAX_DEGREES = 30 # max rotation allowed during rotation augmentation
MAX_TRUNCATION_FRACTION = 0.25 # max fraction to be truncated = MAX_TRUNCACTION_FRACTION*(WIDTH/HEIGHT)
MAX_ALLOWED_IOU = 0.75 # IOU > MAX_ALLOWED_IOU is considered an occlusion
MIN_WIDTH = 6 # Minimum width of object to use for data generation
MIN_HEIGHT = 6 # Minimum height of object to use for data generation
