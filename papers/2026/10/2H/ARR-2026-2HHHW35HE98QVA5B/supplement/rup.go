// Forward RUP checker (Go port of rupcheck2.py's algorithm): 2-watched literals, deletions ignored.
// usage: rup file.cnf file.drup  -> exit 0 if the empty clause (or a level-0 conflict) is derived by RUP
package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

var nv int
var val []int8
var trail []int32
var watch [][]*[]int32

func idx(l int32) int { return int(l) + nv }
func lv(l int32) int8 { return val[idx(l)] }
func setl(l int32)    { val[idx(l)] = 1; val[idx(-l)] = -1; trail = append(trail, l) }

func prop(q int) bool {
	for q < len(trail) {
		l := trail[q]
		q++
		fl := -l
		ws := watch[idx(fl)]
		keep := ws[:0:0]
		i := 0
		confl := false
		for i < len(ws) {
			cp := ws[i]
			i++
			c := *cp
			if c[0] == fl {
				c[0], c[1] = c[1], c[0]
			}
			if lv(c[0]) == 1 {
				keep = append(keep, cp)
				continue
			}
			moved := false
			for k := 2; k < len(c); k++ {
				if lv(c[k]) >= 0 {
					c[1], c[k] = c[k], c[1]
					watch[idx(c[1])] = append(watch[idx(c[1])], cp)
					moved = true
					break
				}
			}
			if !moved {
				keep = append(keep, cp)
				if lv(c[0]) == -1 {
					keep = append(keep, ws[i:]...)
					confl = true
					break
				}
				setl(c[0])
			}
		}
		watch[idx(fl)] = keep
		if confl {
			return true
		}
	}
	return false
}
func readLine(s string) []int32 {
	f := strings.Fields(s)
	r := make([]int32, 0, len(f))
	for _, x := range f {
		v, _ := strconv.Atoi(x)
		r = append(r, int32(v))
	}
	return r
}
func add(c []int32, units *[]int32) {
	if len(c) == 1 {
		*units = append(*units, c[0])
		return
	}
	cp := &c
	watch[idx(c[0])] = append(watch[idx(c[0])], cp)
	watch[idx(c[1])] = append(watch[idx(c[1])], cp)
}
func main() {
	f, _ := os.Open(os.Args[1])
	sc := bufio.NewScanner(f)
	sc.Buffer(make([]byte, 1<<20), 1<<26)
	var cls [][]int32
	for sc.Scan() {
		s := sc.Text()
		if len(s) == 0 || s[0] == 'c' {
			continue
		}
		if s[0] == 'p' {
			fs := strings.Fields(s)
			nv, _ = strconv.Atoi(fs[2])
			continue
		}
		c := readLine(s)
		c = c[:len(c)-1]
		cls = append(cls, c)
	}
	// proof may use fresh variables? (glucose does not); bump nv by checking proof first
	pf, _ := os.Open(os.Args[2])
	ps := bufio.NewScanner(pf)
	ps.Buffer(make([]byte, 1<<20), 1<<26)
	var lemmas [][]int32
	for ps.Scan() {
		s := ps.Text()
		if len(s) == 0 || s[0] == 'd' {
			continue
		}
		c := readLine(s)
		if c[len(c)-1] != 0 {
			fmt.Println("malformed lemma")
			os.Exit(2)
		}
		c = c[:len(c)-1]
		for _, x := range c {
			if int(x) > nv || int(-x) > nv {
				nv = int(max32(x, -x))
			}
		}
		lemmas = append(lemmas, c)
	}
	val = make([]int8, 2*nv+2)
	watch = make([][]*[]int32, 2*nv+2)
	var units []int32
	for _, c := range cls {
		if len(c) == 0 {
			fmt.Println("empty clause in CNF")
			os.Exit(0)
		}
		add(c, &units)
	}
	for _, u := range units {
		if lv(u) == -1 {
			fmt.Println("trivially UNSAT")
			os.Exit(0)
		}
		if lv(u) == 0 {
			setl(u)
		}
	}
	if prop(0) {
		fmt.Println("CNF refuted by UP alone")
		os.Exit(0)
	}
	for n, c := range lemmas {
		mark := len(trail)
		conf := false
		for _, x := range c {
			if lv(-x) == 1 {
				continue
			}
			if lv(-x) == -1 {
				conf = true
				break
			}
			setl(-x)
		}
		if !conf {
			conf = prop(mark)
		}
		for _, l2 := range trail[mark:] {
			val[idx(l2)] = 0
			val[idx(-l2)] = 0
		}
		trail = trail[:mark]
		if !conf {
			fmt.Println("RUP FAIL at lemma", n)
			os.Exit(1)
		}
		if len(c) == 0 {
			fmt.Println("VERIFIED: empty clause derived by RUP;", n+1, "lemmas")
			os.Exit(0)
		}
		if len(c) == 1 {
			if lv(c[0]) == -1 {
				fmt.Println("VERIFIED: unit contradicts level 0;", n+1)
				os.Exit(0)
			}
			if lv(c[0]) == 0 {
				setl(c[0])
				if prop(len(trail) - 1) {
					fmt.Println("VERIFIED: level-0 conflict;", n+1, "lemmas")
					os.Exit(0)
				}
			}
		} else {
			// order: non-false literals first
			for i := 0; i < len(c); i++ {
				for j := i + 1; j < len(c) && i < 2; j++ {
					if lv(c[j]) > lv(c[i]) {
						c[i], c[j] = c[j], c[i]
					}
				}
			}
			add(c, &units)
			if lv(c[0]) == -1 {
				fmt.Println("VERIFIED: lemma falsified at level 0;", n+1)
				os.Exit(0)
			}
			if lv(c[1]) == -1 && lv(c[0]) == 0 {
				setl(c[0])
				if prop(len(trail) - 1) {
					fmt.Println("VERIFIED: level-0 conflict;", n+1)
					os.Exit(0)
				}
			}
		}
	}
	fmt.Println("NOT VERIFIED: proof ended without empty clause")
	os.Exit(1)
}
func max32(a, b int32) int32 {
	if a > b {
		return a
	}
	return b
}
