#!/usr/bin/env python
import os
import sys
import argparse
from re import compile

try:
    from git import Repo, GitCommandError
except ImportError:
    sys.stderr.write('GitPython is required to create the changelog!\n')
    sys.exit(1)

#
# Setup args parser.
#

parser = argparse.ArgumentParser(description='Changelog generator')
parser.add_argument('commit', help='Latest git commit (HEAD, SHA, tag, branch) to include in changelog', type=str)
args = parser.parse_args()

#
# Commit messages to examine from log.
#

reg = '{prefix} ?(#\d+)?: ?(.*)'

examine = (
    (
        'FEATURE',
        'New Features',
        compile(reg.format(prefix='FEATURE'))
    ),
    (
        'BUGFIX',
        'Fixed Bugs',
        compile(reg.format(prefix='BUGFIX'))
    ),
    (
        'DOCS',
        'Documentation Changes',
        compile(reg.format(prefix='DOCS'))
    )
)

#
# Prepare Git instance.
#

# Create Git repo instance.
repo = Repo(os.path.dirname(__file__))
git  = repo.git

# Get all tags and sort them properly.
tags = map(lambda r: r.tag.tag, repo.tags)
tags.sort(key=lambda r: map(int, r[1:].split('.')))
tags.append(args.commit)

#
# Prepare changelog dict.
#

changelog = {}

for tag in tags:
    changelog[tag] = {}
    for prefix, heading, reg in examine:
        changelog[tag][prefix] = []

#
# Examine all commit messages.
#

# Loop through all tags.
for i in range(0, len(tags)):

    # Get current tag.
    current_tag = tags[i]

    # Get last tag.
    # In case there isn't a last tag, use the root commit.
    if i:
        last_tag = tags[i - 1]
    else:
        last_tag = git.rev_list('--max-parents=0', 'HEAD').split()[-1]

    # Get all commits between last and current tag.
    try:
        commits = git.rev_list('{last}..{current}'.format(current=current_tag, last=last_tag)).split()
    except GitCommandError, e:
        sys.stderr.write(str(e) + '\n')
        sys.exit(1)

    # Loop through all commits.
    for commit in commits:

        # Examine commit message.
        message = repo.commit(commit).message.split('\n')[0]

        # Test message against prefixes.
        for prefix, heading, reg in examine:
            match = reg.match(message)
            if match:
                changelog[current_tag][prefix].append(match.groups())

#
# Create markdown.
#

# Reverse tags so that the newest tag is on top.
tags.reverse()

# Loop through all tags.
for tag in tags:

    # Print tag heading.
    sys.stdout.write(tag + '\n')
    sys.stdout.write('=' * len(tag) + '\n\n')

    # Print tag changes.
    changes = changelog[tag]
    for prefix, heading, reg in examine:

        if changes[prefix]:

            sys.stdout.write(heading + '\n')
            sys.stdout.write('-' * len(heading) + '\n\n')

            for change in changes[prefix]:
                issue   = ' [' + change[0] + ']' if change[0] else ''
                message = change[1]
                sys.stdout.write('* ' + message + issue + '\n')

            sys.stdout.write('\n')

    sys.stdout.flush()
