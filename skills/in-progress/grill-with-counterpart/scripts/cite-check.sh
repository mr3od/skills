#!/usr/bin/env bash
# List every `path:line` and `path:line-line` citation in a reply and say
# whether the path exists at the given commit and has that many lines.
# Usage: cite-check.sh <repo> <commit> <reply.md>
# Existence is the deterministic half of a citation check. Whether the cited
# text supports the claim is still read by a person or an agent.
set -euo pipefail
repo=$1; commit=$2; reply=$3
grep -oE '[A-Za-z0-9_./-]+\.[A-Za-z0-9]+:[0-9]+(-[0-9]+)?' "$reply" | sort -u | while IFS= read -r cite; do
    path=${cite%%:*}; range=${cite#*:}; last=${range#*-}
    if ! n=$(git -C "$repo" show "$commit:$path" 2>/dev/null | wc -l); then
        echo "MISSING  $cite  (no such path at $commit)"; continue
    fi
    if [ "$last" -gt "$n" ]; then
        echo "SHORT    $cite  (file has $n lines at $commit)"
    else
        echo "EXISTS   $cite"
    fi
done
