#!/bin/bash

WATCH_DIR="./"  # Replit 프로젝트 폴더 감시

while inotifywait -r -e create,modify "$WATCH_DIR"; do
    git add .
    git commit -m "Auto-commit: $(date +'%Y-%m-%d %H:%M:%S')"
    git push origin master  # 브랜치 이름이 main이 아닐 경우 수정
done