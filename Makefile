infile = relations.txt
outgv  = tree.gv
outpng = tree.png

view: tree
	open $(outpng)

tree:
	python tree.py --in $(infile) --out $(outgv)
	dot -Tpng $(outgv) > $(outpng)

clean:
	rm -f $(outgv) $(outpng)

