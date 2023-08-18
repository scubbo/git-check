These are my own personal notes while developing so that I remember what I did, what I tried, and what I learned! These shouldn't be pushed to `main` :P

## Tasks

- [X] Get a working CLI implementation that can be executed to print "Hello World!"
- [X] Basic Config parsing (monitored directories)
- [ ] Exclusion by pattern (e.g. `node_modules`)
- [ ] Build-and-publish workflow (inc. version-increment?)
- [ ] (Below this line, sequencing is a bit more fluid)
- [ ] Installation logic (prompt for directories to monitor)
- [ ] Background scanning?


## Open Questions

* The [workflow I'm copying from](https://github.com/simonw/datasette/blob/943df09dcca93c3b9861b8c96277a01320db8662/.github/workflows/publish.yml#L60) uses `bdist_wheel`, but that gives an error when I try (`error: invalid command 'bdist_wheel'`) - lets see if just `sdist` is sufficient