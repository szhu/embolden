#!/usr/bin/env python

def main():
    from sys import stdin
    from re import sub
    prefix = '  '
    for line in stdin:
        line = line.rstrip('\n')
        if line.startswith('\\'):
            print line
            continue
        tabsize = (len(line) - len(line.lstrip())) * 0.75
        for word in ('define,if,else,accept,reject,return,loop forever,repeat,fork,for,:='.split(',')):
            pattern = r'\b%s\b' % word
            if word == ':=':
                pattern = word
                word = ':='
            line = sub(pattern, '\\\\textbf{%s}' % word, line)
        print prefix + ('\hspace*{%.1fem} ' % tabsize) + line
        prefix = '\\\\'

    return 0


##


class ProgramError(Exception):
    pass

def run():
    from sys import argv, stderr
    try:
        exit(main(*argv[1:]) or 0)
    except ProgramError, exc:
        print >> stderr, exc
    except TypeError, exc:
        if exc.message.startswith("main() takes"):
            print >> stderr, exc
        else:
            raise

if __name__ == '__main__':
    run()
