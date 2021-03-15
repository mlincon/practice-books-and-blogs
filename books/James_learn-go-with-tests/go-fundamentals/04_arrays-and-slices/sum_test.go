package main

import (
	"reflect"
	"testing"
)

func TestSumFixedSizeArrays(t *testing.T) {

	// arrays have a limited capacity defined during declaration of the variable
	// e.g. variable := [N]type{val1, val2, ..., valN}
	numbers := [5]int{1, 2, 3, 4, 5}

	got := SumFixedSizeArrays(numbers)
	want := 15

	if got != want {
		// %v gives the value in default format, here as array
		t.Errorf("got %d want %d given, %v", got, want, numbers)
	}
}

func TestSumSlices(t *testing.T) {

	assertTest := func(t testing.TB, got, want int, numbers []int) {
		t.Helper()
		if got != want {
			t.Errorf("got %d, want %d, given %v", got, want, numbers)
		}
	}

	t.Run("collection of 5 numbers", func(t *testing.T) {
		numbers := []int{1, 2, 3, 4, 5}
		got := SumSlices(numbers)
		want := 15
		assertTest(t, got, want, numbers)
	})

}

func TestSumAll(t *testing.T) {
	got := SumAll([]int{1, 2}, []int{0, 9, 3})
	want := []int{3, 12}

	// we cannot use equality operators with slices
	// for convenience, we use reflect.DeepEqual
	// otherwise, we would need to compare each value over an iteration
	// word of caution: reflect.DeepEqual is not type safe
	if !reflect.DeepEqual(got, want) {
		t.Errorf("got %v, want %v", got, want)
	}
}

func TestSumAllViaAppend(t *testing.T) {
	got := SumAllViaAppend([]int{1, 2}, []int{0, 9, 3})
	want := []int{3, 12}

	// we cannot use equality operators with slices
	// for convenience, we use reflect.DeepEqual
	// otherwise, we would need to compare each value over an iteration
	// word of caution: reflect.DeepEqual is not type safe
	if !reflect.DeepEqual(got, want) {
		t.Errorf("got %v, want %v", got, want)
	}
}

func TestSumAllTails(t *testing.T) {

	assertTest := func(t testing.TB, got, want []int) {
		t.Helper()
		if !reflect.DeepEqual(got, want) {
			t.Errorf("got %d, want %d", got, want)
		}
	}

	t.Run("make the sums of some slices", func(t *testing.T) {
		got := SumAllTails([]int{1, 2}, []int{0, 9})
		want := []int{2, 9}

		assertTest(t, got, want)
	})

	t.Run("safely sum empty slices", func(t *testing.T) {
		got := SumAllTails([]int{}, []int{3, 4, 5})
		want := []int{0, 9}

		assertTest(t, got, want)
	})
}
