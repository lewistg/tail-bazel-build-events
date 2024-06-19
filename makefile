proto_out := . 
proto_src := proto_src
proto_files := $(wildcard $(proto_src)/proto/*.proto)

.PHONY: proto
proto: $(proto_files)
	protoc -I $(proto_src) --python_out=$(proto_out) $^
