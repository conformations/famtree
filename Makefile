infile = relations.txt
outgv  = tree.gv
outps  = tree.ps
outpdf = tree.pdf

view: tree
	open $(outpdf)

tree:
	python tree.py --in $(infile) --out $(outgv)
	dot $(outgv) -Tps -o $(outps)
	ps2pdf $(outps)

clean:
	rm -f $(outgv) $(outps) $(outpdf)

