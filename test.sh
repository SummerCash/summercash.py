#!/usr/bin/env bash
echo "Installing requirements:"
/usr/bin/python3 -m pip install -r requirements.txt

echo "Testing files:"
for f in ./src/*.py;
    do echo "$f";
done

for f in ./src/*.py;
    do python3 "$f";
done
