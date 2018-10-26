
default:
	@echo "Type \"make clean\" to remove unwanted files"

clean:
	make -C examples clean
	make -C lectures clean
	rm -rf .ipynb_checkpoints
