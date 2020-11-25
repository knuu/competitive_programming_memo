import argparse
from collections import defaultdict
from pathlib import Path
from textwrap import wrap

from prettytable import PrettyTable


class Problem:
    def __init__(self, problem, contest_name):
        self.contest_name = contest_name
        self.name = problem[0][1:].strip()
        tags = [line for line in problem if line.startswith('- タグ')]
        if tags:
            self.tags = tags[0][5:].strip().split('、')
        else:
            self.tags = []
        level = [line for line in problem if line.startswith('- レベル')]
        if level:
            self.level = level[0][6:].strip()
        else:
            self.level = '?'
        score = [line for line in problem if line.startswith('- 配点')]
        if score:
            self.score = int(score[0][5:].strip())
        else:
            self.score = None

    def __str__(self):
        return '{:20}: {:60}|{}|{}'.format(self.contest_name,
                                           self.name,
                                           self.level,
                                           self.tags,
                                           self.score)


all_problems = []

for diary in sorted(Path('.').glob('*.md')):
    contest_name = diary.stem
    if contest_name == 'format':
        continue
    f = open(str(diary))
    lines = f.readlines()
    p_index = [i for i, line in enumerate(lines) if line[0] == '#']
    p_index.append(len(lines))
    for i in range(len(p_index) - 1):
        problem = Problem(lines[p_index[i]:p_index[i+1]], contest_name)
        all_problems.append(problem)


def search_tag(target_tag):
    return [p for p in all_problems if any(target_tag.lower() in tag.lower() for tag in p.tags)]


def show_tagged_problems(target_tag, problems=all_problems):
    probs = search_tag(target_tag)
    show_table(probs)


def show_scored_problems(problems=all_problems):
    probs = [p for p in all_problems if p.score]
    probs.sort(key=lambda x: (x.score, x.contest_name))
    show_table(probs)


def show_table(probs):
    table = PrettyTable(["Contest", "Title", "Lv.", "Tags", "Score"])
    for prob in probs:
        table.add_row([
            prob.contest_name,
            '\n'.join(wrap(prob.name, 25)),
            prob.level,
            '\n'.join(wrap_tags(prob.tags, 20)),
            prob.score])
    print(table)


def wrap_tags(tags, width=20):
    ret = []
    line = ''
    for tag in tags:
        if len(line) + len(tag) + 1 <= width:
            line += tag + ','
        else:
            ret.append(line)
            line = tag + ','
    if line:
        ret.append(line.strip(','))
    return ret


def get_all_tags(problems=all_problems):
    all_tags = set()
    for problem in problems:
        for tag in problem.tags:
            all_tags.add(tag)
    return all_tags


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('tags', metavar='T', help='tags to search', nargs='*')
    parser.add_argument('--alltags', help='show all tags', action="store_true")
    parser.add_argument(
        '--allscores', help='show all problems with score', action="store_true")
    args = parser.parse_args()
    if args.allscores:
        show_scored_problems()
    elif args.alltags:
        tagged_all_problems = [(tag, len(search_tag(tag)))
                               for tag in get_all_tags()]
        tagged_all_problems.sort(key=lambda x: x[0])
        for tag, c in tagged_all_problems:
            print(tag, c)
    elif args.tags:
        for tag in args.tags:
            show_tagged_problems(tag)
    else:
        parser.print_usage()
