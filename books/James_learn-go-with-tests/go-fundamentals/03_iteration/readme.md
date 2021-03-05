In go, there is no `while`, `do` and `until`. Only `for` loop.  

The keyword `Benchmark` can be used similarly to `Test` and `Example` to time how long it takes to execute a function.  

For benchmarking, we use `testing.B` from the `testing` package, which provides access to the `b.N` variable, which again determines how often the function execution will be repeated. A appropriate value is automatically determined. 