echo "testing files:"
for f in ./src/*.py;
    do echo "$f";
done

for f in ./src/*.py;
    do python3 "$f";
done

for f in ./src/proto/*.py;
    do echo "$f";
done

for f in ./src/tests/*.py;
    do python3 "$f";
done