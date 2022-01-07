#!/usr/bin/env bash

if [ "$(uname)" == "Darwin" ]; then
     python3 .        
elif [ "$(expr substr $(uname -s) 1 5)" == "Linux" ]; then
    python3 .
elif [ "$(expr substr $(uname -s) 1 10)" == "MINGW32_NT" ]; then
    python .
elif [ "$(expr substr $(uname -s) 1 10)" == "MINGW64_NT" ]; then
    python .
fi
