@PHONY: clean
clean:
	rm -f *.wav *.mp3

build:
	docker build -t tickloop/kokoro-serve:latest .