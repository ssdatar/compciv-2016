from os.path import join
from glob import glob

def file_read(fname):
    play = open(fname, 'r')
    total_count = 0
    nonblank = 0
    for line in play:
        total_count += 1
        if line.strip() != '':
            nonblank += 1
    play.close()
    
    answer = [nonblank, total_count]

    print(fname, 'has', nonblank,
          'non-blank lines out of', total_count, 'total lines')   

    return answer

total_answer = 0
nonblank_answer = 0

path = join('tempdata', '**', '*')
filenames = glob(path)
for fname in filenames:
    filecounts = file_read(fname)
    nonblank_answer += filecounts[0]
    total_answer += filecounts[1]

print("All together, Shakespeare's",
      len(filenames), "text files have:")
print(nonblank_answer,"non-blank lines out of",
      total_answer, "total lines")