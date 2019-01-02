go_lib:
	go build -buildmode=c-shared -o build/go_lib.so ./go_src

c_api: c_src/main.c build/go_lib.so
	$(CC) -o build/$@.out $^

clean:
	rm -rf build/