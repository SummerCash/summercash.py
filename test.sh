echo "testing files:"
for f in ./src/*.py;
    do echo "$f";
done

for f in ./src/*.py;
    do python3 "$f";
done
