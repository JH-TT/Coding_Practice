#!/bin/bash

WATCH_DIR="./"  # 감시할 디렉토리

# 제외할 파일/디렉토리 패턴 (정규 표현식 사용)
EXCLUDE_PATTERN="(\.git/|watch\.log|node_modules/|.*\.tmp)"

while inotifywait -r -e create,modify --exclude "$EXCLUDE_PATTERN" "$WATCH_DIR"; do
    git add .
    git commit -m "Auto-commit: $(date +'%Y-%m-%d %H:%M:%S')"
    git push origin main
done