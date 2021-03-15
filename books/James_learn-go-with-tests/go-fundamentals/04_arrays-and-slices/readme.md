### Test coverage
Run `go test -cover` to use the test coverage tool.

### Slices

Slices can be created using `make` function.

A slice has both a length and a capacity.

The length of a slice is the number of elements it contains.

The capacity of a slice is the number of elements in the underlying array, counting from the first element in the slice.

The length and capacity of a slice s can be obtained using the expressions `len(s)` and `cap(s)`

**Reference**: [Slice length and capacity](https://tour.golang.org/moretypes/11)