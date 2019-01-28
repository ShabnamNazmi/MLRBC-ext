SEED_NUMBER = 161
NUMBER_OF_FOLDS = 1
NO_EXPERIMENTS_AVERAGING = 1
DO_AVERAGING = True
NO_PARALLEL_JOBS = 10


DATA_HEADER = "data10"
NO_ATTRIBUTES = 2
VALID_DATA_HEADER = DATA_HEADER + "-test"
TRAIN_DATA_HEADER = DATA_HEADER + "-train"
DATA_FOLDER = "C:\Datasets\synthetic"
RUN_RESULT_PATH = "Run_results_MLRBC"

NO_TRAIN_ITERATION = 5000
POP_SIZE = 1000
DISTRIBUTED_MATCHING_TH = 6000
REF_CARDINALITY = None            # set to 'None' for no density adaptation
DOWN_SAMPLE_RATIO = 1
PREDICTION_METHOD = 'max'
ADAPT_THETA_GA = False
PLOT_SETTING = [0, 1, 1, 0, 1]   # population sizes, accuracy, Hloss, generality, TP & TN


