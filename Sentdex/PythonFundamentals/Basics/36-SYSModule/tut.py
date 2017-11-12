import sys

##'sys' is used for system input - output kind of stuff
##Command line - arguments stuff like that
##'argv' functionality is the interesting one
##out - error

sys.stderr.write("This is 'stderr' text!\n") ## Error text
sys.stderr.flush()
sys.stdout.write("This is 'stdout' text!\n") ## Out text

print(sys.argv) ##Basically gives the file name - File path

