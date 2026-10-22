// Independent branch-and-bound for F(n): no SAT. Bitsets over [n]^3 (<=512 bits).
// usage: bnb n initBest   (finds max length > initBest, or proves none; initBest=0 -> exact F(n))
package main

import (
	"fmt"
	"math/bits"
	"os"
	"strconv"
)

const W = 8

type bs [W]uint64

var n, N int
var greater []bs
var lines [3][]bs // lines[p][k]: triples sharing the pair of coordinates (all except p)
var best int
var bestSeq []int
var cur []int
var nodes int64

func (a bs) and(b bs) (c bs) {
	for i := 0; i < W; i++ {
		c[i] = a[i] & b[i]
	}
	return
}
func (a bs) pop() (s int) {
	for i := 0; i < W; i++ {
		s += bits.OnesCount64(a[i])
	}
	return
}
func (a bs) any() bool {
	for i := 0; i < W; i++ {
		if a[i] != 0 {
			return true
		}
	}
	return false
}
func (a *bs) set(i int)        { a[i>>6] |= 1 << uint(i&63) }
func (a bs) has(i int) bool    { return a[i>>6]>>(uint(i&63))&1 == 1 }
func coords(i int) [3]int      { return [3]int{i / (n * n), (i / n) % n, i % n} }
func lt2(a, b int) bool {
	x, y := coords(a), coords(b)
	c := 0
	for i := 0; i < 3; i++ {
		if x[i] < y[i] {
			c++
		}
	}
	return c >= 2
}
func bound(cand bs) int {
	m := cand.pop()
	for p := 0; p < 3; p++ {
		c := 0
		for _, l := range lines[p] {
			if l.and(cand).any() {
				c++
			}
		}
		if c < m {
			m = c
		}
	}
	return m
}
func search(cand bs) {
	nodes++
	if len(cur) > best {
		best = len(cur)
		bestSeq = append([]int(nil), cur...)
	}
	if len(cur)+bound(cand) <= best {
		return
	}
	for i := 0; i < N; i++ {
		if cand.has(i) {
			cur = append(cur, i)
			search(cand.and(greater[i]))
			cur = cur[:len(cur)-1]
		}
	}
}
func main() {
	n, _ = strconv.Atoi(os.Args[1])
	best, _ = strconv.Atoi(os.Args[2])
	N = n * n * n
	greater = make([]bs, N)
	for a := 0; a < N; a++ {
		for b := 0; b < N; b++ {
			if lt2(a, b) {
				greater[a].set(b)
			}
		}
	}
	for p := 0; p < 3; p++ {
		lines[p] = make([]bs, n*n)
		for i := 0; i < N; i++ {
			c := coords(i)
			var key int
			switch p {
			case 0:
				key = c[1]*n + c[2]
			case 1:
				key = c[0]*n + c[2]
			default:
				key = c[0]*n + c[1]
			}
			lines[p][key].set(i)
		}
	}
	// top level: first element with sorted coordinates (S3 symmetry), each such first element handled separately
	init := best
	for i := 0; i < N; i++ {
		c := coords(i)
		if !(c[0] <= c[1] && c[1] <= c[2]) {
			continue
		}
		cur = []int{i}
		if init+0 >= 0 && 1 > best {
			best = 1
			bestSeq = []int{i}
		}
		search(greater[i])
	}
	fmt.Printf("n=%d init=%d best=%d nodes=%d seq=", n, init, best, nodes)
	if len(bestSeq) > 0 && best > init {
		for _, i := range bestSeq {
			c := coords(i)
			fmt.Printf("(%d,%d,%d)", c[0]+1, c[1]+1, c[2]+1)
		}
	}
	fmt.Println()
}
