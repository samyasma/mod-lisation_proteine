# Comparative using a provided initial structure file (inifile)
from modeller import *
from modeller.automodel import *    # Load the automodel class

log.verbose()
env = environ()

# directories for input atom files
env.io.atom_files_directory = ['.', './']

a = automodel(env,
              alnfile  = 'sequence4DOJ_C_BetT.fasta',     # alignment filename
              knowns   = '4DOJ_C',              # codes of the templates
              sequence = 'BetT'             #code of the target
              )    # use 'my' initial structure
a.starting_model= 1                 # index of the first model
a.ending_model  = 5                 # index of the last model
                                    # (determines how many models to calculate)
a.make()                            # do comparative modeling

