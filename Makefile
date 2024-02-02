DISTS:=sid bookworm bullseye buster stretch wheezy precise trusty xenial bionic focal jammy

all: clean
	for i in $(DISTS) ; do \
		./create_dockerfile.sh $$i; \
	done

clean:
	rm -rf $(DISTS)

pull:
	cd src;	git pull
