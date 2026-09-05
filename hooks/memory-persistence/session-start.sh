#!/bin/bash
# SessionStart Hook - Load previous context on new session
#
# Runs when a new OpenCode session starts. Checks for recent session
# files and notifies OpenCode of available context to load.
#
# Hook config (in ~/.config/opencode/opencode.jsonc via plugin or hooks):
# {
#   "hooks": {
#     "SessionStart": [{
#       "matcher": "*",
#       "hooks": [{
#         "type": "command",
#         "command": "~/.config/opencode/hooks/memory-persistence/session-start.sh"
#       }]
#     }]
#   }
# }

SESSIONS_DIR="${HOME}/.config/opencode/sessions"
LEARNED_DIR="${HOME}/.config/opencode/skills/learned"

# Check for recent session files (last 7 days)
recent_sessions=$(find "$SESSIONS_DIR" -name "*.tmp" -mtime -7 2>/dev/null | wc -l | tr -d ' ')

if [ "$recent_sessions" -gt 0 ]; then
  latest=$(ls -t "$SESSIONS_DIR"/*.tmp 2>/dev/null | head -1)
  echo "[SessionStart] Found $recent_sessions recent session(s)" >&2
  echo "[SessionStart] Latest: $latest" >&2
fi

# Check for learned skills
learned_count=$(find "$LEARNED_DIR" -name "*.md" 2>/dev/null | wc -l | tr -d ' ')

if [ "$learned_count" -gt 0 ]; then
  echo "[SessionStart] $learned_count learned skill(s) available in $LEARNED_DIR" >&2
fi
