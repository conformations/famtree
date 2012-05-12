image:
	python tree.py relations.txt
	dot tree.gv -Tps -o tree.ps
	ps2pdf tree.ps

clean:
	rm -f tree.gv tree.pdf tree.ps

