DISTS:=sid trixie bookworm bullseye resolute noble jammy

all: clean
	for i in $(DISTS) ; do \
		./create_dockerfile.sh $$i; \
	done

clean:
	rm -rf $(DISTS)

pull:
	cd src;	git pull
